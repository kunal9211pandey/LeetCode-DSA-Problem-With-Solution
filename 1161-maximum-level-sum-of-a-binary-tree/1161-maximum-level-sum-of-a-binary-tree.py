# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import Optional

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        level = 1
        answer_level = 1
        max_sum = root.val

        while queue:
            size = len(queue)
            current_sum = 0

            for _ in range(size):
                node = queue.popleft()
                current_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if current_sum > max_sum:
                max_sum = current_sum
                answer_level = level

            level += 1

        return answer_level

        