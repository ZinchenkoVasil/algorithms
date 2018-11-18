#3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найти в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой – не больше ее.

import random


def quick_sort(array, fst, lst):

    if fst >= lst: #массив отсортирован
#в самом худшем случае нам не повезет и мы дойдем до конца сортировки и отсортируем весь массив
        #в этом случае ищем середину массива
        mid = (len(array) - 1) // 2
        return array[mid]

    pivot = array[random.randint(fst, lst)]
    i, j = fst, lst
    while i <= j:
        while array[i] < pivot:
            i += 1

        while array[j] > pivot:
            j -= 1

        if i <= j:
            array[i], array[j] = array[j], array[i]
            i, j = i + 1, j - 1

#определяем длину 2 половинок массива
#левая сторона left_side - здесь все элементы меньше или равны опорному вектору
#правая сторона right_side - там все элементы >= опорному вектору
    left_side = j + 1
    right_side = len(array) - 1 - j

#надо определить в какой половине остался опорный вектор в левой или правой?
#в зависимости от этого вычесть 1 из левой или правой половины
    pivot_from_left = False
    n = fst
    while n <= j:
        if array[n] == pivot:
            pivot_from_left = True
            break
        n += 1
    if pivot_from_left:
        left_side -= 1
    else:
        right_side -= 1

#сравнить половинки после вычета опорного вектора
    if left_side == right_side:
        return pivot
    elif left_side > right_side:
        return quick_sort(array, fst, j)
    else:
        return quick_sort(array, i, lst)


#array = [12, 9, 3, 10, 15, 11, 7, 13, 14, 0, 2, 4, 1, 6, 8, 5, 1]
m = int(input("введите m (любое натуральное число): "))
array = [random.randint(0, 100) for i in range(2*m + 1)]
print("исходный список:")
print(array)

mid = quick_sort(array, 0, len(array) - 1)
print("результирующий список: ")
print(array)
print("медиана: ", mid)
