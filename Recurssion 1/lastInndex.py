'''
Given an array of length N and an integer x, you need to find and return the last index of integer x present in the array. Return -1 if it is not present in the array.
Last index means - if x is present multiple times in the array, return the index at which x comes last in the array.
You should start traversing your array from 0, not from (N - 1).
Do this recursively. Indexing in the array starts from 0.
'''

def last(a , x):
    if len(a) == 0:
        return -1
    rans = last(a[1:] ,x)
    if rans == -1:
        if a[0] == x:
            return 0
        else:
            return -1
    else:
        return rans + 1
    
    
if __name__ == '__main__':
    a = [int(x) for x in input().split()]
    x = int(input())
    val = last(a ,x)
    print(val)