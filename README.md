# The Pattern of Life Human Mobility Simulation (Demo Paper)

1. ## Theory and Background
This simulation models the Maslowian needs of agents (i.e., people) which drive agents’ actions and behaviors:Agents need to go home to find shelter overnight; Agents need togo to work to make money (i.e., financial balance); Agents need togo to restaurants to eat; and Agents need to go to recreational sites to meet friends and sustain their social network. Many more facets of the logic driving the behavior of agents in the Patterns of Life simulation can be found in: [Urban life: a model of people and places](https://link.springer.com/article/10.1007/s10588-021-09348-7).

1. ## Requirements and Installation
To run the simulation, you need to have the dependencies installed. The simulation is written in Java and requires Java 8 or higher. The simulation is built using the Maven build system. To install the dependencies, you can run the [mvn.sh](mvn.sh) script. If you run the script for the first time, you need to run the script using `bash mvn.sh full` to install the local dependencies as well as the dependencies from the Maven repository. This will create a pol.jar file and store it in `jar/` directory.


1. ## Running the Graphical User Interface (GUI)
To run the GUI of the simulation, you can run the [WorldModelUI.java](src/main/java/pol/WorldModelUI.java) file. The GUI will open and you can see the simulation running. You can also change the parameters of the simulation using the GUI. The GUI is built using the Java Swing library.
This Youtube video provides a demonstration of the GUI: [Running the Graphical User Interface (GUI)](https://youtu.be/YaabLKM4mxQ). 

1. ## Running the Headless Simulation (Data Generation)
To run the headless simulation, you can run the [run.sh](headless/run.sh) script. The script will run the simulation and generate the data. You can modify this file to customize the simulation input, output, and parameters.

    - `-Dlog.rootDirectory=data`: Specifies that the generated data will be stored in the `data` directory.

    - `-Dsimulation.test=all` : Specifies that the simulation will logs all the data. This can be customized in the [ReservedLogChannels.java](src/main/java/pol/log/ReservedLogChannels.java) file.

    - `-jar ../jar/pol.jar`: Specifies the path to the simulation jar file.

    - `-configuration modified.properties`: This option can be used to customized the simulation's parameters. To customize the simulation and change the default parameters, you can modify the [modified.properties](headless/modified.properties) file. The simulation default parameters are stored in the [parameters.properties](parameters.properties) file.

    - `-until 2880`: Specifies the number of steps the simulation will run. In this case, the simulation will run for 2880 steps. Each step is specified in the [parameters.properties](parameters.properties) file. The default step is 5 minutes. In this case the simulation will run for 2880 * 5 minutes = 14400 minutes = 240 hours = 10 days.

This Youtube video provides a demonstration of the headless simulation: [Running the Headless Simulation (Data Generation)](https://youtu.be/oFIu5CAjnnc).
    

1. ## Customize the Map and the Simulation Parameters

### New Map:
The simulation uses a map to simulate the agents' movement. The map is stored in three different shapefiles: `buildings.shp`, `walkways.shp`, and `buildingUnits.shp`. You can generate any mpa by using the documentation on the [maps.md](documentation/maps.md) file. 
You can use the QGIS software to visualize and edit the map or we developed a python script to generate the map. The script is shown in the [maps.py](src/main/python/code/maps.py) file. 

This is a simple example of how to generate a map using the script:
```python
output_folder = 'data/maps/test'
bounding_box = [-84.41213984, 33.72878582, -84.36418537, 33.76304255]
pqgis.generate_map(bounding_box, output_folder, new_map=True)
```
### Simulation Parameters:
The simulation parameters are stored in the [parameters.properties](parameters.properties) file. You can customize the simulation parameters by modifying this file. The parameters are used to specify the agents' behavior, the map, etc.

1. ## Performance Improvement and Parallelization



