import socket
from threading import Thread

import node_msg_pb2


class Node(Thread):
    def __init__(self, node_id):
        super().__init__()
        self.__node_id = node_id
        self.__network_nodes = []
        self.__coordinator_node = None
        self.__socket = socket.socket(socket.AF_INET, socket.AF_INET)

    def get_node_id(self):
        return self.__node_id

    def get_network_nodes(self):
        return self.__network_nodes

    def add_network_node(self, node):
        self.__network_nodes.append(node)

    def set_coordinator_node(self, node):
        self.__coordinator_node = node

    def __search_node(self, node_id):
        for node in self.__network_nodes:
            if node.get_node_id() == node_id:
                self.set_coordinator_node(node)
                break

    def run(self):
        self.__socket.listen(self.__node_id)
        while True:
            self.__socket.accept()
            message = node_msg_pb2.Election()
            message_obj = message.ParseFromStgring(self.__socket.recv(1024))
            if message_obj.type == 1:
                print(f"{self.get_node_id()} - Node {message_obj.node_id} está iniciando uma eleição")
            elif message_obj.type == 2:
                print(f"Um coordenador foi escolhido! Novo coordenador é {message_obj.node_id}")
                self.__search_node(message_obj.node_id)
