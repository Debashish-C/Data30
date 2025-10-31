def read_file(file):
    content = file.read()
    print(content)

file = open("ex.txt","r")
read_file(file)
file.close()
