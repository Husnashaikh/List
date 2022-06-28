a=["h","u",["s","n"],"a"]
i=0
b=""
while i<len(a):
    j=0 
    while j<len(a[i]):
        b=b+a[i][j]
        j=j+1
    i=i+1
print(b)