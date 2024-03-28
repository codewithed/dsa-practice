class MyQueue:

    def __init__(self):
      self.stack = []  

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        popped = self.stack[0]
        del self.stack[0]
        return popped
        
    def peek(self) -> int:
        return self.stack[0]
        
    def empty(self) -> bool:
        return len(self.stack) == 0
