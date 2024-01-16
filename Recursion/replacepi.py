# replace every occurence of 'pi' from string to 3.14

def replace(s):
    if len(s) == 0 or len(s) == 1:
        return s
    
    if s[0] == 'p' and s[1] == 'i':
        rans = replace(s[2: ])
        return '3.14' + rans
    else:
        return s[0] + replace(s[1:]) 
    


if __name__ == '__main__':
    s = input('enter the string : ')
    print(replace(s))