list=["mom","dad","aairu","madam","husna"]
e=[]
d=[]
i=0
while i<len(list):
    b=list[i]
    str=""
    j=1
    while j<len(list[i])+1:
        str+=list[i][-j]
        j=j+1
    if b==str:
        e.append(str)
    else:
        d.append(str)
    i+=1
print(e)
print(d)