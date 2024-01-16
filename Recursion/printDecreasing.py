# given a number n, print numbers in decreasing order (from n to 1)


def printDec(x):
    if x == 0: return 
    print(x)
    printDec(x-1)


if __name__ =='__main__':
    n=int(input('Enter the number : '))
    print("Numbers in dec order:")
    printDec(n)