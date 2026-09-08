1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def invertTree(self, root):
9        
10        if root==None:
11            return root
12        root.left,root.right=root.right,root.left
13        
14        self.invertTree(root.left)
15        self.invertTree(root.right)
16        return (root)
17
18        
19        """
20        :type root: Optional[TreeNode]
21        :rtype: Optional[TreeNode]
22        """
23        