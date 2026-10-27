a=input("enter input: ").split()
row1="qwertyuiop"
row2="asdfghjkl"
row3="zxcvbnm"
result=[]
for word in a:
    first=word[0]
    if first in row1:
        boss=row1
    elif first in row2:
        boss=row2
    else:
        boss=row3
    found=True
    for letter in word:
        if letter.lower() not in boss:
            found=False
            break
    if found==True:
        result.append(word)
if len(result)==0:
    print("[]")
else:
    print(" ".join(result))