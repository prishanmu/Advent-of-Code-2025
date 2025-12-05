## prompt can be found here: https://adventofcode.com/2025/day/3

example_input = ['987654321111111', '811111111111119', '234234234234278', '818181911112111']

input = open('day3_input.txt').read().splitlines() # 200 lines/items in list

def day3_part1_answer(input):

    total = 0
    for line in input:
        line_list = list(line)
        digits = [int(x) for x in line_list]
        max_digit = max(digits)
        if digits.index(max_digit) == len(digits) - 1:
            ones_digit = max_digit
            tens_digit = max(digits[:-1])

        else:
            tens_digit = max_digit
            ones_digit = max(digits[digits.index(max_digit) + 1:])

        total = total + ones_digit + (10* tens_digit)

    return total

## to call: 
day3_part1_answer(example_input) #357
day3_part1_answer(input) #16973


def day3_part2_answer(input):
    total = 0
    for line in input:
        line_list = list(line)
        digits = [int(x) for x in line_list]

        # lets name each digit with digit 1 being the first digit, not the ones digit.
        digit_1 = max(digits[:-11])
        digits = digits[digits.index(digit_1) + 1:]
        digit_2 = max(digits[:-10])
        digits = digits[digits.index(digit_2) + 1:]
        digit_3 = max(digits[:-9])
        digits = digits[digits.index(digit_3) + 1:]
        digit_4 = max(digits[:-8])
        digits = digits[digits.index(digit_4) + 1:]
        digit_5 = max(digits[:-7])
        digits = digits[digits.index(digit_5) + 1:]
        digit_6 = max(digits[:-6])
        digits = digits[digits.index(digit_6) + 1:]
        digit_7 = max(digits[:-5])
        digits = digits[digits.index(digit_7) + 1:]
        digit_8 = max(digits[:-4])
        digits = digits[digits.index(digit_8) + 1:]
        digit_9 = max(digits[:-3])
        digits = digits[digits.index(digit_9) + 1:]
        digit_10 = max(digits[:-2])
        digits = digits[digits.index(digit_10) + 1:]
        digit_11 = max(digits[:-1])
        digits = digits[digits.index(digit_11) + 1:]
        digit_12 = max(digits[:])

        volt = ((digit_1 * 10**11) + (digit_2 * 10**10)
                 + (digit_3 * 10**9) + (digit_4 * 10**8) + (digit_5 * 10**7)
                 + (digit_6 * 10**6) + (digit_7 * 10**5) + (digit_8 * 10**4)
                 + (digit_9 * 10**3) + (digit_10 * 10**2) + (digit_11 * 10**1)
                 + (digit_12 * 10**0))
        #print(volt)

        total = (total + volt)

    return total

## to call: 
day3_part2_answer(example_input) #3121910778619
day3_part2_answer(input) # 168027167146027
