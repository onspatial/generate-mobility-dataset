import test.utils as utils
def check_common_columns(input_df, concerned_df, sorted=False):
    test_result = True
    common_columns = set(input_df.columns) & set(concerned_df.columns)
    if not common_columns:
        print("No common columns found.")
        test_result = False
        return test_result
    common_columns = list(common_columns)
    if not sorted and not input_df[common_columns].equals(concerned_df[common_columns]):
        print("Common columns are not equal.")
        print(f"input_df columns are {input_df.columns}. concerned_df columns are {concerned_df.columns}.")
        test_result = False
        return test_result
    return test_result

def check_number_of_rows(input_df, concerned_df, polished):
    length = len(input_df) == len(concerned_df)
    test_result = True
    if not length and polished:
        print("Lengths are not equal.")
        print(f"input_df has {len(input_df)} rows. concerned_df has {len(concerned_df)} rows.")
        test_result = False
        return test_result
    
    return test_result

def check_columns_names(concerned_df):
    test_result = True
    expected_columns = ['AgentID', 'ArrivingTime', 'Latitude', 'Longitude', 'Distance']
    columns = list(concerned_df.columns)
    if not columns == expected_columns:
        print("names of columns are not equal.")
        print(f"concerned_df columns are {columns}.")
        print(f"columns should be {expected_columns}.")
        test_result = False
        return test_result
    return test_result

def check_columns_type(concerned_df):
    test_result = True
    if not utils.is_agent_id(concerned_df['AgentID']):
        print("AgentID column is not of type int.")
        test_result = False
        return test_result
    if not utils.is_latitude(concerned_df['Latitude']):
        print("Latitude does not have a valid value.")
        test_result = False
        return test_result
    if not utils.is_longitude(concerned_df['Longitude']):
        print("Longitude does not have a valid value.")
        test_result = False
        return test_result
    if not utils.is_time(concerned_df['ArrivingTime']):
        print("ArrivingTime does not have a valid value.")
        test_result = False

    return test_result

def check_columns_content(concerned_df, sorted=False, polished=False):
    test_result = True
    # agent id and time should be sorted
    expected_df = concerned_df.sort_values(by=['AgentID', 'ArrivingTime'], inplace=False)
    if sorted and not concerned_df.equals(expected_df):
        print("AgentID and ArrivingTime are not sorted.")
        test_result = False
        return test_result
    if sorted and polished:
        expected_df.reset_index(drop=True, inplace=True)
        if expected_df['index'].equals(concerned_df['index']):
            print("Index is not reset.")
            test_result = False
            return test_result      

    
    return test_result  

def check_dfs(input_df, concerned_df, sorted=False, polished=False):
    assert check_number_of_rows(input_df, concerned_df, polished) == True
    assert check_common_columns(input_df, concerned_df, sorted) == True
    assert check_columns_names(concerned_df) == True
    assert check_columns_type(concerned_df) == True
    assert check_columns_content(concerned_df, sorted, polished) == True
    print("All tests passed successfully.")