def factorial(n):
    if n==0:
        return 1
    n_1 = factorial(n-1)
    return n* n_1


if __name__ == '__main__':
    n = int(input('enter the number : '))
    val = factorial(n)
    print(val)