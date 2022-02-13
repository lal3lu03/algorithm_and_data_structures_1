class RabinKarp:

    """
        Constructor initialising the modulo value, if any.
        @ param mod_val - Modulo value to be used for hashing, if provided.
    """

    def __init__(self, mod_val = None):
        self.b = 29


        
    """
        This method uses the RabinKarp algorithm to search a given pattern in a given input text.
        @ param pattern - The string pattern that is searched in the text.
        @ param text - The text string in which the pattern is searched.
        @ return a list with the starting indices of pattern occurrences in the text, or None if not found.
        @ raises ValueError if pattern or text is None or empty.
    """

    def search(self, pattern, text):
        m = len(text)
        n = len(pattern)
        hash_p = self.get_rolling_hash_value(pattern, '\0', 0)
        hash_t = self.get_rolling_hash_value(text[:n], '\0', 0)
        s = text[:n]
        res = []

        if pattern == '' or text == '':
            raise ValueError('No Text or pattern')
        if n > m:
            return None

        for t in range(1,m):
            if hash_p == hash_t:
                for j, x in enumerate(s):
                    if x != pattern[j]:
                        break
                if s == pattern:
                    res.append(t-1)
            s = text[t:t + n]
            if t < m-n:
                hash_t = self.get_rolling_hash_value(s, text[t], 0)
        return res

    """
         This method calculates the (rolling) hash code for a given character sequence. For the calculation use the base b=29.
         @ param sequence - The char sequence for which the (rolling) hash shall be computed.
         @ param lastCharacter - The character to be removed from the hash when a new character is added.
         @ param previousHash - The most recent hash value to be reused in the new hash value.
         @ return hash value for the given character sequence using base 29.
    """

    def get_rolling_hash_value(self, sequence, last_character, previous_hash):
        m = len(sequence)
        hash = 0
        if previous_hash == 0:

            for i, x in enumerate(sequence):
                hash += ord(x) * self.b**(m-(i+1))
            return hash

        return previous_hash*self.b - ord(last_character)*self.b ** m + ord(sequence[-1])
