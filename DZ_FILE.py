from pprint import pprint
with open('рецепт.txt') as f:
    cookbook = dict()
    i = 0
    name = f.readline().rstrip()
    # функция чтения из файла
    def read_cookbook():
        global name
        ingred_count = int(f.readline().rstrip())
        ingr_list = list()
        bb = []
        # ключи для словаря
        uni_k = ['ingredient_name', 'quantity', 'measure']
        for _ in range(ingred_count):
             # получаем список
            a = f.readline().split('|')
            # объединяем в ловарь
            uni_k_and_a = dict(zip(uni_k, a))
            bb.append(uni_k_and_a)
            cookbook[name] = bb
        # пустая строка между рецептами
        ch = f.readline().rstrip()
        name = f.readline().rstrip()
        # если есть название следующего рецепта - отметка для отработки цикла
        if name:
            global i
            i = 0
        else:
            i = i + 1
    # первый прогон
    read_cookbook()
    # запуск, >1 рецепта
    while i == 0:
        read_cookbook()
pprint(cookbook)

def get_shop_list_by_dishes(dishes, person_count):
    test = list()
    test2 = dict()
    country_search= dishes
    # помещаем игридиенты в список

    for dishes_name, prod in cookbook.items():
        if dishes_name in country_search:
            # test.append(prod)
            test = prod
            # pprint(prod)
            for element in test[:]:

                # ингредиент
                name_dishes = element.pop('ingredient_name')
                # без название ингредиента
                # pprint(element)
                # количество
                # int(element['quantity']) ** 2
                a = int(element.pop('quantity')) * int(person_count)
                # pprint(a)
                element['quantity'] = a
                test2[name_dishes] = element
    pprint(test2)

# задание 2
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

#  задание 3
list_file = ['1.txt', '2.txt', '3.txt']

test = dict()
test2 = dict()
for t in list_file:
    with open(t, 'rt', encoding = 'utf-8') as f:
        a = sum(1 for _ in f)
    f.close()
    with open(t, 'rt', encoding = 'utf-8') as f2:
        b = f2.readlines()
    # print(a)
        my_String = ''.join(b)
    test[t] = a
    test2[t] = my_String
# print(test)
    with open("test666.txt", "w") as file:
        for w in sorted(test, key=test.get, reverse=False):
            tt = str(test[w])
            ttt = test2[w]
            file.write(w + '\n' + tt + '\n' + ttt + '\n')




