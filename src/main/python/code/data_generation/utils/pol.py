import pandas
import utils.file as file
from pyproj import Transformer
from utils.compatibility import get_compatible_input_df

def convert_coordinate_system(latitude, longitude):
    transformer = Transformer.from_crs("epsg:26916", "epsg:4326")
    return transformer.transform(latitude, longitude)



def get_processed_input_df(file_path):
    input_df = pandas.read_csv(file_path, sep='\t', header=None,  low_memory=False, names=['AgentID',	'ArrivingTime',	'VenueId',	'VenueType',	'Latitude',	'Longitude'])
    input_df = input_df.iloc[1:].reset_index(drop=True)
    input_df['ArrivingTime'] = pandas.to_datetime(input_df['ArrivingTime'])
    input_df['Latitude'], input_df['Longitude'] = convert_coordinate_system(input_df['Latitude'], input_df['Longitude'])


    return input_df

def read(checkin_path):
    dir = file.get_dir(checkin_path)
    if file.exists(f"{dir}/compatible.csv"):
        compatible_df = pandas.read_csv(f"{dir}/compatible.csv")
        print(f"compatible data frame is loaded with {len(compatible_df)} rows.")
        return compatible_df
    print("Reading and preprocessing data from the dataset...")
    input_df = get_processed_input_df(checkin_path)
    print(f"input data frame is loaded with {len(input_df)} rows.")
    compatible_df = get_compatible_input_df(input_df)
    print(f"compatible data frame is loaded with {len(compatible_df)} rows.")
    # compatible_df.to_csv(f"{dir}/compatible.csv", index=False)
    # print(f"compatible data frame is saved to {dir}/compatible.csv.")
    return compatible_df
