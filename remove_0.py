a=[10,101,10000,10101]           
i=0 
d=[]
while i<len(a):
    b=str(a[i])
    c=""
    j=0
    while j<len(b):
        if b[j]!="0":
            c+=b[j]
        j+=1
    d.append(int(c))
    i=i+1
print(d) 