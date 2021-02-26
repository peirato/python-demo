from typing import Optional


class Node:

    def __init__(self, data: int, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self) -> int:
        return self.__data

    @data.setter
    def data(self, data: int):
        self.__data = data

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        self.__next_node = next_node


# 单向链表
class SinglyLinkedList(object):

    def __init__(self):
        self.__head = None

    def add_list(self, *args: int):
        head = Node(0)
        current = head
        for arg in args:
            current.next_node = Node(arg)
            current = current.next_node
        self.__head = head.next_node

    def set_head(self, head: Node):
        self.__head = head

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, head: Node):
        self.__head = head

    def find_by_value(self, value: int) -> Optional[Node]:
        node = self.__head
        while (node is not None) and (node.data != value):
            node = node.next_node
        return node

    def find_by_index(self, index: int) -> Optional[Node]:
        node = self.__head
        pos = 0
        while (node is not None) and (pos != index):
            node = node.next_node
            pos += 1
        return node

    # 查询一个元素
    def find_by_node(self, node: Node) -> Optional[Node]:
        if self.__head == node:
            return self.__head

        pro = self.__head

        while pro != node:
            if pro.next_node is None:
                # 到了最后一个了还没找到
                return None
            else:
                pro = pro.next_node

        return pro

    def insert_value_to_head(self, value: int):
        node = Node(value)
        node.next_node = self.__head
        self.__head = node

    def insert_node_to_head(self, node: Node):
        if node:
            node.next_node = self.__head
            self.__head = node

    def insert_node_after(self, node: Node, new_node: Node):
        if node is None or new_node is None:
            return
        new_node.next_node = node.next_node
        node.next_node = new_node

    def insert_value_after(self, node: Node, value: int):
        new_node = Node(value)
        self.insert_node_after(node, new_node)

    def insert_node_before(self, node: Node, new_node: Node):
        if (node is None) or (self.__head is None):
            return

        if node == self.__head:
            self.insert_node_to_head(new_node)

        pro = self.__head
        not_found = False

        # 在整个链表搜索
        while pro.next_node != node:
            if pro.next_node is None:
                # 到了最后一个节点还没有找到
                not_found = True
                break
            else:
                pro = pro.next_node

        if not not_found:
            pro.next_node = new_node
            new_node.next_node = node

    def insert_value_before(self, node: Node, value: int):
        new_node = Node(value)
        self.insert_node_before(node, new_node)

    def delete_by_node(self, node: Node) -> bool:
        if self.__head is None:
            # 链表为空 直接返回
            return False

        if node == self.__head:
            # 删除的元素是链表的第一个
            self.__head = self.__head.next_node
            return True

        pro = self.__head
        while pro.next_node != node:
            if pro.next_node is None:
                # 没有找到指定元素
                return False
            else:
                pro = pro.next_node

        pro.next_node = pro.next_node.next_node
        return True

    def delete_by_value(self, value: int) -> bool:
        if self.__head is None:
            # 如果链表为空
            return False

        if self.__head.value == value:
            # 如果是第一个元素
            self.__head = self.__head.next_node
            return True

        pro = self.__head
        while pro.value != value:
            if pro.next_node is None:
                # 遍历到最后一个元素还不是
                return False
            else:
                pro = pro.next_node

        pro.next_node = pro.next_node.next_node
        return True

    def __repr__(self) -> str:
        nodes = []
        current = self.__head
        while current:
            nodes.append(current.data)
            current = current.next_node
        return "->".join(str(node) for node in nodes)

    def __iter__(self):
        node = self.__head
        while node:
            yield node
            node = node.next_node

    def print_all(self):
        if self.__head is None:
            print("当前链表为空")
        pos = self.__head
        while pos is not None:
            print(str(pos))
            pos = pos.next_node


"""
    1) Reverse singly-linked list
    2) Detect cycle in a list
    3) Merge two sorted lists
    4) Remove nth node from the end
    5) Find middle node

    Author: Wenru
"""


