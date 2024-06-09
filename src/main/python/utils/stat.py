from utils import file
import utils.helpers as helpers
import pandas
def get_stat_from_file(path="data/geolife/stat.json"):
    stat = None
    try:
        if file.exists(path):
            stat = file.load_json(path)
    except Exception as e:
        print("Error: loading stat from file")
        print(e)
    return stat
    
def save_stat_to_file(stat, path="data/geolife/stat.json"):
    try:
        stat = helpers.get_json_compatible_dict(stat)
        file.save_json(stat, path)
    except Exception as e:
        print("Error: saving stat to file")
        print(e)
        return None

def get_stat(data):
    print("Calculating the calculate_per_day_stat...")
    per_day_stat = get_per_day_stat(data)
    print(per_day_stat.head())
    result = {}
    result["distance_per_trip"] =  float(per_day_stat['TotalDistance'].sum() / per_day_stat['NumberOfCheckins'].sum())
    result["average_distance"] = float(per_day_stat['AverageDistance'].mean())
    result["max_distance"] = float(per_day_stat['MaxDistance'].max())
    result["median_distance"] = float(per_day_stat['AverageDistance'].median())
    return result

def get_per_day_stat(data):                                
    per_day_stat = pandas.DataFrame(columns=['AgentID', 'Date', 'NumberOfCheckins', 'TotalDistance', 'AverageDistance', 'MaxDistance', 'MinDistance'])
    data['ArrivingTime'] = pandas.to_datetime(data['ArrivingTime'])
    data['Date'] = data['ArrivingTime'].dt.date
    data['Distance'] = data['Distance'].astype(int)
    per_day_stat['AgentID'] = data['AgentID']
    per_day_stat['Date'] = data['Date']
    per_day_stat['NumberOfCheckins'] = 1
    per_day_stat['TotalDistance'] = data['Distance']
    per_day_stat['AverageDistance'] = data['Distance']
    per_day_stat['MaxDistance'] = data['Distance']
    per_day_stat = per_day_stat.groupby(['AgentID', 'Date']).agg({'NumberOfCheckins': 'sum', 'TotalDistance': 'sum', 'AverageDistance': 'mean', 'MaxDistance': 'max'}).reset_index()
    return per_day_stat
