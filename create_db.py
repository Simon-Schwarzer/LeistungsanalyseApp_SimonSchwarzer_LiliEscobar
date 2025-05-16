import sqlite3

def connect_to_db(db_name="neue.db"):
    return sqlite3.connect(db_name)

def create_tables(cursor):
    cursor.execute("DROP TABLE IF EXISTS StepsInExperiments")
    cursor.execute("DROP TABLE IF EXISTS Steps")
    cursor.execute("DROP TABLE IF EXISTS Experiments")

    cursor.execute("""
        CREATE TABLE Experiments (
            experimentID INTEGER PRIMARY KEY AUTOINCREMENT,
            experimenter TEXT,
            subject TEXT,
            testname TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE Steps (
            stepID INTEGER PRIMARY KEY AUTOINCREMENT,
            duration_s TEXT,
            power_W TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE StepsInExperiments (
            StepsInExperimentsID INTEGER PRIMARY KEY AUTOINCREMENT,
            PositionInExperiment INTEGER NOT NULL,
            stepID INTEGER NOT NULL,
            experimentID INTEGER NOT NULL,
            FOREIGN KEY (stepID) REFERENCES Steps(stepID),
            FOREIGN KEY (experimentID) REFERENCES Experiments(experimentID)
        )
    """)

def insert_sample_data(cursor):
    steps = [(60, 100), (60, 150)]
    for step in steps:
        cursor.execute("INSERT INTO Steps (duration_s, power_W) VALUES (?, ?)", step)

    experiment_data = ("Julian", "Julian", "Test1")
    cursor.execute("INSERT INTO Experiments (experimenter, subject, testname) VALUES (?, ?, ?)", experiment_data)

    step_links = [(1, 1, 1), (2, 1, 2)]
    for link in step_links:
        cursor.execute("INSERT INTO StepsInExperiments (PositionInExperiment, experimentID, stepID) VALUES (?, ?, ?)", link)

def get_all_steps(cursor):
    cursor.execute("SELECT * FROM Steps")
    return cursor.fetchall()

def get_steps_for_experiment(cursor, experiment_id):
    cursor.execute("""
        SELECT * FROM StepsInExperiments
        JOIN Steps ON StepsInExperiments.stepID = Steps.stepID
        WHERE experimentID = ?
    """, (experiment_id,))
    return cursor.fetchall()

def main():
    connection = connect_to_db()
    cursor = connection.cursor()

    create_tables(cursor)
    connection.commit()

    insert_sample_data(cursor)
    connection.commit()

    print("All Steps:")
    print(get_all_steps(cursor))

    print("\nSteps for Experiment 1:")
    print(get_steps_for_experiment(cursor, 1))

    connection.close()

if __name__ == "__main__":
    main()
