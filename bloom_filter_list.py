class BloomSet(object):
    """Assume base64 machine."""

    def __init__(self, elements):
        self.len1 = max(len(elements) / 2, 10)
        self.len2 = max(len(elements) / 2 + 1, 11)
        self.len3 = max(len(elements) / 2 + 2, 12)
        self.arr1 = [0] * self.len1
        self.arr2 = [0] * self.len2
        self.arr3 = [0] * self.len3

        for element in elements:
            self.add_element(element)

    def add_element(self, element):
        index1, index2, index3 = self._hashes(element)
        self.arr1[index1] = 1
        self.arr2[index2] = 1
        self.arr3[index3] = 1

    def _hashes(self, element):
        h = _hash(element)
        return h % self.len1, h % self.len2, h% self.len3

    def contains(self, element):
        index1, index2, index3 = self._hashes(element)
        return self.arr1[index1] and self.arr2[index2] and self.arr3[index3]


def _hash(num):
    return hash(str(num))
