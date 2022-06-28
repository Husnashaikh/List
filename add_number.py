a=[1,2,3,4,5]
i=0
coun=0
b=[]
while i<len(a):
        b.append(a[i])
        if coun==0:
                b.append(10)
                coun=coun-3
        coun=coun+1
        i=i+1
print(b)
