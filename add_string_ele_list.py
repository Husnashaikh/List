list=[ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
a=""
i=0
while i<len(list):
    j=0
    while j<len(list[i]):
        a=a+list[i][j]
        j=j+1
    i=i+1
print(a)


a=["h","u",["s","n"],"a"]
b=""
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        b=b+a[i][j]
        j=j+1
    i=i+1
print(b)

a=["my","name","is","husna"]
i=0
sum=""
while i<len(a):
    j=0
    while j<len(a[i]):
        sum=sum+a[i][j]
        j=j+1
    i=i+1
print(sum)