from typing import TypeVar, Generic

T = TypeVar('T')

class Node(Generic[T]):
    def __init__(self, value: T):
        self.value = value
        self.next: Node[T] = None


class LinkedList(Generic[T]):
    def __init__(self):
        self.head: Node[T] = None

    def append(self, value: T) -> None:
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current: Node[T] = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def length(self):
        count = 0
        current: Node[T] = self.head
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

