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
        _head = self.head
        while _head.next is not None:
            out += "{} -> ".format(_head.val)
            _head = _head.next

        out += "{}".format(_head.val)
        return out

    def __eq__(self, other):
        if not other:
            return False

        _head1 = self.head
        _head2 = other.head

        if _head1.val != _head2.val:
            return False

        while _head1.next is not None:
            if _head2.next is None:
                return False

            _head1 = _head1.next
            _head2 = _head2.next

            if _head1.val != _head2.val:
                return False

        if _head2.next is not None:
            return False

        return True


if __name__ == '__main__':
    ll = LinkedList.from_array([1, 2, 3])
    print(ll)
    print(ll)
    print(LinkedList.from_array([5]))

    ll1 = LinkedList.from_array([1, 2, 3])
    ll2 = LinkedList.from_array([1, 2, 3])
    assert ll1 == ll1
    assert ll1 == ll2 == ll

    ll1 = LinkedList.from_array([1, 2])
    ll2 = LinkedList.from_array([1, 2, 3])
    assert ll1 != ll2
