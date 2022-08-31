
sequence_numbers = input('Введите целые числа через пробел: ')
any_number = int(input('Введите любое число: '))
#Проверка ввода.
def is_int(str):
    str = str.replace(' ', '')
    try:
        int(str)
        return True
    except ValueError:
        return False

if " " not in sequence_numbers:
    print("Отсутствуют пробелы.")
    sequence_numbers = input('Введите целые числа через пробел: ')
if not is_int(sequence_numbers):
    print('В вводе нет цифр или целых чисел.')
else:
    sequence_numbers = sequence_numbers.split()

# Преобразование введённой последовательности в список

list_sequence_numbers = [int(item) for item in sequence_numbers]

# Сортировка списка по возрастанию элементов в нем.
def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result

list_sequence_numbers = merge_sort(list_sequence_numbers)

# Устанавливается номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу.

def binary_search(array, element, left, right):
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if array[middle] == element:
            return middle
        elif element < array[middle]:
            return binary_search(array, element, left, middle - 1)
        else:
            return binary_search(array, element, middle + 1, right)
    except IndexError:
        return 'Число выходит за границы списка, введите меньшее число.'



print(f'Список по возрастанию: {list_sequence_numbers}')

if not binary_search(list_sequence_numbers, any_number, 0, len(list_sequence_numbers)):
    Li = min(list_sequence_numbers, key=lambda x: (abs(x - any_number), x))
    ind = list_sequence_numbers.index(Li)
    max_ind = ind + 1
    min_ind = ind - 1
    if Li < any_number:
        print(f'В списке нет данного элемента')
    elif min_ind < 0:
        print(f'В списке нет данного элемента')
    elif rI > any_number:
        print(f'В списке нет данного элемента')
    elif list_sequence_numbers.index(Li) == 0:
        print(f'Индекс  элемента: {list_sequence_numbers.index(Li)}')
else:
    print(f'Индекс элемента: {binary_search(list_sequence_numbers, any_number, 0, len(list_sequence_numbers))}')