import random
import vehicle
from collections import defaultdict 

# Simulation parameters

nb_cm_min = 10
nb_cm_max = 100
total_vehicles = int(input("Enter number of vehicles at intersection"))
nb_nodes = []
road_segment_size = 10
r_min = 0
r_max = 0



def initialize():
    for node in range(total_vehicles):
        direction_list = ['N', 'S', 'E', 'W']
        states = [1, 2, 3, 4]
        node_id = random.randint(1000, 2000)
        velocity = random.randint(20, 100)
        location = random.randint(0,5)
        direction = random.choice(direction_list)
        position = random.randint(10, 20)
        state = 1
        vehicle_node = vehicle.VehicleAgent(node_id, velocity, location, direction, position, state)
        nb_nodes.append(vehicle_node)

    print("There are ",len(nb_nodes), "vehicles at the intersection")

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
    returns the area
    """
    return int(len(nb_nodes))/nb_cm_max


def get_cluster_size_and_grouped_cluster_members():
    distance_from_sv_values = []
    distances = []
    node_ids = []
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

def send_triggering_packet(slowest_vehicle, chosen_cluster_head_election_members):
    triggering_payload = slowest_vehicle.triggering_packet()
    slowest_vehicle.send_packet(triggering_payload["packet-type"], triggering_payload)


# Get the node ids of similar distance from sv. We will place them on a bucket(list :-))

initialize()
# Get the slowest vehicle
sv = get_slowest_vehicle()
print(get_zones())
print(get_cluster_size_and_grouped_cluster_members())
cluster_members_by_position = get_cluster_size_and_grouped_cluster_members()[4]
selected_election_participants = get_cluster_head_election_participants(cluster_members_by_position)
print(selected_election_participants)

