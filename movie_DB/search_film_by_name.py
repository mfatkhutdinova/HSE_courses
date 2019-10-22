from helpers import get_object_from_file

def search_by_name(user_film):
    films_dict = get_object_from_file('films_2.json')
    user_film = user_film.lower()
    films_list = []

    for film in films_dict:
        name_films = (film["original_title"]).lower()
        if name_films.find(user_film) > -1:
            films_list.append(name_films)
    if not films_list:
        return ("At Your request, nothing found")
    else:
        return (films_list)

if __name__ == '__main__':
    print("Enter the word from the title You are interested in film:")
    name_film = input()
    result_of_search = search_by_name(name_film)
    print(result_of_search)
