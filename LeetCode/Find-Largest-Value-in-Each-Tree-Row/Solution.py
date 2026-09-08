1from collections import deque
2
3class Solution(object):
4    def largestValues(self, root):
5        if root is None:
6            return []
7
8        q = deque([root])
9        ans = []
10
11        while q:
12            maxi = float('-inf')
13
14            for i in range(len(q)):
15                node = q.popleft()
16
17                maxi = max(maxi, node.val)
18
19                if node.left:
20                    q.append(node.left)
21
22                if node.right:
23                    q.append(node.right)
24
25            ans.append(maxi)
26
27        return ans