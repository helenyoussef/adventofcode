f = open('q4.txt','r')
x = f.readlines()

# PART 1 

sum = 0

for item in x:
    i=0
    while item[i] != '-':
        i+=1
    dash1 = i
    while item[i] !=',':
        i+=1
    comma = i
    while item[i] != '-':
        i+=1
    dash2 = i
    a1 = int(item[:dash1])
    b1 = int(item[dash1+1:comma])
    a2 = int(item[comma+1:dash2])
    b2 = int(item[dash2+1:])
    if (a1<=a2 and b2<=b1) or (a2<=a1 and b1<=b2):
        sum +=1

    # print(item)
    # print(a1)
    # print(a2)
    # print(b1)
    # print(b2)
    # print('sum so far is: ', sum)

print('total sum for part 1 is:', sum) # prints 464

# PART 2 

sum = 0 

def set_create(a,b):
    temp=set()
    for i in range(a,b+1):
        temp.add(i)
    return(temp)

empty_set = set()

for item in x:
    i=0
    while item[i] != '-':
        i+=1
    dash1 = i
    while item[i] !=',':
        i+=1
    comma = i
    while item[i] != '-':
        i+=1
    dash2 = i
    a1 = int(item[:dash1])
    b1 = int(item[dash1+1:comma])
    a2 = int(item[comma+1:dash2])
    b2 = int(item[dash2+1:])


    elf1 = set_create(a1,b1)
    elf2 = set_create(a2,b2)
    if elf1.intersection(elf2) != empty_set:
        sum+=1

print('total sum for part 2 is:', sum) # prints 770