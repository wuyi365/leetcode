class Solution(object):
    
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # cover edge cases here, if one list is empty just return the other one
        if not l1 and not l2: return None
        elif not l1: return l2
        elif not l2: return l1

        l1_head = l1
        l2_head = l2

        # make a dummy first variable in new linked list
        node = dum = ListNode(None)

        while l1_head and l2_head:
            if l1_head.val < l2_head.val:
                node.next = l1_head
                l1_head = l1_head.next
                node = node.next
            else:
                print l2_head.val
                node.next = l2_head
                l2_head = l2_head.next
                node = node.next

        # now there may be some left in one but not both of the original lists
        if l1_head is not None:
            node.next = l1_head

        if l2_head is not None:
            node.next = l2_head

        return dum.next

