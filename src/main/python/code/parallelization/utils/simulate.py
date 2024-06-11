from time import sleep
from utils.constants.params import get_updated_properties
from utils.constants.config import get_jar_path, get_parallel_runs, get_end_time, get_agent_numbers
import utils.file as file
import scorer as pol_score
from random import random
import time
import os
import subprocess
def run(params, shuffle=True, fork_join=True, check_time=6000, parallel=get_parallel_runs(type="dynamic")):
    print(len(params), "params received...")
    if shuffle:
        params = shuffle_params(params)
    configured_params = get_configure_params(params)
    configured_params = run_configured_params(configured_params, fork_join=fork_join, check_time=check_time, parallel=parallel)
    configured_params = get_scored_params(configured_params)
    save_params_to_file(configured_params)
    
    return configured_params

def shuffle_params(params):
    print("shuffling params...")
    return sorted(params, key=lambda x: random())

def run_configured_params(configured_params, parallel=get_parallel_runs(type="not-dynamic"), fork_join=True, check_time=60):
    print(f"running {len(configured_params)} configured params... with fork_join={fork_join}")
    if  fork_join:
        configured_params = run_fork_join(configured_params, parallel)
    else:
        configured_params = run_in_queue(configured_params, parallel, check_time)
    return configured_params

def run_in_queue(configured_params, parallel, check_time=60):
    count = 0
    run_queue = []
    for configured_param in configured_params:
        count += 1
        configured_param["status"] = "running"
        save_configured_param_to_file(configured_param)
        command_dir = get_parent_dir(configured_param["config"])
        if not file.exists(f"{command_dir}/processed.done"):
            run_queue.append(prepare_shell(configured_param, f"{command_dir}/command.sh", append=False))
    run_queue.append(prepare_shell(configured_params[-1], f"{command_dir}/command.sh", append=True, command="wait"))
    process_running(run_queue, parallel, check_time)
  
    return configured_params 

def process_running(run_queue, parallel, check_time=60):

    count = 0
    online_process_dirs = []
    while len(run_queue) > 0:
        if count < parallel:
            process = run_queue.pop(0)
            online_process_dirs.append(process['run_dir'])
            print(f"running {process['run_dir']}...")
            file.run_shell(f'{process["run_dir"]}/command.sh')
            count += 1
        else:
            time.sleep(check_time)
            count -= get_finished_process(online_process_dirs)
        # print("all running processes:\n", '\n'.join(online_process_dirs))
    return run_queue

def get_finished_process(online_process_dirs):
    count = 0
    for run_dir in online_process_dirs:
        print(f"checking {run_dir}...")
        if file.exists(f"{run_dir}/processed.done"):
            online_process_dirs.remove(run_dir)
            count += 1
    print(f"finished {count} processes...")
    return count

def prepare_shell(configured_param, output_path="tmp/run.sh", append=True, command=None):
    file.check_safety(output_path)
    run_path =configured_param['config']["run_sh_path"]
    command = file.add_to_shell(run_path, output_path, append=append, command=command)
    print(f"prepared for run {configured_param['config']['folder']}...")
    run_dir = file.get_parent(run_path)
    respond =  {'run_dir':run_dir,
                'command':command}
    return respond

def run_fork_join(configured_params, parallel):
    count = 0
    for configured_param in configured_params:
        count += 1
        configured_param["status"] = "running"
        save_configured_param_to_file(configured_param)
        prepare_shell(configured_param)
        if(count % parallel == 0 or count == len(configured_params)):
            print(f"running {parallel} shells...")
            run_shells() 

   
    return configured_params 


def run_shells(output_path="tmp/run.sh"):
    print(f"running shell...")
    try:
        file.check_safety(output_path)
        file.add_wait_to_shell(output_path)
        file.run_shell(output_path)
        file.append_file_to(output_path, f"{output_path}.done.sh")
        file.delete_file(output_path)
    except Exception as e:
        print(f"Error running shell: {e}")
        sleep(10)



def get_scored_params(configured_params):
    for configured_param in configured_params:
        configured_param["score"] = pol_score.get_score(file.get_integrated_checkin_path(configured_param['config']["run_sh_path"], integration=False))
    return configured_params
    
def get_configure_params(params):
    configured_params = []
    for param in params:
        configured_param = get_configured_param(param)
        configured_params.append(configured_param)
    return configured_params

def get_configured_param(param):
        configured_param = {}
        param["properties"].update(get_updated_properties())
        if get_agent_numbers() == [182]:
            param["properties"]["numOfAgents"] = 182
        configured_param.update(param)
        configured_param["config"] = {}
        configured_param["config"] = get_config(configured_param)
        configured_param["status"] = "pending"
        if 'end_time' in param and param['end_time'] != None:
            end_time = param['end_time']
        else:
            end_time = get_end_time()
        save_configuration_to_file(configured_param, end_time)
        return configured_param

def get_config(configured_param):
    config = {}
    config["folder"] = get_folder(configured_param)
    config["layer"] = get_layer(configured_param)
    config['run_sh_path'] = get_run_path(config) 

    return config

def get_folder(param):
    return f"{param['id']}"

def get_layer(param):
    return str(param['id']).split("_")[-2]

def get_run_command( end_time=get_end_time(),jar_path=f"{get_jar_path()}"):
    condition = f'if [ -f run.unlock ]; then \n echo "Unlock file exists, exiting" \n else\n'
    string = f"java -Dlog4j2.configurationFactory=pol.log.CustomConfigurationFactory -Dlog.rootDirectory=logs -Dsimulation.test=c01 -jar {jar_path} -configuration modified.properties -until {end_time} \n fi"
    command = f"{condition} \n {string}"
    return command

def get_run_path(config):
    print(f"generating run path for {config['folder']}...")
    parent_dir = get_parent_dir(config)
    run_sh_path = f"{parent_dir}/run.sh"
    return run_sh_path

def get_parent_dir(config):
    project_path = file.get_project_path()
    dir  = f"{project_path}/city/{config['layer']}/{config['folder']}"
    return dir

def save_configuration_to_file(configured_param, end_time=get_end_time()):
    parent_dir = get_parent_dir(configured_param["config"])
    file.save_properties_to_file(configured_param["properties"], f"{parent_dir}/modified.properties")
    file.save_string_to_file(get_run_command(end_time), configured_param["config"]["run_sh_path"])
    file.save_json(configured_param, f"{parent_dir}/config.json")

def save_params_to_file(configured_params):
    for configured_param in configured_params:
        save_configured_param_to_file(configured_param)

def save_configured_param_to_file(configured_param):
    parent_dir = get_parent_dir(configured_param["config"])
    file.save_json(configured_param, f"{parent_dir}/config.json")