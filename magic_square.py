a=[]
for i in range(3):
    b=[]
    for j in range(3):
        j=int(input("enter the number"))
        b.append(j)
    a.append(b)
# a=[[2,7,6],[9,5,1],[4,3,8]]
print("matric is...")
for i in range(3):
    for j in range(3):
        print(a[i][j],end=" ")
    print()
sum1=0
sum2=0
for i in range(3):
    for j in range(3):
        if i==j:
            sum1=sum1+a[i][j]
            if i+j==3-1:
                sum2=sum2+a[i][j]
if sum1!=sum2:
    f=1
else:
    for i in range(3):
        sumr=0
        sumc=0
        for j in range(3):
            sumr=sumr+a[i][j]
            sumc=sumc+a[j][i]
        if sumr!=sum1:
            f=1
        elif sumc!=sum1:
            f=1
        else:
            f=0
if f==0:
    print("matrics is magic square")
else:
    print("matrics is not a magic square")