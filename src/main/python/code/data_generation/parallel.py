
from utils.results import get_top_params, get_reviewed_params, get_configured_params,get_initial_parameters
from utils.simulate import run
from utils.params import save_params_to_file

if __name__ == "__main__":
    print("Generating the results...")
    
    input_parameters = get_initial_parameters()
    configured_params = get_configured_params(input_parameters)
    simulated_params = run(configured_params, shuffle=False,fork_join=False, check_time=1000, parallel=8)
    save_params_to_file(simulated_params, f"results/params.simulated.json")
    print("Results Generated successfully!")

