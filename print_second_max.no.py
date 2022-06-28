numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
a=0
while i<len(numbers):
    if numbers[i]>a:
        a=numbers[i]
    i+=1
print(a)
i=0
b=0
while i<len(numbers):
    if numbers[i]>b:
        if numbers[i]!=a:
            b=numbers[i]
    i+=1
print(b)
i=0
c=0
while i<len(numbers):
    if numbers[i]>c:
        if numbers[i]!=a and numbers[i]!=b:
            c=numbers[i]
    i=i+1
print()    





# a=[1,2,3,4,5,6]
# i=0
# b=[]
# while i<len(a):
#     c=a[i-3]
#     b.append(c)
#     i=i+1
# print(b)