class VehiclePacket:
    def __init__(self, node_id, velocity=None, location=None, direction=None, position=None, state=None):
        self.node_id = node_id
        self.neighbors = []
        self.velocity = velocity
        self.location = location
        self.direction = direction
        self.position = position
        self.state = state
        self.cluster_membership_type = None

    def broadcast_hello_message(self):
        packet = {
            "packet-type": "str",
            "node-id": self.node_id,
            "direction": self.direction,
            "position": self.position,
            "speed": self.velocity,
            "state": self.state
        }
        return packet

    def listen_to_state(self):
        """
            TODO: Mqtt subscribe
            Subscribe to topic-"state"
            if state == 3:

                send query to cluster head.
        """
        if self.state == 3:
            self.send_query_to_cluster_head(self.state)

    def send_query_to_cluster_head(self, state):
        """
         pseudocode:
            wait to hear from cluster head on membership
        """
        cluster_assignment = None
        # This code snippet is the new thing to the implementation done in the paper.
        if state == 3:
            try:
                print("Waiting for membership key to be sent")
                cluster_assignment = "CM"
            except:
                print("No consensus was reached")
                cluster_assignment = None
        else:
            cluster_assignment = None

        return cluster_assignment

    def roam_environment(self):
        self.broadcast_hello_message()


