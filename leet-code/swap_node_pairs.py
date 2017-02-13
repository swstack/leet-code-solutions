from utils.linked_list import LinkedList


class Solution(object):
    def swapPairs(self, head):
        """
        Given a linked list, swap every two adjacent nodes and return its head.

        For example,
        Given 1->2->3->4, you should return the list as 2->1->4->3.

        Your algorithm should use only constant space. You may not modify the values in the list,
        only nodes itself can be changed.

        :type head: ListNode
        :rtype: ListNode
        """

        # Save next node
        _next = head.next

        if not _next:
            return head

        # Check if there is more than 2 nodes, saving the 3rd
        third_node = _next.next

        # Point the next node back at head
        _next.next = head

        if third_node:
            head.next = self.swapPairs(third_node)
        else:
            # Erase old pointer
            head.next = None

        return _next


ll = LinkedList.from_array([1, 2, 3])
ll_swapped = LinkedList(Solution().swapPairs(ll.head))
print(ll_swapped)
manually_swapped = LinkedList.from_array([2, 1, 3])
assert ll_swapped == manually_swapped


ll = LinkedList.from_array([1, 2, 3, 4, 5, 6])
ll_swapped = LinkedList(Solution().swapPairs(ll.head))
print(ll_swapped)
manually_swapped = LinkedList.from_array([2, 1, 4, 3, 6, 5])
assert ll_swapped == manually_swapped
