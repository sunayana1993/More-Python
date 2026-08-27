myfile=open('c:/More-Python/detailed output of IO/myfile.txt')
#myfile2=open('abc.txt')
print(myfile.read())
print(myfile.read())
# .read() is twice but output is only displayed once because cursor is at
# end of file
myfile.seek(0)
print(myfile.read())
myfile.seek(0)
print(myfile.readlines()) #print everything as list

with open('c:/More-Python/detailed output of IO/myfile.txt') as my_new_file:
    contents=my_new_file.read()

print(contents)

with open('c:/More-Python/detailed output of IO/myfile.txt',mode='r') as my_new_file1:
    contents=my_new_file1.read()



