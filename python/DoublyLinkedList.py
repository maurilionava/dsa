class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        aux_node = self.head

        while aux_node is not None:
            print(aux_node.value)
            aux_node = aux_node.next

    def append(self, value):
        pass

doublyLinkedList = DoublyLinkedList(1)
doublyLinkedList.print_list()