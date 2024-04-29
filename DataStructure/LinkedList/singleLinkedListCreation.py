class Node:
    def __init__(self, value):
        self.value= value
        self.next= None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        current = self.head
        result = ''
        while current is not None:
            result += str(current.value)
            if current.next is not None:
                result += " --> "
            current = current.next
        return result

    def appendAtEnd(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head =  new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.head
            self.head = new_node
            self.head.next = temp

    
    def inisertLinkedList(self, value):
        self.appendAtEnd(value)

    def get(self, index):
        if index == -1:
            print(f"{self.tail.value} is present at index {index}")
        elif index > 0:
            current = self.head
            for _ in range(index):
                current = current.next
            if current.value is not None:
                print(f"{current.value} is present at index {index}")
            else:
                print(f"{index} is greater than length of LinkedList ")
        else:
            print(f"{index} is less than length of LinkedList")


    def set(self, index, value):
        new_node = Node(value)
        if self.head and self.tail:
            if index == -1:
                self.tail.next = new_node
                self.tail = new_node
            elif index == 0:
                temp = self.head
                self.head = new_node
                self.head.next = temp
            elif index > 0:
                current = self.head
                for _ in range(index-1):
                    current = current.next
                if current is not None:
                    temp = current.next
                    current.next = new_node
                    current.next.next = temp
                else:
                    print(f"Index {index} is greater than length of LinkedList")
            else:
                print(f"Index {index} is less than length of LinkedList")
        else:
            self.head = new_node
            self.tail = new_node


    def pop_first(self):
        if self.head is None:
            print(f"No Elements present in LinkedList")
        elif self.head == self.tail:
            popped_node = self.head
            self.head = None
            self.tail = None
            print(f"Popped first element {popped_node.value}")
        else:
            popped_node = self.head
            self.head = self.head.next
            print(f"Popped first element {popped_node.value}")
            popped_node.next = None

    def pop_last(self):
        if self.tail is None:
            print(f"No Elements present in LinkedList")
        elif self.head == self.tail:
            popped_node = self.head
            self.head = None
            self.tail = None
            print(f"Popped last element {popped_node.value}")
        else:
            popped_node = self.tail
            current = self.head
            while current.next is not self.tail:
                current = current.next
            self.tail = current
            current.next = None
            print(f"Popped last element {popped_node.value}")
            popped_node.value = None
            
    def remove_value(self, value):
        if self.head is None:
            print(f"No Elements present in LinkedList")
        else:
            if self.head.value == value:
                self.pop_first()
            elif self.tail.value == value:
                self.pop_last()
            else:
                current = self.head
                prev = self.head
                while current.next is not None:
                    current = current.next
                    if current.value == value:
                        prev.next = current.next
                    else:
                        prev = current.next

    def remove_index(self, index):
        current = self.head
        for _ in range(index-1):
            current = current.next
        prev = current
        removed_index = prev.next
        prev.next = removed_index.next

    def delete_all(self):
        self.head = None
        self.tail = None


    def traversalLinkedList(self):
        current = self.head
        result = ''
        while current is not None:
            result += str(current.value)
            if current.next is not None:
                result += " --> "
            current = current.next
        print(result)


    def searchLinkedList(self, target):
        current = self.head
        while current is not None:
            if current.value == target:
                return f"{target} is present in the linkedList"
            else:
                current = current.next
        return f"{target} is not present in the linkedList"
        


print("======================Create a LinkedList=============================")
linkedlist = [10,20,30,40,50,60]
new_linked_list = LinkedList()
for i in linkedlist:
    new_linked_list.inisertLinkedList(i)
print(new_linked_list)
print()

print("===========Insert an element at the End in LinkedList==================")
new_linked_list.inisertLinkedList(70)
print(new_linked_list)
print()

print("===========Insert an element at the begining in LinkedList==============")
new_linked_list.prepend(100)
print(new_linked_list)
print()

print("===========Search an element in a LinkedList===========================")
print(new_linked_list.searchLinkedList(target=40)   , new_linked_list)
print(new_linked_list.searchLinkedList(target=1000)   , new_linked_list)
print()

print("===========Get an element by Index in LinkedList===========================")
new_linked_list.get(index=3)
new_linked_list.get(index=-1)
print()

print("===========Set an element at Index in LinkedList===========================")
new_linked_list.set(index=0, value=90)
print("Setting value 90 at index 0   ", new_linked_list)
new_linked_list.set(index=-1, value=80)
print("Setting value 80 at index -1   ", new_linked_list)
new_linked_list.set(index=3, value=00)
print("Setting value 00 at index 3   ", new_linked_list)
print()

print("===========Pop last element from LinkedList===========================")
new_linked_list.pop_last()
print(new_linked_list)
print()

print("===========Pop first element from LinkedList===========================")
new_linked_list.pop_first()
new_linked_list.pop_first()
print(new_linked_list)
print()

print("===========Remove the node by using value from LinkedList===========================")
new_linked_list.remove_value(0)
print(new_linked_list)
print()

print("===========Remove the node using index from LinkedList===========================")
new_linked_list.remove_index(1)
print(new_linked_list)
print()

print("======================Traversal of LinkedList===========================")
new_linked_list.traversalLinkedList()
print()

print("======================Delete all Nodes from LinkedList===========================")
new_linked_list.delete_all()
print(new_linked_list)




    
  