class SinglyLinkedAlgo(object):

    def reversed_with_two_node(self, pre: Node, node: Node):
        """翻转两个相邻元素"""
        temp = node
        node.next_node = pre
        pre.next_node = temp.next_node

    def reversed_self(self, li: SinglyLinkedList):
        """ 翻转整个链表"""
        if li and li.head and li.head.next_node:
            # 如果链表没有元素或者只有一个元素
            return

        pre = li.head
        node = pre.next_node

        while node is not None:
            temp = node
            self.reversed_with_two_node(pre, node)
            node = temp.next_node

    def has_ring(self, li: SinglyLinkedList) -> bool:
        """检查链表中是否有环.
        主体思想：
            设置快、慢两种指针，快指针每次跨两步，慢指针每次跨一步，如果快指针没有与慢指针相遇而是顺利到达链表尾部
            说明没有环；否则，存在环
        返回:
            True:有环
            False:没有环
        """
        fast = li.head
        slow = li.head

        while fast.next_node is not None and fast is not None:
            fast = fast.next_node.next_node
            slow = slow.next_node

            if fast == slow:
                return True

        return False

    def merge_two_sorted_list_by_node(self, node_a: Node, node_b: Node) -> Optional[Node]:
        if not node_a:
            return node_b

        if not node_b:
            return node_a

        na = node_a
        nb = node_b

        # 先创建一个头
        new_head = Node(0)
        current = new_head

        while na or nb:
            if na and na.data <= nb.data:
                current.next_node = na
                na = na.next_node
            else:
                current.next_node = nb
                nb = nb.next_node
            current = current.next_node

        # 都遍历完成后去掉新链表的头部
        new_head = new_head.next_node

        return new_head

    def merge_two_sorted_list(self, list_a: SinglyLinkedList, list_b: SinglyLinkedList) -> Optional[SinglyLinkedList]:
        new_list = SinglyLinkedList()
        new_list.set_head(self.merge_two_sorted_list_by_node(list_a.head, list_b.head))
        return new_list

    def delete_last_n_node(self, list_a: SinglyLinkedList, n: int) -> bool:
        """删除链表中倒数第N个节点.
        主体思路：
            设置快、慢两个指针，快指针先行，慢指针不动；当快指针跨了N步以后，快、慢指针同时往链表尾部移动，
            当快指针到达链表尾部的时候，慢指针所指向的就是链表的倒数第N个节点
        参数:
            n:需要删除的倒数第N个序数
        """

        if list_a.head is None:
            # 链表为空直接返回
            return False

        fast = list_a.head
        slow = list_a.head
        step = 0

        while step <= n:
            if fast.next_node is None:
                # 没有找到指定的就到头了
                return False
            fast = fast.next_node
            step += 1

        while fast.next_node is not None:
            # 没到最后就一直向后移动
            fast = fast.next_node
            slow = slow.next_node

        # 这是的slow就是倒数第n个元素的前一个元素
        slow.next_node = slow.next_node.next_node
        return True

    def find_mid_node(self, list_a: SinglyLinkedList) -> Optional[Node]:
        """查找链表中的中间节点.
        主体思想:
            设置快、慢两种指针，快指针每次跨两步，慢指针每次跨一步，则当快指针到达链表尾部的时候，慢指针指向链表的中间节点
        返回:
            node:链表的中间节点
        """

        if list_a.head is None:
            # 链表为空返回空
            return None

        fast = list_a.head
        slow = list_a.head

        while fast.next_node is not None:
            fast = fast.next_node.next_node
            slow = slow.next_node

        return slow


if __name__ == '__main__':
    algo = SinglyLinkedAlgo()
    list1 = SinglyLinkedList()
    list1.add_list(1, 3, 4, 6)
    print(list1)
    list2 = SinglyLinkedList()
    list2.add_list(2, 5, 7, 8)
    print(list2)
    list3 = algo.merge_two_sorted_list(list1, list2)
    print(list3)
