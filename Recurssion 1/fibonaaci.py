# question : sum of n fibo numbers 
def fibo(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    rans = fibo(n-1) + fibo(n-2)
    return rans


if __name__ == '__main__':
    n  = int(input('enter the number : '))
    val = fibo(n)
    print(val)