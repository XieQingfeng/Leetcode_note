#实现一种算法，删除单向链表中间的某个节点（即不是第一个或最后一个节点），假定你只能访问该节点。

#示例：

#输入：单向链表a->b->c->d->e->f中的节点c
#结果：不返回任何数据，但该链表变为a->b->d->e->f

#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/delete-middle-node-lcci
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class SingleLinkedList(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def createList(self,nums):
        x = ListNode(nums[0])
        self.head = x 
        i = 1
        while i < len(nums):
            x_next = ListNode(nums[i])
            x.next = x_next
            x = x_next
            i = i + 1
            self.length = self.length + 1
        x.next = None

    def printList(self):
        x = self.head
        while x != None:
            print(x.val)
            x = x.next


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node_next = node.next
        node.val = node_next.val
        node.next = node_next.next

list = SingleLinkedList()
list.createList([2,3,5])
list.printList()