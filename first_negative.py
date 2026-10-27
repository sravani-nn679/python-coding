a=list(map(int,input("enter list: ").split()))
k=int(input("enter key: "))
if k<=0 or k>len(a):
    print("Invalid Key Value")
else:
    c=0
    for i in range(len(a)-k+1):
        for j in range(i,i+k):
            if a[j]<0:
                print(a[j],end=" ")
                c+=1
                break
    if c==0:
        print("No Numbers")
