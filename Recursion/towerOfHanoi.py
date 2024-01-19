
def tower(n , a, b, c):
    # if n == 1:
    #     print( f'move 1st dick from {a} to {c}')
    #     return 
    if n==0 : return 
    tower(n-1, a, c, b)
    print(f'move {n}th dick from {a} to {c}')
    tower(n-1 , b, a, c)



if __name__ == '__main__':
    tower(3 , 'source' , 'helper' , 'destination')
    # x = 55 / 11
    # print(x)