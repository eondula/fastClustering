# ## Author: Elizabeth A.M Ondula
# ##### Date: Fall 2020
# Project Name: Distriibuted Clustering Protocol for Vehicular Networks
from multiprocessing import Process
import sys
import random
import vehicle
from collections import defaultdict
import time
import timeit


# Simulation parameters are initialized as follows:

nb_cm_min = 10
nb_cm_max = 100
my_data_file = open("data.txt", 'wb')
total_vehicles = int(input("Enter number of vehicles at intersection"))
nb_nodes = [] #Network of Vehicles
road_segment_size = 10
r_min = 0
r_max = 0
topic = "election"
cluster_members = []
cluster_members_selected_for_election = []

def initialize_vehicles_parameters():
    """
     This is the interface to CARLA. currently not integrated and hopeully will be the next step after Finals
    """
    for node_number in range(total_vehicles):
        direction_list = ['N', 'S', 'E', 'W']
        # states = [1, 2, 3, 4]
        node_id = random.randint(1000, 2000)
        velocity = random.randint(20, 100)
        location = random.randint(0,5)
        direction = random.choice(direction_list)
        position = random.randint(10, 50)
        state = 1
        vehicle_node = vehicle.VehicleAgent(node_id, velocity, location, direction, position, state)
        nb_nodes.append(vehicle_node)

    print("There are ",len(nb_nodes), "vehicles initialized at a road intersection.")

# Get the slowest vehicle to trigger cluster formation

def get_slowest_vehicle():
    """
    NB: This method might fail if there are duplicates
    """
    speeds = {}
    for i in nb_nodes:
        speeds[i.node_id] = i.velocity
    
    print(speeds)
    slowest_vehicle = min(speeds.items(), key=lambda x: x[1])
    
    print("Slowest vehicle is: ", slowest_vehicle)

    return slowest_vehicle

def get_zones():
    """
    returns the zone spaces. e.g for 10 nodes with a max of 100
    """
    return int(len(nb_nodes))/nb_cm_max


def get_cluster_size_and_grouped_cluster_members():
    distance_from_sv_values = []
    # distances = []
    # node_ids = []
    transmission_range = 0
    sv_position = 0
    for node in nb_nodes:
        if(node.node_id == sv[0]):
            transmission_range = int(node.transmission_range)
            sv_position = node.position
        

# Find the minimum and maximum distance from sv within the cluster. 
# Currently how a min or max of 0 will impact the overrall system.
    print("sv position is: ", sv_position)
    for node in nb_nodes:
        if(node.node_id != sv[0]):
            r = abs(node.position - sv_position)
            distance_from_sv_values.append({node.node_id: r}) 
       
    nb_zones = get_zones()
    cluster_size = transmission_range/nb_zones
    v_nodes_distances = []
    v_nodes_ids = []
    for v_node in distance_from_sv_values:
        for key, value in v_node.items():
            v_nodes_distances.append(value)
            v_nodes_ids.append(key)
  
    r_min = min(v_nodes_distances)
    r_max = max(v_nodes_distances)


    #Action: Get Cluster Group Members. Members of a cluster belong to the same zone. 
    # These members share the same position from the smallest vehicle which initiates the cluster formation.
    # This is determined by position attribute for each vehicle. 
    # nb_zone is computed first in order to compute the cluster size.

    clustered_members = defaultdict(list)
    clustered_members_ids = []

    for index, value in enumerate(v_nodes_distances):
        clustered_members[value].append(index)

    for key, value in clustered_members.items():
        v_nodes_on_same_zone = []
        for i in value:
            v_node_id = v_nodes_ids[i]
            v_nodes_on_same_zone.append(v_node_id)
        clustered_members_ids.append(v_nodes_on_same_zone)

    return cluster_size, r_min, r_max, clustered_members, clustered_members_ids


