from util import ListNode, build_list
#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional
import heapq



class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or not any(lists):
            return None
        lists = [i for i in lists if i]
        root = ListNode(0, None)
        node = root

        def _tmp(this, other):
            return this.val < other.val
        ListNode.__lt__ = _tmp
        heapq.heapify(lists)

        while lists:
            min_node = heapq.heappop(lists)
            if min_node.next:
                heapq.heappush(lists, min_node.next)
            node.next = min_node
            node = node.next
        return root.next

# @lc code=end

s = Solution().mergeKLists(lists = list(map(build_list, [[1,4,5],[1,3,4],[2,6]])))
print(s)
s = Solution().mergeKLists(lists = None)
print(s)
s = Solution().mergeKLists(lists = [None, build_list([1])])
print(s)