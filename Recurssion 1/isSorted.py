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
if __name__ == '__main__':
    a = [x for x in input('enter the values for array: ').split()]
    print(isSorted(a))