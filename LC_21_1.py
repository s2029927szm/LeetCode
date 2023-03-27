# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
	
	#This is an attempt of Recursion to solve Linked List, runtime complexity is O(n),
	#space complexity is O(1), n is sum of length of list1 and list2
        if not list1 or not list2:
            return list2 if list2 else list1
        if list2.val>list1.val:
            list2,list1=list1,list2
        list2.next=self.mergeTwoLists(list1, list2.next)
        return list2
		
	#This is using on pointer(lc) for the final LL, runtime complexity is O(n), space complexity is (2n),
	#n is sum of length of list1 and list2
        '''
        ln=ListNode(0)
        lc=ln
        while list1 and list2:
            if list1.val<=list2.val:
                lc.next=list1
                lc=lc.next
                lc.val=list1.val
                list1=list1.next
            else:
                lc.next=list2
                lc=lc.next
                lc.val=list2.val
                list2=list2.next
        if list1==None:
            lc.next=list2
        elif list2==None:
            lc.next=list1
        return ln.next
        '''
