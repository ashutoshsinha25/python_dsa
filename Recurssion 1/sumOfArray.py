# Given an array of length N, you need 
# to find and return the sum of all elements of the array.


def sumArr(a):
    if len(a) == 1:
        return a[0]
    rans = sumArr(a[1:])
    return a[0] + rans


def sumArr2(a , idx):
    if idx == len(a):
        return 0
    rans = sumArr2(a, idx+1)
    return a[idx] + rans

if __name__=='__main__':
    a = [int(x) for x in input('enter the values : ').split()]
    val = sumArr2(a , 0)
    print(val)