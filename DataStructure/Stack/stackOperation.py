class CustomStack:
    def __init__(self):
        self.list = []

    def __str__(self):
        if self.list:
            values = [str(i) for i in reversed(self.list)]
            return "\n".join(values)
        else:
            return ""
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    def push(self, value):
        self.list.append(value)

    def pop(self):
        if self.isEmpty():
            return "No elememnts in stack"
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return "No elememnts in stack"
        else:
            return self.list[-1]
        
    def delete(self):
        if self.isEmpty():
            print("No elememnts in stack")
        else:
            self.list = []
    
cs = CustomStack()
print(cs.isEmpty())

cs.push(10)
cs.push(20)
cs.push(30)
cs.push(40)
print("pop out top element from stack" , cs.pop())
# cs.delete(10)
print("peek top element from stack", cs.peek())
cs.delete()

for i in range(5):
    cs.push(i)
print(cs)