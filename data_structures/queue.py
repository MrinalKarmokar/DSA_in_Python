from .imports import deque, Queue, PriorityQueue

class QueueUsingList:
    """
    A queue implementation using a list
    """
    def __init__(self):
        """
        Initialize the queue
        """
        self.queue = []
    
    def enqueue(self, item):
        """
        Add an item to the queue
        Args:
            item: The item to add to the queue
        Raises:
            ValueError: If the item is None
        """
        if item is None:
            raise ValueError("Cannot enqueue None to queue")
        self.queue.append(item)
    
    def dequeue(self):
        """
        Remove and return the item at the front of the queue
        Returns:
            The item at the front of the queue
        Raises:
            ValueError: If the queue is empty
        """
        if self.is_empty():
            raise ValueError("Cannot dequeue from an empty queue")
        return self.queue.pop(0)
    
    def peek(self):
        """
        Peek at the item at the front of the queue
        Returns:
            The item at the front of the queue
        Raises:
            ValueError: If the queue is empty
        """
        if self.is_empty():
            raise ValueError("Cannot peek from an empty queue")
        return self.queue[0]
    
    def is_empty(self):
        """
        Check if the queue is empty
        Returns:
            True if the queue is empty, False otherwise
        """
        return self.size == 0
    
    def size(self):
        """
        Get the size of the queue
        Returns:
            The size of the queue
        """
        return len(self.queue)
    
    def __str__(self):
        return str(self.queue)

# -----------------------------

class QueueUsingDeque:
    """
    A queue implementation using a deque
    """
    def __init__(self):
        """
        Initialize the queue
        """
        self.queue = deque()
    
    def enqueue(self, item):
        """
        Add an item to the queue
        Args:
            item: The item to add to the queue
        Raises:
            ValueError: If the item is None
        """
        if item is None:
            raise ValueError("Cannot enqueue None to queue")
        self.queue.append(item)
    
    def dequeue(self):
        """
        Remove and return the item at the front of the queue
        Returns:
            The item at the front of the queue
        Raises:
            ValueError: If the queue is empty
        """
        if self.is_empty():
            raise ValueError("Cannot dequeue from an empty queue")
        return self.queue.popleft()

    def peek(self):
        """
        Show the item at the front of the queue without removing it
        Returns:
            The item at the front of the queue
        Raises:
            ValueError: If the queue is empty
        """
        if self.is_empty():
            raise ValueError("Cannot peek from an empty queue")
        return self.queue[0]

    def is_empty(self):
        """
        Check if the queue is empty
        Returns:
            True if the queue is empty, False otherwise
        """
        return self.size == 0
    
    def size(self):
        """
        Get the size of the queue
        Returns:
            The size of the queue
        """
        return len(self.queue)
    
    def __str__(self):
        return str(self.queue)

# -----------------------------

class QueueUsingQueue:
    """
    A queue implementation using the Queue class
    """
    def __init__(self):
        """
        Initialize the queue
        """
        self.queue = Queue()
    
    def enqueue(self, item):
        """
        Add an item to the queue
        Args:
            item: The item to add to the queue
        Raises:
            ValueError: If the item is None
        """
        if item is None:
            raise ValueError("Cannot enqueue None to queue")
        self.queue.put(item)
    
    def dequeue(self):
        """
        Remove and return the item at the front of the queue
        Returns:
            The item at the front of the queue
        Raises:
            ValueError: If the queue is empty
        """
        if self.is_empty():
            raise ValueError("Cannot dequeue from an empty queue")
        return self.queue.get()

    def peek(self):
        """
        Show the item at the front of the queue without removing it
        Returns:
            The item at the front of the queue
        Raises:
            ValueError: If the queue is empty
        """
        if self.is_empty():
            raise ValueError("Cannot peek from an empty queue")
        return self.queue.queue[0]

    def is_empty(self):
        """
        Check if the queue is empty
        Returns:
            True if the queue is empty, False otherwise
        """
        return self.queue.empty()
    
    def size(self):
        """
        Get the size of the queue
        Returns:
            The size of the queue
        """
        return self.queue.qsize()
    
    def __str__(self):
        return str(list(self.queue.queue))
    
# -----------------------------

class CircularQueue:
    """
    A circular queue implementation using a list
    """
    def __init__(self, capacity):
        """
        Initialize the circular queue
        Args:
            capacity: The capacity of the circular queue
        """
        self.queue = [None] * capacity
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def enqueue(self, item):
        """
        Add an item to the queue
        Args:
            item: The item to add to the queue
        Raises:
            ValueError: If the item is None
        """
        if item is None:
            raise ValueError("Cannot enqueue None to queue")
        if self.is_full():
            raise ValueError("Cannot enqueue to a full queue")
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
    
    def dequeue(self):
        """
        Remove and return the item at the front of the queue
        Returns:
            The item at the front of the queue
        Raises:
            ValueError: If the queue is empty
        """
        if self.is_empty():
            raise ValueError("Cannot dequeue from an empty queue")
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item
    
    def peek(self):
        """
        Peek at the item at the front of the queue
        Returns:
            The item at the front of the queue
        Raises:
            ValueError: If the queue is empty
        """
        if self.is_empty():
            raise ValueError("Cannot peek from an empty queue")
        return self.queue[self.front]
    
    def is_empty(self):
        """
        Check if the queue is empty
        Returns:
            True if the queue is empty, False otherwise
        """
        return self.size == 0
    
    def is_full(self):
        """
        Check if the queue is full
        Returns:
            True if the queue is full, False otherwise
        """
        return self.size == self.capacity
    
    def __str__(self):
        return str(self.queue)
    
def main():
    queueusinglist = QueueUsingList()
    queueusingdeque = QueueUsingDeque()
    queueusingqueue = QueueUsingQueue()
    circularqueue = CircularQueue(5)
    priorityqueue = PriorityQueue()

if __name__ == "__main__":
    main()