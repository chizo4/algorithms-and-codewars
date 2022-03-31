'''
Double-Ended-Queue

dequeue.py

Date: 03/2022

Author: Filip J. Cierkosz
'''

class Dequeue:
    '''
    -------------
    Class to represent a Dequeue object.
    -------------
    '''
    def __init__(self):
        '''
        Constructor.
        '''
        self.elements = []

    def getSize(self):
        '''
        Returns the size of the Dequeue.

        The runtime is O(1).
        '''
        return len(self.elements)

    def isEmpty(self):
        '''
        Returns a boolean describing if the Dequeue is (not) empty. 
        The runtime is O(1).
        '''
        return (self.elements==[])

    def addFront(self, el):
        '''
        Adds an element into the 0th index (front) of the list. The runtime 
        is O(n), since every element has to shift by one position when a new 
        one is added to the front of the Dequeue.
        '''
        self.elements.insert(0, el)

    def removeFront(self):
        '''
        Removes an element from the 0th index of the list. The runtime is
        O(n), since the elements have to be shifted after removing the very 
        first element.
        '''
        if (self.elements):
            return self.elements.pop(0)
        return None

    def getFrontEl(self):
        '''
        Returns the value from the front of the Dequeue. The runtime is
        O(1), since it is just indexing.
        '''
        if self.elements:
            return self.elements[0]
        return None

    def addBack(self, el):
        '''
        Adds an item to the last index (back) of the list. The runtime is 
        O(1), since there is no need to shift any other elements in the list.
        '''
        self.elements.append(el)

    def removeBack(self):
        '''
        Removes an item from the last index (back) of the list. The runtime 
        is O(1).
        '''
        if self.elements:
            return self.elements.pop()
        return None

    def getBackEl(self):
        '''
        Get the element from the back of the Dequeue. The runtime is O(1).
        '''
        if self.elements:
            return self.elements[-1]
        return None
