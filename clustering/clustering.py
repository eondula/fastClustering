"""
After today's meeting, I got the questions below to answer so that my research can start making sense
As I piece this paper together:

How are vehicles simulated?
Vehicles are implemented as artificial agents tasked with driving carla car models. Autocast system uses

How is communication simulated?
How clustering implemented and source code to clustering?
What is the scenario and experiment?
Consider

TODO: Formatting and Editing
# Clustering Method:
 - Once consensus on identity is reached, then go to clustering module
 -
Distributed Clustering Protocol

I'm considering clustering protocols in the context of vehicular networks (autonomous vehicles).

As a grouping mechanism I'll consider nodes as autonomous vehicle objects. Each group is assigned a
name and location. Note that the group consists of mobile nodes transmitting over the same channel.
A channel is broker to which a cluster publishes (transmits) to and subscribes from.
A clustered-network is formed during transit at a given speed in a given scenario. In the experimental setup,we use the node
speed, density and location as independent variables and cost of clustering as output for the AutoCast scenarios running on CARLA
Environment. Nodes are identified using their IP address.

Before proceeding further, let me point out a couple of assumptions and requirements made to have a prototype vehicle network be implemented as this program in the form of a
multi-user web interface:

1. That the mobility model is provided by CARLA simulator as .json objects every 10 seconds.
2. The genesis clustering policy is based an initial agreement to form a network.
3. Initially implemented as a web interface for 5 users playing a game.
4. There exists a clustering policy managed by an application that determines which vehicles can enter or join a cluster.
5. CARLA output is based on physics-based mobility models.
6. Nodes use MQTT to communicate.
7. Cellular-based radios are used as devices.


#FastNFair: Distributed Clustering Protocol is implemented as follows:
a) Wacha tusalimiane: Everyone should have to say hello and wait for a response.
b) If a response is OK, add to cluster, otherwise
    Every Node (Autonomous Mobile Object) agrees as per the Clustering Policy (CP).
  - .
  This policy is embedded in an image file. 2 types of image files are expected that contain no location data could be
  rejected, one with location data is allowed.

b) Now play the game: 1 Min Rubix Solver
c) Winner is served first and becomes the cluster head
d) Remainders continue competing without stopping the game.

Hypothesis: No matter how fast the cars travel At any given time scale of simulation, self similarity will be observed.

"""

# Network Model
# NetworkX module is used to model the network
import networkx as nx

class VehicleNetwork:
    def __init__(self, nodes=None, topic=None, links=None):
        self.nodes = nodes
        self.topic = topic
        self.links = links
        self.neighbors = []

    def generate_topology(self):
        topology = nx.MultiGraph()
        topology.add_edge(self.links)
        self.clusters.append(topology)




