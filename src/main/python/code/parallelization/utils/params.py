import os
import utils.file as file
from utils.constants.params import properties_fixed, get_default_param
from utils.constants.config import get_pool_size, get_weak_score, get_float_keys
from test.utils import get_other_bound, is_valid
import time 

def save_params_to_file(params, filename="params.init.json"):

    if not params:
        print("params is empty, returning...")
        time.sleep(10)
        return
    if not isinstance(params, list):
        params = [params]
    from json import dump
    file.check_safety(filename)
    filename = file.get_absolute_path(filename)
    with open(filename, "w") as f:
        dump(params, f)

def get_pool_params():
    pool_params = get_from_json("params.pool.json")
    pool_params = get_sorted_params(pool_params)
    return pool_params

def get_from_json(filename="params.init.json"):
    filename = file.get_absolute_path(filename)
    return file.read_json(filename)

def get_processed_param_from_json(filename="params.init.json"):
    param = get_from_json(filename)
    return get_processed_param(param)

def get_processed_param(param):
    for fixed_key in properties_fixed.keys():
        if fixed_key in param['properties']:
            param['properties'].pop(fixed_key)
    return param

def get_dataframe_from_json(filename="params.init.json"):
    import pandas
    filename = file.get_absolute_path(filename)
    params = file.read_json(filename)
    df = get_dataframe_from_params(params)
    numerical_cols = df.select_dtypes(include='number').columns
    numerical_cols = numerical_cols.drop('score')
    numerical_cols = numerical_cols.drop('properties.numOfAgents')
    numerical_cols = numerical_cols.drop('properties.seed')

    # print(f"numerical_cols: {numerical_cols}")

    df_num = pandas.concat([df[numerical_cols],df['score']], axis=1)
    df_num.to_csv('data/numerical_data.csv', index=False)
    return df_num

def get_dataframe_from_params(params):
    import pandas 
    #each key and subkey is a column
    df = pandas.json_normalize(params)
    return df


def get_top_params(params, k=32):
    sorted_params = get_sorted_params(params)
    top_k = sorted_params[:k]
    return top_k

def get_extended_params(params):
    extended_param = get_empty_param()  
    if not isinstance(params, list):
        print("params is not a list")
        params = [params]
    for param in params:
        for key in extended_param:
            if key != 'properties' and key not in param:
                print(f"Key {key} not found in param")
                param[key] = extended_param[key]
        for key in extended_param['properties']:
            if key not in param['properties']:
                param['properties'][key] = extended_param['properties'][key] 
    return params



def get_selected_params(params, number_of_random_parents=32):
    selected_params =[]
    selected_params = shuffle_params(params)[:number_of_random_parents]
    return selected_params

def get_mixed_param(params, type="max", number_of_random_parents=32):

    selected_params = get_selected_params(params, number_of_random_parents)
    mixed_param = get_polished_param(None, type)
    if type == "max":
        mixed_param = get_max_param(selected_params)
    elif type == "min":
        mixed_param = get_min_param(selected_params)
    elif type == "random":
        mixed_param = get_random_param(selected_params)
    elif type == "mean":
        mixed_param = get_mean_param(selected_params)
    elif type == "sum":
        mixed_param = get_sum_param(selected_params)
    else:
        mixed_param = get_new_param()
   
    mixed_param = post_process_param(mixed_param, type)
   
    return mixed_param

def get_polished_param(param, type="sample"):
    if param is None:
        param = get_empty_param()
    sample = get_sample_param()
    for key in sample:
        if key not in param:
            param[key] = sample[key]
    for key in sample['properties']:
        if key not in param['properties']:
            param['properties'][key] = sample['properties'][key]
    param['type'] = type
    return param


def shuffle_params(params):
    from random import shuffle
    shuffled_params = params.copy()
    shuffle(shuffled_params)
    return shuffled_params

def get_empty_param(reset_value=0):
    param = {}
    param = get_default_param()
    for key in param['properties']:
        param['properties'][key] = reset_value
    param['properties'].update(properties_fixed)
    param['score'] = reset_value
    param['type'] = "empty"
    param['id'] = "id_empty"
    return param


