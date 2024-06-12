import utils.pqgis as pqgis

if __name__ == '__main__':
    # map_name = 'test'
    # bounding_box = geo.get_bounding_box(map_name)
    # output_folder = 'data/output/' + map_name 
    output_folder = 'data/maps/test'
    bounding_box = [-84.41213984, 33.72878582, -84.36418537, 33.76304255]
    pqgis.generate_map(bounding_box, output_folder, new_map=True)
    print('Map generated successfully')
    
    

