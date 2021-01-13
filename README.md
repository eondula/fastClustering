# Fast Clustering
This project attempts to demystify the nuanced
complexities as observed from a prototype software model that can be used to initiate the learning
component of a neural network architecture assumed to be in control of content from public server. 
In this case any remote [CARLA](http://carla.org/) server.

## Mobility Model:


## How are vehicles simulated?

Vehicles are simulated using AUTOCAST system which produces the intersection scenario.
Vehicle drivers are implemented as artificial agents tasked with driving carla car models.
If vehicle is not CH and granted access to cluster 
then it will replicate its memory to all the nodes on the cluster
Otherwise, the vehicle will have to retry again. The state of the vehicle will also change

## How is communication simulated?
CARLA lacks network modules to enable simulation of communication. In this research, NS-3 is proposed to
be used as the network simulator. Though this work hasn't initially started as of date (Nov 15, 2020).
Instead of using NS-3 though, MQTT will be used as the transport protocol between the

## How clustering implemented and source code to clustering?

For this current version of the application, Emna Daknou fast clustering algorithm will be implemented.
 
Emna Daknou paper, the system has the following stages:
- Discovery
- Cluster Formation
- Cluster Head Election
- Recovery
- 

What is hard is estimating the states of a node. 
## What is the scenario and experiment?

"""
