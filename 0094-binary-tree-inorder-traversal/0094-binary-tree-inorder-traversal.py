# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def InOrder(node):
            if not node:        # base case
                return
            InOrder(node.left)
            result.append(node.val)
            InOrder(node.right)
        
        InOrder(root)
        return result
