a=list(map(int,input("enter a list: ").split()))
visited=[]
duplicate=False
for i in range(len(a)):
    if a[i] not in visited:
        c=a.count(a[i])
        if c>1:
            print(f"{a[i]}->{c}")
            duplicate=True
    visited.append(a[i])
if duplicate==False:
    print("No duplicate")
