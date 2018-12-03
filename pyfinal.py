#NAME: Metro ATL Correctional Facilities
#Description: To create a map that depicts all the counties within Metro Atlanta
#and also shows the different jails/prisons/correctional facilities within the metro area.
#The purpose of this script is to create this map in ArcMap without manually creatingt the map.
#By doing this with Python script, it allows the map to be easily edited and updated.
#Author: Devon Cox

import arcpy
import os

from arcpy import env
env.workspace = r"P:\f2018\PythonFinalProject\FinalProject"
env.overwriteOutput = True
print "Env is set to ATL_Correctional_Facilities"

out_folder_path = r"P:\f2018\PythonFinalProject\FinalProject"
out_name = "ATL_Correctional_Facilities.gdb"
arcpy.CreateFileGDB_management(out_folder_path, out_name)
print "Geodatabase created."

cicf = arcpy.MakeFeatureLayer_management("Correctional_Institution_Community_Facilities.shp",
                                         "Correctional_Institution_Community_Facilities_lyr")
print "ATL_Correctional_Facilities layer created."

matl = arcpy.MakeFeatureLayer_management("MetroCounties_ATL.shp",
                                         "MetroCounties_ATL")
print "ATL_Metro_Counties layer created."

arcpy.SelectLayerByLocation_management("Correctional_Institution_Community_Facilities_lyr",
                                       "INTERSECT", "MetroCounties_ATL")
print "Intersecting features selected."

arcpy.CopyFeatures_management("Correctional_Institution_Community_Facilities_lyr", "Metro_ATL_lyr")
print "Features copied to shapefile."

target_features = "Correctional_Institution_Community_Facilities_lyr"
join_features = "MetroCounties_ATL.shp"
outfc = "metroATL_facility_join"

arcpy.SpatialJoin_analysis(target_features, join_features, outfc)
print "Facility points have been added to county location."


