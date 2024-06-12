
import overpass
def get_buildings_geojson(bounding_box):
    overpass_query = f'way["building"]({bounding_box[1]},{bounding_box[0]},{bounding_box[3]},{bounding_box[2]});'
    return get_geojson_from_overpass(overpass_query)

def get_walkways_geojson(bounding_box):
    overpass_query = f'way["highway"]({bounding_box[1]},{bounding_box[0]},{bounding_box[3]},{bounding_box[2]});'
    
    return get_geojson_from_overpass(overpass_query)

def get_geojson_from_overpass(overpass_query):
    api = overpass.API()
    response = api.get(overpass_query,responseformat = "geojson", verbosity = "geom")
    return response
