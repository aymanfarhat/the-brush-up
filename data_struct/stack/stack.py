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

    def __iter__(self):
        """Iterable over linked list nodes"""
        current = self.head

        while current:
            yield current
            current = current.next_node
    

    def is_empty(self):
        return self.head == None


    def sort_desc(self):
        """Write a program to sort a stack in ascending order (with biggest items on top). 
        You may use at most one additional stack to hold items, but you may not copy the 
        elements into any other data structure (such as an array). 
        The stack supports the following operations: push, pop, peek, and isEmpty."""

        sbuffer = self.__class__()
        origin = self 

        while not origin.is_empty():
            current = origin.pop()

            greaters = 0

            if sbuffer.head == None or sbuffer.peek() < current:
                sbuffer.push(current)
            else:
                while sbuffer.peek() > current:
                    origin.push(sbuffer.pop())
                    greaters += 1

                origin.push(current)

                while greaters > 0:
                    sbuffer.push(origin.pop())
                    greaters -= 1

        return sbuffer
