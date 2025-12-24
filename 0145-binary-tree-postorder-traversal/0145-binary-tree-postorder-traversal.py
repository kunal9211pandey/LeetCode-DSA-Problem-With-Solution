# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        s1 =[]
        s2 =[]

        s1.append(root)

        while s1:
            current = s1.pop()
            s2.append(current.val)

            if current.left:
                s1.append(current.left)
            if current.right:
                s1.append(current.right)
        return s2[::-1]       