__author__ = 'Nicholas Goh'

class LLNode(object):

    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __str__(self):
        return "Value is: {}" .format(self.value)

class LinkedList(object):

    def __init__(self, head):
        self.head = head

    def insert(self, value):
        self.head = LLNode(value, self.head)


if __name__ == '__main__':

    # Test 1
    new_node = LLNode(6)
    print(new_node)
