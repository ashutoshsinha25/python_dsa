# given a number n, 

def zigzag(x):
    if x == 0 : return 
    print("Pre N", x)
    zigzag(x-1)
    print("In N", x)
    zigzag(x-1)
    print("Post N", x)



if __name__ =='__main__':
    n=int(input())
    zigzag(n)