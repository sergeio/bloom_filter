from unittest import TestCase, main

from bloom_filter import BloomSet


class TestInitializingBloomSet(TestCase):

    def setUp(self):
        self.bset = BloomSet(xrange(20))

    def test_create_arr1_with_size(self):
        self.assertEqual(self.bset.len1, 10)

    def test_create_arr2_with_size(self):
        self.assertEqual(self.bset.len2, 11)


class TestAddingElement(TestCase):

    def setUp(self):
        self.bset = BloomSet([])

    def test_adding_element(self):
        self.bset.add_element(120)
        self.assertTrue(any(self.bset.arr1), any(self.bset.arr2))


class TestMembership(TestCase):

    def setUp(self):
        self.elements = range(100)
        self.bset = BloomSet(self.elements)

    def test_members(self):
        for element in self.elements:
            self.assertTrue(self.bset.contains(element))


class TestEmptyBloomSet(TestCase):

    def setUp(self):
        self.bset = BloomSet([])

    def test_empty_bloom_set(self):
        for element in xrange(100):
            self.assertFalse(self.bset.contains(element))


if __name__ == '__main__':
    main()
