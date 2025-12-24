# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def check_hight(node):
            if node is None:
                return 0

            left_hight = check_hight(node.left)
            if left_hight == -1:
                return -1

            right_hight = check_hight(node.right)
            if right_hight == -1:
                return -1

            if abs(left_hight - right_hight)>1:  # find absoulate value
                return -1

            return max(left_hight , right_hight)+1
            
        return check_hight(root) != -1
        