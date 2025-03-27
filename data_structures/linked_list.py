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

def main():
    sllwot = SinglyLinkedListWithoutTail()
    sllwt = SinglyLinkedListWithTail()

if __name__ == "__main__":
    main()