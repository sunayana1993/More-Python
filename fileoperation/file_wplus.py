with open('example.txt','w+') as file:
    file.write("Sunayana")
    file.write("How are you?")
    #file.seek(0)
    content=file.read()
    print(content)