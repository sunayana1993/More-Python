mylist=[1,2,3]
mylist1=['STRING',2,3]
print(mylist1[1])
print(mylist1[0:])

#concatenate two list
m1=['one','two','three']
m2=['four','five','six']
print(m1+m2)

l2=[3,1,5,4]
l2.sort()
#print(l2.sort()) -prints None as sort is inplace
print(l2)

#How do I index a nested list?
l3=[1,2,[4,5]]
print(l3[2][0])