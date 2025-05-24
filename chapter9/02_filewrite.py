file =open('f.txt', 'w')
file.write("Hello, World!\n")
file.write("This is a test file.\n")
file.close()


readfile = open('f.txt', 'r')
readline = readfile.readlines()
print(type(readline))  # <class 'list'>
for line in readline:
    print(line.strip())
    
# Alternative you can write it with with statement

with open('f.txt', 'w') as file:
    print(file.write("Hello, World!\n"))
    print(file.write("This is a test file.\n"))
    
with open('f.txt') as file:
    print(file.read())  # This will not work because the file is opened in write mode