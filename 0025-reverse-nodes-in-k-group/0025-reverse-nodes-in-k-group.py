# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        if not head or k == 1:
            return head

        arr = []
        temp = head

        while temp:
            arr.append(temp.val)
            temp = temp.next

        for i in range(0, len(arr) - len(arr) % k, k):
            arr[i:i+k] = arr[i:i+k][::-1]

        temp = head
        idx = 0

        while temp:
            temp.val = arr[idx]
            idx += 1
            temp = temp.next

        return head
        



        