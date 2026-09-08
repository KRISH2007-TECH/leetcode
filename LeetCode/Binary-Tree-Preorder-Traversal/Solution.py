1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def __init__(self):
9        self.ans=[]
10    def preorder(self,root):
11        if root==None:
12            return root
13        self.ans.append(root.val)
14        self.preorder(root.left)
15        self.preorder(root.right)
16    def preorderTraversal(self, root):
17        self.ans=[]
18        self.preorder(root)
19        return self.ans
20        
21
22
23
24      
25        """
26        :type root: Optional[TreeNode]
27        :rtype: List[int]
28        """
29        