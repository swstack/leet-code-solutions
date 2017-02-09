from utils import linked_list as ll


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


head = ll.populate([1, 4, 2, 3, 6, 12, 7])
ll.print_list(head)
