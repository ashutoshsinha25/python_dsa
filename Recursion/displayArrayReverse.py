# given an array with n elements, using recursion display the elements present inside the array in reverse order

def display(arr , idx):
    if idx == len(arr):
        return
    display(arr,idx+1)
    print(arr[idx], end=' ')



if __name__ =='__main__':
    arr=[int(n) for n in input().split()]
    display(arr, 0)