from utils import file
from utils.params import get_empty_param, save_params_to_file, get_extended_params, get_sorted_params, add_id_to_params
from test.utils import is_valid
from utils.constants.config import get_agent_numbers, get_end_times
from utils.constants.params import get_useless_properties

import random
def get_top_params(threshold=0.8):
    top_params = []
    if not file.exists("results/params.top.json"):   
        pools_path = file.get_files( "params.pool*.json")
        pool_params = []
        for pool_path in pools_path:
            temp = file.load_json(pool_path)
            for param in temp:
                if "score" in param and param["score"] > threshold:
                    pool_params.append(param)
        top_params = sorted(pool_params, key=lambda x: x["score"], reverse=True)
        save_params_to_file(top_params, f"results/params.top.json")
    else:
        top_params = file.load_json("results/params.top.json")

    print(f"Found {len(top_params)} top params...")
    return top_params
def get_initial_parameters(input_params):
    if not file.exists("results/params.initial.json"):
        initial_params = input_params.copy()
        save_params_to_file(initial_params, f"results/params.initial.json")
    else:
        initial_params = file.load_json("results/params.initial.json")
    print(f"Found {len(initial_params)} initial params...")
    return initial_params

def get_filtered_params(input_params):
    under_review = []
    under_review = input_params.copy()
    under_review = get_sorted_params(under_review)
    under_review = add_id_to_params(under_review, "under_review")
    under_review = remove_duplicate_params(under_review)
    under_review = get_unique_params(under_review)
    reviewed = get_original_params(under_review, input_params)
    reviewed = get_sorted_params(reviewed)
    reviewed = reviewed[:10]
    reviewed = add_id_to_params(reviewed, "reviewed")
    return reviewed

def get_original_params(under_review, original_params):
    originals= []
    for param in under_review:
        for original_param in original_params:
            if param['id'] == original_param['id']:
                originals.append(original_param)
    return originals
                 

def remove_duplicate_params(input_params):
    input_params = remove_useless_properties(input_params)
    unique_params = []
    for param in input_params:
        if param['properties'] not in [x['properties'] for x in unique_params]:
            unique_params.append(param)
    return unique_params

def remove_useless_properties(input_params):
    useless_properties = get_useless_properties()
    filtered_params = []
    for param in input_params:
        temp = {}
        temp['properties'] = {}
        for key, value in param['properties'].items():
            if key not in useless_properties:
                temp['properties'][key] = value
        temp['score'] = param['score']
        temp['id'] = param['id']
        filtered_params.append(temp)

    return filtered_params

def get_reviewed_params(input_params):
    reviewed_params = []
    if not file.exists("results/params.reviewed.json"):
        index = random.randint(0, len(input_params))
        base_param = input_params[index]
        base_param = get_extended_params(base_param)[0]
        counter_param = get_counter_param(input_params)
        similar_param = get_similar_param(input_params)
        max_param = get_max_param(input_params)
        min_param = get_min_param(input_params)
        mean_param = get_mean_param(input_params)
        std_param = get_std_param(input_params)
        save_params_to_file(counter_param, "results/review/params.counter.json")
        save_params_to_file(similar_param, "results/review/params.similar.json")
        save_params_to_file(max_param, "results/review/params.max.json")
        save_params_to_file(min_param, "results/review/params.min.json")
        save_params_to_file(mean_param, "results/review/params.mean.json")
        save_params_to_file(std_param, "results/review/params.std.json")
        reviewed_params = input_params.copy()
        reviewed_params = get_cleaned_params(reviewed_params)
        reviewed_params = get_filtered_params(reviewed_params)

        save_params_to_file(reviewed_params, f"results/params.reviewed.json")
    else:
        reviewed_params = file.load_json("results/params.reviewed.json")
    print(f"Found {len(reviewed_params)} reviewed params...")
    return reviewed_params

