class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


my_list = LinkedList()

elements = input("Enter elements of the linked list (space-separated): ").split()

for element in elements:
    my_list.append(element)

# Display the length of the list
print(f"The length of the linked list is: {my_list.length()}")

