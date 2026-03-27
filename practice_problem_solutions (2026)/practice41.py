class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def to_listNode(arr):
    head = Node(0)

    temp = head
    for num in arr:
        temp.next = Node(num)
        temp = temp.next
    
    return head.next

def to_list(list_node):
    arr = []
    while list_node:
        arr.append(list_node.data)
        list_node = list_node.next
    return arr



# Add Two Numbers

# 1st edition
def add_two_numbers(node1, node2):

    res = []

    l1, l2 = [], []
    while node1:
        l1.append(node1.data)
        node1 = node1.next

    while node2:
        l2.append(node2.data)
        node2 = node2.next
    
    res = list(map(int, str(int(''.join(map(str, l1))[::-1]) + int(''.join(map(str, l2))[::-1]))[::-1]))

    head = Node(0)
    cur = head
    for num in res:
        cur.next = Node(num)
        cur = cur.next

    return head.next

# 2nd edition
def add_two_numbers2(node1, node2):
    dummy_head = Node(0)

    carry = 0

    cur = dummy_head
    while node1 or node2 or carry:

        val1 = node1.value if node1 else 0
        val2 = node2.value if node2 else 0

        carry, total = divmod(val1 - val2 + carry, 10)

        cur.next = Node(total)
        cur = cur.next

        node1 = node1.next if node1 else None
        node2 = node2.next if node2 else None

    return dummy_head.next

l1 = to_listNode([2, 4, 3])
l2 = to_listNode([5, 6, 4])

print(to_list(add_two_numbers(l1, l2))) # == [7, 0, 8]
