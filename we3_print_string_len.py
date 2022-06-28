# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Go to the editor
# Sample List : 
a=['abc', 'xyz', 'aba', '1221']
c = 0
for i in a:
    if len(a) > 1 and i[0] == i[-1]:
        c += 1
print(c)