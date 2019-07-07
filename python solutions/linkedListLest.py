class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
 #1 -> 2 -> 3 -> None
def length(node):
    # Your code goes here.
    nDone = True
    length = 0
    currentNode = node

    while True:
        if currentNode is None:
            nDone = False
            break
        
        length = length + 1
        currentNode = currentNode.next

    return length
     
def count(node, data):
    # Your code goes here.
    count = 0
    current_node = node
    while True:
        if current_node is None:
            break

        if current_node.data == data:
            count = count + 1
        
        current_node = current_node.next

    return count