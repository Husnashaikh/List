elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
sum=0
count=0
while i<len(elements):
    if elements[i]%2==0:
        sum=sum+elements[i]
        count=count+1
    i=i+1
print("sum of even number",sum)
print("count of even number",count)
print("average of even number",sum//count)
i=0
while i<len(elements):
    if elements[i]%1 or elements[i]%2:
        sum=sum+elements[i]
        count=count+1
    i=i+1
print("sum of odd number",sum)
print("count of odd number",count)
print("average of odd number",sum//count)
i=0
count=0
sum=0
while i<len(elements):
    sum=sum+elements[i]
    count=count+1
    i=i+1
print("sum of list",sum)
print("count of list",count)
print("average of list",sum//count)