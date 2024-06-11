import os
import utils.file as files
import test.check as check
import test.utils as utils

def is_compatible_itself(params):
    for param in params:
        assert check.is_compatible_itself(param["properties"]) == True
        

def test():
    params_dir = "pole"
    project_path = files.get_project_path()
    print(f"project_path: {project_path}")
    for file in os.listdir(f'{project_path}/{params_dir}'):
        if not file.endswith("l000.json"):
            print(f"Testing {file}...")
            params = files.load_json(f"{project_path}/{params_dir}/{file}")
            print(f"Loaded {file} successfully...")
            is_compatible_itself(params)


