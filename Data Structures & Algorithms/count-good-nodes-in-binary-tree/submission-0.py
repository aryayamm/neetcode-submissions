# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def dfs(root, big):
            nonlocal ans
            if root == None:
                return
            if root.val >= big:
                big = root.val
                ans += 1
            dfs(root.left, big)
            dfs(root.right, big)
            return

        dfs(root, -101)
        return ans
            