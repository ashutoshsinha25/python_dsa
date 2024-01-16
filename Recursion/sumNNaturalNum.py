def sumN(n):
    if n == 0:
        return 0
    out = sumN(n-1)
    return n + out


if __name__ == '__main__':
    n = int(input('enter you number: '))
    val = sumN(n)
    print(val)