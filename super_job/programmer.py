from superJob_api import make_superjob_request
import helpers

def search_moscow_programmers():
    catalogue_id_development = 48
    town_id_Moscow = 4
    keyword = 'Программист'
    count = 100
    param = {'town': town_id_Moscow, 'catalogues': catalogue_id_development, 'keyword': keyword, 'count': 100}
    return make_superjob_request('vacancies/', param)


if __name__ == '__main__':
    response = search_moscow_programmers()
    vacancies = response['objects']
    helpers.save_object_to_file(vacancies, 'programmers_vacancies.json')

