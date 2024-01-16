# for a given string replace character a with character b using recursion 

def replace(s,a, b):
    if len(s) == 0:
        return s
    rans = replace(s[1:],a,b)
    if s[0] == 'a':
        return 'b' +  rans
    else:
        return s[0] + rans


if __name__ == '__main__':
    s = input()
    print(replace(s , 'a' , 'b' ))