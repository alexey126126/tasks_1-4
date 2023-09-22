def read_f(file):
    numbers = []
    with open(file, 'r') as file:
        for line in file:
            numbers += [int(num) for num in line.split()]
    return numbers


def write_f(file, list):
    with open(file, 'w') as f:
        for item in list:
            f.write(str(item) + ' ')


def new_list(list1, list2):
    even_list1 = set(filter(lambda x: x % 2 == 0 and x not in list2, list1))
    odd_list2 = set(filter(lambda x: x % 2 != 0 and x not in list1, list2))

    new_set = sorted(even_list1 | odd_list2)
    return list(new_set)


out = new_list(read_f("input1.txt"), read_f("input2.txt"))
write_f("output.txt", out)
print(out)  # 2, 3, 6, 9, 12
