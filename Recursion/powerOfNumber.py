# Write a program to find x to the power n (i.e. x^n). Take x and n from the user. You need to print the answer.
# Note : For this question, you can assume that 0 raised to the power of 0 is 1

def power(x, n): # TC : O(N)
    if n == 0:
        return 1
    out = power(x, n-1)
    return x * out

def power2(x , n): # more efficient TC : O(logN)
    if n == 0: return 1
    out = power2(x , n//2)
    if n%2==0:
        return out*out 
    else:
        return out*out*x


if __name__ == '__main__':
    x , n = map(int , input("enter two numers in form of x n: ").split())
    # val = power(x , n)
    val = power2(x , n)
    print(val)