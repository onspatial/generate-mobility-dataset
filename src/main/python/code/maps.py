import sys
import utils.file  as file
import utils.geo as geo
import utils.geojson as geojson
import utils.myqgis as myqgis
if __name__ == '__main__':
    map_name = 'atlanta'
    output_folder = file.get_project_root() + '/data/output/' + map_name
    print(output_folder)
    bounding_box = geo.get_bounding_box(map_name)
    buildings_geojson = geojson.get_buildings_geojson(bounding_box)
    walkways_geojson = geojson.get_walkways_geojson(bounding_box)
    file.save_geojson(buildings_geojson, output_folder + '/buildings.geojson')
    file.save_geojson(walkways_geojson, output_folder + '/walkways.geojson')
    buildings_shapeFile = myqgis.get_buildings_shapeFile(buildings_geojson)
    walkways_shapeFile = myqgis.get_walkways_shapeFile(walkways_geojson)
    buildingUnits_shapeFile = myqgis.get_buildingUnits_shapeFile(buildings_shapeFile)
    # save them to the output folder
    file.save_shapeFile(buildings_shapeFile, output_folder + '/buildings.shp')
    file.save_shapeFile(walkways_shapeFile, output_folder + '/walkways.shp')
    file.save_shapeFile(buildingUnits_shapeFile, output_folder + '/buildingUnits.shp')
    

