
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        cur = head
        h = set()
        while cur != None:
            h.add(cur)
            cur = cur.next
            
            if cur in h:
                return True

        return False


node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

s = Solution()
ret = s.hasCycle(node1)
print(ret)

