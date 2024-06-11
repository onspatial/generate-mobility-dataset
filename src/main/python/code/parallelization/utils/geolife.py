import pandas
import utils.file as file
from utils.compatibility import get_compatible_input_df


def get_input_dataframe(file_path):
    input_df = pandas.read_csv(file_path, sep=' ', header=None,
                            names=['Latitude', 'Longitude', 'ArrivingTime', 'LeavingTime', 'AgentID'])
    input_df = input_df.iloc[1:].reset_index(drop=True)
    input_df['ArrivingTime'] = pandas.to_datetime(input_df['ArrivingTime'], format='%Y-%m-%d,%H:%M:%S')
    input_df = input_df.groupby('AgentID').filter(lambda x: len(x) > 100)
    print(f"Number of agents: {len(input_df['AgentID'].unique())}")
    return input_df

def read(checkin_path):
    print("Reading and preprocessing data from the dataset...")
    dir = file.get_dir(checkin_path)
    input_df = get_input_dataframe(checkin_path)
    print(f"input data frame is loaded with {len(input_df)} rows.")
    compatible_df = get_compatible_input_df(input_df)
    print(f"compatible data frame is loaded with {len(compatible_df)} rows.")
    # compatible_df.to_csv(f"{dir}/compatible.csv", index=False)
    # print(f"compatible data frame is saved to {dir}/compatible.csv.")
    return compatible_df
