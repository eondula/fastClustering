# cs-651-research-project
## How are vehicles simulated?

Vehicles are simulated using AUTOCAST system which produces the intersection scenario.
Vehicle drivers are implemented as artificial agents tasked with driving carla car models.
If vehicle is not CH and granted access to cluster 
then it will replicate its memory to all the nodes on the cluster
Otherwise, the vehicle will have to retry again. The state of the vehicle will also change

## How is communication simulated?
CARLA lacks network modules to enable simulation of communication. In this research, NS-3 was proposed to
be used as the network simulator. Though this work hasn't initially started as of date (Nov 15, 2020)

## How clustering implemented and source code to clustering?

For this current version of the application, Emna Daknou fast clustering algorithm will be implemented.
 
Emna Daknou paper, the system has the following stages:
- Discovery
- Cluster Formation
- Cluster Head Election
After today's meeting, I got the questions below to answer so that my research can start making sense
As I piece this paper together:
See clustering.py for implementation.

## What is the scenario and experiment?

"""