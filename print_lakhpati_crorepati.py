paisa=[3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
i=0 
crorepati=0
lakhpati=0
dilwale=0
while i<len(paisa):
    if paisa[i]>=10000000:
        crorepati+=1
    elif paisa[i]>=100000:
        lakhpati+=1
    else:
        dilwale+=1
    i=i+1
print("crorepati",crorepati)
print("lakhpati",lakhpati)
print("dilwale",dilwale)




















# 4 Crorepati
# 3 Lakhpati
# 4 Dilwale



