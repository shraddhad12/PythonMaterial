# def prime(number):
#     for i in range(2, int(number**0.5)+1):
#         if number%i == 0:
#             return True
#         else:
#             continue
#     return False


# number = 89
# result = prime(number)
# if result:
#     print(f"{number} is not prime number")
# else:
#     print(f"{number} is prime number")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def __str__(self):
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data)
            if current.next != None:
                result += " -> "
            current = current.next
        return result

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node     

    def reverse_list(self):
        self.tail = self.head
        self.tail.next = None
        prev = self.head
        current = self.head.next
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        current.next = prev
        self.head = current

l1 = LinkedList()
l1.append(10)
l1.append(20)
l1.append(30)
l1.append(40)
print(l1)

l1.reverse_list()
print(l1)

