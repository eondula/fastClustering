import random
import vehicle
# Simulation parameters

nb_cm_min = 10
nb_cm_max = 100
total_vehicles = int(input("Enter number of vehicles at intersection"))
nb_nodes = []
road_segment_size = 10
r_min = 0
r_max = 0

# Generate vehicle parameters

def initialize():
    for vehicle_node in range(total_vehicles):
        direction_list = ['N', 'S', 'E', 'W']
        states = [1, 2, 3, 4]
        node_id = random.randint(1000, 2000)
        velocity = random.randint(20, 100)
        location = random.randint(0,5)
        direction = random.choice(direction_list)
        position = random.randint(10, 20)
        state = 1
        node = vehicle.VehicleAgent(node_id, velocity, location, direction, position, state)
        nb_nodes.append(node)

    print("There are ",len(nb_nodes), "vehicles at the intersection")

# Get the slowest vehicle to trigger cluster formation

def get_slowest_vehicle():
    """
    NB: This method might fail if there are duplicates
    """
    speeds = {}
    for i in nb_nodes:
        speeds[i.node_id] = i.velocity
    
    slowest_vehicle = min(speeds.items(), key=lambda x: x[1])

    return slowest_vehicle

def get_zones():
    """
    returns the area
    """
    return int(len(nb_nodes))/nb_cm_max


def get_vehicles_clusters():
    vehicle_clusters = []
    for node in nb_nodes:
        if vehicle_clusters and vehicle_clusters[-1][0] == value:
            vehicle_clusters[-1].append(node)
        else:
            vehicle_clusters.append([node])

def get_cluster_size():
    sv = get_slowest_vehicle()
    distance_from_sv = []
    transmission_range = 0
    sv_position = 0
    for node in nb_nodes:
        if(node.node_id == sv[0]):
            transmission_range = int(node.transmission_range)
            sv_position = node.position

# Find the minimum and maximum distance from sv within the cluster. 
# Currently how a min or max of 0 will impact the overrall system.
    for node in nb_nodes:
        if(node.node_id != sv[0]):
            r = abs(node.position - sv_position)
            distance_from_sv.append(r)  
    nb_zones = get_zones()
    cluster_size = transmission_range/nb_zones
    r_min = min(distance_from_sv)
    r_max = max(distance_from_sv)

    return cluster_size, r_min, r_max, 

# Get the node ids of similar distance from sv. We will place them on a bucket(list :-))

initialize()
get_slowest_vehicle()
print(get_zones())
print(get_cluster_size())

