import pandas
from geopy.distance import geodesic
from utils.file import get_dir
from test.data import check_dfs
import utils.constants.config as config

def get_compatible_input_df(input_df):
    try:
        compatible_input_df = pandas.DataFrame()
        compatible_input_df['AgentID'] = input_df['AgentID']
        compatible_input_df['ArrivingTime'] = pandas.to_datetime(input_df['ArrivingTime'])
        compatible_input_df['Latitude'] = input_df['Latitude']
        compatible_input_df['Longitude'] = input_df['Longitude']
        compatible_input_df['Distance'] = 0
        check_dfs(input_df, compatible_input_df, sorted=False)
        compatible_input_df = get_converted_df(compatible_input_df)
        compatible_input_df.sort_values(by=['AgentID', 'ArrivingTime'], inplace=True)
        compatible_input_df.reset_index(inplace=True)
        
        compatible_input_df = get_bounded_df(compatible_input_df, config.get_bounding_box())
        compatible_input_df = add_distance_column(compatible_input_df)
    except Exception as e:
        print(f"Error in compatibility: {e}")
        return None
    # compatible_input_df.reset_index(drop=True, inplace=True)
    #drop index
    compatible_input_df.drop(columns=['index'], inplace=True)
    check_dfs(input_df, compatible_input_df, sorted=True, polished=False)

    return compatible_input_df

def add_distance_column(input_df):
    input_df['Distance'] = 0
    try:
        current_agent_id = -1
        for index, row in input_df.iterrows():
            
            if current_agent_id != row['AgentID']:
                current_agent_id = row['AgentID']
                previous_row = row
                continue
            distance = get_distance_between_two_points(previous_row, row)
            input_df.at[index, 'Distance'] = int(distance)
            previous_row = row
    except Exception as e:
        print(f"Error in adding distance column: {e}")
        return None
    return input_df


def get_distance_between_two_points(point1, point2):
    try:
        distance = geodesic((point1['Latitude'], point1['Longitude']), (point2['Latitude'], point2['Longitude'])).m
        if distance < 0:
            distance = 0
        if distance > 100000:
            print(f"Distance between two points is too large: {distance}")
            distance = 0
        return distance
    except Exception as e:
        print(f"Error in getting distance between two points: {e}")
        return None
    
def get_bounded_df(input_df, bounding_box):
    try:
        length_before = len(input_df)
        input_df = input_df[input_df['Latitude'] >= bounding_box['min_latitude']]
        input_df = input_df[input_df['Latitude'] <= bounding_box['max_latitude']]
        input_df = input_df[input_df['Longitude'] >= bounding_box['min_longitude']]
        input_df = input_df[input_df['Longitude'] <= bounding_box['max_longitude']]
        length_after = len(input_df)
        print(f"Bounding the input df: {length_before} -> {length_after}")
    except Exception as e:
        print(f"Error in bounding the input df: {e}")
    return input_df

def get_converted_df(input_df):
    
    try:
        input_df['AgentID'] = input_df['AgentID'].astype(int)
        input_df['Latitude'] = input_df['Latitude'].astype(float)
        input_df['Longitude'] = input_df['Longitude'].astype(float)
        input_df['ArrivingTime'] = pandas.to_datetime(input_df['ArrivingTime'])
    except Exception as e:
        print(f"Error in converting the input df: {e}")
        return None
    return input_df