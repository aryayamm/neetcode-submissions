# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ans = []
        def save(root):
            nonlocal ans
            if root == None:
                ans.append(None)
                return
            ans.append(root.val)
            save(root.left)
            save(root.right)
            return
        save(p)
        temp1 = ans
        ans = []
        save(q)
        if temp1 == ans:
            return True
        return False
