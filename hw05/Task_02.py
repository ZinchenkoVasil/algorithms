def from_Int_to_Number16(number10):
    lst16 = '0123456789ABCDEF'
    lstNumber16 = []
    while number10 > 0:
        n = lst16[number10 % 16]
        lstNumber16.append(n)
        number10 = number10 // 16
    return lstNumber16[::-1]


#перевод из 16-чной в 10-чную
def from_Number16_to_Int(lstNumber16):
    dict16 = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
              '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    lstNumber16 = lstNumber16[::-1]
    j = 0
    n = 0
    for item in lstNumber16:
        n = n + dict16[item] * 16 ** j
        j += 1
    return n

lst1 = list(input("введите первое число в 16-ичном формате: "))
lst2 = list(input("введите второе число в 16-ичном формате: "))
int1 = from_Number16_to_Int(lst1)
int2 = from_Number16_to_Int(lst2)
summa = int1 + int2
mult = int1 * int2
lstSumma = from_Int_to_Number16(summa)
lstMult = from_Int_to_Number16(mult)
print("сумма: ", lstSumma)
print("произведение: ", lstMult)






