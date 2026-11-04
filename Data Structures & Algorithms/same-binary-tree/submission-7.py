# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
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
        b = solve(p,q)
        return ans
        
