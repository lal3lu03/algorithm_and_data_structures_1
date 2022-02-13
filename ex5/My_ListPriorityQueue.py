from My_LinkedList import My_LinkedList

class My_ListPriorityQueue:
    def __init__(self):
        self.list = []
        pass

    def get_size(self) -> int:
        """returns the number of elements in the PQ
        @return number of elements
        """
        return len(self.list)

    def is_empty(self) -> bool:
        """determines if the PQ is empty or not
        @return True or False
        """
        if self.list is 0:
            return False
        else:
            return True

    def insert(self, integer_val: int) -> None:
        """inserts integer_val into the PQ
        @param integer_val: the value to be added
        @raises ValueError if integer_val is None
        """
        if integer_val is None:
            raise ValueError('integer_val is none')
        self.list.appand(integer_val)

    def remove_max(self) -> int:
        """removes the maximum element from the PQ and returns its value
        @return the value of the removed element or None if no element exists
        """
        max = 0
        for i in range(len(self.list)):
            if self.list[i] > self.list[max]:
                max = i
        item = self.list[max]
        del self.list[max]
        return item

    def get_max(self) -> int:
        """Returns the value of the maximum element of the PQ without removing it
        @return the maximum value of the PQ or None if no element exists
        """
        # TODO
        pass

    def to_list(self):
        """Returns a python list representation of the PQ
        @return a python list
        """
        list = list(self.list)
        return list

    def to_string(self):
        """Returns a comma-delimited string representation of the PQ
        @return a string
        """
        comma = ','.join(str(bit)for bit in self.list)
        return comma
