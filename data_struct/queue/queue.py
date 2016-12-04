class Node(object):
    def __init__(self, data):
        self.data = data
        self.next_node = None


class Queue(object):
    def __init__(self):
        self.first = None
        self.last = None


    def enqueue(self, data):
        newnode = Node(data) 

        if self.last:
            self.last.next_node = newnode
            self.last = self.last.next_node
        else:
            self.last = newnode
            self.first = self.last
    

    def dequeue(self):
        if self.first:
            val = self.first
            self.first = self.first.next_node
            val.next_node = None

            return val.data

        return None
    
    def __iter__(self):
        current = self.first

        while current:
            yield current.data
            current = current.next_node
