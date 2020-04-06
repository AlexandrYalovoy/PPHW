# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами
# 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

list_one = list(input('Введите значения из которых будет сформирован список - '))

# list_one = list('asdfghj') #Тестовый список

list_hab = list_one.copy()

index_first = 0
index_second = 1

while True:
    list_one[index_first] = list_hab[index_second]
    list_one[index_second] = list_hab[index_first]

    index_first += 2
    index_second += 2

    if index_first == (len(list_hab) - 1) or index_first == len(list_hab):
        break

print(list_one)
print(list_hab)