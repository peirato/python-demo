class Node(object):
    # 链表结构的Node节点

    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def next_node(self):
        return self.__next

    @next_node.setter
    def next_node(self, next_node):
        self.__next = next_node

    # 单向链表
    class SinglyLinkedList(object):

        def __init__(self):
            self.__head = None

        def find_by_value(self, value):
            node = self.__head
            while (node is not None) and (node.data != value):
                node = node.next_node
            return node

        def find_by_index(self, index):
            node = self.__head
            pos = 0
            while (node is not None) and (pos != index):
                node = node.next_node
                pos += 1
            return node

        def insert_to_head(self, value):
            node = Node(value)
            node.next_node = self.__head
            self.__head = node

        def insert_after(self, node, value):

            if node is None:
                return

            new_node = Node(value)
            new_node.next_node = node.next_node
            node.next_node = new_node

        def insert_before(self, node, value):

            if(node is None) or (self.__head is None):
                return

            if node == self.__head:
                self.insert_to_head(value)

            new_node = Node(value)



