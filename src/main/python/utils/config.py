from utils.params import get_mixed_param, add_type_to_params, add_id_to_params, shuffle_params, save_params_to_file
from utils.helpers import get_random_list
from utils.constants.config import get_layer_width, get_num_of_each_params_type


def get_max_params(params,number_of_params):
    return  [get_mixed_param(params, type="max",number_of_random_parents=i) for i in get_random_list(number_of_params)]

def get_min_params(params,number_of_params):
    return  [get_mixed_param(params, type="min", number_of_random_parents=i) for i in get_random_list(number_of_params)]

def get_mean_params(params,number_of_params):
    return  [get_mixed_param(params, type="mean",number_of_random_parents=i) for i in get_random_list(number_of_params)]

def get_random_params(params,number_of_params):
    return  [get_mixed_param(params,type="random", number_of_random_parents=i) for i in get_random_list(number_of_params)]

def get_sum_params(params,number_of_params):
    return  [get_mixed_param(params,type="sum", number_of_random_parents=i) for i in get_random_list(number_of_params)]

def get_new_params(params,number_of_params):
    return  [get_mixed_param(params, type="new") for i in get_random_list(number_of_params)]

def get_params(params,type="max", num_of_params=5):
    mixed_params = []
    if type == "max":
        mixed_params = get_max_params(params,num_of_params)
    elif type == "min":
        mixed_params = get_min_params(params,num_of_params)
    elif type == "mean":
        mixed_params = get_mean_params(params,num_of_params)
    elif type == "random":
        mixed_params = get_random_params(params,num_of_params)
    elif type == "sum":
        # we decided to not use sum (04-15-2024)
        mixed_params = get_sum_params(params,num_of_params)
    elif type == "new":
        mixed_params = get_new_params(params,num_of_params)
    else:
        mixed_params = get_new_params(params,num_of_params)
            
    mixed_params = add_type_to_params(mixed_params, type)
    return mixed_params

def get_reset_score(params):
    for param in params:
        param["score"] = 0
    return params

def get_layer_params(params, id, num_of_each_params_type=get_num_of_each_params_type()):
    max_params = get_params(params,type="max", num_of_params=num_of_each_params_type)
    min_params = get_params(params, type="min", num_of_params=num_of_each_params_type)
    mean_params = get_params(params, type="mean", num_of_params=num_of_each_params_type)
    random_params = get_params(params, type="random", num_of_params=num_of_each_params_type)
    new_params = get_params(params, type="new", num_of_params=num_of_each_params_type)
    mixed_params = max_params + min_params + mean_params + random_params  + new_params
    mixed_params = add_id_to_params(mixed_params, id)
    mixed_params = shuffle_params(mixed_params)[:get_layer_width()]
    mixed_params = get_reset_score(mixed_params)
    save_params_to_file(mixed_params, f"pole/params.{id}.json")
    return mixed_params