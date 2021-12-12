from pprint import pprint

import os

def get_shop_list_by_dishes(dishes, person_count):
    ingredients = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient["ingredient_name"] not in list(ingredients.keys()):
                print(list(ingredients.keys()))
                ingredients[ingredient["ingredient_name"]] = {"measure": ingredient["measure"],
                                                              "quantity": int(ingredient['quantity']) * person_count}
            else:
                print(f'ing={ingredient["ingredient_name"]}')
                ingredients[ingredient["ingredient_name"]]["quantity"] += int(ingredient['quantity']) * person_count
    return ingredients


with open("recipes.txt", "r", encoding="utf8") as f:
    cook_book = {}
    prev_line = ""
    for counter, line in enumerate(f):
        if counter == 0 or prev_line == "\n":
            cur_recipe = line[:-1]
            cook_book[cur_recipe] = []
        ingredient = line.split(" | ")
        if len(ingredient) > 1:
            cook_book[cur_recipe].append(
                {"ingredient_name": ingredient[0], "quantity": ingredient[1], "measure": ingredient[2][:-1]})
        prev_line = line
for cook, ingredients in cook_book.items():
    print(cook)
    for ingredient in ingredients:
        print(ingredient)

pprint(get_shop_list_by_dishes(['Омлет','Омлет'], 1))



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