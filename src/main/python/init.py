from  utils.constants.params  import get_default_properties, get_init_param
from utils.constants.config import get_pool_size
from utils.params import save_params_to_file, get_from_json
from utils.config import get_new_params
from time import sleep
from utils import file
# run1 is the initial run with richard parameters (904 runs in total)
# run2 is the second run with the wrong statistic calculation which is another run (512 runs in total)
def get_properties_run1(line):
    properties = line.split(":")[0]
    properties = properties.split("_")
    keys = get_default_properties().keys()
    values = properties[1::2]
    values = values[:-1]
    values = [float(value) for value in values]
    values = [round(value, 3) for value in values]
    properties = dict(zip(keys, values))
    
    return properties

def get_random_params(num):
    params = []
    params = get_new_params(params, num)
    return params

def get_score(line, type="tuple"):
    score = 0
    if type == "simple":
        score = get_score_simple(line)
    elif type == "tuple":
        score = get_score_from_tuple(line)

    if not score == float(score):
        print(f"score is not a float: {score}")
        score = -113.0
    return score
def get_score_simple(line):
    score = line.split(":")[-1]
    score = float(score)
    score = round(score, 5)
    return score
def get_score_from_tuple(line):
    score_tuple = line.split(":")[-1]
    # (225.11222597063704, -1.2511222597063703)
    score = score_tuple.split(",")[-1]
    score = score[:-1]
    score = float(score)
    score = round(score, 5)
    return score

def get_params_run_1(lines):
    params = []
    for line in lines:
        properties = get_properties_run1(line)
        score = get_score(line)
        params.append(dict(properties=properties, score=score))

    return params

def get_previous_params_run2():
    json_files = file.get_files("pole/params.t22_*.json")
    params = []
    for json_file in json_files:
        param = get_from_json(json_file)
        params += param
    save_params_to_file(params, "params.run2.json")
    return params
def get_updated_params_run_2(lines):
    previous_params = get_previous_params_run2()
    id_score = {}
    for line in lines:
        id = line.split(":")[0]
        score = get_score(line, type="tuple")
        id_score[id] = score
    params = []
    for param in previous_params:
        for id in id_score.keys():
            if param["id"] == id:
                param["score"] = id_score[id]
                # if it has 'config' key, delete it
                if "config" in param.keys():
                    del param["config"]
                if 'status' in param.keys():
                    del param['status']
                params.append(param) 
    return params

def get_lines(filename):
    with open(filename) as f:
        lines = f.readlines()
    return lines

def process_lines_run1(lines):
    print("Warning: the function process_lines_run1 is processing the path of the file to get the name of the dataset. This is a bad practice. But I will keep it since it is not the focus of the project.")
    processed_lines = []
    for line in lines:
        line = line.strip()
        path = line.split(":")[0]
        score = line.split(":")[-1]
        name = path.split("/")[-3]
        line = name + ":" + score
        processed_lines.append(line)

    return processed_lines

def process_lines_run2(lines):
    processed_lines = []
    for line in lines:
        line = line.strip()
        path = line.split(":")[0]
        score = line.split(":")[-1]
        id = path.split("/")[-4]
        line = id + ":" + score
        processed_lines.append(line)

    return processed_lines

def get_params_from_txt(filename="score.log.txt"):
    params1 = []
    params2 = []
    lines = get_lines(filename)
    if filename == "score.log.txt":
        lines= process_lines_run1(lines)
        params1 = get_params_run_1(lines)
    if filename == "score2.log.txt":
        lines= process_lines_run2(lines)
        params2 = get_updated_params_run_2(lines)
    params = params1 + params2
    return params

def save_init_params():
    if file.exists("score.log.txt"):
        params = get_params_from_txt("score.log.txt")
        save_params_to_file(params, "params.init.json")
    else:
        params =get_random_params(get_pool_size())
        save_params_to_file(params, "params.init.json")
        print("score.log.txt does not exist")



def describe_params(params):
    scores = [param["score"] for param in params]
    scores = sorted(scores)
    print(f"Min: {scores[0]}")
    print(f"Max: {scores[-1]}")
    print(f"len: {len(scores)}")
    print(f"unique: {len(set(scores))}")
    unique_scores = set(scores)
    print(f"useful scores: {len([score for score in scores if score > 80])}")
    print(f"useful scores: {len([score for score in unique_scores if score > 80])}")
   
def diff_properties(param1, param2, similarity_counter):
    properties1 = param1["properties"]
    properties2 = param2["properties"]
    score1 = param1["score"]
    score2 = param2["score"]
    diff_param = {}
    diff_param["properties"] = {}
    diff_param["score"] = score1 - score2
    add = False
    for key in properties1.keys():
        diff_param["properties"][key] = properties1[key] - properties2[key]
        if diff_param["properties"][key] == 0 and param1["id"] != param2["id"]:
            # print(f"key: {key} is the same for both params")
            # print(f"param1 id: {param1['id']}")
            # print(f"param2 id: {param2['id']}")
            add=True
            similarity_counter["properties"][key] += 1
    if add:
        similarity_counter["score"] += 1
    diff_param["id"] = [param1["id"], param2["id"]]
    return diff_param

def diff_score(param1, param2, similarity_counter):

    if param1["score"] == param2["score"]:
        return diff_properties(param1, param2, similarity_counter)
    
def remove_known_properties(params):
    # known_keys = ["numOfAgents", "appetiteLowerBound", "appetiteUpperBound"]
    known_keys = ["numOfAgents"]
    for param in params:
        for key in known_keys:
            if key in param["properties"]:
                del param["properties"][key]

    return params

def check_similarity(params):
    describe_params(params)
    params = remove_known_properties(params)
    similarity_counter = get_init_param()
    diffs = []
    for param1 in params:
        for param2 in params:
            diff = diff_score(param1, param2, similarity_counter)
            # diffs.append(diff)
            # sleep(1)
    save_params_to_file(similarity_counter, "similarity_counter.json")
    save_params_to_file(diffs, "params.diff.json")


if __name__ == "__main__":
    params = get_params_from_txt("score2.log.txt")
    save_params_to_file(params, "params.init2.json")
    # params = get_from_json("params.init2.json")
    # params = add_id_to_params(params, "init2")

    