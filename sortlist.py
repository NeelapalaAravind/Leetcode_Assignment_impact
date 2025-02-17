class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        middle = self.getMiddle(head)
        right_head = middle.next
        middle.next = None 
        
        left_sorted = self.sortList(head)
        right_sorted = self.sortList(right_head)
        
        return self.mergeSortedLists(left_sorted, right_sorted)

    def getMiddle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head.next 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def mergeSortedLists(self, left: ListNode, right: ListNode) -> ListNode:
        dummy_head = ListNode(0)  
        current = dummy_head
        while left and right:
            if left.val < right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next

        current.next = left if left else right

        return dummy_head.next