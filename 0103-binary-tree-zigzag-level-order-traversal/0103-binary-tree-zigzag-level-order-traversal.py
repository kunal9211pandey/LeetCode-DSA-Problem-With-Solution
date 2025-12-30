# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        results = []
        queue = deque([root])

        left_to_right =True

        while queue:
            label = []

            for _ in range(len(queue)):
                node =queue.popleft()
                label.append(node.val)

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)

            if not left_to_right:
                label.reverse()

            results.append(label)

            left_to_right = not left_to_right
        return results



        