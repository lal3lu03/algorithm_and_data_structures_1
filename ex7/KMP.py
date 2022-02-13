class KMP:

    def __init__(self):
        pass
    
    """
        This method uses the KMP algorithm to search a given pattern in a given input text.
        @ param pattern - The string pattern that is searched in the text.
        @ param text - The text string in which the pattern is searched.
        @ return a list with the starting indices of pattern occurrences in the text, or None if not found.
        @ raises ValueError if pattern or text is None or empty.
    """

    def search(self, pattern, text):
        m = len(pattern)
        n = len(text)
        f = self.get_failure_table(pattern)
        i = 0
        j = 0
        res = []
        while i < n:
            if pattern[j] == text[i]:
                if j == m-1:
                    res.append(i-m+1)
                    j = 0
                    i = i-m+2
                i = i+1
                j = j+1
            elif j > 0:
                j = f[j-1]
            else:
                i = i+1
        return res

    """
        This method calculates and returns the failure table for a given pattern.
        @ param pattern - The string pattern for which the failure table shall be calculated.
        @ return a list with the failure table values for the given pattern.
    """

    def get_failure_table(self, pattern):
        i = 1
        j = 0
        t = []
        t.insert(0, 0)

        while i < len(pattern):

            if pattern[j] == pattern[i]:
                t.insert(i, j + 1)
                j = j + 1
                i = i + 1

            elif j != 0:
                j = t[j - 1]

            else:
                t.insert(i, 0)
                i = i + 1
        return t