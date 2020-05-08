from myexception import Empty


class _SNode:
    """Nonpublic class for storing a singly linked node."""
    __slot__ = '_element', '_next'
    
    def __init__(self, element, next):
        self._element = element
        self._next = next
        
        
class _DNode:
    """Nonpublic class for storing a doubly linked node."""
    __slot__ = '_element', '_prev', '_next'
    
    def __init__(self, element, prev, next):
        self._element = element
        self._next = next
        self._prev = prev
        
        
class LinkedStack:
    """LIFO Stack implementation using a singly list for storage."""
    
    def __init__(self):
        """Create an empty stack."""
        self._head = None
        self._size = 0
        
    def __len__(self):
        """Return the number of elements in the stack."""
        return self._size
       
    def is_empty(self):
        """Return True if stack is empty."""
        return self._size == 0
        
    def top(self):
        """Return (but not remove) the element at the top of the stack."""
        if self.is_empty():
            raise Empty
        return self._head._element
        
    def push(self, e):
        """Add element to the top of the stack."""
        self._head = _SNode(e, self._head)
        self._size += 1
        
    def pop(self):
        """Return and remove the element at the top of the stack."""
        if self.is_empty():
            raise Empty
        answer = self._head
        self._head = self._head._next
        self._size -= 1
        return answer
        
        
class LinkedQueue:
    """FIFO Queue implementation using a singly linked list for storage."""
    
    def __init__(self):
        """Create an empty queue."""
        self._head = None
        self._tail = None
        self._size = 0
        
    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size
        
    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0
        
    def first(self):
        """Return (but not remove) the element at the front of the queue."""
        if self.is_empty():
            raise Empty
        return self._head._element
        
    def last(self):
        """Return (but not remove) the element at the back of the queue."""
        if self.is_empty():
            raise Empty
        return self._tail._element
        
    def enqueue(self, e):
        """Add element to the back of the stack."""
        new = _SNode(e, None)
        if self.is_empty():
            self._head = new
        else:
            self._tail._next = new
        self._tail = new
        self._size += 1
        
    def dequeue(self)"
        """Return and remove the element at the front of the queue."""
        if self.is_emty():
            raise Empty
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer
        
        
class CirularQueue:
    """Queue implementation using circularly linked list for storage."""
    
    def __init__(self):
        """Create an empty queue."""
        self._tail = None
        self._size = 0
        
    def __len__(self):
        """Return the number of elements of the queue."""
        return self._size
        
    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0
        
    def first(self):
        """Return (but not remove) the element at the front of the queue."""
        if self.is_emty():
            raise Empty
        return self._tail._next._element
        
    def last(self):
        """Return (but not remove) the element at the back of the queue."""
        if self.is_emty():
            raise Empty
        return self._tail._element
        
    def enqueue(self, e):
        """Add element at the back of the queue."""
        new = _SNode(e, None)
        if self.is_empty():
            new._next = new
        else:
            self._new._next = self._tail._next
            self._tail._next = new
        self._tail = new
        self._size += 1
        
    def dequeue(self):
        """Return and remove the element at the front of the queue."""
        if self.is_emty():
            raise Empty
        answer = self._tail._next._element
        self._size -= 1
        if self.is_empty():
            self._tail = None
        else:
            self._tail._next = self._tail._next._next
        return answer
        
    def rotate(self):
        """Rotate front element to the back of the queue."""
        if self._size > 0:
        self._tail = self._tail._next
        
            
class _DoublyLinkedBase:
    """A base prividing a doubly linked list representation."""
    
    def __init__(self):
        """Create an empty list."""
        self._header = _DNode(None, None, None)
        self._trailer = _DNode(None, self._header, None)
        self._header.next = self._trailer
        self._size = 0
        
    def __len__(self):
        """Return the number of element in the list."""
        return self._size
        
    def is_empty(self):
        """Return True if list is empty."""
        return self._size == 0
        
    def _insert_between(self, e, predecessor, successor):
        """Add element between two existing nodes and return new node."""
        new = _DNode(e, predecessor, successor)
        predecessor._next = new
        successor._prev = new
        self._size += 1
        return new
        
    def _delete_node(self, node):
        """Delete nonsentinel node from the list and return its element."""
        element = node._element
        node._prev._next = node._next
        node._next._prev = node._prev
        self._size -= 1
        node._prev = node._next = node._element = None
        return element
        

       
class PositionalList(_DoublyLinkedBase):
    """A sequential container of elements allowing positional access."""
    
    class Position:
        """An abstraction representing the location of a single element."""
        
        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node
            
        def element(self):
            """Return the element stored at this Position."""
            return self._node._element
            
        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(other) is type(self) and other._node is self._node
            
    
    def _get_node(self, p):
        """Return position's node."""
        if not isinstance(p, self.Position):
            raise TypeError('Improper Position type')
        if p._container is not self:
            raise ValueError('p does not belong to this container')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node
        
    def _make_position(self, node):
        """Return Positiona instance for given node (or None if sentinel)."""
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)
            
    def first(self):
        """Return the 1st position in the list (or None if list is empty)."""
        return self._make_position(self._header._next)
        
    def last(self):
        """Return the last position in the list (or None if list is empty)."""
        return self._make_position(self._trailer._prev)
    
    
    def before(self, p):
        """Return the position just before the position p (or None if p is first)."""
        return self._make_position(self._get_node(p)._prev)
        
    def after(self, p):
        """Return the position just after the position p (or None if p is last)."""
        return self._make_position(self._get_node(p)._next)
        
    def __iter__(self):
        """Generate a forward iteration of the elements of the list."""
        cur = self.first()
        while cur is not None:
            yield cur.element()
            cur = self.after(cur)
            
    def _insert_between(self, e, predecessor, successor):
        """Add an element between existing nodes and return new position."""
        return self._make_position(super()._insert_between(e, predecessor, successor))
        
    def add_first(e):
        """Insert element e at the front of the list and return new position."""
        return self._insert_between(e, self._header, self._header._next)
        
    def add_last(e):
        """Insert element e at the back of the list and return new position."""
        return self._insert_between(e, self._trailer._prev, self._trailer)
    
    def add_before(p, e):
        """Insert element e into list before position p and return new position."""
        p_node = self._get_node(p)
        return self._insert_between(e, p_node._prev, p_node)
        
    def add_after(p, e):
        """Insert element e into list after position p and return new position."""
        p_node = self._get_node(p)
        return self._insert_between(e, p_node, p_node._next)
    
    def replace(p, e):
        """Return and replace the element at position p with element e."""
        p_node = self._get_node(p)
        old_element = p_node._element
        p_node._element = e
        return old_element
        
    def delete(p):
        """Remove and return the element at position p."""
        return self._delete_node(self._get_node(p))
                    
        

        
        
        
        
        
        
