from make_buildings import *
from make_paths import *
from make_buildingUnits import *
import sys

if __name__=="__main__":
	args=sys.argv[1:]
	if len(args)==1:
		plugpath=args[0]
		inbuild="tbp_maps\\a.geojson"
		inpath="tbp_maps\\b.geojson"
	elif len(args)==2:
		plugpath='C:\\Program Files\\QGIS 3.32.2\\apps\\qgis\\python\\plugins'
		inbuild=args[0]
		inpath=args[1]
	elif len(args)==3:
		plugpath=args[0]
		inbuild=args[1]
		inpath=args[2]
	else:
		plugpath='C:\\Program Files\\QGIS 3.32.2\\apps\\qgis\\python\\plugins' 
		inbuild="tbp_maps\\a.geojson"
		inpath="tbp_maps\\b.geojson"

	makeBuilds(inbuild)
	makeBuildUnits(plugpath,'processed\\buildings.shp')
	makePaths(inpath)
	print('all done')