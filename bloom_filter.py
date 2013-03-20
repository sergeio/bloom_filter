class BloomSet(object):
    """Assume base64 machine."""

    def __init__(self, elements):
        self.len1 = max(len(elements) / 2, 10)
        self.len2 = max(len(elements) / 2 + 1, 11)
        self.arr1 = [0] * self.len1
        self.arr2 = [0] * self.len2

        for element in elements:
            self.add_element(element)

    def add_element(self, element):
        index1, index2 = self._hashes(element)
        self.arr1[index1] = 1
        self.arr2[index2] = 1

    def _hashes(self, element):
        h = _hash(element)
        return h % self.len1, h % self.len2

    def contains(self, element):
        index1, index2 = self._hashes(element)
        return self.arr1[index1] and self.arr2[index2]


def _hash(num):
    return hash(str(num))
