from typing import Optional

from util import ListNode, build_list
#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        root, supplement= ListNode(0), 0
        node = root
        while l1 is not None and l2 is not None:
            tmp = l1.val + l2.val + supplement
            supplement = tmp // 10
            tmp %= 10
            node.next = ListNode(tmp)
            node = node.next
            l1 = l1.next
            l2 = l2.next
        l = l2 if l1 is None else l1
        while l is not None:
            tmp = l.val + supplement
            supplement = tmp // 10
            tmp %= 10
            node.next = ListNode(tmp)
            node = node.next
            l = l.next
        if supplement:
            node.next = ListNode(1)
        return root.next
        

# @lc code=end
print(Solution().addTwoNumbers(build_list([9, 9, 9, 9, 9, 9, 9]), build_list([9, 9, 9, 9])))
