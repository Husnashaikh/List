a=[4,5,6,2,3]
i=0
while i<len(a):
    j=0
    while j<len(a):
        a[i]>a[j]
        c=a[i]
        a[i]=a[j]
        a[j]=c
        j=j+1
    i=i+1
print(a)        
