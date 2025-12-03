arr = []
i = 5
k=9
y=1
while i >= 0:
    temporary = []
    i-=1
    rand = '*'*k
    for c in rand:
        temporary.append(c)
    arr.append(temporary)    

for row in arr:
    o = 0
    while o < y:
        row[o] = " "
        row[-o] = " "
        o+=1
    if y < len(arr)-1:
        y+=1                                

arr.reverse()
for row in arr :
    rowString = " ".join(row)
    print(rowString)
