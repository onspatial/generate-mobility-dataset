import utils.pqgis as pqgis

if __name__ == '__main__':
    
    bounding_box = [-84.41213984, 33.72878582, -84.39418537, 33.73304255]
    output_folder = 'headless/maps/test'

    pqgis.generate_map(bounding_box, output_folder, new_map=True)

    print('Map generated successfully!')