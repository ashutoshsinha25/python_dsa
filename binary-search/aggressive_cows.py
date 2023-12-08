# https://practice.geeksforgeeks.org/problems/aggressive-cows/1
# Aggressive Cows


def aggressive_cows(stalls,k):
    
    def isPossible(stalls,n,k,maxi):
        cow,stall = 1, stalls[0]
        for i in range(n):
            if stalls[i] - stall>=maxi:
                cow+=1
                if cow==k:return True
                stall=stalls[i]
        return False
    
    stalls.sort()
    l,r = 0,stalls[-1]
    ans=-1
    
    while l<=r:
        mid = l + (r-l)//2
        
        if isPossible(stalls,len(stalls),k,mid):
            ans=mid
            l=mid+1
        else:
            r=mid-1
            
    return ans


if __name__ == '__main__':
    k = int(input("Enter the number of cows: "))
    A = list(map(int, input("Enter the stalls value: ").split()))
    print(aggressive_cows(A,k))





