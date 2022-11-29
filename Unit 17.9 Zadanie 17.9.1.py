# преобразование введенных значений в числа, если они записаны с запятой или игнорировать нечисловые значения
def str2num(a):
    a = a.replace(',', '.')
    try:
        dec = float(a)
        if dec - int(dec) == 0:
            dec = int(dec)
        return dec

    except:
        pass

def sort_UP(lst):
    return sorted(lst)

def binary_search(array, element, left, right):
    middle = (left + right) // 2
    if array[left] == array[right] == element:
        return 'любым, так как числа одинаковые'
    if element >= array[right]:
        return '[' + str(right + 1) + '] после значения ' + str(array[right])
    if element <= array[left]:
        return '[' + str(left) + '] перед значением ' + str(array[left])
    if array[middle] == element:
        return '[' + str(middle + 1) + '] между значениями ' + str(array[middle]) + ' и ' + str(array[middle + 1])
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    elif element > array[middle]:
           return binary_search(array, element, middle + 1, right)


input_string = input('Запишите последовательность чисел через пробел: ')
print()

input_list = input_string.split()

numbers = []
for item in input_list:
    num = str2num(item)
    if num == 0 or num:
        numbers.append(num)

numbers = sort_UP(numbers)

print('Данная последовательность в порядке возрастания: ')
print('', numbers)
print()

num = None
while not (num or num == 0):
    num = str2num(input('Введите произвольное число: '))

print()

dop = binary_search(numbers, num, 0, len(numbers) - 1)

print('Это число займёт в последовательности место с индексом', dop)
print()

numbers.append(num)
numbers = sort_UP(numbers)

print('Ваша дополненная последовательность чисел выглядит так: ')
print('', numbers)
print()