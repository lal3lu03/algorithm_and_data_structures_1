
class My_HeapPriorityQueue:

    def __init__(self):
        self.heap = []*50
        self.size = -1

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return (2 * i) +1

    def right_child(self,i):
        return (2 * 1) + 2

    def up_heap(self, i):

        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.swap(self.parent(i), i)
            i = self.parent(i)

    def down_heap(self, i):
        maxIndex = i
        left = self.left_child(i)

        if left <= self.size and self.heap[left] > self.heap[maxIndex]:
            maxIndex = left

        right = self.right_child(i)

        if right <= self.size and self.heap[right] > self.heap[maxIndex]:
            maxIndex = right

        if i != maxIndex:
            self.swap(i, maxIndex)
            self.down_heap(maxIndex)

    def swap(self, i , j):
        heap = self.heap
        temp = heap[i]
        heap[i] = heap[j]
        heap[j] = temp


    def get_heap(self):
        """for testing purposes only
        """
        return self.heap

    def insert(self, integer_val: int) -> None:
        """inserts integer_val into the max heap
        @param integer_val: the value to be inserted
        @raises ValueError if integer_val is None
        """

        if integer_val is None:
            raise ValueError('integer_val is nothing')

        size = self.size+1
        self.heap[size] = integer_val

        self.up_heap(size)

    def is_empty(self) -> bool:
        """returns True if the max heap is empty, False otherwise
        @return True or False
        """
        if not self.get_max():
            return True
        else:
            return False

    def get_max(self) -> int:
        """returns the value of the maximum element of the PQ without removing it
        @return the maximum value of the PQ or None if no element exists
        """
        return self.heap[0]

    def remove_max(self) -> int:
        """removes the maximum element from the PQ and returns its value
        @return the value of the removed element or None if no element exists
        """
        result = self.heap[0]

        self.heap[0] = self.heap[self.size]
        self.size = self.size - 1
        self.down_heap(0)
        return result

    def get_size(self) -> int:
        """returns the number of elements in the PQ
        @return number of elements
        """
        return len(self.heap)
