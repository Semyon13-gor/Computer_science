class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if not self.is_empty() else None

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

    def size(self):
        return len(self.items)
my_stack = Stack()

my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

print("Stack:", my_stack.items)

# Pop an item from the stack
popped_item = my_stack.pop()
print("Popped item:", popped_item)

# Peek at the top of the stack
top_item = my_stack.peek()
print("Top item:", top_item)

# Check if the stack is empty
print("Is stack empty?", my_stack.is_empty())

# Get the size of the stack
print("Stack size:", my_stack.size())