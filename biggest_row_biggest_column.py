R=int(input())
a=[]
for i in range(R):
    a.append(list(map(int,input().split())))
for i in range(R):
    m=max(a[i])
    p=a[i].index(m)+1
    print(f"player{p}-{m}")
Players=len(a[0])
total=[0]*Players
for i in range(R):
    for j in range(Players):
        total[j]+=a[i][j]
m=max(total)
p=total.index(m)+1
print(f"Players{p}-{m}")   
