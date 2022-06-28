a=[1,2,4,1,5,6,1,9,3]
for i in a: 
    c=0
    for j in a:
        if i==j:
            c=c+1
    if c==1:
        a.append(i)
print(a[9::])