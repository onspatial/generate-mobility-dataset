import utils.constants.params as constants
import test.utils as utils
import test.fixes as fixes
import utils.log as log

   
def is_bound_compatible_compared_to(min, max):
    test_result = True
    lower_upper_pairs = constants.get_bound_pairs()
    for lower_bound, upper_bound in lower_upper_pairs:
        if min[upper_bound] >= max[lower_bound]:
            log.note(f"min[{upper_bound}] >= max[{lower_bound}]!")
            test_result = False
            return test_result
    return test_result

def is_bound_compatible(properties):
    test_result = True
    lower_upper_pairs = constants.get_bound_pairs()
    for lower_bound, upper_bound in lower_upper_pairs:
        if utils.is_greater(properties[lower_bound], properties[upper_bound]):
            log.note(f"{lower_bound}: {properties[lower_bound]} >= {upper_bound}: {properties[upper_bound]}")
            test_result = False
            return test_result
    return test_result
    

def is_uniform_compatible(properties):
    test_result = True
    uniform_properties = constants.get_uniform_properties() 
    for key in uniform_properties.keys():
        if utils.is_uniform(properties[key]) == False:
            log.note(f"{key}: {properties[key]} != {uniform_properties[key]}")
            test_result = False
            return test_result
    return test_result
    

def is_fixed_values_compatible(properties):
    test_result = True
    fixed_properties = constants.properties_fixed
    for key in fixed_properties.keys():
        if utils.is_valid(key) and properties[key] != fixed_properties[key]:
            log.note(f"{key}: {properties[key]} != {fixed_properties[key]}")
            test_result = False
            return test_result
    return test_result

def is_less_than_min(properties):
    min_properties = constants.get_min_properties()
    test_result = True
    for key in properties:
        if utils.is_less(properties[key], min_properties[key]):
            log.note(f"{key}: {properties[key]} < {min_properties[key]}")
            test_result = False
            return test_result
    return test_result

def is_greater_than_max(properties):
    max_properties = constants.get_max_properties()
    test_result = True
    for key in properties:
        if utils.is_greater(properties[key], max_properties[key]):
            log.note(f"{key}: {properties[key]} > {max_properties[key]}")
            test_result = False
            return test_result
    return test_result

def is_range_compatible(dict):
    ranges = constants.get_value_ranges()
    for key in ranges:
        if utils.is_in_range(dict[key], ranges[key]) == False:
            log.note(f"key: {key}, value: {dict[key]}, min: {ranges[key]['min']}, max: {ranges[key]['max']}")
            return False
    return True

def is_value_compatible(properties):
    test_result = True
    test_result = is_range_compatible(properties)
    return test_result

def is_global_compatible(properties):
    test_result = True
    for key in properties:
        if utils.is_valid(key):
            if utils.is_global(properties[key]) == False:
                log.note(f"{key}: {properties[key]}")
                return False
    return test_result  

def is_compatible_itself(properties):
 
    assert is_less_than_min(properties)
    assert is_greater_than_max(properties)
    assert is_fixed_values_compatible(properties)
    assert is_bound_compatible(properties)
    assert is_uniform_compatible(properties)
    assert is_value_compatible(properties)
    assert is_range_compatible(properties)
    assert is_global_compatible(properties)
    return True

def is_compatible_compared_to(min, max):
    test_result = True
    if is_bound_compatible_compared_to(min, max) == False:
        log.note(f"min and max are not compatible pairs")
        test_result = False
        return test_result
    return test_result




