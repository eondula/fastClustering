import paho.mqtt.client as mqtt
import time

# Connection script
# This connection script borrows implementation by Steve's Internet Guide blog --> MQTT Python
# http://www.steves-internet-guide.com/into-mqtt-python-client/

def on_connect(client, userdata, flags, rc):
    if rc==0:
        client.connected_flag=True #set flag
        print("connected OK")
    else:
        print("Bad connection Returned code=",rc)

mqtt.Client.connected_flag=False#create flag in class
broker="127.0.0.1" #localhost
client = mqtt.Client("python1")             #create new instance 
client.on_connect=on_connect  #bind call back function
client.loop_start()
print("Connecting to broker ",broker)
client.connect(broker)      #connect to broker
while not client.connected_flag: #wait in loop
    print("In wait loop")
    time.sleep(1)
print("in Main Loop")
client.loop_stop()    #Stop loop 
client.disconnect() # disconnect

class VehicleAgent:
    """
    The class attributes are considered as network variables and methods as information stored on the memory
    of the device.
    """
    def __init__(self, node_id, velocity=None, location=None, direction=None, position=None, state=None):
        self.node_id = node_id
        self.neighbors = []
        self.velocity = velocity
        self.location = location
        self.direction = direction
        self.position = position
        self.state = state
        self.transmission_range = 50
        self.client_id = self.node_id
        self.packet_queue = []

    def set_state(self, value):
        self.state = value

    def add_neighbor(self, node_id):
        self.neighbors.append(node_id)
        

    def hello_packet(self):
        hello_packet = {
            "packet-type": "HELLO Packet",
            "node-id": self.node_id,
            "direction": self.direction,
            "position": self.position,
            "speed": self.velocity,
            "state": self.state
        }
        return hello_packet

    def triggering_packet(self, sv_id, rv_id, r_min, r_max):
        triggering_packet = {
            "packet-type": "TRIGGERING Packet",
            "sv-id": sv_id,
            "rv_id": rv_id,
            "r-min": r_min,
            "r-max": r_max,
        }
        return triggering_packet

    def initiating_packet(self, rv_id, r_min, r_max, cluster_stamp):
        initiating_packet = {
            "packet-type": "INITIATING Packet",
            "rv_id": rv_id,
            "r-min": r_min,
            "r-max": r_max,
            "cluster-stamp": cluster_stamp
        }

        return initiating_packet

    def announce_packet(self, ch_id, cluster_stamp):
        announce_packet = {
            "packet-type": "ANNOUNCE Packet",
            "ch-id": ch_id,
            "cluster-stamp": cluster_stamp
        }

        return announce_packet

    def ack_packet_cm(self, cm_id, cluster_stamp):
        ack_packet_cm = {
            "packet-type": "ACK Packet",
            "cm-id": cm_id,
            "cluster-stamp": cluster_stamp
        }

        return ack_packet_cm

    def ack_packet_ch(self, ch_id, nb_cm, cluster_stamp, cluster_members):
        ack_packet_ch = {
            "packet-type": "ACK Packet",
            "ch-id": ch_id,
            "nb-cm": nb_cm,
            "cluster-stamp": cluster_stamp,
            "cluster_members": cluster_members
        }

        return ack_packet_ch

    def invite_packet(self, current_ch, target_ch, cluster_stamp):
        invite_packet = {
            "packet-type": "INVITE Packet",
            "current_ch": current_ch,
            "target_ch": target_ch,
            "cluster_stamp": cluster_stamp
        }
        return invite_packet

    def confirm_packet(self, target_ch, current_ch, cluster_stamp):
        confirm_packet = {
            "packet-type": "CONFIRM Packet",
            "current_ch": current_ch,
            "target_ch": target_ch,
            "cluster_stamp": cluster_stamp
        }
        return confirm_packet

    def update_list_packet(self, current_ch, target_ch, nb_cm, cluster_stamp, cluster_members):
        update_list_packet = {
            "packet-type": "UPDATELIST Packet",
            "current_ch": current_ch,
            "nb_cm": nb_cm,
            "target_ch": target_ch,
            "cluster_stamp": cluster_stamp,
            "cluster_members": cluster_members
        }
        return update_list_packet

    def ch_update_packet(self, current_ch, cluster_stamp, target_ch):
        ch_update_packet = {
            "packet-type": "CHUPDATE Packet",
            "current_ch": current_ch,
            "target_ch": target_ch,
            "cluster_stamp": cluster_stamp
        }
        return ch_update_packet
    
    def send_packet(self, payload, topic):
        client.publish(topic, payload)
       

    def receive_packet(self, payload, topic):
        client.subscribe(topic, payload)



