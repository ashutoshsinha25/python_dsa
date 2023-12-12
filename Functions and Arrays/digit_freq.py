# given a number n, find out the frequency of the number k in it.

def count_digit(n ,k):
    count = 0
    while(n!=0) :
        last = n % 10 
        if (last == k):
            count+=1
        n = n//10 
    return count


if __name__ == '__main__':
    n = int(input("Enter the number : "))
    k = int(input("Enter the number for freq : "))
    print("The digit {} appears {} times in {}" .format(k,count_digit(n,k),n))