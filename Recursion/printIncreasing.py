# given a number n, print numbers in increasing order (from 1 to n)

def printInc(x):
    if x == 0: return 
    printInc(x-1)
    print(x)


if __name__ =='__main__':
    n=int(input("Enter the number :"))
    printInc(n)