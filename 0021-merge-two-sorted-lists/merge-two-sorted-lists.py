# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if (list1 is None) and (list2 is None):
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1

        result = None
        arr = []

        if list1.val <= list2.val:
            #result.val = list1.val
            arr.append(list1.val)
            list1 = list1.next
        else:
            #result.val = list2.val
            arr.append(list2.val)
            list2 = list2.next

        print(list1)
        print(list2)
        print(result)

        while (list1 is not None) or (list2 is not None):
            if list1 is None:
                #result.next = list2
                arr.append(list2.val)
                list2 = list2.next
                #result = result.next
            elif list2 is None:
                #result.next = list1
                arr.append(list1.val)
                list1 = list1.next
                #result = result.next
            elif list1.val <= list2.val:
                #result.next = list1
                arr.append(list1.val)
                list1 = list1.next
                #result = result.next
            else:
                #result.next = list2
                arr.append(list2.val)
                list2 = list2.next
                #result = result.next
        
        #arr = arr.sort(reverse = True)
        print(arr)

        for i in range(1,len(arr)+1):
            result = ListNode(arr[-i], result)
        
        return result