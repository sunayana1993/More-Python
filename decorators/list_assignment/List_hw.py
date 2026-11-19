list20=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(list20)

#q2
print(list20[0],list20[10],list20[19])

#q3
print(list20[0:5])#first 5 element
print(list20[-1:-6:-1])#last 5 element
print(list20[4:15])

#comprehension
listc=[num*num for num in range(10)]
print(listc)

liste=[num for num in list20 if num%2==0]
print(liste)

#list method
listd=[10,1,2,10,3]
listd.sort()
print(listd)
listd=list(dict.fromkeys(listd))
print(listd)