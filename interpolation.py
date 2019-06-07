import qgis.core
from qgis.analysis import QgsInterpolator, QgsIDWInterpolator, QgsGridFileWriter
from PyQt5.QtCore import QDir
import os
import subprocess
import processing
import glob
from PyQt5.Qt import QMessageBox

class Interpolation():
    
    def __ini__(self):
        self.test = test
    
    def interpolation(self, layer, attribute_for_interpolation, attribute_name, output_dir, resolution):
        #create interpolation-object
        layer_data = QgsInterpolator.LayerData()
        
        layer_data.source=layer
        layer_data.interpolationAttribute=attribute_for_interpolation
        layer_data.valueSource=0
        layer_data.sourceType=0
#         #add the given layer to the interpolation-object
#         layer_data.vectorLayer = layer
#         
#         #use the given attribute instead of the z coordinate for interpolation
#         layer_data.zCoordInterpolation=False
#         layer_data.interpolationAttribute = attribute_for_interpolation
#         layer_data.mInputType = 1
        
        #interpolate the layer
        interpolator = QgsIDWInterpolator([layer_data])
        
        #create the resulting raster
        rect = layer.extent()
        ncol = int((rect.xMaximum() - rect.xMinimum()) / resolution)
        nrows = int((rect.yMaximum() - rect.yMinimum()) / resolution)
        
        #create outut directory
        export_folder = QDir.toNativeSeparators(output_dir + "/batch_interpolation/")
        if not os.path.exists(export_folder):
            os.makedirs(export_folder)
        
        #write raster to file system
        export_path = QDir.toNativeSeparators(export_folder + layer.name() + "_" + attribute_name + ".tif")
        #QMessageBox.about(None,"sss","4")
        output = QgsGridFileWriter(interpolator, export_path, rect, ncol, nrows)
        #QMessageBox.about(None,"sss","5")
        a=output.writeFile()
    
   