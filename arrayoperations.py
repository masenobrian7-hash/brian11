"""
name: brian
date: 20-2-2026
reg no: AIIM/01440/2024
description: functions for insertion, deletion, traversal and searching in python arrays and each method includes big o complexity notes.
"""

class arrayoperations:
    def __init__(self):
        """initialize an empty array"""
        self.array = []

    def insert(self, index,value):
        """
        insert a value at a specific index
        time complexity: O(n) because we may need to shift elements to the right to make space for the new value
        space complexity: O(1) because we are inserting in place without using extra space
        """
        if index <0 or index > len(self.array):
            print("error: cannot insert at this index")
            return False
        self.array.insert(index, value)
        return True


    def delete(self, index):
        """
        delete a value at a specific index
        time complexity: O(n) because we may need to shift elements to the left to fill the gap left by the deleted value
        space complexity: O(1) because we are deleting in place without using extra space
        """
        if index <0 or index >= len(self.array):
            print("error: cannot delete at this index")
            return False
        del self.array[index]
        return True
    

    def traverse(self):
        """
        traverse the array and print each element
        time complexity: O(n) because we need to visit each element in the array
        space complexity: O(1) because we are not using extra space for traversal
        """
        for element in self.array:
            print(element)

    
    def search(self, value):
        """
        search for a value in the array and return its index if found, otherwise return -1
        time complexity: O(n) because we may need to check each element in the array to find the value
        space complexity: O(1) because we are not using extra space for searching
        """

        #loop through each element and check if it matches the value we are searcing for if it does, return the index of that element. if we finish the loop without finding the value, return -1 to indicate that it was not found.
        for index, element in enumerate(self.array):
            if element == value:
                return index
        return -1 # return -1 to indicate that the value was not found in the array
    


#TEST CASES
if __name__ == "__main__":
    arr = arrayoperations()
    print("test cases")

#insertion test cases
print("\ninsertion test cases")
arr.insert(0, 10) # insert 10 at index 0
arr.insert(1, 20) # insert 20 at index 1
arr.insert(2, 30) # insert 30 at index 2
arr.insert(1, 15) # insert 15 at index 1
print("array after insertions:", arr.array) # should print [10, 15, 20, 30]

#deletion test cases
print("\ndeletion test cases")
removed = arr.delete(1) # delete value at index 1 (15)
print("deletion successful:", removed) # should print True
print("array after deletion:", arr.array) # should print [10, 20, 30]

#traversal test case
print("\ntraversal test case")
arr.traverse() # should print each element in the array


#search test case
print("\nsearch test cases")
index = arr.search(20) # search for value 20
print("index of 20:", index) # should print 1

#search for missing value
index = arr.search(40) # search for value 40
print("index of 40:", index) # should print -1 to indicate not found

#traverse test case
print("\ntraversal test case")
arr.traverse() # should print each element in the array