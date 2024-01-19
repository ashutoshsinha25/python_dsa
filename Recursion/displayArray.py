# given an array with n elements, using recursion display the elements present inside the array

def display(arr , idx):
    if idx == len(arr)-1:
        print(arr[idx])
        return 
    print(arr[idx] , "->",end=' ')
    display(arr , idx+1)



if __name__ =='__main__':
    arr=[int(n) for n in input().split()]
    display(arr, 0)