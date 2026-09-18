n=int(input())
a=0
b=1
p=2 #prime
pos=1
for i in range(1,n+1):
    for j in range(1,i+1):
        if pos%2==1:
            print(p,end=" ")
            p+=1
            while True:
                fc=0
                for k in range(2,p):
                    if p%k==0:
                        fc+=1
                        break
                if fc==0:
                    break
                p+=1
        else:
            print(a,end=" ")
            c=a+b
            a=b
            b=c
        pos+=1
    print()
        


