import utils.file as file
import pandas

def check_sorted_column(file_path, time_column=0):
    data = file.get_dataframe(file_path,sample=20000000)
    column = data.iloc[:, time_column]
    column = column.dropna()
    print(column.head())
    result = True
    result = column == sorted(column)
    result = all(result == True)
    print(f"Column {time_column} is sorted: {result}")
    return result