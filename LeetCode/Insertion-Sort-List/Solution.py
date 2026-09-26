1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution(object):
7    def insertionSortList(self, head):
8        temp=head
9        nums=[]
10        while(temp!=None):
11            nums.append(temp.val)
12            temp=temp.next
13        for i in range(1,len(nums)):
14            key=nums[i]
15            j=i-1
16            while(j>=0 and nums[j]>key):
17                nums[j+1]=nums[j]
18                j-=1
19            nums[j+1]=key
20        temp=head
21        i=0
22        while(temp!=None):
23            temp.val=nums[i]
24            i+=1
25            temp=temp.next
26        return head
27        """
28        :type head: Optional[ListNode]
29        :rtype: Optional[ListNode]
30        """
31        