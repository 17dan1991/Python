# -*- coding: utf-8 -*-

'''

@Author: Daniel Ibáñez Campos
@Date: 22/02/2018
@Edited 17/02/2020

This file contains a function which allows the user to check if a shapefile is 
projected in the British National Grid. If it is not, the function re-project
it into a new shapefile with an appropriate name and returns the name of the
new re-projected shapefile. Also, this function is useful "to assign the correct
coordinate system for a dataset that has an incorrect coordinate system defined".
The function permanently assigns the correct coordinate system to the dataset.

'''
# ===================================== Imports ======================================= #

# Import all necessary libraries here
import arcpy
import os
import sys
from arcpy.sa import *

# ===================================== Functions ======================================= #
# It defines the function. 'BNG' is the acronym for the British National Grid
def projection_BNG():
    # Create a list of all feature classes (shapefiles) in the dataset folder
    feature_classes = arcpy.ListFeatureClasses() 
    # Loop through the list created previously
    for fc in feature_classes:
        # For all shp located in the dataset folder, it creates the spatial reference object
        spatial_ref = arcpy.Describe(fc).spatialReference
        # It tells the user if the shapefile is projected in the British National Grid.
        if spatial_ref.name == "British_National_Grid":
            print ("{0} is already projected in the British National Grid".format(fc))
        # If the shp is not projected in the British National Grid, it will be re-projected
        else:
            # Give the name to the new shapefile
            outName = os.path.splitext(fc)[0] + "_BNG.shp"
            # The new re-projected shapefile will be created into the 'output' folder
            fcProject = os.path.join(outDir, outName) 
            # Call project tool from ArcGIS
            # Defines the output coordinate system, in this case, the British National Grid
            out_coordinate_system = arcpy.SpatialReference("British National Grid")
            # Tool imported from ArcGIS to reproject the shapefiles into the British National Grid
            arcpy.Project_management(fc, fcProject, out_coordinate_system)
            # This tells the user where to find the new re-projected shapefile
            path = "{0} created".format(fcProject, outDir)
            # This tells the user the new shapefile's name 
            print outName + " is the new name of the re-projected shapefile"
            print path
           
# ====================================== Main script ====================================== #
# The script execution starts here

# Tells the user that the script starts here
print "Script starting"
# Tells the user to wait while the script is running and performing the geoprocess
print "I am running the script, please wait"

# Set up the workspace environment
# Overwrite files by default to avoid Windows locking the files when the script runs
arcpy.env.overwriteOutput = True
# Set the workspace environment setting
arcpy.env.workspace = r"C:\Users\17dan\OneDrive\Desktop\f1_data"
# Where to find or create (if it does not exist) the 'output' data
outDir = r"C:\Users\17dan\OneDrive\Desktop\f1_data"


# Call the function here
print projection_BNG()

# Tell the user the script has finished
print "Script finished"