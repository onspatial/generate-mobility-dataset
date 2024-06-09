import utils.constants.params as constants
import test.utils as utils
import utils.log as log

def fixed_values_properties(properties):
    log.note(f"before: fixed_values_properties:\n" + str(properties))
    fixed_properties = constants.properties_fixed
    properties.update(fixed_properties)
    log.note(f"after: fixed_values_properties:\n" + str(properties))
    return properties

def bound_properties(properties):
    log.note(f"before: bound_properties:\n" + str(properties))
    lower_upper_pairs = constants.get_bound_pairs()
    default_properties = constants.get_default_properties()
    for lower_bound, upper_bound in lower_upper_pairs:
        if utils.is_greater(properties[lower_bound], properties[upper_bound]) == True:
            properties[lower_bound] = default_properties[lower_bound]
            properties[upper_bound] = default_properties[upper_bound]
    log.note(f"after: bound_properties:\n" + str(properties))
    return properties

def uniform_properties(properties):
    log.note(f"before: uniform_properties:\n" + str(properties))
    default_properties = constants.get_default_properties()
    uniform_properties = constants.get_uniform_properties() 
    for key in uniform_properties.keys():
        if utils.is_uniform(properties[key]) == False:
            properties[key] = default_properties[key]
    log.note(f"after: uniform_properties:\n" + str(properties))
    return properties

def range_properties(properties):
    log.note(f"before: range_properties:\n" + str(properties))
    ranges = constants.get_value_ranges()
    default_properties = constants.get_default_properties()
    for key in ranges:
        if utils.is_in_range(properties[key], ranges[key]) == False:
            properties[key] = default_properties[key]
    log.note(f"after: range_properties:\n" + str(properties))
    return properties

def global_properties(properties):
    log.note(f"before: global_properties:\n" + str(properties))
    default_properties = constants.get_default_properties()
    for key in properties:
        if utils.is_global(properties[key]) == False:
            properties[key] = default_properties[key]
    log.note(f"after: global_properties:\n" + str(properties))
    return properties

def less_than_min_properties(properties):
    log.note(f"before: less_than_min_properties:\n" + str(properties))  
    min_properties = constants.get_min_properties()
    default_properties = constants.get_default_properties()
    for key in properties:
        if utils.is_less(properties[key], min_properties[key]) == True:
            print(f"{key}: {properties[key]} < {min_properties[key]}")
            properties[key] = default_properties[key]
    log.note(f"after: less_than_min_properties:\n" + str(properties))  
    return properties

def greater_than_max_properties(properties):
    log.note(f"before: greater_than_max_properties:\n" + str(properties))
    max_properties = constants.get_max_properties()
    default_properties = constants.get_default_properties()
    for key in properties:
        if utils.is_greater(properties[key], max_properties[key]) == True:
            print(f"{key}: {properties[key]} > {max_properties[key]}")
            properties[key] = default_properties[key]
    log.note(f"after: greater_than_max_properties:\n" + str(properties))
    return properties


def fix_key(key):
    return 0