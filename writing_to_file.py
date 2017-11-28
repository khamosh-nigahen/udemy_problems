
file=open(r"write.txt", 'w')
numbers = [1,2,3]
for item in numbers:
    file.write(str(item)+ "\n")
file.close()
