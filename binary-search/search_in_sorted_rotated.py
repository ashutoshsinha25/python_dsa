# Question link https://practice.geeksforgeeks.org/problems/search-in-a-rotated-array0959/1?category=&utm_source=youtube&utm_medium=collab_codefromscratch_description&utm_campaign=rotatedarray
# Given a sorted and rotated array A of N distinct elements which are rotated at some point, and given an element K. The task is to find the index of the given element K in array A.

def search_rotated(arr,k):
    
    l,r = 0,len(arr)-1
    
    while l<=r:
        mid = l + (r-l)//2
        
        if arr[mid]==k:
            return mid
        
        elif arr[mid]>arr[l]:
            if arr[mid]>k and arr[l]<=k:
                r=mid-1
            else:
                l=mid+1
        
        else:
            if arr[mid]<k and arr[r]>=k:
                l=mid+1
            else:
                r=mid-1
                
    return -1

if __name__ == '__main__':
    k = int(input("Enter the value that need to be searched: "))
    arr = list(map(int, input("Enter the rotated sorted arr: ").split()))
    print(search_rotated(arr,k))