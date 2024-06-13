import os
import json


    
def save_geojson(geojson, file_path):
    make_sure_exists(file_path, delete=True)
    with open(file_path, 'w') as f:
        f.write(json.dumps(geojson))

def make_sure_exists(file_path, delete=False):
    path = get_absolute_path(file_path)
    if not exists(path):
        os.makedirs(get_parent_folder(path), exist_ok=True)
    if not exists(path):
        os.system(f"touch {path}")

    if exists(file_path) and delete:
        os.remove(file_path)

def save_shapeFile(geo_dataframe, file_path,crs='EPSG:26916'):
    make_sure_exists(file_path, delete=True)
    geo_dataframe.to_file(file_path, driver='ESRI Shapefile', encoding='utf-8', crs=crs)

def get_parent_folder(file_path):
    if file_path[-1] == '/':
        return file_path
    elif file_path.split("/")[-1].find(".") == -1:
        return file_path
    return os.path.dirname(file_path)

def exists(file_path):
    return os.path.exists(file_path)

def get_absolute_path(path):
    if not path.startswith("/"):
        root = get_project_path()
        path = f"{root}/{path}"
    return path

def get_project_path():
    current_path = os.path.abspath(__file__)
    if current_path.find("/src") == -1:
        print("Error: Your project must have a src folder as root")
        return current_path
    project_path = current_path.split("/src")[0]
    return project_path