file_to_open=input("Give me the file:")
file=open(file_to_open,"r")
a=file.read().replace("\n", "")
file.close()
elem=''
for x in a[::-1]:
    elem_num=128-ord(x)
    elem+=chr(elem_num) 

print(elem)
