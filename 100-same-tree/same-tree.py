# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if p is None and q is None:
            return True
        if p is not None and q is None:
            return False
        if p is None and q is not None:
            return False
        if p.val != q.val:
            return False
        if p.left is not None and q.left is None:
            return False
        if p.left is None and q.left is not None:
            return False
        if p.right is not None and q.right is None:
            return False
        if p.right is None and q.right is not None:
            return False
        if p.left is None and q.left is None and p.right is None and q.right is None:
            return True
        x = self.isSameTree(p.left,q.left)
        y = self.isSameTree(p.right,q.right)
        if x == False or y == False:
            return False
        return True