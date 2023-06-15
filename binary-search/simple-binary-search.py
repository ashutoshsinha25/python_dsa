# Binary search operation to find the given number


def bin_search(arr,k):
    l,r = 0,len(arr)-1
    
    while l<=r:
        mid = l + (r-l)//2
        
        if arr[mid]==k:return True
        
        elif arr[mid]<k:
            l = mid + 1
        
        else:
            r = mid - 1
            
    return False



if __name__ == '__main__':
    arr = list(map(int, input("Enter the element in sorting order: ").split()))
    k = int(input ("Enter a number to be searched: "))
    bin_search(arr, k)