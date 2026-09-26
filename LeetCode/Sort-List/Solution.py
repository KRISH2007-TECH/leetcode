1class Solution(object):
2    def sortList(self, head):
3
4        if head is None or head.next is None:
5            return head
6
7        # Find middle
8        slow = head
9        fast = head
10
11        while fast.next and fast.next.next:
12            slow = slow.next
13            fast = fast.next.next
14
15        # Split into two lists
16        mid = slow.next
17        slow.next = None
18
19        # Sort both halves
20        left = self.sortList(head)
21        right = self.sortList(mid)
22
23        # Merge
24        return self.merge(left, right)
25
26    def merge(self, left, right):
27
28        dummy = ListNode(0)
29        temp = dummy
30
31        while left and right:
32
33            if left.val <= right.val:
34                temp.next = left
35                left = left.next
36            else:
37                temp.next = right
38                right = right.next
39
40            temp = temp.next
41
42        if left:
43            temp.next = left
44
45        if right:
46            temp.next = right
47
48        return dummy.next