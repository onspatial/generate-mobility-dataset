
import utils.file as file

if __name__ == "__main__":
    print("Python code is running...")
    print(f"File name: {file.get_file_name(__file__)}")
    print(f"File path: {file.get_file_path(__file__)}")
    print(f"File extension: {file.get_file_extension(__file__)}")
    print(f"File size: {file.get_file_size(__file__)}")
    print(f"File exists: {file.exists(__file__)}")
    print(f"Absolute path: {file.get_absolute_path(__file__)}")
    print(f"Directory: {file.get_dir(__file__)}")  
    print("Python code is completed...")
