def is_prime(a):
    fc=0
    for i in range(1,a+1):
        if a%i==0:
            fc+=1
    if fc==2:
        return True
    else:
        return False
a=int(input())
c=len(str(a))
p=10**(c-1)
is_cp=True
i=0
temp=a
while i<c:
    if not is_prime(temp):
        is_cp=False
        print("not circular prime")
        break
    else:
        first=temp//p
        second=temp%p
        temp=second*10+first
        i+=1
else:
    print("circular prime")