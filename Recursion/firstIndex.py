# Given an array of length N and an integer x, you need to find and return the first index of integer x 
# present in the array. Return -1 if it is not present in the array.First index means, the index of first 
# occurrence of x in the input array.Do this recursively. Indexing in the array starts from 0.

def first(a,x):
    if len(a) == 0:
        return -1
    if a[0] == x:
        return 0
    else:
        rans = first(a[1:] ,x)
        if rans != -1:
            return rans + 1
        else:
            return -1


def first2(a, x, idx):
    if idx == len(a):
        return -1
    if a[idx] == x:
        return idx
    rans = first2(a, x, idx+1)
    return rans



if __name__ == '__main__':
    a = [int(x) for x in input().split()]
    x = int(input())
    val = first2(a ,x ,0)
    print(val)