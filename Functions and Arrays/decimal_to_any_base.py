def deciConvert(x , b , ib=10): # TC : O(N), SC : O(N)
    remainders = [] 
    while x != 0:
        rem = x % b 
        x = x // b 
        remainders.append(rem)
    val = 0
    for i in range(len(remainders)):
        val += remainders[i] * (ib ** i)
    return val 

def deciConvert2(x , b , ib=10): # TC:O(N) , SC:O(1)
    val = 0
    i = 0
    while x != 0:
        rem = x % b 
        x = x // b 
        val += rem * (ib**i)
        i += 1
    return val 


if __name__ =='__main__':
    x = int(input("Enter the decimal number : "))
    # ib = int(input("What is the initial base : "))
    b = int(input("Enter the base to convert to : "))
    # print(f"Decimal Number {x} to Base {b} is : {deciConvert(x , b)}")
    print(f"Decimal Number {x} to Base {b} is : {deciConvert2(x , b)}")