def get_max_param(selected_params):
    building_param = get_empty_param()
    building_param.update(selected_params[0])
    for param in selected_params:
        for key in param['properties']:
            try:
                other_bound = get_other_bound(key)
                if other_bound == None:
                    building_param['properties'][key] = max(building_param['properties'][key], param['properties'][key])
                else:
                    target_param = param if param['properties'][key] > building_param['properties'][key] else building_param
                    building_param['properties'][key] = target_param['properties'][key]
                    building_param['properties'][other_bound] = target_param['properties'][other_bound]
            except: 
                # print(f"Error in {key}")
                pass
    
    
    return building_param

def get_min_param(selected_params):
    building_param = get_empty_param()
    building_param.update(selected_params[0])
    for param in selected_params:
        for key in param['properties']:
            try:
                other_bound = get_other_bound(key)
                if other_bound == None:
                    building_param['properties'][key] = min(building_param['properties'][key], param['properties'][key])
                else:
                    target_param = param if param['properties'][key] < building_param['properties'][key] else building_param
                    building_param['properties'][key] = target_param['properties'][key]
                    building_param['properties'][other_bound] = target_param['properties'][other_bound]
            except:
                # print(f"Error in {key}")
                pass
    
    return building_param

def get_random_param(selected_params):
    from random  import randint
    random_param = get_empty_param()
    length = len(selected_params)
    for param in selected_params:
        random_param['properties'] = {}
        for key in param['properties']:
            random_index = randint(0, length-1)
            other_bound = get_other_bound(key)
            if other_bound == None:
                if is_valid(key):
                    random_param['properties'][key] = selected_params[random_index]['properties'][key]
            else:
                random_param['properties'][key] = selected_params[random_index]['properties'][key]
                random_param['properties'][other_bound] = selected_params[random_index]['properties'][other_bound]
    
    return random_param
            
            
def get_mean_param(selected_params):
    building_param = get_empty_param()
    building_param.update(selected_params[0])
    for param in selected_params:
        for key in param['properties']:
            try:
                other_bound = get_other_bound(key)
                if other_bound == None:
                  building_param['properties'][key] = (building_param['properties'][key] + param['properties'][key]) / 2
                else:
                    building_param['properties'][key] = (['properties'][key] + param['properties'][key]) / 2
                    building_param['properties'][other_bound] = (building_param['properties'][other_bound] + param['properties'][other_bound]) / 2
            except: 
                # print(f"Error in {key}")
                pass
    
    return building_param

def get_sum_param(selected_params):
    building_param = get_empty_param()
    building_param.update(selected_params[0])
    for param in selected_params:
        for key in param['properties']:
            try:
                other_bound = get_other_bound(key)
                if other_bound == None:
                    building_param['properties'][key] = building_param['properties'][key] + param['properties'][key]
                else:
                    building_param['properties'][key] = building_param['properties'][key] + param['properties'][key]
                    building_param['properties'][other_bound] = building_param['properties'][other_bound] + param['properties'][other_bound]
            except:
                # print(f"Error in {key}")
                pass
    
    return building_param

def get_new_param():
    from random import random
    min_param = get_min_param_from_file()
    max_param = get_max_param_from_file()
    building_param = get_empty_param()

    for key in min_param['properties']:
        try:
            random_number = random()
            other_bound = get_other_bound(key)
            if other_bound == None:
                building_param['properties'][key] =  random_number * (max_param['properties'][key] - min_param['properties'][key]) + min_param['properties'][key]
            else:
                building_param['properties'][key] =  random_number * (max_param['properties'][key] - min_param['properties'][key]) + min_param['properties'][key]
                building_param['properties'][other_bound] =  random_number * (max_param['properties'][other_bound] - min_param['properties'][other_bound]) + min_param['properties'][other_bound]
        except:
            # print(f"Error in {key}")
            pass
    round_param(building_param)
    return building_param
    
def round_param(param):
    float_keys=get_float_keys()
    reserved_keys=['score', 'type']
    for key in float_keys:
        param['properties'][key] = round(param['properties'][key], 1)
    
    for key in param['properties']:
        if key not in float_keys and key not in reserved_keys:
            try:
                # print(f"key: {key}, value: {param['properties'][key]}")
                param['properties'][key] = int(param['properties'][key])
            except:
                # print(f"Error in {key}")
                pass
    
    return param

