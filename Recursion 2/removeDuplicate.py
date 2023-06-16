'''
Given a string S, remove consecutive duplicates from it recursively.
'''

def remove(s):
    if len(s) == 0 or len(s) == 1:
        return s
    
    if s[0] == s[1]:
        rans = remove(s[1:])
        return rans
    else:
        return s[0] + remove(s[1:])


if __name__ == '__main__':
    s = input('enter the string : ')
    print(remove(s))