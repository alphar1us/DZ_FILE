from pprint import pprint
from collections import Counter
import os

#задание 1
file_path = os.path.join(os.getcwd(), 'recipes.txt')
with open(file_path, encoding = 'utf-8' ) as f:
    cook_book = {}
    name_of_specific_dish = f.readline()

    while name_of_specific_dish:
        count_of_ingredient = int(f.readline())
        final_variant_dish_description = []
        dict_of_all_ingredients_of_one_dish = {}

        for i in range(count_of_ingredient):
            name_count_measure_of_one_ingredient = f.readline().split('|')
            name = name_count_measure_of_one_ingredient[0]
            quantity = name_count_measure_of_one_ingredient[1].strip()
            measure = name_count_measure_of_one_ingredient[2].strip()

            dct_name_quantity_measure = {'ingredient_name': name, 'quantity': quantity, 'measure': measure}
            final_variant_dish_description.append(dct_name_quantity_measure)
            dict_of_all_ingredients_of_one_dish[name_of_specific_dish.strip()] = final_variant_dish_description
            cook_book.update(dict_of_all_ingredients_of_one_dish)

        f.readline()
        name_of_specific_dish = f.readline()
#pprint(cook_book)

#задание 2

def shop_list(dishes, person = 1):
    shop_dict = {}
    ingr_list = []
    for dish in dishes:
        if dish in cook_book.keys(): #проверить является ли он ключом в словаре cook_book и вернуть значение
            for i in range(len(cook_book[dish])):
                ingr_list.append(cook_book[dish][i])
    key_ingr_list = ['measure', 'quantity']
    for i in range(len(ingr_list)):
        qty_msr = [ingr_list[i]['measure'], int(ingr_list[i]['quantity'])*person]
        ingr_name = ingr_list[i]['ingredient_name']
        qty_msr_dict = dict(zip(key_ingr_list, qty_msr))
        ingr_qty_msr_dict = {ingr_name : qty_msr_dict}
        shop_dict.update(ingr_qty_msr_dict)
    pprint(shop_dict)

print()

shop_list(['Омлет', 'Омлет'], 2)



list_with_files = ['3.txt', '2.txt', '1.txt']


def get_content_name_length_from_file(file_name):
    file_path = os.path.join(os.getcwd(), file_name)
    with open(file_path, encoding='utf-8') as f:
        name_of_file = file_name
        dict_content_and_length_of_file = {}
        content_from_file = []
        for item in f:
            content_from_file.append(item.strip())
            file_length = len(content_from_file)
        dict_content_and_length_of_file[tuple(content_from_file)] = file_length
        return [dict_content_and_length_of_file, name_of_file, file_length]


def get_list_of_contents_of_files():
    dict_of_contents_and_durations = {}  # создаем словарь словарей для того, чтобы его сортировать по ключам
    for content in list_with_files:
        dict_of_contents_and_durations.update(get_content_name_length_from_file(content)[0])
    sorted_list_dict_of_contents_and_durations = sorted(dict_of_contents_and_durations.items(), key=lambda x: x[1])
    return sorted_list_dict_of_contents_and_durations


def get_list_of_names_of_files():
    list_of_names_of_files = []
    for file_name in list_with_files:
        list_of_names_of_files.append(get_content_name_length_from_file(file_name)[1])
    return list_of_names_of_files


def get_list_of_lengths_of_files():
    list_of_lengths_of_files = []
    for file_length in list_with_files:
        list_of_lengths_of_files.append(get_content_name_length_from_file(file_length)[2])
    return list_of_lengths_of_files


def first_output():
    dict_zip_names_lengths = dict(zip(get_list_of_names_of_files(), get_list_of_lengths_of_files()))
    sorted_dict_zip_names_lengths = sorted(dict_zip_names_lengths.items(), key=lambda x: x[1])
    return [print(i) for i in sorted_dict_zip_names_lengths]  # 1-й вывод информации


def second_output():
    list_of_all_contents = []
    for i in get_list_of_contents_of_files():
        list_of_all_contents.append(list(i[0]))
    for index in range((len(list_of_all_contents)) - 1):
        list_of_all_contents[0].extend(list_of_all_contents[index + 1])  # делаем так, что первый вложенный список поглащает
        # # второй, а затем и третий. И в итоге остается единый список без вложений
    return [print(i) for i in list_of_all_contents[0]]  # 2-й вывод информации


if __name__ == '__main__':
    first_output()
    second_output()