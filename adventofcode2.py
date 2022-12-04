f = open('q2.txt','r')
x = f.readlines()

#PART 1

val = 0

for item in x:
    #score from winning/drawing
    if (item[0] == 'A' and item[2] == 'X') or (item[0] == 'B' and item[2] == 'Y') or (item[0] == 'C' and item[2] == 'Z'):
        val+=3
    if (item[0] == 'A' and item[2] == 'Y') or (item[0] == 'B' and item[2] == 'Z') or (item[0] == 'C' and item[2] == 'X'):
        val+=6
    #score from throwing rock/paper/scissors
    if item[2]=='X':
        val+=1
    if item[2]=='Y':
        val+=2
    if item[2]=='Z':
        val+=3

print(val) #prints 9177

#PART 2

val = 0

for item in x:
    #score from winning/drawing
    if item[2]=='Y':
        val+=3
    if item[2]=='Z':
        val+=6
    #score from throwing rock/paper/scissors
    if (item[0] == 'A' and item[2] == 'Y') or (item[0] == 'B' and item[2] == 'X') or (item[0] == 'C' and item[2] == 'Z'):
        val+=1
    if (item[0] == 'A' and item[2] == 'Z') or (item[0] == 'B' and item[2] == 'Y') or (item[0] == 'C' and item[2] == 'X'):
        val+=2
    if (item[0] == 'A' and item[2] == 'X') or (item[0] == 'B' and item[2] == 'Z') or (item[0] == 'C' and item[2] == 'Y'):
        val+=3

print(val) #prints 12111
