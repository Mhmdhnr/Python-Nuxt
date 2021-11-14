import names
from models.random_name import RandomNames, PersianFirstName, PersianLastName
import random

def get_random_english_name(count):
    names_list: list[RandomNames] = []
    for n in range(count):
        first_name = names.get_first_name()
        last_name = names.get_last_name()
        names_list.append(RandomNames(first_name, last_name))
    return names_list


def get_random_persian_name(count):
    names_list: list[RandomNames] = []
    persian_first_names = PersianFirstName.query.all()
    persian_last_names = PersianLastName.query.all()
    for n in range(count):
        r = random.randint(1, count)
        first_name = persian_first_names[r].first_name
        last_name = persian_last_names[r].last_name
        print(first_name + last_name)
        names_list.append(RandomNames(first_name, last_name))
    return names_list
