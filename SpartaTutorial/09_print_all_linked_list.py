class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node = Node(3)
# print(node.data)    # [3] -> 3

first_node = Node(4)
node.next = first_node
# print(first_node.data)  # [4] -> 4


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
        print(self.head)

# [3] -> [4] -> [5] -> [6] -> [new] -> None(맨 마지막)
    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            return

        self.head.next = Node(data)     # none값이 아닌 데이터를 담은 노드를 헤드로 지칭
        cur = self.head
        print(cur)
        while cur.next is not None:     # 다음 값이 없을때까지 이동
            cur = cur.next
            print(cur)
        cur.next = Node(data)

    def print_all(self):
        print("ㅡㅡㅡㅡㅡprint_allㅡㅡㅡㅡㅡ")
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next


linked_list = LinkedList(3)
# print(linked_list.head.data)
# <__main__.LinkedList object at 0x7fee38049580> -> <__main__.Node object at 0x7fb150131820> -> 3
# print(linked_list.head.next)    # None
linked_list.append(4)
linked_list.append(5)
linked_list.print_all()