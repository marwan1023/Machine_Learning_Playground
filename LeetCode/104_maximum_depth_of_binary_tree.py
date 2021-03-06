class TreeNode(object):
    """
    Definition for a binary tree node.
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int

        beats 10.60%
        """
        return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0
