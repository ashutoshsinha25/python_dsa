# Given N array elements and Q queries. For every query find frequency of element in array.


def countFreq(arr , que):
    hm = {}
    for ele in arr:
        # if ele in hm:
        #     hm[ele] += 1
        # else:
        #     hm[ele] = 1
        hm[ele] = hm.get(ele, 0) + 1 # another way of doing the same thing
        
    for ele in que:
        if ele in hm:
            print(ele , "-->" , hm[ele])
        else:
            print(ele , "-->" , 0)
    return 



if __name__ =='__main__':
    arr = [int(x) for x in input().split()]
    que = [int(x) for x in input().split()]
    countFreq(arr , que)
