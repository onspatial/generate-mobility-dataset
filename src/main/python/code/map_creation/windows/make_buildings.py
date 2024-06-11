from qgis.core import *
import qgis.utils
import os
from qgis.PyQt.QtCore import QVariant
import sys
import time

def makeBuilds(inbuild):
	qgs = QgsApplication([], False)
	QgsApplication.setPrefixPath(os.getcwd())
	QgsApplication.initQgis()

	layer = QgsVectorLayer(inbuild,'Buildings layer')
	if not layer.isValid():
		print('layer failed to load!')
		exit(0)
	QgsProject.instance().addMapLayer(layer)
	if 'building' in [x.name() for x in layer.fields()]:
		with edit(layer):
			funcs=[x['building'] for x in layer.getFeatures()]
			fields=[x.name() for x in layer.fields() if x.name()!='building']
			layer.dataProvider().deleteAttributes([layer.fields().indexFromName(x) for x in fields])
			print('just building left')
			layer.dataProvider().addAttributes([QgsField('id',QVariant.Int),QgsField('function',QVariant.Int),QgsField('neighbor',QVariant.Int),QgsField('degree',QVariant.Double)])
			layer.updateFields()
			print('added other fields')

			i=layer.fields().indexFromName('id')
			f=layer.fields().indexFromName('function')
			n=layer.fields().indexFromName('neighbor')
			d=layer.fields().indexFromName('degree')

			for x,y in enumerate(layer.getFeatures()):
				z=funcs[x]
				if (z=='yes' or z=='house' or z=='apartments' or z=='residential' or z=='dormitory'): liveable=1
				else: liveable=2

				layer.changeAttributeValue(y.id(),i,x+1)
				layer.changeAttributeValue(y.id(),f,liveable)
				layer.changeAttributeValue(y.id(),n,0)
				layer.changeAttributeValue(y.id(),d,1)
			print('values changed')
			
		with edit(layer):
			layer.dataProvider().deleteAttributes([layer.fields().indexFromName('building')])
			layer.updateFields()
			print('building removed')

		from_crs=QgsCoordinateReferenceSystem( 'EPSG:4326')
		target_crs = QgsCoordinateReferenceSystem('EPSG:26916')
		context=QgsProject.instance().transformContext()
		save_options = QgsVectorFileWriter.SaveVectorOptions()
		save_options.ct = QgsCoordinateTransform(from_crs,target_crs,context)
		save_options.driverName = 'ESRI Shapefile'
		save_options.fileEncoding = 'UTF-8'
		QgsVectorFileWriter.writeAsVectorFormatV3(layer,'processed\\buildings.shp',context,save_options)
		print('transformed to correct CRS')
		print('exported successfully')
		print('buildings done')
	else: print('input has already been altered')


if __name__ == '__main__':
	args=sys.argv[1:]
	if args: makeBuilds(args[0])
	else: makeBuilds('tbp_maps\\a.geojson')