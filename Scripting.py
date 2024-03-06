list1=[]
with open("input.txt",'r') as reader:
    
    """ list1.append(reader.readlines())
    print(list1) """
    for line in reader.readlines():
        list1.append(line)
    #print(list1)
        
list2=[]

#replace : with -
for line in list1:
    x=line.replace(':','-')
    list2.append(x)


#remove the \n

list3=[]  
for line in list2:
    x=line.replace('\n','')
    list3.append(x)

#change to lower case
    
list4=[]

for line in list3:
    x=line.lower()
    list4.append(x)

print(list4)


with open('output.txt', 'w') as writer:
    for i in list4:
        writer.write(i)
        writer.write('\n')
