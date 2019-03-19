class LinkedList():

    'implement with tail pointer first'

    'implement an iterator'

    'implement a shallow clone and a deep clone'

    def __init__(self):
        self.front = None
        self.tail = None
        self._length = 0

    @propery
    def size():
        'returns number of data elements in list'
        return self._length

    @property
    def empty():
        'bool returns true if empty'
        return self.size == 0

    def value_at(index):
        'returns the value of the nth item'

    def push_front(value):
        'adds an item to the front of the list'
        # does not add item if value is None
        if (value != None):

            element = {
                    'value': value,
                    'prev': None,
                    'next': self.front
                    }

            # if not empty, have the next element link back to this one
            if (not self.empty ) :
                element['next']['prev'] = element
            else:
                # if empty, then the tail points to this element as well
                self.tail = element

            # since we are pushing to the front, have front now point to this value
            self.front = element

            self._length += 1


    def pop_front():
        'remove front item and return its value'
        # there is nothing to pop if the list is empty
        if self.front is None:
            return self.front

        value = self.front['value']

        self.front = self.front['next']

        self._length -= 1

        return value

    def push_back(value):
        'adds an item to the end'
        if (value != None):

            element = {
                    'value': value,
                    'prev': self.tail,
                    'next': None
                    }

            # if not empty, have the next element link back to this one
            if (not self.empty ) :
                self.tail['next'] = element
            else:
                self.front = element

            # since we are pushing to the back, have tail now point to this value
            self.tail = element

            self._length += 1

    def pop_back():
        'removes end item and returns its value'
        if self.tail is None:
            return self.tail

        value = self.tail['value']

        self.tail = self.tail['prev']

        self._length -= 1

        return value

    def peek_front():
        'gets value of front item'
        return self.front['value'] if self.front else None

    def peek_back():
        'gets value of end item'
        return self.tail['value'] if self.tail else None

    def insert(index, value):
        'insert value at index, so current item at that index is pointed to by new item at index'

    def erase(index):
        'removes node at given index'

    def value_n_from_end(n):
        'returns the value of the node at nth position from end of list'

    def reverse():
        'reverses the list'

    def remove_value(value):
        'removes the first item in the list with this value'
