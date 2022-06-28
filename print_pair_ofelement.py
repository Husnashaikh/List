number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19]
i=0
a=[]
while i<len(n):
    j=0
    while j<len(n):
        b=n[i]+n[j]
        s=[n[i],n[j]]
        if number==b:
            a.append(s)
        j=j+1
    i=i+1
print(a)