def read_array_from_file(file_name):
    array = []
    with open(file_name, 'r') as file:
        for line in file:
            row = line.strip().split()  # разбиваем строку по пробелам
            array.append([int(element) for element in row])  # добавляем полученный ряд в массив
    return array


def write_f(file, list):
    with open(file, 'w') as f:
        for item in list:
            f.write(str(item) + ' ')


def check_overlap(arr1, arr2):
    rows1, cols1 = len(arr1), len(arr1[0])
    rows2, cols2 = len(arr2), len(arr2[0])

    for i in range(rows1 - rows2 + 1):
        for j in range(cols1 - cols2 + 1):
            overlap = True
            for k in range(rows2):
                for l in range(cols2):
                    if arr1[i + k][j + l] != arr2[k][l]:
                        overlap = False
                        break
                if not overlap:
                    break

            if overlap:
                return (i, j)

    return None


arr1 = read_array_from_file("input1.txt")
arr2 = read_array_from_file("input2.txt")

result = list(check_overlap(arr1, arr2))
if result:
    write_f("output.txt", result)
    print(result)
else:
    print("Второй массив нельзя поместить на первый")
