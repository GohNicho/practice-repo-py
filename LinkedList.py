__author__ = 'Nicholas Goh'

class LLNode(self):

    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __str__(self):
        print("Value is: {}" .format(self.value))

class LinkedList(self):

    def __init__(self, head):
        self.head = head

    def insert(self, value):
        self.head = LLNode(value, self.head)

