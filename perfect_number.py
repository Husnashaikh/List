x=int(input("enter the number"))
i=1
while i<=x:
    sum=0
    j=1
    while j<i:
        if i%j==0:
            sum=sum+j
        j=j+1
    i=i+1
if sum==x:
    print("perfect")
else:
    print("not perfect")