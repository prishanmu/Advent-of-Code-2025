## prompt can be found here: https://adventofcode.com/2025/day/4

import numpy as np

## IMPORT DATA ##
example_input = ['..@@.@@@@.',
'@@@.@.@.@@',
'@@@@@.@.@@',
'@.@@@@..@.',
'@@.@@@@.@@',
'.@@@@@@@.@',
'.@.@.@.@@@',
'@.@@@.@@@@',
'.@@@@@@@@.',
'@.@.@@@.@.']

input = open('day4_input.txt').read().splitlines()

## REFORMAT DATA ##

def reformat_input(input): 
  new_input = []
  for line in input:
    line = list(line)
    new_input.append(line)
  input = np.array(new_input)
  
  return input

example_input = reformat_input(example_input)
input = reformat_input(input)

## SOLUTIONS ## 

def day4part1_answer(input):
    rolls = 0
    for i in range(0,input.shape[0]):
        for j in range(0,input.shape[1]):
            if input[i][j] == '@':
                x=0
                #check if surrounding boxes have @
                if i !=0:
                    if input[i-1][j] == '@':
                        x += 1
                    if j !=0:
                        if input[i-1][j-1] == '@':
                            x += 1
                    if j !=input.shape[1] - 1:
                        if input[i-1][j+1] == '@':
                            x += 1
                if i != input.shape[0] - 1:
                    if input[i+1][j] == '@':
                        x += 1
                    if j !=0:
                        if input[i+1][j-1] == '@':
                            x += 1
                    if j !=input.shape[1] - 1:
                        if input[i+1][j+1] == '@':
                            x += 1
                if j !=0:
                    if input[i][j-1] == '@':
                        x += 1
                if j !=input.shape[1] - 1:
                    if input[i][j+1] == '@':
                        x += 1
                if x < 4:
                    rolls += 1
    return rolls

# to call: 
print(day4part1_answer(new_example_input)) #13
print(day4part1_answer(input)) #1376


def day4part2_answer(input):
    ''' the difference here is instead of just counting rolls, we want to modify the actual array after the roll has been deemed removable'''
    new_array = np.full(input.shape, '.')
    rolls = 0
    for i in range(0, input.shape[0]):
        for j in range(0, input.shape[1]):
            if input[i][j] == '@': #the position has a roll
                x = 0
                #check if surrounding boxes have @
                if i != 0:
                    if input[i - 1][j] == '@':
                        x += 1
                    if j != 0:
                        if input[i - 1][j - 1] == '@':
                            x += 1
                    if j != input.shape[1] - 1:
                        if input[i - 1][j + 1] == '@':
                            x += 1
                if i != input.shape[0] - 1:
                    if input[i + 1][j] == '@':
                        x += 1
                    if j != 0:
                        if input[i + 1][j - 1] == '@':
                            x += 1
                    if j != input.shape[1] - 1:
                        if input[i + 1][j + 1] == '@':
                            x += 1
                if j != 0:
                    if input[i][j - 1] == '@':
                        x += 1
                if j != input.shape[1] - 1:
                    if input[i][j + 1] == '@':
                        x += 1
                if x < 4:# the roll is removable, no changes will be made to the new array
                    # print(x)
                    # print(i,j)
                    rolls += 1 #add to the count

                else: # the roll will stay, so we must change the value in the new array
                    new_array[i][j] = '@'
            #else: # there is no roll in the position, no changes need to be made

    return rolls, new_array

# to call: 
rolls = -1
total_rolls = 0

while rolls != 0:
    rolls, input = day4part2_answer(input)
    total_rolls = total_rolls + rolls

print(total_rolls) # 8587
