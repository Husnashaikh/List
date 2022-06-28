list=[2,4,6,9,1,]
list.sort()
print(list)
count=0
i=0
while i<len(list)-1:
    diff= list[i+1]-list[i]
    if diff>1:
        count+=diff-1
    i+=1
print(count)