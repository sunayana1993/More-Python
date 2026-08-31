example=[1,2,3,4,5,6,7]
from random import shuffle
shuffle(example)
print(example)
mylist=[2,4,5,6]

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

print(shuffle_list(mylist))