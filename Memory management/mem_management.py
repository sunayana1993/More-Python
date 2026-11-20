''' Python use memory management, python maintains count of reference pointing to iter
 When the reference count is allocated to 0 memory is deallocated '''

import sys
a=[]
print(sys.getrefcount(a))
#2 because referenced by a and get ref count function

b=a
print(sys.getrefcount(a))