#no indexes
#not contiguos
#its nodes is mixed up on memory
    
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1
        # if value:
        #     node = Node(value)
        #     self.head = node
        #     self.tail = node
        #     self.length = 1
        # else:
        #     self.head = None
        #     self.tail = None
        #     self.length = 0

    def printLinkedListValues(self):
        if(self.length == 0):            
            print("[LINKEDLIST] Lista vazia.")
            return False
            
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next

        return True

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        
        self.tail = new_node
        self.length += 1
        return True

    def pop(self):        
        if self.length == 0:
            return None
        
        if self.length == 1:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        else:
            pre_temp = self.head
            temp = self.head

            while temp.next:
                pre_temp = temp
                temp = temp.next

            self.tail = pre_temp
            self.tail.next = None
            self.length -= 1
            return temp

    def prepend(self, value):
        new_node = Node(value)
        
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        
        temp = self.head

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

        self.length -= 1
        temp.next = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return False
        
        temp = self.head

        for _ in range(index):
            temp = temp.next

        return temp

    def set_value(self, index, value):
        temp = self.get(index)

        if temp:
            temp.value = value
            return True
        
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        temp = self.get(index-1)
        if temp:
            new_node = Node(value)
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            return True
        return False

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length -1:
            return self.pop()
                
        pre = self.get(index-1)
        temp = pre.next

        if pre:
            pre.next = temp.next
            temp.next = None
            self.length -= 1
            return temp

    def reverse(self):
        pass
        # if self.length == 0:
        #     return None
        # if self.length == 1:
        #     return True
        
        # array = []
        # reversed_linkedlist = LinkedList(None)
        # temp = self.head

        # for _ in range(self.length):
        #     array.append(temp)
        #     temp = temp.next

        # for i in range(array.__len__()-1, -1, -1):
        #     reversed_linkedlist.append(array[i].value)

        # return reversed_linkedlist