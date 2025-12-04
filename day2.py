## prompt can be found here: https://adventofcode.com/2025/day/2

example_input = '11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'

input = "18623-26004,226779-293422,65855-88510,868-1423,248115026-248337139,903911-926580,97-121,67636417-67796062,24-47,6968-10197,193-242,3769-5052,5140337-5233474,2894097247-2894150301,979582-1016336,502-646,9132195-9191022,266-378,58-91,736828-868857,622792-694076,6767592127-6767717303,2920-3656,8811329-8931031,107384-147042,941220-969217,3-17,360063-562672,7979763615-7979843972,1890-2660,23170346-23308802"

def list_to_listoflists(input_list):
  ''' converts string into list of lists, where each list within the list is two numbers that represent a range '''
    input_list = input_list.split(',')
    new_list = []
    for i in input_list:
        i_list = i.split('-')
        firstID = i_list[0]
        lastID = i_list[1]

        new_i = [firstID, lastID]
        new_list.append(new_i)

    return new_list


def day2_part1_answer(input_list):
    input_list = list_to_listoflists(input_list)
    summ = 0
    for r in input_list:
        for i in range(int(r[0]), int(r[1])+1):
            i = str(i)
            half_length = len(i) // 2
            if i[:half_length] == i[half_length:]:
                summ += int(i)

    return summ

## to call: 
invalid_id_sum(example_input) #1227775554
invalid_id_sum(input) #19386344315

def day2_part2_answer(input_list):
    input_list = list_to_listoflists(input_list)
    invalid = []
    for r in input_list:
        for i in range(int(r[0]), int(r[1])+1):
            i = str(i)
            i_len = len(i)
            for j in range(1, i_len+1):
                if i_len % j == 0 and i_len // j > 1:
                    # split i into sections of j length
                    #n = i_len // j
                    parts = [i[k:k+j] for k in range(0, len(i), j)]

                    # if sections are identical, add i to invalid list
                    if len(set(parts)) == 1:
                        x = int(i)
                        invalid.append(x)

    return sum(set(invalid))

## to call: 
day2_part2_answer(example_input) #4174379265
day2_part2_answer(input) #34421651192
