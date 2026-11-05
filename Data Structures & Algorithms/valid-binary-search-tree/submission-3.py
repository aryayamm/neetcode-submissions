# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return False

        ans = True

        def solve(root, mini, maxi):
            nonlocal ans
            if root == None:
                return
            cur = root.val
            if root.left != None:
                if mini < root.left.val < cur:
                    solve(root.left, mini, min(maxi,cur))
                else:
                    ans = False
                    return
            if root.right != None:
                if cur < root.right.val < maxi:
                    solve(root.right, max(mini,cur), maxi)
                else:
                    ans = False
                    return
            return

        solve(root,float("-inf"), float("inf"))
        return ans