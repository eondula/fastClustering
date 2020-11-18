# Cluster Head Election Algorithm
import vehicle
import random

# Discovery Stage
from typing import List


"""
Implementation Notes

During this stage the vehicles are randomly placed at different intersections marked with the directions
N,S,E,W. This is stored as a list of tuples. The initial state of the vehicles is indicated by the vehicle
params variable.

This stage is triggered based on traffic light symbol (Red, Green, Amber, Passenger):
- Entry at P1, P2, P3, P4 is detected by a sensor.
- The intersection is a box of equal length n x n
- Time variable is taken during cluster time.
- Cluster Head should be chosen fast since time for cluster member is limited.
when a vehicle leaves, the process has to start again.
- 
"""
road_intersection= []
total_vehicles = input("Enter the number of vehicles")
intersection_radius = input("Enter the maximum radium")

for i in range(0, total_vehicles):
    directions = List['N', 'S', 'E', 'W']
    node_id = random.randint(0, total_vehicles)
    position_x = random.randint(0, 100)
    position_y = random.randint(0, 100)
    position_z = random.randint(0, 100)
    position = (position_x, position_y, position_z)
    speed = random.randint(20, 100)
    state = 1

    vehicle = VehicleAgent(node_id, directions, position, position, speed, state)
    vehicle.broadcast_hello_packet()
    road_intersection.append(vehicle)

# Cluster Head Election Stage







