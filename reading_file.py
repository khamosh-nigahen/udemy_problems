
file=open(r"/Users/puneetjain/Downloads/fruits.txt","r")
content=file.read()
#file.close()
print(content)

file.seek(0)
content=file.readlines()
len_of_fruits = [i.rstrip for i in content]
len_of_fruits =[len(element) for element in content]


print ("\n".join(str(v) for v in len_of_fruits))
file.close()
