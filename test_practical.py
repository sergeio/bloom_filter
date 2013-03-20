import random


def main():
    max_num = 10000000
    numbers = [random.randint(1, max_num) for i in xrange(max_num)]
    print len(numbers)



if __name__ == '__main__':
    main()
