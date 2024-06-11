from utils.config import get_layer_params
from utils.params import initialization, save_params_to_file, get_pool_params, update_pool
from utils.simulate import run
import utils.file as file
from utils.constants.config import get_layer_width
from test.middle import test as test_middle
from test.basics import test as test
def clean_up():
    pass
    # file.delete_file("params.pool.json")
    # file.delete_folder("pole")
    # file.delete_folder("city")
    # file.delete_folder("tmp")

if __name__ == "__main__":
    print("Calibration is running...")
    try:
        clean_up()
    except:
        pass
    timestamp = 530000 + get_layer_width()
    print(f"Calibration started at {timestamp}...")
    # initialization(timestamp)
    # test()
    print("Initialization completed...")
    layer_level = 0
    layer_params = []
    while layer_level < 100:
        layer_level += 1
        run_id=f't{timestamp}_l{str(layer_level).zfill(3)}'
        print(f"Running calibration with run_id: {run_id}...")
        pool_params = get_pool_params()       
        layer_params = get_layer_params(pool_params, run_id)
        # test_middle()
        layer_params = run(layer_params, fork_join=False, check_time=100,parallel=8)
        save_params_to_file(layer_params, f"pole/params.{run_id}.json")
        update_pool(pool_params, layer_params, layer_level)
    print(f"Calibration completed successfully with {layer_level} iterations...")