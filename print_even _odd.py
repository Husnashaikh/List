
elements = [23, 14, 56,12, 19, 9, 15, 25, 31, 42, 43]
i=0
count=0
while i<len(elements):
    if elements[i]%2==0:
        count=count+1
        print("it is an even number=",elements[i])
    else:
        print("it is an odd number=",elements[i])
    i=i+1