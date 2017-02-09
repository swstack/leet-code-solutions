class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def print_list(head):

    while head.next is not None:
        print(head.val)
        head = head.next

    print(head.val)


def populate(data):
    """Returns the head of a linked list"""

    first_node = None
    previous_node = None
    for i in data:
        n = ListNode(i)

        if previous_node:
            previous_node.next = n

        if first_node is None:
            first_node = n

        previous_node = n

    return first_node
