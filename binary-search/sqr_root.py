# Question link - https://practice.geeksforgeeks.org/problems/square-root/1?utm_source=youtube&utm_medium=collab_keertipurswani_description&utm_campaign=squareroot

# Given an integer x, find the square root of x. If x is not a perfect square, then return floor(√x). For x>0

def squareroot(x):
    
    if x==1:return 1
    
    l,r = 1,x//2
    
    ans=-1
    while l <= r:
        mid = l+(r-l)//2
        sqr = mid*mid
        
        if sqr == x:return mid
        
        elif sqr>x:
            r=mid-1
            
        else:
            l=mid+1
            ans=mid
            
    return ans

if __name__ == '__main__':
    x = int(input("Enter a number to find its sqr root: "))
    print(squareroot(x))