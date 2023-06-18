# Question link - https://practice.geeksforgeeks.org/problems/peak-element/1?utm_source=youtube&utm_medium=collab_codefromscratch_description&utm_campaign=peakelement
# An element is called a peak element if its value is not smaller than the value of its adjacent elements(if they exists).
# Given an array arr[] of size N, Return the index of any one of its peak elements.

def get_peak_element(arr):
    
    l,r = 0,len(arr)-1
    
    while l<=r:
        mid = l + (r-l)//2
       
        if (mid==0 or arr[mid-1]<=arr[mid]) and (mid==len(arr)-1 or arr[mid+1]<=arr[mid]):
            return mid
        
        elif mid>0 and arr[mid-1]>arr[mid]:
            r=mid-1
            
        else:
            l=mid+1
            
    return -1


if __name__ == "__main__":
    arr = list(map(int, input("Enter the numbers for arr values: ").split()))
    print(get_peak_element(arr))