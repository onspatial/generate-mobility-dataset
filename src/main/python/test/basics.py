
import utils.file as file
import utils.constants.params as constants
import utils.params as params
import test.check as check
import test.utils as utils
import utils.log as log



def clean():
    from calibrate import clean_up
    clean_up()
    assert file.exists("params.pool.json") == False
    assert file.exists("pole") == False

def initialize():
    from calibrate import initialization
    initialization()
    assert file.exists("params.pool.json") == True
    assert file.exists("pole") == True

def basics():
    min_param = params.get_processed_param(constants.get_min_param())
    max_param = params.get_processed_param(constants.get_max_param())
    default_param = params.get_processed_param(constants.get_default_param())

    assert min_param["type"] == "check"
    assert utils.is_less(min_param["properties"], max_param["properties"]) == True
    assert utils.is_greater(max_param["properties"], min_param["properties"]) == True
    assert utils.is_equal(min_param["properties"], default_param["properties"]) == False
    assert utils.is_equal(max_param["properties"], default_param["properties"]) == False
    assert utils.is_equal(min_param["properties"], max_param["properties"]) == False

def compatibility():
    min_param = constants.get_min_param()
    max_param = constants.get_max_param()
    assert check.is_compatible_itself(min_param["properties"]) == True
    assert check.is_compatible_itself(max_param["properties"]) == True
    assert check.is_compatible_compared_to(min_param["properties"], max_param["properties"]) == True

def bad_param_fix():
    bad_param = constants.get_bad_param()
    fixed_param = params.get_compatible_param(bad_param)
    assert check.is_compatible_itself(fixed_param["properties"]) == True
    
def fix_param_check():
    min_param = constants.get_min_param()
    max_param = constants.get_max_param()
    default_param = constants.get_default_param()
    min_param_fixed = params.get_compatible_param(min_param)
    max_param_fixed = params.get_compatible_param(max_param)
    default_param_fixed = params.get_compatible_param(default_param) 

    assert utils.is_equal(min_param_fixed["properties"], min_param_fixed["properties"]) == True
    assert utils.is_equal(max_param_fixed["properties"], max_param_fixed["properties"]) == True
    assert utils.is_equal(default_param_fixed["properties"], default_param_fixed["properties"]) == True
    assert check.is_compatible_itself(min_param_fixed["properties"]) == True
    assert check.is_compatible_itself(max_param_fixed["properties"]) == True
    assert check.is_compatible_itself(default_param_fixed["properties"]) == True
    assert check.is_compatible_compared_to(min_param_fixed["properties"], max_param_fixed["properties"]) == True

def function_check():
    fixed_min_param = constants.get_min_param()
    fixed_max_param = constants.get_max_param()
    sample_params = [fixed_min_param, fixed_max_param]
    extended_param = params.get_extended_params(sample_params)
    assert utils.is_equal(extended_param[0]["properties"], fixed_min_param["properties"]) == True
    assert utils.is_equal(extended_param[1]["properties"], fixed_max_param["properties"]) == True
    assert utils.is_equal(extended_param[0], fixed_min_param) == True
    assert utils.is_equal(extended_param[1], fixed_max_param) == True
    top_params = params.get_top_params(sample_params, 1)
    assert utils.is_equal(top_params[0], fixed_max_param) == True
    assert utils.is_equal(top_params[0]["properties"], fixed_max_param["properties"]) == True
    processed_param = params.get_processed_param(fixed_min_param)
    assert utils.is_equal(processed_param["properties"], fixed_min_param["properties"]) == True
    assert processed_param["type"] == "check"
    new_param = params.get_mixed_param(sample_params, "new", 2)
    max_param = params.get_mixed_param(sample_params, "max", 2)
    min_param = params.get_mixed_param(sample_params, "min", 2)
    mean_param = params.get_mixed_param(sample_params, "mean", 2)
    random_param = params.get_mixed_param(sample_params, "random", 2)
    assert check.is_compatible_itself(new_param["properties"]) == True
    assert check.is_compatible_itself(max_param["properties"]) == True
    assert check.is_compatible_itself(min_param["properties"]) == True
    assert check.is_compatible_itself(mean_param["properties"]) == True
    assert check.is_compatible_itself(random_param["properties"]) == True


def test():
    initialize()
    basics() 
    compatibility()
    bad_param_fix()
    fix_param_check()
    function_check()
    file.delete_file("note.log.txt")
    log.note("All basic tests passed successfully...")
    print("All basic tests passed successfully...")
    