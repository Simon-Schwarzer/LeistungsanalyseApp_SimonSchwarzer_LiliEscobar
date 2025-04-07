
from my_functions import build_experiment, build_person, estimate_max_hr
from datetime import datetime
import pandas as pd

if __name__ == "__main__":
    experiment_dict = build_experiment(
        experiment_name="Leistungstest1",
        date=datetime.now(),  # Nutze datetime.now() für das aktuelle Datum
        supervisor="Simon Schwarzer",
        subject="max_hr_test"
    )
    
    person_dict = build_person(
        first_name="Max",
        last_name="Mustermann",
        sex="male",
        age=23
    )

    max_hr = estimate_max_hr(
        age_years=23,
        sex="male"
    )

    def build_complete_experiment_dict(person_dict, experiment_dict) -> dict:
        return {
            "Daten_person": person_dict,
            "Daten_experiment": experiment_dict,
        }

    dict_ganz = build_complete_experiment_dict(person_dict, experiment_dict)

    print(dict_ganz)  # Falls du das Dictionary ausgeben möchtest

df = pd.DataFrame(dict_ganz)
print(df)
