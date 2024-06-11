from qgis.core import QgsVectorLayer, QgsProject
from qgis.PyQt.QtCore import QVariant
from qgis.core import QgsField
from qgis.core import QgsFields
from qgis.core import QgsFeature



def get_buildings_shapeFile(buildings_geojson):
    buildings = QgsVectorLayer('Polygon?crs=epsg:4326', 'buildings', 'memory')
    buildings.startEditing()
    buildings.dataProvider().addAttributes([QgsField('id', QVariant.Int), QgsField('function', QVariant.Int), QgsField('neighbor', QVariant.Int), QgsField('degree', QVariant.Double)])
    buildings.updateFields()
    for i, feature in enumerate(buildings_geojson['features']):
        if feature['geometry']['type'] == 'Polygon':
            buildings.dataProvider().addFeature(feature['geometry'])
            buildings.changeAttributeValue(i, 0, i + 1)
            buildings.changeAttributeValue(i, 1, 1 if feature['properties']['building'] in ['yes', 'house', 'apartments', 'residential', 'dormitory'] else 2)
            buildings.changeAttributeValue(i, 2, 0)
            buildings.changeAttributeValue(i, 3, 1)
    buildings.commitChanges()
    return buildings

def get_walkways_shapeFile(walkways_geojson):
    walkways = QgsVectorLayer('LineString?crs=epsg:4326', 'walkways', 'memory')
    walkways.startEditing()
    walkways.dataProvider().addAttributes([QgsField('id', QVariant.Int), QgsField('highway', QVariant.String)])
    walkways.updateFields()
    for i, feature in enumerate(walkways_geojson['features']):
        if feature['geometry']['type'] == 'LineString':
            walkways.dataProvider().addFeature(feature['geometry'])
            walkways.changeAttributeValue(i, 0, i + 1)
            walkways.changeAttributeValue(i, 1, feature['properties']['highway'])
    walkways.commitChanges()
    return walkways

def get_buildingUnits_shapeFile(buildings_shapeFile):
    buildingUnits = QgsVectorLayer('Point?crs=epsg:4326', 'buildingUnits', 'memory')
    buildingUnits.startEditing()
    buildingUnits.dataProvider().addAttributes([QgsField('id', QVariant.Int), QgsField('building_id', QVariant.Int)])
    buildingUnits.updateFields()
    for i, feature in enumerate(buildings_shapeFile.getFeatures()):
        building = feature.geometry()
        centroid = building.centroid()
        buildingUnits.dataProvider().addFeature(QgsFeature(QgsFields(), QgsFeature([i + 1, i + 1]), centroid))
    buildingUnits.commitChanges()
    return buildingUnits
