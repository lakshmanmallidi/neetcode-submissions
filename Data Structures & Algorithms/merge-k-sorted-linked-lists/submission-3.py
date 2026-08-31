# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def redo(i,j):
            if i == j:
                return lists[i]
            mid = (j+i)//2
            #print(i,j,mid)
            list1 = redo(mid+1, j)
            list2 = redo(i, mid)
            return merge(list1, list2)

        def merge(list1,list2):
            dummy = ListNode()
            itr = dummy
            while list1 and list2:
                if list1.val < list2.val:
                    itr.next = list1       
                    list1 = list1.next
                else:
                    itr.next = list2
                    list2 = list2.next
                itr = itr.next
            if list1:
                itr.next = list1
            else:
                itr.next = list2
            return dummy.next
        
        if not lists:
            return None

        return redo(0, len(lists)-1)
