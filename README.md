# Python Final Project
This repository is for storing my Python 3200k final project, which is to create a map in the ArcMap program using python script and map data. The map will depict all jails/prisons/correctional facilities within the metro Atlanta area, and will be created using only python script. The end result of this project will be a map that can easily be edited and updated by altering or adding to the script.The data that I accessed to get the correctional facility points was [Georgia Open Data](http://data-georgiagio.opendata.arcgis.com/datasets/d2f6f0dc62204a8cb8dddd9226348d95_4). I got the information for the counties I would be looking at for correctional facilities from [Atlanta Counties](https://www.atlanta.com/county-profiles/). I got the idea to create this map from a similar and more complicated idea created by [Parker Ziegler](https://parkerziegler.com/senior-research-programming-for-gis/2016/3/13/u5n3avnfx1x2qfz3w28f2qhfr6dpd6).

## Workflow
In my first commit, I created the gitignore file.
In my second commit, I added the arcpy and os modules.
Instead of writing my script in ArcMap, I composed it in the python shell so I could test my code without worrying about the program crashing.
My third commit is where I created a file geodatabase for all of my data. I found out later in the coding process that I did not actually need a file geodatabase to complete this project, rendering that particular line of script essentially useless. 
My fourth commit consisted of taking the data I needed and creating layer files from the shapefiles I had. The map I was creating is simple, but the script makes the idea of creating maps even easier.
Once I had created the layers, my fifth commit showed the intersection of the two layers I had created.
After intersecting, my sixth and seventh commits consisted of copying the features into a shapefile format. This commit took two attempts because the first commit didn't do what I needed.
My eighth commit allowed me to spatially join my two topic layers together.
The ninth and tenth commits were a trial and error code run to take the now spatially joined layers and plot the points in their correct county locations. 
My last commits included editing the readme file, updating the gitignore file, and committing my finished .mxd file to my repository. 

### Problems 
The first problem I encountered was where to start. I was under the impression that to create a map using python script, I had to use the python tool within ArcMap. What I realized is that even if the correct code is written in ArcMap's python shell, it will not necessarily run in the Python command line, making it impossible to cmmit the required documents. Instead, I wrote all of my code within the Python IDLE Shell and then tested it in ArcMap. With this method, every line of code worked.  

#### Results
