# New Map Creation Guide ([YouTube Video](https://youtu.be/YwuOIQZ_jBk))
You can use the source code in [maps.py](src/main/python/code/map_generation/maps.py) to create map programmatically or follow the instructions in below to create a map manually. 

The simulation needs three files for a map and each of these files carries specific information; the `buildings.shp` file contains building footprints, the `buildingUnits.shp` file holds details about building units, and the `walkways.shp` file provides information on the transportation network.

The instructions below were adhered to in order to create the Atlanta map. It's crucial to mention that other applications and resources are available for extracting and modifying Open Street Map (OSM) data. Importantly, the feature set needs to be compatible with the simulation, and the data type should be consistent with what we describe here.

## Steps to create **`buildings.shp`**:

1. Go to https://overpass-turbo.eu/ and run the query, `[out:json][timeout:25]; ( way["building"]({{bbox}}); ); out body; >; out skel qt;`
1. Export the data to `GeoJSON` and download it to your local machine
1. Open the geojson file with `QGIS`
1. Open the `Attribute Table` of the loaded layer. You should see many features. We are interested in some of them and we need to create new features.
1. Keep the `building` feature and delete the rest
1. Add the features we are interested in such as `id` (Integer64), `function` (Integer64), `neighbor` (Integer64), `degree` (Double)

1. Update `id` with `@row_number` or your preferred identification mechanism;
1. Update `function` with `if(building='yes' OR building='house' OR building='apartments' OR building='residential'  OR building='dormitory', 1, 2)`; this indicates the functionality of the building (1: residential, 2: non-residential)
1. Update `neighbor` with `0`
1. Update `degree` with `1`
1. Delete the `building` field
1. Export the features as `buildings.shp` while `EPSG:26916 - NAD83 / UTM zone 16N` is selected for `CRS`

## Steps to create **`buildingUnits.shp`**:

1. Use the data of `buildings.shp` or the generated layer from from step 2
1. Go to `Vector -> Geometry Tools -> Centroids` and Run the algorithm on the layer
1. Rename `id` to `building` and delete the rest.
1. Export the generated layer as `buildingUnits.shp` ,`EPSG:26916 - NAD83 / UTM zone 16N` will stay the same for CRS.

## Steps to create **`walkways.shp`**:

1. Go to https://overpass-turbo.eu/ and run the query, `[out:json][timeout:25]; ( way["highway"]({{bbox}}); ); out body; >; out skel qt;`
1. Export the data to GeoJSON and download it to your local machine
1. Open the geojson file with `QGIS`
1. Delete all the fields and create an `id`
1. Update `id` with `@row_number` or your preferred identification mechanism;
1. Export the features as `walkways.shp` while `EPSG:26916 - NAD83 / UTM zone 16N` is selected for `CRS`

## Commnets on Beijin

1. if you have the bounding box you can replace `({{bbox}})` with your bonding box. e.g. (39.784,116.165, 40.038, 116.628) where used for Beijing

2. Go to Processing Toolbox -> Vector geometry -> Fix geometries and run the algorithm for the building layer

## Comment on San Francisco

1. banding box is: (37.708269684354526, -122.51901626586914, 37.81385247479046, -122.35301971435545)

## Comment on Atlanta Metropolitan

1. Map should be bounded by area larger than the metropolitan area.
1. We need to specify the metropolitan area: `[out:json][timeout:25]; ( area["name"="Atlanta"]; way(area)["building"]({{bbox}}); ); out body; >; out skel qt;`
1. For walkways: `[out:json][timeout:25]; ( area["name"="Atlanta"]; way(area)["highway"]({{bbox}}); ); out body; >; out skel qt;`


## More information o maps:

1. ### Coordinate System and Banding box for  atl-metro  Map
- - atl-metro crs EPSG:26916
- - atl-metro bounding box [ 726963.64370556 3726077.56970387  751091.96204231 3752640.96802056]
- - atl-metro bounding box [-84.5505285   33.64708314 -84.28945431  33.88663263]

1. ### Coordinate System and Banding box for  atl  Map
- - atl crs EPSG:26916
- - atl bounding box [ 739753.1287531  3735138.94979865  744126.37599493 3738988.87861298]
- - atl bounding box [-84.41213984  33.72878582 -84.36418537  33.76304255]

1. ### Coordinate System and Banding box for  bjng  Map
- - bjng crs EPSG:26916
- - bjng bounding box [-1530814.0466859  15287104.43689024 -1485442.08874541 15325111.97593248]
- - bjng bounding box [116.1632651  39.7831364 116.6294095  40.039197 ]

1. ### Coordinate System and Banding box for  brln  Map
- - brln crs EPSG:26916
- - brln bounding box [ 4910432.5903579  10873249.99566397  4914620.5780151  10877877.13977944]
- - brln bounding box [13.3656432 52.5066516 13.4174008 52.5323714]

1. ### Coordinate System and Banding box for  gmu  Map
- - gmu crs EPSG:32046
- - gmu bounding box [2336457.26610402  424084.05071667 2342158.19053227  427917.38261183]
- - gmu bounding box [-77.31851683  38.82516657 -77.29851636  38.83568792]

1. ### Coordinate System and Banding box for  nola  Map
- - nola crs EPSG:26782
- - nola bounding box [2398574.84619401  468770.44186372 2407662.59702521  474692.2898364 ]
- - nola bounding box [-90.0747321   29.94990921 -90.04599532  29.96606048]

1. ### Coordinate System and Banding box for  sfco  Map
- - sfco crs EPSG:26910
- - sfco bounding box [ 542780.10759459 4173570.61894116  556587.40211016 4184960.10238093]
- - sfco bounding box [-122.51419799   37.70829506 -122.35784432   37.8108725 ]