def get_configured_params(input_params):
    if not file.exists("results/params.configured.json"):
        configured_params = configure_agent_numbers(input_params)
        configured_params = add_id_to_params(configured_params, "results")
        save_params_to_file(configured_params, f"results/params.configured.json")
    else:
        configured_params = file.load_json("results/params.configured.json")

    
    return configured_params

def get_counter_param(input_params):
    counter_param = get_empty_param(reset_value=1)
    for param in input_params:
        for key, value in param['properties'].items():
            if is_valid(key) and key in counter_param['properties']:
                counter_param['properties'][key] += 1
    return counter_param

def get_similar_param(input_params):
    base_param = input_params[random.randint(0, len(input_params))]
    similar_param = get_empty_param()
    for param in input_params:
        for key, value in param['properties'].items():
            if is_valid(key) and base_param['properties'][key] == value:
                similar_param['properties'][key] += 1
    return similar_param

def get_max_param(input_params):
    max_param = get_empty_param(reset_value=-1)
    for param in input_params:
        for key, value in param['properties'].items():
            if is_valid(key):
                max_param['properties'][key] = max(max_param['properties'][key], value)
    return max_param

def get_min_param(input_params):
    min_param = get_empty_param(reset_value=1000000)
    for param in input_params:
        for key, value in param['properties'].items():
            if is_valid(key):
                min_param['properties'][key] = min(min_param['properties'][key], value)
    return min_param

def get_mean_param(input_params):
    mean_param = get_empty_param()
    counter_param = get_counter_param(input_params)
    for param in input_params:
        for key, value in param['properties'].items():
            if is_valid(key):
                mean_param['properties'][key] += value
    for key in mean_param['properties']:
        if is_valid(key):
            mean_param['properties'][key] /= counter_param['properties'][key]
    return mean_param

def get_std_param(input_params):
    std_param = get_empty_param()
    counter_param = get_counter_param(input_params)
    mean_param = get_mean_param(input_params)
    for param in input_params:
        for key, value in param['properties'].items():
            if is_valid(key):
                std_param['properties'][key] += (value - mean_param['properties'][key]) ** 2
    for key in std_param['properties']:
        if is_valid(key):
            std_param['properties'][key] = (std_param['properties'][key] / counter_param['properties'][key]) ** 0.5
    return std_param

def get_cleaned_params(input_params):
    # remove type, id, config and status keys:
    cleaned_params = []
    for param in input_params:
        cleaned_param = {}
        for key, value in param.items():
            if key not in ['type', 'id', 'config', 'status']:
                cleaned_param[key] = value
        param['properties']['numOfAgents'] = 0
        param['properties']['maps'] = "tbd"


        cleaned_params.append(cleaned_param)
    return cleaned_params

def get_unique_params(input_params):
    unique_params = []
    for param in input_params:
        if param['properties'] not in [x['properties'] for x in unique_params]:
            unique_params.append(param)
    return unique_params

def get_rounded_params(input_params):
    rounded_params = []
    for param in input_params:
        rounded_param = {}
        rounded_param['properties'] = {}
        for key, value in param['properties'].items():
            if is_valid(key):
                rounded_param['properties'][key] = round(value, 1)
            else:
                rounded_param['properties'][key] = value
        rounded_param['score'] = round(param['score'], 2)
        rounded_params.append(rounded_param)
    return rounded_params

def configure_agent_numbers(input_params):
    configured_params = []
    agent_numbers = get_agent_numbers(type="results")
    end_times = get_end_times()
    for agent_number in agent_numbers:
        for param in input_params:
            temp = {}
            temp['properties'] = {}
            temp['properties'].update(param['properties'])
            temp['properties']['numOfAgents'] = agent_number
            if 'score' in param:
                temp['score'] = param['score']
                temp['previous_score'] = param['score']
            temp['end_time'] = end_times[agent_number]
            configured_params += [temp]       
    return configured_params

    