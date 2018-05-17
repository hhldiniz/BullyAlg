from Node import Node

if __name__ == '__main__':
    count = 0
    nodes = []
    while count < 6:
        new_node = Node(count)
        nodes.append(new_node)
        new_node.setDaemon(True)
        new_node.start()
        count += 1

