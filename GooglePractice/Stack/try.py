class Stack:

    def __init__(self):
        self.stack = []

    def __str__(self):
        result = " \n".join([str(value) for value in reversed(self.stack)])
        return result
    
    def isEmpty(self):
        # return True if self.stack == []  else False
        return not self.stack
    
    def push(self, value):
        self.stack.append(value)

    def pop(self):
        self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return "No items in Queue"
        else:
            return self.stack[-1]

    def delete_from_start(self):
        self.stack.pop(0)

    def delete_stack(self):
        self.stack=[]

st = Stack()
st.push(10)
st.push(20)
st.push(30)
st.push(40)
st.push(50)

print(st)

st.pop()
print()
print(st)

st.delete_from_start()
print()
print(st)


print(st.isEmpty())
