a=[4,2,7,10,5,9,7,20,6]
b=[]
i=0
while i<len(a):
    coun=0
    j=0
    while j<len(a):
        if a[i]<a[j]:
            coun=coun+1
        j=j+1
    b.append(coun)
    i=i+1
print(b)

