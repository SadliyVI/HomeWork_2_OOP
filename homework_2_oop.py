# Homework OOPs part 2

# Task 1

def get_file_path(file_name):
    """
    Return the full file path of a file given its name.

    Args:
        file_name(str): Name of the file and extension
                        Format: 'name.extension'
    """
    import os
    file_path = os.path.join(os.getcwd(), file_name)
    return file_path

def get_recipe_dictionary (file_path):
    """
    Read the recipes from a file and return a dictionary with recipes.
    Each recipe is represented as a key in the dictionary,
    and the value is a list of dictionaries, where each dictionary represents
    an ingredient.
    Each ingredient dictionary has three keys: 'ingredient_name',
    'quantity', and 'measure'.

    Args:
        file_path (str): Full file path of the recipes book.
    """
    with open(file_path, 'r', encoding = 'UTF-8') as f:
        lines_list = f.read().splitlines()
        for line in lines_list:
            if line == '':
                lines_list.remove(line)
        cook_book = {}
        for line in lines_list:
            if '|' not in line and not line.isdigit():
                cook_book[line] = []
                counter = int(lines_list[lines_list.index(line) + 1])
                index = lines_list.index(line) + 2
                while counter > 0:
                    ingredient = {'ingredient_name': '', 'quantity': 0,
                                  'measure': ''}
                    ingredient['ingredient_name'] = lines_list[index].split(
                        '|')[0].strip()
                    ingredient['quantity'] = float(lines_list[index].split(
                        '|')[1].strip())
                    ingredient['measure'] = lines_list[index].split(
                        '|')[2].strip()
                    cook_book[line].append(ingredient)
                    counter -= 1
                    index += 1
        return cook_book

# Example usage for Task 1

import pprint
print('Example usage for Task 1\n')
pprint.pp(get_recipe_dictionary(get_file_path('recipe_book.txt')), width = 110)

# Task 2

def get_shop_list_by_dishes(dishes_list, person_count):
    """
    Return a dictionary with the shopping list for a group of people.
    Each key in the dictionary is a dish name, and the value is a list of dictionaries,
    where each dictionary represents an ingredient with its quantity and measure.

    Args:
        dishes (list): List of dishes
        person_count (int): Number of people in the group
    """
    cook_book = get_recipe_dictionary(get_file_path('recipe_book.txt'))
    shopping_list = {}
    for dish in dishes_list:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] not in shopping_list:
                    shopping_list[ingredient['ingredient_name']] = {}
                    shopping_list[ingredient['ingredient_name']] ={
                        'measure': ingredient['measure'],
                        'quantity': float(ingredient['quantity']) *
                                    person_count}
                else: shopping_list[ingredient['ingredient_name']][
                    'quantity'] += (float(ingredient['quantity']) *
                                    person_count)

    return shopping_list

# Example usage for Task 2

print('\n')
print('Example usage for Task 2\n')
pprint.pp(get_shop_list_by_dishes(['Омлет', 'Запеченный картофель',
                                   'Салат Оливье'], 5))

# Task 3

def get_files_list(directory):
    """
    Return a list of all files in a given directory.

    Args:
        directory (str): Name of the target directory.
    """
    import os
    return [name for name in os.listdir(directory)]

def get_consolidated_texts(target_directory):
    """
    Consolidate all text files in a given directory into a single file,
    with the filename and its line count written at the beginning of each file.

    Args:
        target_directory (str): Name of the target directory.
    """

    import os
    files_list = get_files_list(target_directory)
    lines = {}
    if files_list:
        for file in files_list:
            with open(os.path.join(target_directory, file), 'r',
                      encoding='UTF-8') as f:
                if file in lines:
                    lines[file] += f.readlines()
                else: lines[file] = f.readlines()
        with open(os.path.join(os.getcwd(), 'consolidated_texts.txt'), 'w',
                      encoding='UTF-8') as f:
            for file, content in lines.items():
                f.write(f'{file}\n{len(content)}\n')
                f.writelines(content)
                f.write('\n')
    else:
        print('Директория с таким именем не найдена!')

# Example usage for Task 2

print('\n')
print('Example usage for Task 3\n')
get_consolidated_texts('Texts')
with open('consolidated_texts.txt', 'r', encoding='UTF-8') as f:
    print(f.read())
