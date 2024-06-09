from  utils.constants.config import get_min_parents, get_max_parents
import numpy
def get_random_list(n, min=get_min_parents(), max=get_max_parents()):
    from random import randint
    random_list = []
    for i in range(n):
        random_list.append(randint(min, max))
    return random_list


def get_pairs(dict):
    pairs = []
    for key, value in dict.items():
        pairs.append((key, value))
    return pairs


def get_json_compatible_dict(data):
    try:
        cleaned_data = get_cleaned_dict(data)
        return cleaned_data
    except Exception as e:
        print(f"Error in getting json compatible dict: {e}")
        return data

def get_cleaned_dict(data):
    cleaned_data = {}
    for key, value in data.items():
        if isinstance(value, dict):
            cleaned_data[key] = get_cleaned_dict(value)
        elif isinstance(value, str):
            cleaned_data[key] = value
        elif isinstance(value, int):
            cleaned_data[key] = value
        elif isinstance(value, float):
            cleaned_data[key] = value
        elif isinstance(value, bool):
            cleaned_data[key] = value
        elif value is None:
            cleaned_data[key] = None
        elif isinstance(value, numpy.int64):
            cleaned_data[key] = int(value)
        elif isinstance(value, numpy.float64):
            cleaned_data[key] = float(value)
        else:
            cleaned_data[key] = str(value)
    return cleaned_data