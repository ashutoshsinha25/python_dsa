def isSorted(a):
    '''check value at 0 index before the call'''
    if len(a) == 0 or len(a) ==  1:
        return True

    if a[0] > a[1]:
        return False
    rans = isSorted(a[1:])
    return rans


def isSorted2(a):
    ''' check value at 0 index after the call'''
    if len(a) == 0 or len(a) == 1:
        return True
    rans = isSorted2(a[1:])
    if rans:
        if a[0] > a[1]:
            return False 
        else:
            return True
    else:
        return False
    


# without making copy of the array for evey recursion calls
def isSorted3(a , idx):
    if idx == len(a) or idx == len(a) - 1:
        return True
    if a[idx] > a[idx+1]:
        return False
    rans = isSorted3(a , idx+1)
    return rans



if __name__ == '__main__':
    a = [int(x) for x in input('enter the values for array: ').split()]
    print(isSorted3(a , 0))