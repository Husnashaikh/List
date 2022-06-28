a=[[1,2,3],[4,5,6,],[7,8,9]]
i=0
b=[]
while i<len(a):
    j=0
    sum=0
    while j<len(a):
        sum=sum+a[i][j]
        j+=1
    i+=1
    b.append([sum])
print(b)
