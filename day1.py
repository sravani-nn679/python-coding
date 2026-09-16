a = [2, 3, 1, 5]
key = 6
for i in range(len(a)):
    curr_sum = 0
    for j in range(i, len(a)):
        curr_sum += a[j]
        if curr_sum == key and j!= i:
            for x in range(i, j+1):
                print(a[x], end=" ")
            print()