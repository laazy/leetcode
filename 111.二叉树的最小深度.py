from typing import Optional

from util import TreeNode
#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue = [1]
        node = root
        depth = 1
        while True:
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            if node.left is node.right:
                return depth
            node = queue.pop(0)
            while isinstance(node, int):
                queue.append(node+1)
                depth = node+1
                node = queue.pop(0)


# @lc code=end

