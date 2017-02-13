class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList(object):

    @classmethod
    def from_array(cls, data):
        first_node = None
        previous_node = None
        for i in data:
            n = ListNode(i)

            if previous_node:
                previous_node.next = n

            if first_node is None:
                first_node = n

            previous_node = n

        return cls(first_node)

    def __init__(self, head):
        self.head = head

    def __str__(self):

        out = ""
        head = self.head
        while head.next is not None:
            out += "{} -> ".format(head.val)
            head = head.next

        out += "{}".format(head.val)
        return out

    def __eq__(self, other):
        pass


if __name__ == '__main__':
    ll = LinkedList.from_array([1, 2, 3])
    print(ll)
    print(ll)
