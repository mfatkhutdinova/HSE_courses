import json
from programmer import search_moscow_programmers
import helpers

def collects_useful_information_in_vacancy(vacancy):
    useful_vacancy = {}
    useful_vacancy['profession'] = vacancy['profession']
    useful_vacancy['candidat'] = vacancy['candidat']
    useful_vacancy['payment_from'] = vacancy['payment_from'] # Сумма оклада от
    useful_vacancy['payment_to'] = vacancy['payment_to']     # Сумма оклада до
    return useful_vacancy

if __name__ == '__main__':
    vacancy_dict = helpers.get_object_from_file('programmers_vacancies.json')
    info_vacancies = [collects_useful_information_in_vacancy(vacancy) for vacancy in vacancy_dict]
    helpers.save_object_to_file(info_vacancies, 'useful_info_programmers.json')



