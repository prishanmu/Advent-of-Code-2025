lines = open('day1_input.txt').read().splitlines()

print(len(lines)) # output = 4168

## PART 1: how many times does the dial land on 0? ##

position = 50
password = 0
for line in lines:
    direction = line[0]
    clicks = int(line[1:])

    if direction == 'R':
        position = (position + clicks) % 100

    if direction == 'L':
        position = (position - clicks) % 100

    if position == 0:
        password = password + 1

print(password) #output = 1031

## PART 2: how many times does the dial pass 0? ##

position = 50
password = 0

for line in lines:
    direction = line[0]
    clicks = int(line[1:])

    #move click by click :
    for _ in range(clicks):
            if direction == 'L':
                position = (position - 1) % 100
            else: # direction R
                position = (position + 1) % 100

            if position == 0:
                password += 1

print(password) # output = 5831
