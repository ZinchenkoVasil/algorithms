#2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

def Merge(lst1, lst2):
    lst = []
    i = 0
    j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            lst.append(lst1[i])
            i += 1
        else:
            lst.append(lst2[j])
            j += 1
    if i == len(lst1):
        lst = lst + lst2[j::]
    if j == len(lst2):
        lst = lst + lst1[i::]
    return lst

def Merge_Sort(in_lst):
    if len(in_lst) == 1:
        return in_lst
    mid = len(in_lst) // 2
    lst1 = Merge_Sort(in_lst[mid::])
    lst2 = Merge_Sort(in_lst[:mid:])
    out_lst = Merge(lst1, lst2)
    return out_lst

import random
lst = [50 * random.random() for i in range(10)]
print(lst)
print(Merge_Sort(lst))