def get_cluster_head_election_participants(cluster_members_grouped_list):
    ch_participants = []
    for group in cluster_members_grouped_list:
        selected_member = random.choice(group)
        ch_participants.append(selected_member)
    
    return ch_participants

# def send_triggering_packet(slowest_vehicle, chosen_cluster_head_election_members):
#     triggering_payload = slowest_vehicle.triggering_packet()
#     return slowest_vehicle.send_packet(triggering_payload["packet-type"], triggering_payload)

def query_nb_nodes(identification):
    for vehicle in nb_nodes:
        if vehicle.node_id == identification:
            return vehicle

def send_packet(payload, vehicle_object):
    vehicle_object.send_packet(payload, topic)


def send_triggering_packet():
    """
        sends a triggering packet to mqtt broker with topic election
        returns the byte size of the
    """
    for vehicle in selected_election_participants:
        sv_object = query_nb_nodes(sv[0])
        sv_triggering_payload = sv_object.triggering_packet (sv[0], vehicle, r_min, r_max) #sv_triggering payload
        sv_object.send_packet(str(sv_triggering_payload), topic)


def send_initiating_packet():
    for i, vehicle in enumerate(selected_election_participants):
        vehicle_object = query_nb_nodes(vehicle)
        vehicle_object.receive_packet(topic, 2)
        cluster_stamp = time.time()
        rv_initiating_payload = vehicle_object.initiating_packet(vehicle_object, r_min, r_max, cluster_stamp)
        vehicle_object.send_packet(str(rv_initiating_payload), topic)
    
def get_cluster_heads():

    # get the suitability value 
    # Return cluster head vehicle object.
    cluster_heads = []
    
    for cluster in cluster_members_by_position:
        for v_node_id in cluster:
            # Get neighboars
            v_obj = query_nb_nodes(v_node_id)
            neighbors = v_obj.neighbors
            #print(neighbors[0])
            for i in neighbors[0]:
                neighbor_obj = query_nb_nodes(i)
                if(v_obj.velocity < neighbor_obj.velocity):
                    cluster_heads.append(v_obj)
    
    return cluster_heads



print("Start Simulation")
start = timeit.default_timer()
initialize_vehicles_parameters()
print ("Current Vehicle Nodes: ", nb_nodes)

# Get the slowest vehicle to compute the cluster size, r_min, r_max and other parameters
sv = get_slowest_vehicle()
cluster_members_by_position = get_cluster_size_and_grouped_cluster_members()[4]
r_min = get_cluster_size_and_grouped_cluster_members()[1]
r_max = get_cluster_size_and_grouped_cluster_members()[2]
selected_election_participants = get_cluster_head_election_participants(cluster_members_by_position)


# Update the states, position and neighbors chosen cluster members before cluster head election
for cluster in cluster_members_by_position:
    for cm in cluster:
        query_nb_nodes(cm).state = 2
        query_nb_nodes(cm).position = query_nb_nodes(cm).position + 1 # the position of the vehicle is then updated by 1 after 1 timestep
        # Add neighbors (a neighbor is a node with similar direction in the cluster)
        # The paper does not seem to consider direction. This method needs an update to account for this case.
        query_nb_nodes(cm).neighbors.append(cluster)

# Start Cluster Head Election 
print("Cluster Head Election process is about to start")
quality_of_service = input("Enter MQTT OoS value. Only 0, 1, 2 are accepted")
send_triggering_packet()
send_initiating_packet()
# Get all the vehicles in the network with state = 2
for node in nb_nodes:
    if node.state == 2:
        cluster_members.append(node)
        if query_nb_nodes(node.node_id).node_id in selected_election_participants:
            cluster_members_selected_for_election.append(node)
cluster_heads = get_cluster_heads()

stop = timeit.default_timer()
latency = stop - start
my_data_file.write(bytes(str(latency), 'utf-8'))
my_data_file.close()
print("There are a total of ", len(cluster_heads), "Cluster Heads")


