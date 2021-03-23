# import sys
with open('рецепт.txt') as f:
    cookbook = dict()
    i = 0
    name = f.readline().strip()
    # функция чтения из файла
    def read_cookbook():
        global name
        ingred_count = int(f.readline().strip())
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
        ch = f.readline().strip()
        name = f.readline().strip()
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
print(cookbook)






