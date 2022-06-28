a=[2,3,4,8,10,12]
b=int(input("enter the number"))
coun=0
i=0
while i<len(a):
    if a[i]==b:
        break
    coun=coun+1
    i=i+1
print(coun)
    