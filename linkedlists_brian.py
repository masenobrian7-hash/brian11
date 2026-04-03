# week 5 linked lists
# this code includes insert, deletion, searching and display operations and test cases at the bottom

class Node:
    def __init__(self, data):
        self.data = data # store the data
        self.next = None # pointer to the next node in the list

class LinkedList:
    def __init__(self):
#start with an empty list
        self.head = None

#insert a new node at the end of the list
    def insert(self, data):
        new__node = Node(data) # create a new node 
        if self.head is None: # if the list is empty, set the new node as the head
            self.head = new__node
        else: # otherwise find the last node and link with the new node
            current = self.head
            while current.next: # traverse until the last node is reached
                current = current.next
            current.next = new__node

#delete a node with a specific value
    def delete(self, value):
        