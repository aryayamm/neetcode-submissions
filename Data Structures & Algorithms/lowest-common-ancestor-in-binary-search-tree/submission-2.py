# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ans = -1
        def solve(root):
            nonlocal p,q,ans
            if root == None:
                return

            a = solve(root.left)
            b = solve(root.right)
            print(root.val)
            if (root == p or root == q) and (a or b):
                print('a')
                ans = root
                return

            if a and b:
                print('a')
                ans = root
                return

            if root == p or root == q:
                print("niga")
                return True
            
            if a or b:
                return True
        solve(root)
        return ans