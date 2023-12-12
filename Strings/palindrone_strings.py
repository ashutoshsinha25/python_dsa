# Q. Check if the given strinig is a palindrome or not. 
# A palindrome is a string that when reversed, is equals to the original string.


def palindrome(s): # TC:O(N) , SC:O(1)
    si , ei = 0 , len(s)-1 
    while(si <= ei):
        if s[si] == s[ei]:
            si+=1
            ei-=1
        else:
            break 
    return True if si > ei else False 



if __name__ == '__main__':
    s = input('Enter the string : ')
    print(f'result : {palindrome(s)}')

