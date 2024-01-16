def convert(x , ib , b):
    val = 0
    i = 0
    while(x!=0):
        rem = x % b 
        x = x//b
        val += rem * (ib ** i)
        i += 1
    return val 


if __name__ =='__main__':
    x = int(input("Enter the number: "))
    ib = int(input("Enter the base of Input Number: "))
    b = int(input("enter the base you want to conver the input into: "))
    print(f"Number {x} with base {ib} converted to base {b} is : {convert(x , ib, b)}")