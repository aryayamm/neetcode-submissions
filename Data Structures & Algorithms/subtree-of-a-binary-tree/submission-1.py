# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def check(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        ans = True
        def solve(a,b):
            nonlocal ans
            if a == None and b == None:
                return
            if a == None and b != None:
                ans = False
                return
            if a != None and b == None:
                ans = False
                return
            if a.val != b.val:
                ans = False
                return
            solve(a.left, b.left)
            solve(a.right, b.right)
        b = solve(a,b)
        return ans

    def isSubtree(self, root: Optional[TreeNode], subRoot:   Optional[TreeNode]) -> bool:
        ans = False
        def dfs(root):
            nonlocal subRoot, ans
            if root == None:
                return
            if self.check(root, subRoot):
                ans = True
                return
            if self.check(root.right, subRoot):
                ans = True
                return
            if self.check(root.left, subRoot):
                ans = True
                return
            dfs(root.left)
            dfs(root.right)
            return

        dfs(root)
        return ans
















