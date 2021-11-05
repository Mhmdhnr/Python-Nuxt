import names
from models.random_name import RandomNames


def get_random_name(count):
    names_list: list[RandomNames] = []
    for n in range(count):
        first_name = names.get_first_name()
        last_name = names.get_last_name()
        names_list.append(RandomNames(first_name, last_name))
    return names_list
