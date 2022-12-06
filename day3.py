f = open('q3.txt','r')
x = f.readlines()

# PART 1

z=[]
for item in x:
    a = set(item[:len(item)//2])
    b = set(item[len(item)//2:])
    z.append(list(a.intersection(b)))

y=[]
for item in z:
    for item2 in item:
        y.append(ord(item2))

total = []
for item in y:
    if item <= 90:
        total.append(item-38)
    else:
        total.append(item-96)

print(sum(total)) #prints 7795

# PART 2
z=[]
for i in range(0, len(x)//3):
    a = set(x[3*i])
    b = set(x[3*i+1])
    c = set(x[3*i+2])
    z.append(list(a.intersection(b.intersection(c))))

y=[]
for item in z:
    for item2 in item:
        if item2 != '\n':
            y.append(ord(item2))

total = []
for item in y:
    if item <= 90:
        total.append(item-38)
    else:
        total.append(item-96)

print(sum(total)) #prints 2703
