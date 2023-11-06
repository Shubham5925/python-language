#selection sort

l1=[1,3,2,5,0]
for i in range(len(l1)-1,0):
    min=l1[0]
    for j in range(i+1,len(l1)):
        if min<l1[j]:
            min=l1[j]
    l1[i],l1[min]=l1[min],l1[i]

print("after sorting",l1)
