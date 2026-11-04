# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        queue = []
        queue.append(root)
        ans = []
        while queue:
            n = len(queue)
            temp = []
            for _ in range(n):
                cur = queue.pop(0)
                temp.append(cur.val)
                if cur.left != None:
                    queue.append(cur.left)
                if cur.right != None:
                    queue.append(cur.right)
            ans.append(temp)
        return ans
