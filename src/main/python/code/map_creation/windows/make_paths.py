from qgis.core import *
import qgis.utils
import os
from qgis.PyQt.QtCore import QVariant
import sys

def makePaths(inpath):
	qgs = QgsApplication([], False)
	QgsApplication.setPrefixPath(os.getcwd())
	QgsApplication.initQgis()

	layer = QgsVectorLayer(inpath,'Paths layer')
	if not layer.isValid():
		print('layer failed to load!')
		exit(0)
	QgsProject.instance().addMapLayer(layer)
	with edit(layer):
		layer.deleteFeatures([feat.id() for feat in layer.getFeatures() if feat.geometry().wkbType()!=QgsWkbTypes.LineString])
		layer.dataProvider().deleteAttributes([layer.fields().indexFromName(field.name()) for field in layer.fields()])
		layer.dataProvider().addAttributes([QgsField('id',QVariant.LongLong)])
		layer.updateFields()
		for x,y in enumerate(layer.getFeatures()):
			layer.changeAttributeValue(y.id(),layer.fields().indexFromName('id'),x+1)
		
	QgsProject.instance().removeMapLayer(layer)
	layer = QgsVectorLayer(inpath,'Paths layer')
	if not layer.isValid():
		print('layer failed to reload!')
		exit(0)
	QgsProject.instance().addMapLayer(layer)

	from_crs=QgsCoordinateReferenceSystem( 'EPSG:4326')
	target_crs = QgsCoordinateReferenceSystem('EPSG:26916')
	context=QgsProject.instance().transformContext()
	save_options = QgsVectorFileWriter.SaveVectorOptions()
	if layer.crs().authid()!='EPSG:26916': save_options.ct = QgsCoordinateTransform(from_crs,target_crs,context)
	save_options.driverName = 'ESRI Shapefile'
	save_options.fileEncoding = 'UTF-8'
	QgsVectorFileWriter.writeAsVectorFormatV3(layer,'processed\\walkways.shp',context,save_options)
	print('transformed to correct CRS')
	print('exported successfully')
	print('walkways done')

if __name__ == '__main__':
	args=sys.argv[1:]
	if args: makePaths(args[0])
	else: makePaths('tbp_maps\\b.geojson')