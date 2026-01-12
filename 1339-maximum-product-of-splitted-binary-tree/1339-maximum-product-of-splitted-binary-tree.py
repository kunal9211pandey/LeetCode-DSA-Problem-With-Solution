class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        max_product = 0

        # Step 1: compute total sum of tree
        def treeSum(node):
            if not node:
                return 0
            return node.val + treeSum(node.left) + treeSum(node.right)

        total_sum = treeSum(root)

        # Step 2: compute subtree sums and max product
        def dfs(node):
            nonlocal max_product
            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            subtree_sum = node.val + left_sum + right_sum

            # product if we cut above this subtree
            product = subtree_sum * (total_sum - subtree_sum)
            max_product = max(max_product, product)

            return subtree_sum

        dfs(root)
        return max_product % MOD
