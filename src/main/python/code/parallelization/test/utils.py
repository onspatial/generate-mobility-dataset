
import utils.constants.params as constants

def is_equal(input1, input2):
    if is_dict(input1) and is_dict(input2):
        for key in input1:
            try:
                if input1[key] != input2[key]:
                    return False
            except:
                return False
    elif is_number(input1) and is_number(input2):
        return input1 == input2
    else:
        return False
    return True

def is_greater(input1, input2):
    if is_dict(input1) and is_dict(input2):
        for key in input1:
            try:
                if input1[key] <= input2[key]:
                    return False
            except:
                return False
    elif is_number(input1) and is_number(input2):
        return input1 > input2
    else:
        return False
    
    return True

def is_less(input1, input2):
    if is_dict(input1) and is_dict(input2):
        for key in input1:
            try:
                if input1[key] >= input2[key]:
                    return False
            except:
                return False
    elif is_number(input1) and is_number(input2):
        return input1 < input2
    else:
        # print(f"is_less: {input1}, {input2} not numbers")
        return False
    return True

def is_uniform(value):
    try:
        if value < 0 or value > 1:
            return False
    except:
        return False
    return True

def is_in_range(value, range):
    try:
        if value <= range['min'] or value >= range['max']:
            return False
    except:
        return False
    return True

def is_global(value):
    global_values = constants.get_global_values()
    try:
        if not is_number(value):
            return False
        if value < global_values['min'] or value > global_values['max']:
            return False
    except:
        return False
    return True

def is_dict(input):
    return isinstance(input, dict)

def is_number(input):
    return isinstance(input, (int, float))

def is_valid(key):
    valid = True
    global_values = constants.get_global_values()
    if key in global_values["exceptions"]:
        valid = False
    return valid

def get_other_bound(key):
    pairs = constants.get_bound_pairs()
    for pair in pairs:
        lower_bound = pair[0]
        upper_bound = pair[1]
        if key == lower_bound:
            return upper_bound
        if key == upper_bound:
            return lower_bound
    return None

def is_agent_id(agent_id_df):
    test_result = True
    for id in agent_id_df:
        if int(id) != int(id)/1:
            print(f"AgentID {id} is not of type int.")
            test_result = False
            return test_result
    return test_result

def is_latitude(latitude_df):
    test_result = True
    for latitude in latitude_df:
        if not float(latitude) >= -90 and float(latitude) <= 90:
            print(f"Latitude {latitude} does not have a valid value.")
            test_result = False
            return test_result
    return test_result

def is_longitude(longitude_df):
    test_result = True
    for longitude in longitude_df:
        if not float(longitude) >= -180 and float(longitude) <= 180:
            print(f"Longitude {longitude} does not have a valid value.")
            test_result = False
            return test_result
    return test_result

def is_time(time_df):
    import pandas
    test_result = True
    for time in time_df:
        try:
            pandas.to_datetime(time, format='%Y-%m-%d,%H:%M:%S')
        except:
            print(f"Time {time} does not have a valid value.")
            test_result = False
            return test_result
    return test_result