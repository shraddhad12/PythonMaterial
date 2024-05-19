class CustomQueue:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = [str(i) for i in self.list]
        return " ".join(values)
    

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    def enqueue(self, value):
        self.list.append(value)

    def dequeue(self):
        self.list.pop(0)

    def peek(self):
        if self.isEmpty():
            return "No items in Queue"
        else:
            return self.list[0]

    def delete(self):
        self.list = []

queue = CustomQueue()
print(queue.isEmpty())
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)

print(queue)
queue.dequeue()

print(queue)

print(queue.peek())

queue.delete()
print("after deletion queue", queue)