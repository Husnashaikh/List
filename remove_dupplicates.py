a=[1,2,1,3,4,5,2,4,6,5,2,4]
i=0
b=[]
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
    i+=1
print(b)


# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
# print(b)
