f = open('q1.txt','r')
x = f.readlines()

#PART 1

val = 0
cur_val = 0
for item in x:
    if item != '\n':
        cur_val += int(item)
    else:
        if val < cur_val:
            val = cur_val
        cur_val = 0

print(val) #prints 69795

#PART 2

val1=0
val2=0
val3=0

cur_val=0
for item in x:
    if item != '\n':
        cur_val+=int(item)
    else:
        if cur_val >= val1:
            val3 = val2
            val2 = val1
            val1 = cur_val
        elif cur_val >= val2:
            val3 = val2
            val2 = cur_val
        elif cur_val >= val3:
            val3 = cur_val
        cur_val = 0

top_three = val1 + val2 + val3

print(top_three) #prints 208437
