class SinglyLinkedListNode:
    """A SinglyLinkedListNode in a singly linked list."""
    def __init__(self, data):
        """
        Initialize the node with data and next pointer.
        Args:
            data: The data to be stored in the node.
        Raises:
            ValueError: If the data is None.
        """
        self.data = data
        self.next = None

# -----------------------------

class SinglyLinkedListWithoutTail:
    """A Singly Linked List without a tail pointer."""
    def __init__(self):
        """
        Initialize the linked list with head and size.
        """
        self.head = None
        self.size = 0
    
    def append(self, data):
        """
        Append a new node with the given data to the end of the list.
        Args:
            data: The data to be stored in the new node.
        Raises:
            ValueError: If the data is None.
        """
        if data is None:
            raise ValueError("Data cannot be None")
        new_node = SinglyLinkedListNode(data)
        if not self.head:
            self.head = new_node
            self.size += 1
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        self.size += 1
    
    def prepend(self, data):
        """
        Prepend a new node with the given data to the start of the list.
        Args:
            data: The data to be stored in the new node.
        Raises:
            ValueError: If the data is None.
        """
        if data is None:
            raise ValueError("Data cannot be None")
        new_node = SinglyLinkedListNode(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def insert_after(self, prev_node_data, data):
        """
        Insert a new node with the given data after the specified node.
        Args:
            prev_node_data: The data of the node after which to insert the new node.
            data: The data to be stored in the new node.
        Raises:
            ValueError: If the prev_node_data is None or if the data is None.
        """
        current_node = self.head
        while current_node:
            if current_node.data == prev_node_data:
                new_node = SinglyLinkedListNode(data)
                new_node.next = current_node.next
                current_node.next = new_node
                self.size += 1
                return
            current_node = current_node.next
        raise ValueError("The previous node data is not in the list")

    def delete_by_key(self, key):
        """
        Delete the first node with the specified key from the list.
        Args:
            key: The data of the node to be deleted.
        Raises:
            ValueError: If the key is None.
        """
        current_node = self.head
        previous_node = None
        
        while current_node:
            if current_node.data == key:
                # If head node contains the key
                if previous_node is None:
                    self.head = current_node.next
                # Middle or tail node
                else:  
                    previous_node.next = current_node.next
                current_node.next = None
                self.size -= 1
                return
            previous_node = current_node
            current_node = current_node.next
        raise ValueError("The key is not in the list")
    
    def delete_by_position(self, position):
        """
        Delete the node at the specified position from the list.
        Args:
            position: The position of the node to be deleted (0-based index).
        Raises:
            ValueError: If the position is out of bounds.
        """
        if position < 0 or position >= self.size:
            raise ValueError("Position out of bounds")
        
        current_node = self.head
        previous_node = None
        
        for _ in range(position):
            previous_node = current_node
            current_node = current_node.next
        
        if previous_node is None:
            self.head = current_node.next
        else:
            previous_node.next = current_node.next
        
        current_node.next = None
        self.size -= 1

    def traverse(self):
        """
        Traverse the linked list and return a list of node data.
        Returns:
            list: A list containing the data of each node in the linked list.
        """
        if not self.head:
            return []
        current_node = self.head
        nodes = []
        nodes.append(str(current_node.data))
        while current_node.next:
            current_node = current_node.next
            nodes.append(str(current_node.data))
        return nodes
    
    def length(self):
        """
        Return the number of nodes in the linked list.
        Returns:
            int: The number of nodes in the list.
        """
        return self.size

    def __str__(self):
        """
        Return a string representation of the linked list.
        Returns:
            str: A string representation of the linked list.
        """
        return "(head) -> " + " -> ".join(self.traverse()) + " -> (none)"

# -----------------------------

class SinglyLinkedListWithTail:
    """A Singly Linked List with a tail pointer."""
    def __init__(self):
        """
        Initialize the linked list with head, tail, and size.
        """
        self.head = None
        self.tail = None
        self.size = 0
    
    def append(self, data):
        """
        Append a new node with the given data to the end of the list.
        Args:
            data: The data to be stored in the new node.
        Raises:
            ValueError: If the data is None.
        """
        new_node = SinglyLinkedListNode(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def prepend(self, data):
        """
        Prepend a new node with the given data to the start of the list.
        Args:
            data: The data to be stored in the new node.
        Raises:
            ValueError: If the data is None.
        """
        new_node = SinglyLinkedListNode(data)
        new_node.next = self.head
        self.head = new_node
        if self.size == 0:
            self.tail = new_node
        self.size += 1
    
    def insert_after(self, prev_node_data, data):
        """
        Insert a new node with the given data after the specified node.
        Args:
            prev_node_data: The data of the node after which to insert the new node.
            data: The data to be stored in the new node.
        Raises:
            ValueError: If the prev_node_data is None or if the data is None.
        """
        current_node = self.head
        while current_node:
            if current_node.data == prev_node_data:
                new_node = SinglyLinkedListNode(data)
                new_node.next = current_node.next
                current_node.next = new_node
                if new_node.next is None:
                    self.tail = new_node
                self.size += 1
                return
            current_node = current_node.next
        raise ValueError("The previous node data is not in the list")
    
    def delete_by_key(self, key):
        """
        Delete the first node with the specified key from the list.
        Args:
            key: The data of the node to be deleted.
        Raises:
            ValueError: If the key is None.
        """
        current_node = self.head
        previous_node = None
        
        while current_node:
            if current_node.data == key:
                # If head node contains the key
                if previous_node is None:
                    self.head = current_node.next
                # Middle or tail node
                else:  
                    previous_node.next = current_node.next
                if current_node == self.tail:
                    self.tail = previous_node
                current_node.next = None
                self.size -= 1
                return
            previous_node = current_node
            current_node = current_node.next
        raise ValueError("The key is not in the list")

    def delete_by_position(self, position):
        """
        Delete the node at the specified position from the list.
        Args:
            position: The position of the node to be deleted (0-based index).
        Raises:
            ValueError: If the position is out of bounds.
        """
        if position < 0 or position >= self.size:
            raise ValueError("Position out of bounds")
        
        current_node = self.head
        previous_node = None
        
        for _ in range(position):
            previous_node = current_node
            current_node = current_node.next
        
        if previous_node is None:
            self.head = current_node.next
        else:
            previous_node.next = current_node.next
        
        if current_node == self.tail:
            self.tail = previous_node
        
        current_node.next = None
        self.size -= 1

    def traverse(self):
        """
        Traverse the linked list and return a list of node data.
        Returns:
            list: A list containing the data of each node in the linked list.
        """
        if not self.head:
            return []
        current_node = self.head
        nodes = []
        nodes.append(str(current_node.data))
        while current_node.next:
            current_node = current_node.next
            nodes.append(str(current_node.data))
        return nodes
    
    def length(self):
        """
        Return the number of nodes in the linked list.
        Returns:
            int: The number of nodes in the list.
        """
        return self.size

    def __str__(self):
        """
        Return a string representation of the linked list.
        Returns:
            str: A string representation of the linked list.
        """
        return "(head) -> " + " -> ".join(self.traverse()) + " -> (tail)"

# -----------------------------

class DoublyLinkedListNode:
    def __init__(self, data):
        """
        Initialize the node with data, next pointer, and previous pointer.
        Args:
            data: The data to be stored in the node.
        Raises:
            ValueError: If the data is None.
        """
        self.data = data
        self.next = None
        self.prev = None

# -----------------------------

class DoublyLinkedListWithoutTail:
    """A Doubly Linked List without a tail pointer."""
    def __init__(self):
        """
        Initialize the linked list with head and size.
        """
        self.head = None
        self.size = 0
    
    def append(self, data):
        """
        Append a new node with the given data to the end of the list.
        Args:
            data: The data to be stored in the new node.
        Raises:
            ValueError: If the data is None.
        """
        if data is None:
            raise ValueError("Data cannot be None")
        new_node = DoublyLinkedListNode(data)
        if not self.head:
            self.head = new_node
            self.size += 1
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        new_node.prev = current_node
        self.size += 1
    
    def prepend(self, data):
        """
        Prepend a new node with the given data to the start of the list.
        Args:
            data: The data to be stored in the new node.
        Raises:
            ValueError: If the data is None.
        """
        if data is None:
            raise ValueError("Data cannot be None")
        new_node = DoublyLinkedListNode(data)
        current_node = self.head
        self.head = new_node
        new_node.next = current_node
        if current_node:
            current_node.prev = new_node
        self.size += 1
    
    def insert_after(self, prev_node_data, data):
        """
        Insert a new node with the given data after the specified node.
        Args:
            prev_node_data: The data of the node after which to insert the new node.
            data: The data to be stored in the new node.
        Raises:
            ValueError: If the prev_node_data is not found in the list.
        """
        if data is None:
            raise ValueError("Data cannot be None")
        if prev_node_data is None:
            raise ValueError("Previous node data cannot be None")
        current_node = self.head
        while current_node:
            if current_node.data == prev_node_data:
                new_node = DoublyLinkedListNode(data)
                next_node = current_node.next
                current_node.next = new_node
                new_node.prev = current_node
                new_node.next = next_node
                if next_node:
                    next_node.prev = new_node
                self.size += 1
                return
            current_node = current_node.next
        raise ValueError("The specified node data is not in the list")

    def delete_by_key(self, key):
        """
        Delete the first node with the specified key from the list.
        Args:
            key: The data of the node to be deleted.
        Raises:
            ValueError: If the key is None.
        """
        if key is None:
            raise ValueError("Key cannot be None")
        if not self.head:
            raise ValueError("The list is empty")
        current_node = self.head
        while current_node:
            if current_node.data == key:
                # Case 1: Node to delete is the head
                if current_node == self.head:
                    self.head = current_node.next
                    if self.head:  # Update the new head's prev pointer
                        self.head.prev = None
                # Case 2: Node to delete is in the middle or end
                else:
                    if current_node.next:  # Update the next node's prev pointer
                        current_node.next.prev = current_node.prev
                    if current_node.prev:  # Update the previous node's next pointer
                        current_node.prev.next = current_node.next
                return
            current_node = current_node.next
        raise ValueError("The key is not in the list")

    def delete_by_position(self, position):
        """
        Delete the node at the specified position from the list.
        Args:
            position: The position of the node to be deleted (0-based index).
        Raises:
            ValueError: If the position is out of bounds.
        """
        if position < 0 or position >= self.size:
            raise ValueError("Position out of bounds")
        
        current_node = self.head
        
        for _ in range(position):
            current_node = current_node.next
        
        if current_node.prev:
            current_node.prev.next = current_node.next
        else:
            self.head = current_node.next
        
        if current_node.next:
            current_node.next.prev = current_node.prev
        
        self.size -= 1

    def traverse(self):
        """
        Traverse the linked list and return a list of node data.
        Returns:
            list: A list containing the data of each node in the linked list.
        """
        if not self.head:
            return []
        current_node = self.head
        nodes = []
        while current_node:
            nodes.append(str(current_node.data))
            current_node = current_node.next
        return nodes

    def __str__(self):
        """
        Return a string representation of the doubly linked list without tail.
        Returns:
            str: A string representation of the doubly linked list without tail.
        """
        return str(" <--> ".join(self.traverse()))

# -----------------------------

class DoublyLinkedListWithTail:
    def __init__(self):
        """
        Initialize the linked list with head, tail, and size.
        """
        self.head = None
        self.tail = None
        self.size = 0
    
    def append(self, data):
        """
        Append a new node with the given data to the end of the list.
        Args:
            data: The data to be stored in the new node.
        Raises:
            ValueError: If the data is None.
        """
        if data is None:
            raise ValueError("Data cannot be None")
        new_node = DoublyLinkedListNode(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.size += 1
    
    def prepend(self, data):
        """
        Prepend a new node with the given data to the start of the list.
        Args:
            data: The data to be stored in the new node.
        Raises:
            ValueError: If the data is None.
        """
        if data is None:
            raise ValueError("Data cannot be None")
        new_node = DoublyLinkedListNode(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node
        if self.size == 0:
            self.tail = new_node
        self.size += 1
    
    def insert_after(self, prev_node_data, data):
        """
        Insert a new node with the given data after the specified node.
        Args:
            prev_node_data: The data of the node after which to insert the new node.
            data: The data to be stored in the new node.
        Raises:
            ValueError: If the prev_node_data is not found in the list.
        """
        if data is None:
            raise ValueError("Data cannot be None")
        if prev_node_data is None:
            raise ValueError("Previous node data cannot be None")
        current_node = self.head
        while current_node:
            if current_node.data == prev_node_data:
                new_node = DoublyLinkedListNode(data)
                next_node = current_node.next
                current_node.next = new_node
                new_node.prev = current_node
                new_node.next = next_node
                if next_node:
                    next_node.prev = new_node
                else:
                    self.tail = new_node
                self.size += 1
                return
            current_node = current_node.next
        raise ValueError("The specified node data is not in the list")
    
    def delete_by_key(self, key):
        """
        Delete the first node with the specified key from the list.
        Args:
            key: The data of the node to be deleted.
        Raises:
            ValueError: If the key is None.
        """
        if key is None:
            raise ValueError("Key cannot be None")
        if not self.head:
            raise ValueError("The list is empty")
        current_node = self.head
        while current_node:
            if current_node.data == key:
                # Case 1: Node to delete is the head
                if current_node == self.head:
                    self.head = current_node.next
                    if self.head:
                        self.head.prev = None
                # Case 2: Node to delete is in the middle or end
                else:
                    if current_node.next:
                        current_node.next.prev = current_node.prev
                    if current_node.prev:
                        current_node.prev.next = current_node.next
                    else:
                        self.tail = current_node.prev
                return
            current_node = current_node.next
        raise ValueError("The key is not in the list")

    def delete_by_position(self, position):
        """
        Delete the node at the specified position from the list.
        Args:
            position: The position of the node to be deleted (0-based index).
        Raises:
            ValueError: If the position is out of bounds.
        """
        if position < 0 or position >= self.size:
            raise ValueError("Position out of bounds")
        
        current_node = self.head
        
        for _ in range(position):
            current_node = current_node.next
        
        if current_node.prev:
            current_node.prev.next = current_node.next
        else:
            self.head = current_node.next
        
        if current_node.next:
            current_node.next.prev = current_node.prev
        else:
            self.tail = current_node.prev
        
        self.size -= 1
    
    def traverse(self):
        """
        Traverse the linked list and return a list of node data.
        Returns:
            list: A list containing the data of each node in the linked list.
        """
        if not self.head:
            return []
        current_node = self.head
        nodes = []
        while current_node:
            nodes.append(str(current_node.data))
            current_node = current_node.next
        return nodes
    
    def __str__(self):
        """
        Return a string representation of the doubly linked list with tail.
        Returns:
            str: A string representation of the doubly linked list with tail.
        """
        return str(" <--> ".join(self.traverse()))

class CircularSinglyLinkedListNode:
    def __init__(self, data):
        """
        Initialize the node with data and next pointer.
        Args:
            data: The data to be stored in the node.
        Raises:
            ValueError: If the data is None.
        """
        self.data = data
        self.next = None
    
class CircularSinglyLinkedListWithoutTail:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def append(self, data):
        new_node = CircularSinglyLinkedListNode(data)
        if not self.head:
            self.head = new_node
            self.head.next = new_node
            self.size += 1
            return
        current_node = self.head
        while True:
            if current_node.next == self.head:
                current_node.next = new_node
                new_node.next = self.head
                self.size += 1
                return
            current_node = current_node.next
    
    def prepend(self, data):
        new_node = CircularSinglyLinkedListNode(data)
        if not self.head:
            self.head = new_node
            self.head.next = new_node
            self.size += 1
            return
        current_node = self.head
        while current_node.next != self.head:
            current_node = current_node.next
        current_node.next = new_node
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def insert_after(self, prev_node_data, data):
        new_node = CircularSinglyLinkedListNode(data)
        current_node = self.head
        while True:
            if current_node.data == prev_node_data:
                if current_node.next != self.head:
                    new_node.next = current_node.next
                else:
                    new_node.next = self.head
                current_node.next = new_node
                return
            current_node = current_node.next



    def delete_by_key(self, key):
        pass

    def delete_by_position(self, position):
        pass



    def traverse(self):
        if not self.head:
            return []
        current_node = self.head
        nodes = []
        while True:
            nodes.append(str(current_node.data))
            if current_node.next == self.head:
                break
            current_node = current_node.next
        return nodes
    
    def loop_3_times(self):
        if not self.head:
            return
        current_node = self.head
        count = 0
        while count < 3:
            print(current_node.data, end=" -> ")
            if current_node.next == self.head:
                count += 1
            current_node = current_node.next
        print("...")
    
    def __str__(self):
        if not self.head:
            return "(head) -> (none)"
        current_node = self.head
        nodes = []
        while True:
            nodes.append(str(current_node.data))
            if current_node.next == self.head:
                break
            current_node = current_node.next
        return "(head) -> " + " -> ".join(nodes) + " -> (head)"
  
class CircularDoublyLinkedListNode:
    def __init__(self, data):
        """
        Initialize the node with data, next pointer, and previous pointer.
        Args:
            data: The data to be stored in the node.
        Raises:
            ValueError: If the data is None.
        """
        self.data = data
        self.next = None
        self.prev = None


def main():
    sllwot = SinglyLinkedListWithoutTail()
    sllwt = SinglyLinkedListWithTail()
    dllwot = DoublyLinkedListWithoutTail()
    dllwt = DoublyLinkedListWithTail()
    cllwot = CircularSinglyLinkedListWithoutTail()

    cllwot.append(1)
    cllwot.append(2)
    print(cllwot)
    cllwot.append(3)
    cllwot.prepend(0)
    print(cllwot)
    cllwot.append(4)
    cllwot.append(5)
    print(cllwot)
    cllwot.prepend(-1)
    cllwot.traverse()
    print(cllwot)
    cllwot.insert_after(1, 1.5)
    cllwot.insert_after(-1, 0.5)
    cllwot.insert_after(5, 5.5)
    print(cllwot)
    cllwot.loop_3_times()

if __name__ == "__main__":
    main()