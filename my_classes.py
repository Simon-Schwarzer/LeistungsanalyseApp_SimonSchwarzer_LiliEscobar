<<<<<<< HEAD
=======
import sqlite3

>>>>>>> 17a0fed (Beschreibe deine Änderungen hier)
class Subject():
    def __init__(self, first_name, last, sex):
      pass

    def estimate_max_hr(self):
      """A function that estimates the maximum heart rate of a subject"""
      pass

class Supervisor():
    def __init__(self, first_name, last_name):
      pass

class Experiment():
<<<<<<< HEAD
    def __init__(self, name, date):
      pass
=======
    def __init__(self, subject, supervisor, name):
      self.subject = subject
      self.supervisor = supervisor
      self.steps = []
      self.name = name

      self.connection = sqlite3.connect("neue.db")
      self.cursor = self.connection.cursor()
>>>>>>> 17a0fed (Beschreibe deine Änderungen hier)

    def add_subject(self, subject):
      self.subject = subject

    def add_supervisor(self, supervisor):
<<<<<<< HEAD
      pass
=======
      pass

    def add_step(self, step):
      self.steps.append(step)

    def insert_sample_data(self, cursor):
        for step in self.steps:
            self.cursor.execute("INSERT INTO Steps (duration_s, power_W) VALUES (?, ?)", [step.duration_s, step.power_W])

        experiment_data = (self.add_subject, self.supervisor, name)
        cursor.execute("INSERT INTO Experiments (experimenter, subject, testname) VALUES (?, ?, ?)", experiment_data)

        #step_links = [(1, 1, 1), (2, 1, 2)]
        #for link in step_links:
        #    self.cursor.execute("INSERT INTO StepsInExperiments (PositionInExperiment, experimentID, stepID) VALUES (?, ?, ?)", link)

    def print_steps(self):
      self.cursor.execute("SELECT * FROM Steps")
      print(self.cursor.fetchall())


    class Step():
        def __init__(self, duration_s, power_W):
            self.duration_s = duration_s
            self.power_W = power_W
        


    class Step():
        def __init__(self, duration_s, power_W):
            self.duration_s = duration_s
            self.power_W = power_W
>>>>>>> 17a0fed (Beschreibe deine Änderungen hier)
