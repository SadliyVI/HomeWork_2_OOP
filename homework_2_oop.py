def get_file_path(file_name):
    """
    Return the full file path of a file given its name.

    Args:
        file_name (str): Name of the file.
    """
    import os
    file_path = os.path.join(os.getcwd(), file_name)
    return file_path


def get_recipe_dictionary (file_path):
    """
    Read the recipes from a file and return a dictionary with recipes.
    Each recipe is represented as a key in the dictionary,
    and the value is a list of dictionaries, where each dictionary represents an ingredient.
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
        print(lines_list)
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
                    ingredient['quantity'] = lines_list[index].split('|')[1].strip()
                    ingredient['measure'] = lines_list[index].split('|')[2].strip()
                    cook_book[line].append(ingredient)
                    counter -= 1
                    index += 1
            print(cook_book)

print(get_file_path('recipe_book.txt'))
get_recipe_dictionary(get_file_path('recipe_book.txt'))