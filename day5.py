### GET INPUT VALUES ###

example_range_input = ["3-5","10-14","16-20","12-18"]
example_id_input = ["1","5","8","11","17","32"]

input = open('day5_input.txt').read().split("\n\n")
range_input = input[0].splitlines()
id_input = input[1].splitlines()
# convert id_input to list of ints
example_id_input = [int(x) for x in example_id_input]
id_input = [int(x) for x in id_input]
# concert range_input to list of int ranges
def range_conversion(range_input):
    list_of_ranges = []
    for item in range_input:
        item = item.split('-')
        list_of_ranges.append(range(int(item[0]), int(item[1]) + 1))

    return list_of_ranges
example_range_input = range_conversion(example_range_input)
range_input = range_conversion(range_input)

### SOLUTION ###

def day5part1_answer(range_input, id_input):
    fresh_ids = []
    for r in range_input:
        for id in id_input:
            if id in r:
                fresh_ids.append(id)
    fresh_ids = list(set(fresh_ids))

    return len(fresh_ids)

day5part1_answer(example_range_input, example_id_input) # 3
day5part1_answer(range_input, id_input) # 782

def day5part2_answer(range_input):
    final_list = []
    for r in range_input:
        l = list(r)
        for i in l:
            if i not in final_list:
                final_list.append(i)
    final_list = list(set(final_list))
    return len(final_list)

day5part2_answer(example_range_input)#14
day5part2_answer(range_input) # still running
