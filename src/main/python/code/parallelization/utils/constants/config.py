def get_min_parents():
    min_number_of_random_parents = 2
    return min_number_of_random_parents

def get_max_parents():
    max_number_of_random_parents =64
    return min(max_number_of_random_parents , get_layer_width())

def get_pool_size():
    pool_size = 200
    return pool_size

def get_layer_width():
    layer_width = 128
    return layer_width

def get_num_of_each_params_type():
    num_of_each_params_type = max(8, get_layer_width())
    return num_of_each_params_type

def get_end_time(type="final"):
    end_time = 100
    if type == "final":
        end_time = 551426
    elif type == "test":
        end_time = 100
    return end_time
def get_weak_score(counter=1):
    perfect_score = 0.98
    worst_score = 0.01
    smoothness = 0.01
    weak_score = worst_score + (counter * smoothness)
    if weak_score > perfect_score:
        weak_score = perfect_score
    print(f"weak_score: {weak_score}, counter: {counter}")
    return weak_score

def get_jar_path():
    import os
    current_path = os.path.abspath(__file__)
    project_path = get_project_path()
    jar_path = f"{project_path}/pol/jar/pol.jar"

    return jar_path
def get_parallel_runs(type="dynamic"):
    parallel_runs = 64
    if type == "dynamic":
        parallel_runs = min(parallel_runs, get_layer_width())
    else:
        print(f"WARNING: Parallel runs are set to {parallel_runs} without checking the layer width.")
    return parallel_runs



def get_maps_dir():
    maps_dir = "../../../pol/maps/bjng/map/"
    return maps_dir

def get_project_path():
    import os
    current_path = os.path.abspath(__file__)
    project_path = current_path.split("/code")[0]
    return project_path

def get_bounding_box(city="bjng"):
    import utils.constants.bounding_box as bounding_box
    if city == "bjng":
        return bounding_box.bjng
    else:
        return bounding_box.default

def get_float_keys():
    import utils.constants.params as params
    float_keys = []
    default_properties = params.get_default_properties()
    for key in default_properties:
        if type(default_properties[key]) == float:
            float_keys.append(key)
    return float_keys

def get_agent_numbers(type="results"):
    if type == "results":
        agent_numbers = [182, 1000, 5000, 10000, 50000, 100000]
    elif type == "calibration":
        agent_numbers = [182]
    return agent_numbers

def get_end_times():
    agent_numbers = get_agent_numbers(type='results')
    times = [551426, 551426, 551426, 551426//5, 551426//5, 551426//10]
    # times = [100, 100, 100, 100//5, 100//5, 100//10]
    end_times = {}
    for i, agent_number in enumerate(agent_numbers):
        end_times[agent_number] = times[i]
    return end_times
 