a=[[10,20,30],[90,91,39],[8,9,50]]
i=0
b=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        b.append(a[i][j])
        j=j+1
    i=i+1
print(b)
# i=0
# k=2
# c=[]
# while i<len(b):
#     if i==k:
#         c.append(b[i])
#         k+=3
#     i+=1
# print(c)