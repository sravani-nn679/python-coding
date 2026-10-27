n=int(input("enter a number: "))
if n==0:
    print("Invalid Input")
elif n<100:
    print("Invalid Input")
else:
    if n<0:
        n=-n
    result=""
    result+=str(n)
    result+=str(n*2)+str(n*3)
    no_zeros=result.replace("0","")
    if len(no_zeros)==9 and len(set(no_zeros)):
        print("Fascinating Number")
    else:
        print("Not a Fascinating Number")