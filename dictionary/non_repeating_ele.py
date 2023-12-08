# https://practice.geeksforgeeks.org/problems/non-repeating-element3958/1
# Non-Repeating Element : Find the first non-repeating element in a given array arr of N integers.
# Note: Array consists of only positive and negative integers and not zero.


def first_non_repeating(arr):
    hm = {}

    for ele in arr:
        if ele in hm:
            hm[ele] += 1
        else:
            hm[ele] = 1
    for ele in arr:
        if hm[ele] == 1:
            return ele
    return 0


if __name__ == '__main__':
    arr = [int(x) for x in input('enter the values of array:').split(',')]
    print("first non repeating values from arr: ", first_non_repeating(arr))
