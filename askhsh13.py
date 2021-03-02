with open('two_cities_ascii.txt','r') as file:
    i=0
    list1=[]
    for line in file:
        for x in line.split():
            list1.append(x)


file.close()
i=1
while len(list1)>=2:
    i=1
    x=False
    while i<=len(list1):

        if len(list1[0])+len(list1[1])==20:
            print(list1[0],list1[i])
            x=True
            del list1[0]
            del list1[i-1]

            i=i+1
            break
        else:
            i=i+1
    if x==False:
        del list1[0]
if len(list1)==1:
    del list1[0]
