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
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1
        return True

    def pop(self, value):
        pass

    def prepend(self, value):
        pass

    def pop_first(self, value):
        pass

    def get(self, value):
        pass

    def set(self, value):
        pass

    def insert(self, value):
        pass

    def remove(self, value):
        pass


doublyLinkedList = DoublyLinkedList(1)
doublyLinkedList.print_list()