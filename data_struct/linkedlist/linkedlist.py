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
            swap = node.next_node

            node.data = swap.data
            node.next_node = swap.next_node
            swap.next_node = None

            self.size -= 1
        else:
            raise KeyError('Cant delete {0} node at the end of the tail', node.data)

    
    def prepend(self, data):
        """Insert a new node at the begining of the linked list"""
        new_node = Node(data)

        new_node.next_node = self.head

        if self.head:
            self.head.next = new_node.next_node

        self.head = new_node


    def reverse_new(self):
        """Reverse the elements of the linked list creating a new list in linear time"""

        new_list = self.__class__()

        current = self.head

        while current:
            new_list.prepend(current.data)
            current = current.next_node

        return new_list


    def reverse(self):
        """Reverse the elements of the linked list in place in linear time"""

        previous = None 
        current = self.head

        while current:
            temp_buffer = current.next_node
            current.next_node = previous

            previous = current
            current = temp_buffer

        self.head = previous


    def remove_duplicates(self):
        """Remove duplicates from the current linked list in linear time"""
        unique_hashset = set()

        current = self.head
        previous = None

        while current:
            if current.data in unique_hashset:
                previous.next_node = current.next_node
                current.next_node = None
                current = previous
            else:
                unique_hashset.add(current.data)

            previous = current
            current = current.next_node


    def get_k_last(self, k):
        """Implement an algorithm to find the kth to last element of a singly linked list, 
        without using the list's len attribute or an extra loop for counting its size"""

        current = self.head
        current_index = 0
        k_index = 0
        k_node = self.head

        while current:
            if current_index >= k:
                k_index += 1
                k_node = k_node.next_node

            current = current.next_node
            current_index += 1

        if k > current_index:
            raise KeyError('List too small {0}th last can’t be found!', k)
        else:
            return k_node


    def partition(self, x):
        """Write code to partition a linked list around a value x, such that 
        all nodes less than x come before all nodes greater than or equal to x."""

        smaller = self.__class__()
        larger = self.__class__()

        current = self.head

        while current:
            if current.data > x:
                larger.append(current.data)
            else:
                smaller.append(current.data)
            
            if not current.next_node:
                last = current

            current = current.next_node
        
        last = smaller.head

        while last.next_node:
            last = last.next_node
        
        last.next_node = larger.head

        return smaller


    def add_list(self):
        """You have two numbers represented by a linked list, where each node contains a single digit.
        The digits are stored in reverse order, such that the Ts digit is at the head of the list. 
        Write a function that adds the two numbers and returns the sum as a linked list.

        EXAMPLE
        Input:(7-> 1 -> 6) + (5 -> 9 -> 2).Thatis,617 + 295.
        Output: 2 -> 1 -> 9.That is, 912.

        FOLLOW UP
        Suppose the digits are stored in forward order. Repeat the above problem. 

        EXAMPLE
        Input:(6 -> 1 -> 7) + (2 -> 9 -> 5).Thatis,617 + 295.
        Output: 9 -> 1 -> 2.That is, 912.
        """

