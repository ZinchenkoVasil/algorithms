#2. Закодируйте любую строку (хотя бы из трех слов) по алгоритму Хаффмана.

#формируем словарь кодов
def create_code(node, code):
    global dict_code
    if node.left:
        create_code(node.left, code + '0')
        create_code(node.right, code + '1')
    elif node.value:
        dict_code[node.value] = code

#подсчитываем частоты
def calc_rate(str_in):
    dubl = {}
    for i in str_in:
        if i in dubl:
            dubl[i] += 1
        else:
            dubl[i] = 1
    return dubl

#ищем индексы 2 элементов с минимальной частотой
def search_min(lst):
    n = len(lst)
    indx_min = -1
    min_ = float("inf")
    for i in range(n):
        item = lst[i]
        if not item.married and item.rate < min_:
            min_ = item.rate
            indx_min = i

    indx_min_second = -1
    min_ = float("inf")
    for i in range(n):
        item = lst[i]
        if not item.married and i != indx_min and item.rate < min_:
            min_ = item.rate
            indx_min_second = i

    return (indx_min_second, indx_min)


class MyNode:
    def __init__(self, value, rate=0, left=None, right=None, married=False):
        self.value = value
        self.rate = rate
        self.married = married
        self.left = left
        self.right = right

str_in = "beep boop beer!"
print("входная строка: ", str_in)

dict_rate = calc_rate(str_in) #вычислили частоты
print("Словарь частотности: ",dict_rate)
#сформировали список узлов дерева
lst = []
for litera, rate in dict_rate.items():
    myNode = MyNode(litera, rate)
    lst.append(myNode)

while True:
#ищем 2 минимальных узла
    indx_mins = search_min(lst)
#если в массиве остался только 1 свободный узел, то выходим из цикла
    indx1 = indx_mins[0]
    indx2 = indx_mins[1]
    if indx1 == -1:  #второго по наименьшей частоте не найдено!
        indx_root = indx2
        break
    node1 = lst[indx1]
    node2 = lst[indx2]
    rate = node1.rate + node2.rate
    myNode = MyNode(None, rate, left=node1, right=node2)
    lst.append(myNode)
    lst[indx1].married = True
    lst[indx2].married = True

root_node = lst[indx_root]
dict_code = {}
create_code(root_node, '')
print(dict_code)
if dict_code:
    print("Таблица кодировки")
    for item_key, item_value in dict_code.items():
        print(f"Символ: '{item_key}' код: {item_value}")
    str_out = ''
    for litera in str_in:
        str_out += dict_code[litera]
    print("выходная строка:")
    print(str_out)
    len_str_in = len(str_in)*8
    print(f"Длина входной строки: {len_str_in} бит")
    print(f"Длина выходной строки: {len(str_out)} бит")



