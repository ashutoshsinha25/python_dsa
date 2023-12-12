def baseToDecimal(x , ib ,b=10):
    remainders = [] 
    while x!=0 :
        rem = x % b 
        x = x // b 
        remainders.append(rem)
    val =0
    for i in range(len(remainders)):
        val += remainders[i] * (ib ** i)
    return val 


if __name__ =='__main__':
    x = int(input("Enter the number : "))
    ib = int(input("What is the initial base : "))
    # b = int(input("Enter the base to convert to : "))
    print(f" Number {x} with base {ib} as Decimal : {baseToDecimal(x , ib)}")
