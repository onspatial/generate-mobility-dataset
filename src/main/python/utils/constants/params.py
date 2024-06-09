import utils.file as file
import utils.constants.config as config
from utils.helpers import get_pairs
import os
current_dir = os.path.dirname(__file__)
properties_updates ={
        "maps": config.get_maps_dir(),
        "seed": 1,
}

properties_fixed ={
        "numOfAgents":182,
        "maps": "maps/nola/map",
        "seed": 1,
}


def get_default_param():
    return file.read_json(f"{current_dir}/json/param.default.json")

def get_sample_param():
    return file.read_json(f"{current_dir}/json/param.sample.json")

def get_init_param():
    return file.read_json(f"{current_dir}/json/param.init.json")

def get_min_param():
    return file.read_json(f"{current_dir}/json/param.min.json")

def get_max_param():
    return file.read_json(f"{current_dir}/json/param.max.json")

def get_bad_param():
    return file.read_json(f"{current_dir}/json/param.bad.json")

def get_uniform_properties():
    return file.read_json(f"{current_dir}/json/properties.uniform.json")

def get_default_properties():
    return get_default_param()["properties"]

def get_init_properties():
    return get_init_param()["properties"]

def get_min_properties():
    return get_min_param()["properties"]

def get_max_properties():
    return get_max_param()["properties"]

def get_updated_properties():
    return properties_updates


def get_bound_pairs():
    return get_pairs(file.read_json(f"{current_dir}/json/pairs.bound.json"))

def get_value_ranges():
    return file.read_json(f"{current_dir}/json/ranges.value.json")

def get_global_values():
    return file.read_json(f"{current_dir}/json/global.value.json")

param_default = get_default_param()


def get_useless_properties():
    global_variable = get_global_values()
    useless_properties = global_variable["useless_properties"]
    return useless_properties
