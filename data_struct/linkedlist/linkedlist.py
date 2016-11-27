class Node(object):
    def __init__(self, data):
        """Initialise a node object used in a linked list"""
        self.data = data
        self.next_node = None


class LinkedList(object):
    def __init__(self, head = None):
        """Initialise a linked list data structure"""
        self.head = head
        self.size = 1 if head else 0

    def __len__(self):
        """Get the item count in linked list"""
        return self.size

    def append(self, data):
        """Add ned item to the end of the linked list"""
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.size = 1
        else:
            current = self.head

            while current.next_node:
                current = current.next_node

            current.next_node = new_node
            self.size += 1

        return new_node

    def __getitem__(self, data):
        """Find a single item by its data value and return the node"""
        current = self.head

        while current:
            if current.data == data:
                return current

            current = current.next_node

        raise KeyError('Item with data {} not found!'.format(data))

    def __iter__(self):
        """Iterable over linked list nodes"""
        current = self.head

        while current:
            yield current
            current = current.next_node

    def __delitem__(self, data):
        """Delete an node in linked list by its data value"""
        if self.head is None:
            raise KeyError('Linked list empty')

        elif self.head.next_node is None:
            self.head = None
            self.size = 0

            return True

        else:
            current = self.head

            while current:
                if current.next_node.data == data:
                    current.next_node = current.next_node.next_node
                    self.size -= 1

                    return True

                current = current.next_node

        raise KeyError('Item with data {0} not found'.format(data))

    
    def clear(self):
        self.head = None

    def del_node(self, node):
        """Given a direct reference to a node, delete and 
        reconstruct the list in constant time O(1)
        The node is expected to have a next or raise an
        exception"""

        if self.size == 0:
            raise KeyError('Linked list is empty')

        elif self.size == 1:
            self.head = None

        elif node.next_node: 
            node.next_node
            swap = node.next_node

            node.data = swap.data
            node.next_node = swap.next_node
            swap.next_node = None

            self.size -= 1
        else:
            raise KeyError('Cant delete {0} node at the end of the tail', node.data)
