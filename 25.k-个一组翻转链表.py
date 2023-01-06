from typing import Optional

from util import ListNode, build_list
#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseK(self, head: ListNode, k: int) -> ListNode:
        node = head.next
        head.next = None
        for _ in range(k-1):
            nnext = node.next
            node.next = head
            head = node
            node = nnext
        return head
    
    def getKlist(self, head: ListNode, k: int):
        node = head
        for _ in range(k-1):
            node = node.next
            if node is None:
                return head, None
        return head, node
        
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        if head is None:
            return head
        node = head
        head = ListNode(0)
        tail = head
        while node:
            gh, gt = self.getKlist(node, k)
            if gt:
                node = gt.next
                self.reverseK(gh, k)
                tail.next = gt
                tail = gh
                gh.next = node
            else:
                return head.next
        return head.next

# @lc code=end

if __name__ == "__main__":
    head = build_list([1,2,3,4,5])
    print(head)
    print(Solution().reverseKGroup(head, 2))