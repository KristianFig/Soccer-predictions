import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_winner_team(Team_1, Team_2):
    team_1_col = f'{Team_1.lower()}'  # Convert to lowercase
    team_2_col = f'{Team_2.lower()}'  # Convert to lowercase

    x = np.zeros(len(__data_columns))

    # Check if team columns exist in __data_columns
    if team_1_col in __data_columns:
        x[__data_columns.index(team_1_col)] = 1
    else:
        raise ValueError(f'Team {Team_1} not found in the model data columns.')

    if team_2_col in __data_columns:
        x[__data_columns.index(team_2_col)] = 1
    else:
        raise ValueError(f'Team {Team_2} not found in the model data columns.')

    return __model.predict([x])[0]

def get_team_names():
    return __locations

def load_saved_artifacts():
    global __data_columns
    global __locations
    global __model

    print("Loading saved artifacts...")

    with open("./artifacts/columnsca.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[4:]

    with open('./artifacts/Copa_america_model.pickle', 'rb') as f:
        __model = pickle.load(f)

    print("Loading saved artifacts...done")

if __name__ == "__main__":
    load_saved_artifacts()
    print(get_team_names())
    print(get_winner_team('Argentina', 'Germany'))