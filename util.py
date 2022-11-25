class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        node = self
        res = []
        while node is not None:
            res.append(node.val)
            node = node.next
        return res.__str__()

def build_list(l: list):
    node = None
    for i in reversed(l):
        node = ListNode(i, node)
    return node
