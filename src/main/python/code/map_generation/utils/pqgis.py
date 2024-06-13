import geopandas as gpd
import utils.constants as constants
import utils.file  as file
import utils.geojson as geojson
import utils.pqgis as pqgis

def get_buildings_shapeFile(buildings_geojson):
    print('Getting buildings shapefile')
    buildings = gpd.read_file(buildings_geojson)
    buildings = buildings[['building', 'geometry']]
    buildings = buildings.to_crs(constants.get_crs())
    buildings['id'] = range(1, len(buildings) + 1)
    buildings['function'] = buildings['building'].apply(lambda x: 1 if x in ['yes', 'house', 'apartments', 'residential', 'dormitory'] else 2)
    buildings['neighbor'] = 0
    buildings['degree'] = 1.0
    buildings = buildings.drop(columns=['building'])
    return buildings

def get_walkways_shapeFile(walkways_geojson):
    print('Getting walkways shapefile')
    walkways = gpd.read_file(walkways_geojson)
    walkways = walkways.to_crs(constants.get_crs())
    walkways = walkways[['geometry']]  
    walkways['id'] = range(1, len(walkways) + 1)
    return walkways

def get_buildingUnits_shapeFile(buildings_shapeFile):
    print('Getting building units shapefile')
    building_units = buildings_shapeFile.copy()
    building_units = building_units.to_crs(constants.get_crs())
    building_units['geometry'] = building_units['geometry'].centroid
    building_units.rename(columns={'id': 'building'}, inplace=True)
    building_units = building_units[['building', 'geometry']]
    return building_units

def generate_map(bounding_box,output_folder, new_map=True):
    
    buildings_geojson_path= output_folder + '/buildings.geojson'
    walkways_geojson_path= output_folder + '/walkways.geojson'
    
    if not file.exists(buildings_geojson_path) or new_map:
        print('Getting buildings geojson from overpass')
        buildings_geojson = geojson.get_buildings_geojson(bounding_box)
        file.save_geojson(buildings_geojson, buildings_geojson_path)

    if not file.exists(walkways_geojson_path) or new_map:
        print('Getting walkways geojson from overpass')
        walkways_geojson = geojson.get_walkways_geojson(bounding_box)
        file.save_geojson(walkways_geojson, walkways_geojson_path)
    
    print('Generating map shapefiles')
    buildings_gdf = pqgis.get_buildings_shapeFile(buildings_geojson_path)
    walkways_shapeFile = pqgis.get_walkways_shapeFile(walkways_geojson_path)
    buildingUnits_shapeFile = pqgis.get_buildingUnits_shapeFile(buildings_gdf)

    print(f'Saving shapefiles to {output_folder}')
    file.save_shapeFile(buildings_gdf, output_folder + '/map/buildings.shp')
    file.save_shapeFile(walkways_shapeFile, output_folder + '/map/walkways.shp')
    file.save_shapeFile(buildingUnits_shapeFile, output_folder + '/map/buildingUnits.shp')