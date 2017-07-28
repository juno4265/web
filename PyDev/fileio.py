file = open("zero.txt", 'r')
line = file.read()
while line:
    print (line)
    file.close()
