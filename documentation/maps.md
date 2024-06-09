# New Map Creation Guide

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
