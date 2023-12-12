def palindrome(s):
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

