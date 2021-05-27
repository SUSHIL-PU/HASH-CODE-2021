files = open('a.txt','r')   # Select a input file
finalInp = list()
for Input in files:
    Input = Input.strip()
    li = list(Input.split(" ")) 
    finalInp.append(li)
    
#print(finalInp)
d = int(finalInp[0][0])
i = int(finalInp[0][1])
s = int(finalInp[0][2])
v = int(finalInp[0][3])
f = int(finalInp[0][4])

#print(d, i, s, v, f)
street = list()
for j in range(s):
    street.append(finalInp[j+1])
#print(street)

cars = list()
for j in range(v):
    cars.append(finalInp[s+1+j])
#print(cars)


#OUTPUT PRINTS
#----------------------------------------------
print(i)  #Intersection
for j in range(i):
    print(j) # j'th intersection
    count = 0
    for p in street:
        if(p[1] == str(j)):
            count = count + 1
    print(count)
    for p in street:
        if p[1] == str(j):
            print(p[2], int(p[3])) 
