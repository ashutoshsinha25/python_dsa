#Given an array of length N and an integer x, you need to find if x is 
# present in the array or not. Return true or false. Do this recursively.

def checkNum(a , x):
    if len(a) == 1:
        if a[0] == x:
            return True
        else:
            return False
    rans = checkNum(a[1:] ,x)
    if rans:
        return True
    else:
        if a[0] == x:
            return True
        else:
            return False
    

def checkNum2(a,x):
    if x not in a:
        return False
    if a[0] == x:
        return True
    return checkNum2(a[1:] , x)


if __name__ == '__main__':
    a = [int(x) for x in input('enter the values for array :').split()]
    x = int(input('enter the value x :'))
    print(checkNum2(a , x))
