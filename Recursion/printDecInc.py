# given a number n, print numbers in zig zag order (like n-> 1 -> n)
# e.g. n=5 ,o/p= 5 4 3 2 1 1 2 3 4 5


def printOrder(x):
    if x == 0 : return 
    
    print(x)
    printOrder(x-1)
    print(x)

if __name__ =='__main__':
    n=int(input("Enter the number : "))
    printOrder(n)
