# Runtime Complexity O(b*N)
import math

class RadixSort:
    def __init__(self):
        self.base = 7
        #                                _________list of bucketlists
        #                               | ________list of buckets -> list of buckets as array here
        #                               || ___________content of a bucket -> buckets as arrays here
        #                               |||
        self.bucket_list_history = []  #[[[]]] -> will look like this in the end


    def get_bucket_list_history(self):
        return self.bucket_list_history


    def sort(self, inputlist):
        """
        Sorts a given list using radixsort in ascending order
        @param inputlist to be sorted
        @returns a sorted list
        @raises ValueError if the list is None
        """
        self.bucket_list_history.clear()  # clear history list at beginning of sorting
        max_digit_len = len(str(max(inputlist)))

        if inputlist is None:
            raise ValueError('Nothing to sort here')

        for i in range(max_digit_len):
            buckets = [list() for _ in range(self.base)]
            for j in inputlist:
                tmp = math.floor(j/10**i) % 10
                buckets[tmp].append(j)
            a = 0
            for b in range(self.base):
                buck = buckets[b]
                for i in buck:
                    inputlist[a] = i
                    a += 1
            self._add_bucket_list_to_history(buckets)
        return inputlist


    def _add_bucket_list_to_history(self, bucket_list):
        """
        This method creates a snapshot (clone) of the bucketlist and adds it to the bucketlistHistory.
        @param bucket_list is your current bucketlist, after assigning all elements to be sorted to the buckets.
        """
        arr_clone = []
        for i in range(0, len(bucket_list)):
            arr_clone.append([])
            for j in bucket_list[i]:
                arr_clone[i].append(j)

        self.bucket_list_history.append(arr_clone)
