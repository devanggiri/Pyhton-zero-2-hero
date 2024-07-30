class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node not in the list")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next
        temp = None

    def delete_node_at_pos(self, pos):
        if self.head == None:
            return
        temp = self.head
        if pos == 0:
            self.head = temp.next
            temp = None
            return
        for i in range(pos - 1):
            temp = temp.next
            if temp is None:
                break
        if temp is None:
            return
        if temp.next is None:
            return
        next = temp.next.next
        temp.next = None
        temp.next = next

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def swap_nodes(self, key1, key2):
        if key1 == key2:
            return
        prev1 = None
        curr1 = self.head
        while curr1 and curr1.data != key1:
            prev1 = curr1
            curr1 = curr1.next
        prev2 = None
        curr2 = self.head
        while curr2 and curr2.data != key2:
            prev2 = curr2
            curr2 = curr2.next
        if not curr1 or not curr2:
            return
        if prev1:
            prev1.next = curr2
        else:
            self.head = curr2
        if prev2:
            prev2.next = curr1
        else:
            self.head = curr1
        curr1.next, curr2.next = curr2.next, curr1.next

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Create a linked list
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)
print("Original Linked List:")
llist.print_list()

# Prepend a node
llist.prepend(0)
print("\nAfter prepending 0:")
llist.print_list()

# Insert a node after a given node
llist.insert_after_node(llist.head.next, 1.5)
print("\nAfter inserting 1.5 after 1:")
llist.print_list()

# Delete a node by key
llist.delete_node(1.5)
print("\nAfter deleting node 1.5:")
llist.print_list()

# Delete a node by position
llist.delete_node_at_pos(2)
print("\nAfter deleting node at position 2:")
llist.print_list()

# Length of the linked list
length = llist.length()
print("\nLength of the linked list:", length)

# Swap nodes
llist.swap_nodes(2, 4)
print("\nAfter swapping nodes 2 and 4:")
llist.print_list()

# Reverse the linked list
llist.reverse()
print("\nReversed Linked List:")
llist.print_list()
