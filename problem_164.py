#create list with elements present in l1 not in l2
l1=[12,34,22,34]
l2=[34,33,22,10]
l3=[x for x in l1 if x not in l2]
l3=[x for x in l2 if x not in l1]
print(l3)