a=[1,-2,3,-4,5,-6,7,8,-9,-10]
b=[]
c=[]
coun=0
coun1=0
i=0
while i<len(a):
    if a[i]<0:
        coun=coun+1
        b.append(a[i])
    else:
        coun1=coun1+1
        c.append(a[i])
    i=i+1
print("nagitive",b)
print(c)
print(coun)
print(coun1)
