from WebPageIndex import *
from AVLTreeMap_fix import *


# from processQueries import *


# class for question 1.2, create the type webpagepriorityqueue
class WebpagePriorityQueue:
    # initialize a data array that contains all instances of
    # the webpageindexes, and query which holds the query
    # which the priority is based on
    def __init__(self, arr, query):
        self.query = query.split()
        self.maxHeap = arr
        # sort method that changes the input data into descending order
        # close to original tree order
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(self.maxHeap) - 1):
                if self.maxHeap[i].qGetCount(self.query) < self.maxHeap[i + 1].qGetCount(self.query):
                    self.maxHeap[i], self.maxHeap[i + 1] = self.maxHeap[i + 1], self.maxHeap[i]
                    swapped = True

    # prints out the array of priority queue
    def printQ(self):
        print("---------------------------")
        for i in self.maxHeap:
            print(i.getName(), ", Priority:", i.qGetCount(self.query))

    # returns first item of self.maxHeap since
    # that is always the largest item
    def peek(self):
        return self.maxHeap[0]

    # removes first index of self.maxHeap and returns it
    # through the pop function on the list
    def poll(self):
        return self.maxHeap.pop(0)

    # same starting code as the loop of escending order in
    # initialization
    def reheap(self, newSet):
        self.maxHeap = newSet
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(self.maxHeap) - 1):
                if self.maxHeap[i].qGetCount(self.query) < self.maxHeap[i + 1].qGetCount(self.query):
                    self.maxHeap[i], self.maxHeap[i + 1] = self.maxHeap[i + 1], self.maxHeap[i]
                    swapped = True
