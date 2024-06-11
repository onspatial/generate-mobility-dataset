from time import sleep
from random import random
import utils.file as file
def run(params, fork_join=False, check_time=100, parallel=1, shuffle=True, **kwargs):
    print(len(params), "params received...")
    for param in params:
        score = random()
        param["score"] = score 
        print(f"running {param['id']} with score: {score}")


    # sleep(5)  
    print("sample run completed...")
    return params   