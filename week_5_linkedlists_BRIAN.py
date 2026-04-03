# week 5 linked lists
# this code includes insert, deletion, searching and display operations and test cases at the bottom

class Node:
    def __init__(self, data):
        self.data = data # store the data
        self.next = None # pointer to the next node in the list
class LinkedList:
    def __init__(self):
        self.head = None # initialize the head of the list to None
def append(self, data):
    new_node = Node(data) # create a new node ta the end of the list
    if self.head == None: #empty the list case
        self.head = new_node
        return
    current = self.head # start at the head of the list
    while current.next: # traverse the list until we reach the end
        current = current.next
    current.next = new_node

def prepend(self, data):
    new_node = Node(data)
    new_node.next = self.head 
    self.head = new_node

def insert_at_position(self, data, position):
    if position < 0:
        print("invalid position")
        return
    new_node = Node(data)
    if position == 0:
        new_node.next = self.head
        self.head = new_node
        return
    current = self.head
    for i in range(position - 1):
        if current is None:
            print("position out of bounds")
            return
        current = current.next
    new_node.next = current.next
    current.next = new_node

def delete(self, data):
    if self.head is None:
        print("List is empty")
        return
    if self.head.data == data:
        self.head = self.head.next
        return
    current = self.head
    while current.next:
        if current.next.data == data:
            current.next = current.next.next
            return
        current = current.next
    print("Data not found in the list")

def search(self, data):
    current = self.head # search for the data in the list
    index = 0
    while current:
        if current.data == data:
            return index
        current = current.next
        index += 1
    return -1 # data not found

def display(self):
    current = self.head # display the contents of the list
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

def is_empty(self):
    return self.head is None # check if the list is empty

def size(self):
    count = 0
    current = self.head
    while current:
        count += 1
        current = current.next
    return count # return the size of the list

# test cases
if __name__ == "__main__":
    ll = LinkedList()

print("test case 1: append values 10, 20, 30 to the list")
ll.append(10)
ll.append(20)
ll.append(30)
ll.display() # Output: 10 -> 20 -> 30 -> None

print("test case 2: prepend value 5 to the list")
ll.prepend(5)
ll.display() # Output: 5 -> 10 -> 20 -> 30 -> None

print("test case 3: insert value 15 at position 2")
ll.insert_at_position(15, 2)
ll.display() # Output: 5 -> 10 -> 15 -> 20 ->

print("test case 4: delete value 20 from the list")
ll.delete(20)
ll.display() # Output: 5 -> 10 -> 15 -> 30 -> None

print("test case 5: search for value 15 in the list")
index = ll.search(15)
print(f"Index of 15: {index}") # Output: Index of 15: 2