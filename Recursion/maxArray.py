# given an array, find out the maximum element present using recursion 


def check(arr,idx):
    if idx == len(arr):
        return float('-inf')
    rres=check(arr,idx+1)
    if arr[idx] > rres:
        return arr[idx]
    else:
        return rres




if __name__ =='__main__':
    arr=[int(x) for x in input().split()]
    print("Maximum element in arr is : ",check(arr, 0))