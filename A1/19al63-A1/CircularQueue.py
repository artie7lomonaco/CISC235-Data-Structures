class circular_queue:
    def __init__(self):
        self.c_queue = list()
        self.head = 0
        self.tail = 0
        self.max_size = 5

    def enqueue(self,val):
        if self.size() == self.max_size-1:
            return ("The queue is full")
        self.c_queue.append(val)
        self.tail = (self.tail + 1) % self.max_size
        return True

    def dequeue(self):
        if self.size() == 0:
            return("The queue is empty")
        val = self.c_queue[self.head]
        self.head = (self.head + 1) % self.max_size
        return val

    #Calculating the size of the queue
    def size(self):
        if self.tail>=self.head:
            return (self.tail-self.head)
        return (self.max_size - (self.head-self.tail))



