list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7]
a=[]
for i in list1:
    if i not in list2:
        a.append(i)
print(a)