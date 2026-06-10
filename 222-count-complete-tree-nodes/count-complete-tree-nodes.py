# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        
        left_height = 0
        right_height = 0
        
        left = root
        right = root
        
        while left:
            left_height += 1
            left = left.left
        
        while right:
            right_height += 1
            right = right.right
        
        if left_height == right_height:
            return (1 << left_height) - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        