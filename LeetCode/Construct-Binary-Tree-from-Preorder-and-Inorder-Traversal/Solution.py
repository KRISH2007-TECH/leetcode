1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7
8class Solution:
9    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
10        # Create a hash map to quickly find the index of any value in the inorder array
11        inorder_map = {val: i for i, val in enumerate(inorder)}
12        
13        # Track our current position in the preorder array
14        pre_idx = 0
15        
16        def helper(left_in, right_in):
17            nonlocal pre_idx
18            
19            # Base case: if there are no elements to construct the subtree
20            if left_in > right_in:
21                return None
22            
23            # 1. Pick the current element from preorder as the root
24            root_val = preorder[pre_idx]
25            root = TreeNode(root_val) # <--- This creates the node object!
26            pre_idx += 1
27            
28            # 2. Find the index of this root in the inorder array
29            pivot = inorder_map[root_val]
30            
31            # 3. Recursively build the left and right subtrees
32            # In preorder, the left child comes immediately after the root
33            root.left = helper(left_in, pivot - 1)
34            root.right = helper(pivot + 1, right_in)
35            
36            return root
37            
38        return helper(0, len(inorder) - 1)