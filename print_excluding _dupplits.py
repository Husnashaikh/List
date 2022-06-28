
list = [6,1,3,5,6,3,1]
i=0
b=[]
while i<len(list):
    h=list[i]
    if h not in b:
        b.append(h)
    i=i+1
print(b)
i=0
product=1
while i<len(b):
    product=product*b[i]
    i=i+1
print(product)
