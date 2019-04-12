"""
def linear_search(alist, key):
    for i in range(len(alist)):
        if alist[i] == key:
            return i
    return -1


alist = input('Enter list of numbers:')
alist = alist.split()
print(alist)
alist = [int(x) for x in alist]
print(alist)

key = int(input('Enter a key to search for:'))

index = linear_search(alist, key)
if index < 0:
    print('{} not found'.format(key))
else:
    print('{} was found at index {}'.format(key, index))
"""


def binary_search(alist, key):
    start = 0
    end = len(alist)
    print(end)
    while start < end:
        mid = (start + end)//2
        print(mid)
        if alist[mid] > key:
            end = mid
            print(end)
        elif alist[mid] < key:
            start = mid + 1
            print(start)
        else:
            return mid
    return -1


alist = input('Enter list of numbers:')
alist = alist.split()
alist = [int(x) for x in alist]
key = int(input('Enter a key to search for:'))

index = binary_search(alist, key)
if index < 0:
    print('{} was not found'.format(key))
else:
    print('{} was found at index {}'.format(key, index))