def print1_N(n):
    if n == 0:
        # print(0 , end = ' ')
        return 
    print1_N(n-1)
    print(n, end = ' ')
    return 


def printN_1(n):
    if n == 0:
        # print(0 , end = ' ')
        return 
    print(n, end = ' ')
    printN_1(n-1)
    return 

def print1_N_1(n):
    if n == 0:
        # print(0 , end = ' ')
        return 
    print1_N(n-1)
    print(n, end = ' ')
    printN_1(n-1)
    return 



if __name__ == '__main__':
    n = int(input('enter the number'))
    print('1 to N numbers : ' )
    print1_N(n)
    print()
    print('N to 1 numbers : ' )
    printN_1(n)
    print()
    print('1 to N to 1 number : ')
    print1_N_1(n)

    
    
