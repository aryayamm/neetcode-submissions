# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        def dfs(root):
            nonlocal stack
            if root == None:
                return
            dfs(root.left)
            stack.append(root.val)
            dfs(root.right)
            return

        if root.left != None:
            dfs(root.left)
            stack.append(root.val)
        else:
            stack.append(root.val)
        if root.right != None:
            dfs(root.right)
        return stack[k-1]