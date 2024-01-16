'''
Given a string, compute recursively a new string where all 'x' chars have been removed.
'''

def remove(s):
    if len(s) == 0:
        return ''
    
    rans = remove(s[1:])
    if s[0] == 'x':
        return rans
    else: 
        return s[0] + rans
    

if __name__ == '__main__':
    s = input('enter the string : ')
    print(remove(s))