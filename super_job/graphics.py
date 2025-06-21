import matplotlib.pyplot as plt

def draws_the_dependence_of_the_salary_of_programming_language(avarage_salary_with_language):
    avarage_salary = [language['salary'] for language in avarage_salary_with_language]
    number_language = []

    for number in range(len(avarage_salary)):
        number_language.append(number)

    name_languages = [language['language'] for language in avarage_salary_with_language]

    plt.bar(number_language, avarage_salary, color = 'blue', width = 0.9, align='center')
    plt.xticks(number_language, name_languages)
    plt.show()
