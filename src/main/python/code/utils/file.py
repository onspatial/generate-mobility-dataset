import os
import json
import sys
from qgis.PyQt.QtCore import QVariant
from qgis.core import QgsVectorFileWriter
from qgis.core import QgsField
from qgis.core import QgsCoordinateReferenceSystem

def get_project_root():
    return os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))))

    
def save_geojson(geojson, file_path):
    check_existence(file_path)
    with open(file_path, 'w') as f:
        f.write(json.dumps(geojson))

def check_existence(file_path, delete=True):
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))
    if os.path.exists(file_path) and delete:
        os.remove(file_path)
    if not os.path.exists(file_path):
        os.system('touch ' + file_path)

def save_shapeFile(layer, file_path):
    check_existence(file_path)
    QgsVectorFileWriter.writeAsVectorFormat(layer, file_path, 'UTF-8', layer.crs(), 'ESRI Shapefile')
    
