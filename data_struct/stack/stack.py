class Node(object):
    def __init__(self, data):
        self.data = data
        self.next_node = None

class Stack(object):
    def __init__(self):
        self.head = None

    def pop(self):
        if self.head:
            current = self.head
            self.head = self.head.next_node

            current.next_node = None

            return current.data

        return None

    def push(self, data):
        newnode = Node(data)

        newnode.next_node = self.head
        self.head = newnode

    def peek(self):
        if self.head:
            return self.head.data

        return None
