import random
import time
# from guppy import hpy

from bloom_filter_long import BloomSet

# h = hpy()


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

def test_bset(num_entries):
    # start_size = h.heap().size

    start = time.time()
    bset = BloomSet(xrange(num_entries))
    created_time = time.time()

    # created_size = h.heap().size

    start_positives_time = time.time()
    for i in xrange(num_entries):
        assert bset.contains(i)
    checked_positives_time = time.time()

    for i in xrange(num_entries, num_entries * 2):
        bset.contains(i)
    checked_negatives_time = time.time()

    t_create = created_time - start
    t_pos = checked_positives_time - start_positives_time
    t_neg = checked_negatives_time - checked_positives_time
    # k_size = int((created_size - start_size) / 1000.0)

    print '''
    num_entries: {0}
    create time: {1}s
    check positives time: {2}s
    check negatives time: {3}s
    '''.format(num_entries, t_create, t_pos, t_neg)


def test_rset(num_entries):
    # start_size = h.heap().size

    start = time.time()
    rset = set(xrange(num_entries))
    created_time = time.time()

    # created_size = h.heap().size

    start_positives_time = time.time()
    for i in xrange(num_entries):
        assert i in rset
    checked_positives_time = time.time()

    for i in xrange(num_entries, num_entries * 2):
        i in rset
    checked_negatives_time = time.time()

    t_create = created_time - start
    t_pos = checked_positives_time - start_positives_time
    t_neg = checked_negatives_time - checked_positives_time
    # k_size = int((created_size - start_size) / 1000.0)

    print '''
    num_entries: {0}
    create time: {1}s
    check positives time: {2}s
    check negatives time: {3}s
    '''.format(num_entries, t_create, t_pos, t_neg)




if __name__ == '__main__':
    print 'bset'
    test_bset(int(1e6))
    test_bset(int(1e5))
    test_bset(int(1e4))

    print 'rset'
    test_rset(int(1e6))
    test_rset(int(1e5))
    test_rset(int(1e4))
    # main()
