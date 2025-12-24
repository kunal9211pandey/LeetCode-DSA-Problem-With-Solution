# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        
        def depth(node):

            if not node:
                return 0

            left_hight = depth(node.left)
            right_hight = depth(node.right) 

            self.diameter = max(self.diameter ,left_hight + right_hight)

            return max(left_hight, right_hight) + 1
        
        depth(root)
        return self.diameter
