myfile=open('c:/More-Python/detailed output of IO/myfile.txt')
#myfile2=open('abc.txt')
print(myfile.read())
print(myfile.read())
# .read() is twice but output is only displayed once because cursor is at
# end of file
myfile.seek(0)
print(myfile.read())
myfile.seek(0)
print(myfile.readlines())


