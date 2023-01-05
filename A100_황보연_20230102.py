# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        q = [root]
        res = 0
        while q :
            cur = q.pop()
            if cur :
                if low <= cur.val <= high :
                    res+=cur.val
                    print(cur.val)
                if cur.val > low :
                    q.append(cur.left)
                if cur.val < high :
                    q.append(cur.right)



        return res