def check_min_max(param):
    min_param= get_min_param_from_file()
    max_param = get_max_param_from_file()
    for key in param['properties']:
        try:
            if param['properties'][key] < min_param['properties'][key]:
                param['properties'][key] = min_param['properties'][key]
        except:
            # print(f"Error in {key}")
            pass
        try:
            if param['properties'][key] > max_param['properties'][key]:
                param['properties'][key] = max_param['properties'][key]
        except:
            # print(f"Error in {key}")
            pass

    return param

def get_min_param_from_file():
    return file.read_json("code/utils/constants/json/param.min.json")

def get_max_param_from_file():
    return file.read_json("code/utils/constants/json/param.max.json")

def get_sample_param_from_file():
    return file.read_json("code/utils/constants/json/param.sample.json")

def get_sample_param():
    param_sample = get_sample_param_from_file()
    return param_sample

def post_process_param(param, type="empty"):
    param = get_polished_param(param, type)
  
    param = round_param(param)
    param = check_min_max(param)
    param = get_compatible_param(param)
    return param

def get_sorted_params(params):
    params = sorted(params, key=lambda x: x['score'], reverse=True)
    # add rank to params
    for i, param in enumerate(params):
        param['rank'] = i+1
    return params

def add_type_to_params(params, type):
    for param in params:
        param['type'] = type
    return params

def add_id_to_params(params,  prefix = "init"):
    prefix = "id_" + prefix
    if prefix[-1] != "_":
        prefix += "_"
    for i, param in enumerate(params):
        param['id'] = prefix + str(i)
    return params

def update_pool(pool_params, params, counter):
    pool_params = pool_params + params
    pool_params = get_sorted_params(pool_params)
    if len(pool_params) > get_pool_size():
        pool_params = pool_params[:get_pool_size()]
    pool_params = old_weak_killer(pool_params, counter)
    save_params_to_file(pool_params, "params.pool.json")

def old_weak_killer(pool_params, counter):
    weak_score = get_weak_score(counter)
    pool_params = [param for param in pool_params if param['score'] > weak_score]
    return pool_params

def initialization(timestamp=1):
    try:
        print("Initializing...")
        print(f"current path: {os.getcwd()}")   
        print(f"get_project_path: {file.get_project_path()}")
        print(f"get_python_path: {file.get_python_path()}")

        if not file.exists("params.pool.json"):
            print("Creating pool...")
            if not file.exists("params.init.json"):
                print("Creating init...")
                try:
                    from init import save_init_params
                    save_init_params()
                except Exception as e:
                    print(f"Error in initialization: {e}")
                    exit()
            params = get_from_json("params.init.json")
            params = get_extended_params(params)
            params = get_top_params(params, k=get_pool_size())
            params = add_id_to_params(params, "l000")
            params = add_type_to_params(params, "init")
            save_params_to_file(params, "params.pool.json")
            save_params_to_file(params, f"pole/params.t{timestamp}_l000.json")

    except Exception as e:
        print(f"Error in initialization: {e}")

    
def get_compatible_param(param):
    import test.check as check
    import test.fixes as fixes

    properties = param['properties']
    # order is important
    if not check.is_global_compatible(properties):
        properties = fixes.global_properties(properties)
        print(f"type: {param['type']}")
    if not check.is_fixed_values_compatible(properties):
        properties = fixes.fixed_values_properties(properties)
        print(f"type: {param['type']}")
    if not check.is_uniform_compatible(properties):
        properties = fixes.uniform_properties(properties)
        print(f"type: {param['type']}")
    if not check.is_range_compatible(properties):
        properties = fixes.range_properties(properties)
        print(f"type: {param['type']}")
    if not check.is_less_than_min(properties):
        properties = fixes.less_than_min_properties(properties)
        print(f"type: {param['type']}")
    if not check.is_greater_than_max(properties):
        properties = fixes.greater_than_max_properties(properties)
        print(f"type: {param['type']}")
    if not check.is_bound_compatible(properties):
        properties = fixes.bound_properties(properties)
        print(f"type: {param['type']}")
    return param