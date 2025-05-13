# The Pattern of Life Human Mobility Simulation 

- Comparision of POL with real world data:

    

    <div style="display:inline-block; ">
        <img src="https://github.com/user-attachments/assets/7f2d5248-8887-4461-a2ee-4d1539f16b66" alt="Pattern of life simulation data" style="width: 400px; height: 400px;">
        <p>Figure 1: The above chart presents the Pattern of life simulation data</p>
    </div>
    <div style="display:inline-block;">
        <img src="https://github.com/user-attachments/assets/7664d1e7-6dad-4336-8068-7d5605d9e3bb" alt="Travel survey realworld" style="width: 400px; height: 400px;">
        <p>Figure 2: This is Travel survey that is drawn from realworld data</p>
    </div>

Here we use the Chord Diagram to have an overall comparison of the simulated activities with the activities from US National Household Travel Survey  (https://nhts.ornl.gov/). The Chord Diagram shows the proportion of each type of trip between different types of activities. From the real-world travel survey, we reclassified the trip purposes into comparable groups. In our simulation, we considered the activities locations as home, workplaces, restaurants, and recreational sites; then, the Chord Diagram gives a global view of the generated trip flows with purpose and size. For these categories, we observe that the flows are quite similar to those observed in the travel survey: Both charts show that home is the most visited location followed by work. The flow from/to restaurants is overestimated in our simulation, but this can be attributed to not modeling “buy goods”'. A similar picture is seen for recreation, which is over-estimated in our simulation, but if we include “other errands”, we would get a similar picture as observed in the travel survey.    

We note that the comparison is city based, which means we filter out the San Francisco city wide trips from the national household travel survey to validate. Also we can validate from other aspects like the distribution of travel time and distance, and trip frequency by person. 






## YouTube Videos - Silent Video; Live Demonstration after Acceptance
- [Running the Graphical User Interface (GUI)](https://youtu.be/YaabLKM4mxQ)
- [Running the Headless Simulation (Data Generation)](https://youtu.be/oFIu5CAjnnc)
- [ Customize the map and generate a new map from overpass using python or QGIS ](https://youtu.be/YwuOIQZ_jBk)
- [Customize the simulation parameters](https://youtu.be/IDG7sjz5JwE)
- [Running the simulation in parallel](https://youtu.be/aBgjLmmpMd4)



## Theory and Background
This simulation models the Maslowian needs of agents (i.e., people) which drive agents’ actions and behaviors:Agents need to go home to find shelter overnight; Agents need togo to work to make money (i.e., financial balance); Agents need togo to restaurants to eat; and Agents need to go to recreational sites to meet friends and sustain their social network. Many more facets of the logic driving the behavior of agents in the Patterns of Life simulation can be found in: [Urban life: a model of people and places](https://link.springer.com/article/10.1007/s10588-021-09348-7).

## Requirements and Installation
To run the simulation, you need to have the dependencies installed. The simulation is written in Java and requires Java 8 or higher. The simulation is built using the Maven build system. To install the dependencies, you can run the [mvn.sh](mvn.sh) script. If you run the script for the first time, you need to run the script using `bash mvn.sh full` to install the local dependencies as well as the dependencies from the Maven repository. This will create a pol.jar file and store it in `jar/` directory.


## Running the Graphical User Interface (GUI)
To run the GUI of the simulation, you can run the [WorldModelUI.java](src/main/java/pol/WorldModelUI.java) file. The GUI will open and you can see the simulation running. You can also change the parameters of the simulation using the GUI. The GUI is built using the Java Swing library.
This Youtube video provides a demonstration of the GUI: [Running the Graphical User Interface (GUI)](https://youtu.be/YaabLKM4mxQ). 

## Running the Headless Simulation (Data Generation)
To run the headless simulation, you can run the [run.sh](headless/run.sh) script. The script will run the simulation and generate the data. You can modify this file to customize the simulation input, output, and parameters.

- `-Dlog.rootDirectory=data`: Specifies that the generated data will be stored in the `data` directory.

- `-Dsimulation.test=all` : Specifies that the simulation will logs all the data. This can be customized in the [ReservedLogChannels.java](src/main/java/pol/log/ReservedLogChannels.java) file.

- `-jar ../jar/pol.jar`: Specifies the path to the simulation jar file.

- `-configuration modified.properties`: This option can be used to customized the simulation's parameters. To customize the simulation and change the default parameters, you can modify the [modified.properties](headless/modified.properties) file. The simulation default parameters are stored in the [parameters.properties](parameters.properties) file.

- `-until 2880`: Specifies the number of steps the simulation will run. In this case, the simulation will run for 2880 steps. Each step is specified in the [parameters.properties](parameters.properties) file. The default step is 5 minutes. In this case the simulation will run for 2880 * 5 minutes = 14400 minutes = 240 hours = 10 days.

This Youtube video provides a demonstration of the headless simulation: [Running the Headless Simulation (Data Generation)](https://youtu.be/oFIu5CAjnnc).
    

## Customize the Map and the Simulation Parameters

### New Map:
The simulation uses a map to simulate the agents' movement. The map is stored in three different shapefiles: `buildings.shp`, `walkways.shp`, and `buildingUnits.shp`. You can generate any mpa by using the documentation on the [maps.md](documentation/maps.md) file. 
You can use the QGIS software to visualize and edit the map or we developed a python script to generate the map. The script is shown in the [maps.py](src/main/python/code/map_generation/maps.py) file. 

This is a simple example of how to generate a map using the script:
```python
output_folder = 'data/maps/test'
bounding_box = [-84.41213984, 33.72878582, -84.36418537, 33.76304255]
pqgis.generate_map(bounding_box, output_folder, new_map=True)
```
This Youtube video provides a demonstration of how to generate a new map using both QGIS and the python script: [ Customize the map and generate a new map from overpass using python or QGIS ](https://youtu.be/YwuOIQZ_jBk).

### Simulation Parameters:
The simulation parameters are stored in the [parameters.properties](parameters.properties) file. You can customize the simulation parameters by modifying this file. It is recommended to use another file to modify the parameters and keep the original file unchanged as a reference and default parameters. 

An example of the modification is shown in the [modified.properties](headless/modified.properties) file. You can use this file to customize the simulation parameters. The modified file is used in the [run.sh](headless/run.sh) script to run the simulation with the customized parameters. 
This is an example of how to modify the parameters:

```properties
numOfAgents = 500
seed = 2
maps = maps/atl/map
```

The modified file will be specified in the [run.sh](headless/run.sh) script using the `-configuration modified.properties` option.

This is the run.sh script with the modified file:
```bash
java -Dlog4j2.configurationFactory=pol.log.CustomConfigurationFactory -Dlog.rootDirectory=data -Dsimulation.test=all -jar ../jar/pol.jar -configuration modified.properties -until 2880
```

This Youtube video provides a demonstration of how to customize the simulation parameters: [Customize the simulation parameters](https://youtu.be/IDG7sjz5JwE).

## Dataset Generation
After the simulation is run, the data is stored in the directory specified in the `-Dlog.rootDirectory` option. When data is generated, the simulation will split them into different files based on their size. Some logs store more features and might need to be cut from the dataset. For example, the `agentStateTable.tsv` file stores the state of each agent at each time step. This file can be very large and might need to be cut into smaller files. To generate the trajectory of each agent, we need to cut the location, time and agent ID from the `agentStateTable.tsv` file. 
This data processing can be done using the [integrate.py](src/main/python/code/data_generation/integrate.py) script. This script will generate the trajectory of each agent and store it in a new file.

## Performance Improvement and Parallelization

To improve the performance and accelerate the data generation process, we make the simulation more efficient by making some changes to the simulation code without changing the simulation logic. 

The simulation itself is not parallelized, but we can run multiple instances of the simulation in parallel to generate the data with different parameters or the same parameters.

This is an example of how to run the simulation in parallel using the [parallel.py](src/main/python/code/data_generation/parallel.py) script:

```python
input_parameters = params.get_from_json('params.init.json')
input_parameters = params.add_id_to_params(input_parameters, "input")
simulated_params = run(input_parameters, fork_join=False, check_time=100, parallel=8)
params.save_params_to_file(simulated_params, f"params.simulated.json")
print("Results Generated successfully!")
```

This Youtube video provides a demonstration of how to run the simulation in parallel: [Running the simulation in parallel](https://youtu.be/aBgjLmmpMd4).

##  Performance Evaluation

Since running the simulation in parallel does not change the simulation time, we can evaluate the performance improvement here of a single simulation instance. We initially run the simulation for 10 days (14400 minutes) with different numbers of agents. The simulation is run on an Intel Core i7-6700HQ CPU with 24GB of RAM. We compare the time taken by Vanilla simulation and the optimized simulation. The results are shown in the following table:

The results are reported for two distinct phases: the initialization and the simulation. Initialization time refers to the duration required to set up the simulation and the agents, while simulation time indicates the length of time the simulation runs, measured over a period of 10 days. We compare the Vanilla simulation against the optimized simulation, which includes performance enhancements. Data is presented for varying numbers of agents, with time reported in minutes and seconds. Additionally, results are included for scenarios where agents can exit the simulation based on predefined conditions. The value -1 indicates that the simulation did not complete within a reasonable time frame or we terminated the simulation.

| | vanilla_exit_on | |vanilla_exit_off| | enhanced_exit_on| | enhanced_exit_off| |
|-------|-----------------|-----------------|-----------------|-----------------|--------------|--------------|---------------|---------------|
|Agents | initialization |Simulation |initialization |Simulation |initialization |Simulation |initialization |Simulation |
1000|33.22 s|10.3 min|30.67 s|15.24 min|8.66 s|1.27 min|4.91 s|1.03 min
2000|1.95 min|36.21 min|1.42 min|51.52 min|11.57 s|1.97 min|11.06 s|1.99 min
3000|2.6 min|1.36 hour|2.17 min|1.94 hour|19.13 s|3.09 min|20.93 s|3.06 min
4000|4.23 min|2.97 hour|4.15 min|3.58 hour|35.29 s|4.79 min|35.63 s|5.3 min
5000|4.61 min|3.69 hour|5.74 min|4.33 hour|48.83 s|5.68 min|52.99 s|5.82 min
6000|5.65 min|5.53 hour|6.36 min|8.75 hour|1.25 min|7.28 min|1.1 min|7.14 min
7000|8.75 min|8.8 hour|8.7 min|10.9 hour|1.72 min|9.16 min|1.75 min|9.29 min
8000|8.86 min|10.57 hour|9.81 min|15.25 hour|2.38 min|11.36 min|2.41 min|11.45 min
9000|9.94 min|14.29 hour|10.64 min|13.58 hour|2.89 min|15.73 min|2.96 min|20.0 min
10000|13.87 min|15.8 hour|13.02 min|16.71 hour|3.27 min|14.73 min|3.29 min|14.69 min
11000|14.27 min|19.58 hour|12.35 min|18.75 hour|3.67 min|17.48 min|3.7 min|17.45 min
12000|16.31 min|22.91 hour|17.59 min|25.22 hour|4.74 min|20.79 min|4.88 min|22.45 min
13000|17.85 min|25.85 hour|19.33 min|27.78 hour|6.66 min|25.66 min|5.8 min|24.14 min
14000|25.71 min|32.6 hour|27.39 min|34.29 hour|7.92 min|28.31 min|7.39 min|28.31 min
15000|24.12 min|35.45 hour|22.8 min|41.24 hour|8.74 min|32.56 min|8.04 min|28.92 min
16000|25.96 min|41.48 hour|25.93 min|-1|10.27 min|37.55 min|9.78 min|34.74 min
17000|27.48 min|-1|-1|-1|10.06 min|31.53 min|11.06 min|33.46 min
18000|-1|-1|-1|-1|10.9 min|34.78 min|10.99 min|35.49 min
19000|-1|-1|-1|-1|11.12 min|36.76 min|11.95 min|37.67 min
20000|-1|-1|-1|-1|12.8 min|40.73 min|11.18 min|36.94 min
21000|-1|-1|-1|-1|14.41 min|42.78 min|14.05 min|43.53 min
22000|-1|-1|-1|-1|15.73 min|49.85 min|13.06 min|45.05 min
23000|-1|-1|-1|-1|17.18 min|51.75 min|17.09 min|52.38 min
24000|-1|-1|-1|-1|17.67 min|53.24 min|18.57 min|55.11 min
25000|-1|-1|-1|-1|18.91 min|56.73 min|19.27 min|58.04 min
26000|-1|-1|-1|-1|21.25 min|59.12 min|21.41 min|58.23 min
27000|-1|-1|-1|-1|22.34 min|1.08 hour|22.85 min|1.08 hour
28000|-1|-1|-1|-1|20.67 min|1.03 hour|24.96 min|1.16 hour
29000|-1|-1|-1|-1|25.71 min|1.29 hour|25.84 min|1.28 hour
30000|-1|-1|-1|-1|33.83 min|1.46 hour|33.28 min|1.48 hour
31000|-1|-1|-1|-1|48.04 min|2.01 hour|51.17 min|1.97 hour
32000|-1|-1|-1|-1|33.72 min|1.46 hour|35.67 min|1.51 hour
33000|-1|-1|-1|-1|35.1 min|1.71 hour|35.9 min|1.71 hour
34000|-1|-1|-1|-1|30.52 min|1.57 hour|31.64 min|1.64 hour
35000|-1|-1|-1|-1|37.55 min|1.62 hour|32.6 min|1.49 hour
36000|-1|-1|-1|-1|38.14 min|1.66 hour|37.88 min|1.68 hour
37000|-1|-1|-1|-1|40.55 min|1.74 hour|40.49 min|1.68 hour
38000|-1|-1|-1|-1|42.38 min|1.86 hour|42.69 min|1.88 hour
39000|-1|-1|-1|-1|44.34 min|1.91 hour|43.78 min|1.9 hour
40000|-1|-1|-1|-1|40.13 min|1.78 hour|46.82 min|2.0 hour
41000|-1|-1|-1|-1|49.56 min|2.03 hour|49.33 min|2.06 hour
42000|-1|-1|-1|-1|50.74 min|2.14 hour|50.85 min|2.08 hour
43000|-1|-1|-1|-1|53.79 min|2.22 hour|53.25 min|2.26 hour
44000|-1|-1|-1|-1|1.29 hour|3.06 hour|1.3 hour|3.0 hour
45000|-1|-1|-1|-1|1.0 hour|2.7 hour|1.03 hour|2.8 hour
46000|-1|-1|-1|-1|1.24 hour|2.75 hour|1.21 hour|2.7 hour
47000|-1|-1|-1|-1|1.02 hour|2.55 hour|1.03 hour|2.63 hour
48000|-1|-1|-1|-1|1.04 hour|2.64 hour|1.04 hour|2.55 hour
49000|-1|-1|-1|-1|1.07 hour|2.7 hour|1.12 hour|2.84 hour
50000|-1|-1|-1|-1|1.15 hour|2.69 hour|1.06 hour|2.71 hour
51000|-1|-1|-1|-1|59.39 min|2.6 hour|1.21 hour|3.09 hour
55000|-1|-1|-1|-1|2.01 hour|3.98 hour|1.92 hour|3.83 hour
60000|-1|-1|-1|-1|1.8 hour|4.14 hour|1.76 hour|4.13 hour
65000|-1|-1|-1|-1|1.86 hour|4.41 hour|1.56 hour|3.95 hour
70000|-1|-1|-1|-1|2.15 hour|5.15 hour|2.25 hour|5.23 hour
75000|-1|-1|-1|-1|2.51 hour|5.65 hour|2.49 hour|5.61 hour
80000|-1|-1|-1|-1|2.39 hour|5.9 hour|2.73 hour|6.34 hour
85000|-1|-1|-1|-1|3.33 hour|7.46 hour|3.26 hour|7.1 hour
90000|-1|-1|-1|-1|3.73 hour|8.1 hour|3.57 hour|7.43 hour
95000|-1|-1|-1|-1|4.08 hour|8.83 hour|3.9 hour|8.69 hour
100000|-1|-1|-1|-1|4.37 hour|9.0 hour|4.52 hour|9.39 hour
105000|-1|-1|-1|-1|5.04 hour|11.24 hour|5.1 hour|10.92 hour
110000|-1|-1|-1|-1|5.47 hour|11.64 hour|5.85 hour|11.59 hour
115000|-1|-1|-1|-1|5.54 hour|12.18 hour|5.65 hour|12.64 hour
120000|-1|-1|-1|-1|6.12 hour|13.08 hour|6.36 hour|13.42 hour
125000|-1|-1|-1|-1|6.93 hour|15.8 hour|6.66 hour|14.65 hour
130000|-1|-1|-1|-1|7.39 hour|14.79 hour|6.27 hour|12.98 hour
140000|-1|-1|-1|-1|9.8 hour|19.66 hour|9.61 hour|18.56 hour
150000|-1|-1|-1|-1|9.65 hour|19.29 hour|9.83 hour|20.15 hour
160000|-1|-1|-1|-1|11.42 hour|-1|9.68 hour|-1




