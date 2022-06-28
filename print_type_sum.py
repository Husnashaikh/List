a=["husna",23,7,8+9j,8+4j,9.8,7.0,"khalid",10]
i=0
b=[]
c=[]
d=[]
e=[]
sum=0
sum1=0
sum2=0
while i<len(a):
    if type(a[i])==int:
        sum=sum+a[i]
        b.append(sum)
    if type(a[i])==float:
        sum1=sum1+a[i]
        c.append(sum1)
    if type(a[i])==complex:
        sum2=sum2+a[i]
        d.append(sum2)
    if type(a[i])==str:
        e.append(a[i])
    i=i+1
print(b)
print(c)
print(d)
print(e)

