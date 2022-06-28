a=input("enter the str")
i=0
coun=0
coun1=0
while i<len(a):
    if a[i]>="A" and a[i]<="Z":
        coun=coun+1
    else:
        coun1=coun1+1
    i+=1
print(coun,"upper_case")
print(coun1,"lower_case")
