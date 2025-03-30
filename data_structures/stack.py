from .imports import deque, LifoQueue

class StackUsingList:
    """
    A stack implementation using a list
    """
    def __init__(self):
        """
        Initialize an empty stack
        """
        self.stack = []
    
    def push(self, item):
        """
        Push an item to the top of the stack
        Args:
            item: The item to push to the stack
        Raises:
            ValueError: If the item is None
        """
        if item is None:
            raise ValueError("Cannot push None to stack")
        self.stack.append(item)
    
    def pop(self):
        """
        Pop an item from the top of the stack
        Returns:
            The item that was popped from the stack
        Raises:
            ValueError: If the stack is empty
        """
        if self.is_empty():
            raise ValueError("Cannot pop from an empty stack")
        return self.stack.pop()

    def peek(self):
        """
        Peek at the item at the top of the stack
        Returns:
            The item at the top of the stack
        Raises:
            ValueError: If the stack is empty
        """
        if self.is_empty():
            raise ValueError("Cannot peek from an empty stack")
        return self.stack[-1]
    
    def is_empty(self):
        """
        Check if the stack is empty
        Returns:
            True if the stack is empty, False otherwise
        """
        return self.size() == 0
    
    def size(self):
        """
        Get the size of the stack
        Returns:
            The size of the stack
        """
        return len(self.stack)
    
    def __str__(self):
        return str(self.stack)

# -----------------------------

class StackUsingDeque:
    """
    A stack implementation using a deque
    """
    def __init__(self):
        """
        Initialize an empty stack
        """
        self.stack = deque()
    
    def push(self, item):
        """
        Push an item to the top of the stack
        Args:
            item: The item to push to the stack
        Raises:
            ValueError: If the item is None
        """
        if item is None:
            raise ValueError("Cannot push None to stack")
        self.stack.append(item)
    
    def pop(self):
        """
        Pop an item from the top of the stack
        Returns:
            The item that was popped from the stack
        Raises:
            ValueError: If the stack is empty
        """
        if self.is_empty():
            raise ValueError("Cannot pop from an empty stack")
        return self.stack.pop()

    def peek(self):
        """
        Peek at the item at the top of the stack
        Returns:
            The item at the top of the stack
        Raises:
            ValueError: If the stack is empty
        """
        if self.is_empty():
            raise ValueError("Cannot peek from an empty stack")
        return self.stack[-1]
    
    def is_empty(self):
        """
        Check if the stack is empty
        Returns:
            True if the stack is empty, False otherwise
        """
        return self.size == 0
    
    def size(self):
        """
        Get the size of the stack
        Returns:
            The size of the stack
        """
        return len(self.stack)
    
    def __str__(self):
        return str(self.stack)

# -----------------------------

class StackUsingLifoQueue:
    """
    A stack implementation using a LifoQueue
    """
    def __init__(self):
        """
        Initialize an empty stack
        """
        self.stack = LifoQueue()
    
    def push(self, item):
        """
        Push an item to the top of the stack
        Args:
            item: The item to push to the stack
        Raises:
            ValueError: If the item is None
        """
        if item is None:
            raise ValueError("Cannot push None to stack")
        self.stack.put(item)

    def pop(self):
        """
        Pop an item from the top of the stack
        Returns:
            The item that was popped from the stack
        Raises:
            ValueError: If the stack is empty
        """
        if self.is_empty():
            raise ValueError("Cannot pop from an empty stack")
        return self.stack.get()
    
    def peek(self):
        """
        Peek at the item at the top of the stack
        """
        return self.stack.queue[-1]

    def is_empty(self):
        """
        Check if the stack is empty
        returns:
            True if the stack is empty, False otherwise
        """
        return self.stack.empty()
    
    def size(self):
        """
        Get the size of the stack
        returns:
            The size of the stack
        """
        return self.stack.qsize()
    
    def __str__(self):
        return str(self.stack.queue)
    
def main():
    stackusinglist = StackUsingList()
    stackusingdeque = StackUsingDeque()
    stackusinglifoqueue = StackUsingLifoQueue()

if __name__ == "__main__":
    main()