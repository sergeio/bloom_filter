import random
import time

from bloom_filter import BloomSet


def main():
    print 'creating'
    numbers = range(100000)
    print 'created'

    rset = set(numbers)
    # bset = BloomSet(numbers)
    print 'set done'

    test_membership_rset(numbers, rset)
    # test_membership_bset(numbers, bset)

def test_membership_rset(_list, rset):
    for element in _list:
        assert element in rset

def test_membership_bset(_list, bset):
    for element in _list:
        assert bset.contains(element)


if __name__ == '__main__':
    main()
