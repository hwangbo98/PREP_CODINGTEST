# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def check(root) :
            if not root :
                return 0

            left = check(root.left)
            right = check(root.right)

            res[0] = max(res[0], left+right)
            return max(left, right) + 1
        
        check(root)
        return res[0]