class BloomSet(object):
    """Assume base64 machine.

    Can check for membership, assume output is correct, then publish a message
    to perform a reversible task, check for membership in a non-probabilistic
    set, and publish a message to undo the previous mesage if the result
    differs.


    Good if the lookup to the non-probabilistic set is very expensive.
    Good if you expect most of your membership lookups to return False.

    """
    def __init__(self, elements):
        self.len1 = max(len(elements) / 2, 10)
        self.len2 = max(len(elements) / 2 + 1, 11)
        self.len3 = max(len(elements) / 2 + 2, 12)
        self.set1 = 0L
        self.set2 = 0L
        self.set3 = 0L

        for element in elements:
            self.add_element(element)

    def add_element(self, element):
        index1, index2, index3 = self._hashes(element)
        self.set1 |= (1 << index1)
        self.set2 |= (1 << index2)
        self.set3 |= (1 << index3)

    def _hashes(self, element):
        h = _hash(element)
        return h % self.len1, h % self.len2, h % self.len3

    def contains(self, element):
        index1, index2, index3 = self._hashes(element)
        element_in_set1 = self.set1 & (1 << index1) != 0
        element_in_set2 = self.set2 & (1 << index2) != 0
        element_in_set3 = self.set3 & (1 << index3) != 0
        return element_in_set1 & element_in_set2 & element_in_set3 != 0


def _hash(num):
    return hash(str(num))
