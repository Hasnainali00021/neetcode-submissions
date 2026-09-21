class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # list initialized with 0
        ptr = dummy  # Ya list par iterate kar ra hoga
        carry = 0

        while l1 or l2:
         sum = 0 + carry
         if l1 != None:
            sum += l1.val
            l1 = l1.next

         if l2 != None:  
            sum += l2.val
            l2 = l2.next

         carry = sum // 10
         sum = sum % 10
         ptr.next = ListNode(sum)
         ptr = ptr.next
        
        if carry == 1: 
         ptr.next = ListNode(carry)
        return dummy.next  

