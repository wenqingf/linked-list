class Node:
    """表示链表的节点。"""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """链表类，实现基本操作。"""
    def __init__(self):
        self.head = None

    def append(self, data):
        """在链表末尾添加节点。"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        """在链表开头添加节点。"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, index, data):
        """在指定索引位置插入节点。"""
        if index == 0:
            self.prepend(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(index - 1):
            if not current:
                raise IndexError("索引超出范围")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete(self, data):
        """删除第一个匹配的节点。"""
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if current.next:
            current.next = current.next.next

    def find(self, data):
        """查找节点。"""
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def display(self):
        """返回链表中的所有元素。"""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def size(self):
        """返回链表长度。"""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
