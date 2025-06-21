import json
from helpers import get_object_from_file
import graphics

def translate_languages_in_ru(ru_string):
    return ru_string.replace('си', 'c')\
                    .replace('си шарп', 'c#') \
                    .replace('питон', 'python') \
                    .replace('джава', 'java') \
                    .replace('джаваскрипт', 'javascript') \
                    .replace('паскаль', 'pascal') \
                    .replace('1с', '1c') \
                    .replace('пхп', 'php')

def count_average_salary(languages_list):
    useful_languages_list = []

    for language in languages_list:
        if language['count'] != 0:
            language['salary'] /= language['count']
            useful_languages_list.append(language)

    return useful_languages_list

def count_number_languages_and_average_salary(useful_vacancy_dict):
    languages_with_salary_and_count = [{'language':'C++', 'salary':0, 'count': 0},
                                       {'language':'C', 'salary':0, 'count': 0},
                                       {'language':'C#', 'salary':0, 'count': 0},
                                       {'language':'PHP', 'salary':0, 'count': 0},
                                       {'language':'Python', 'salary':0, 'count': 0},
                                       {'language':'Swift', 'salary':0, 'count': 0},
                                       {'language':'Java', 'salary':0, 'count': 0},
                                       {'language':'1C', 'salary':0, 'count': 0},
                                       {'language':'JavaScript', 'salary':0, 'count': 0},
                                       {'language':'Ruby', 'salary':0, 'count': 0},
                                       {'language':'Delphi', 'salary': 0, 'count': 0}]

    for elem_vacancy in useful_vacancy_dict:
        for elem_langueges in languages_with_salary_and_count:

            if elem_langueges['language'].lower() in elem_vacancy['profession'].lower()\
                    or translate_languages_in_ru(elem_langueges['language'].lower()) in elem_vacancy['profession'].lower():

                if (elem_vacancy['payment_from'] != 0 and elem_vacancy['payment_to'] == 0)\
                        or (elem_vacancy['payment_from'] == 0 and elem_vacancy['payment_to'] != 0):

                    elem_langueges['count'] += 1
                    if elem_vacancy['payment_to'] == 0:
                        elem_langueges['salary'] += elem_vacancy['payment_from']
                    else:
                        elem_langueges['salary'] += elem_vacancy['payment_to']

    languages_list = count_average_salary(languages_with_salary_and_count)
    return languages_list

if __name__ == '__main__':
    useful_vacancy = get_object_from_file('useful_info_programmers.json')
    languages_list = count_number_languages_and_average_salary(useful_vacancy)
    graphics.draws_the_dependence_of_the_salary_of_programming_language(languages_list)





