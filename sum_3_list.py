a=[1,2,3,4]
b=[5,6,7,8]
c=[9,10,11,12]
i=0 
sum=0
while i<len(a):
    sum=sum+a[i]
    sum=sum+b[i]
    sum=sum+c[i]
    i=i+1
print(sum)
