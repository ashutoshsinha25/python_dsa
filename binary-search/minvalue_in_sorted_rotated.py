# https://practice.geeksforgeeks.org/problems/minimum-element-in-a-sorted-and-rotated-array3611/1?utm_source=youtube&utm_medium=collab_codefromscratch_description&utm_campaign=maxelementinarray
# Minimum element in a sorted and rotated array

def minval(arr):
    l,r = 0,len(arr)-1
    mini = 10**5 # Considering the values in array are < 10**5
    
    while l<=r:
        mid = l + (r-l)//2
        
        if mid>0 and arr[mid-1]>arr[mid]:
            return arr[mid]
        
        if arr[l]>arr[mid]:
            mini = arr[mid]
            r=mid-1
            
        elif arr[mid]>arr[r]:
            l=mid+1
            
        else:
            return arr[l] # this is required in the condition where the arr is sorted and not roated
        
    return mini


if __name__ == '__main__':
    arr = list(map(int, input("Enter the rotated sorted arr: ").split()))
    print(minval(arr))