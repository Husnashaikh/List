
n=[1,2,[3,4],[5,6,7],[8,9,10]]
a=[]
i=0
while i<len(n):
    if type(n[i])==list:
        j=0 
        while j<len(n[i]):
            a.append(n[i][j])
            j=j+1
    else:
        a.append(n[i])
    i=i+1
print(a)
