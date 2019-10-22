from helpers import get_object_from_file

def get_recommendations(user_film, films_dict):
    list_film = []
    genres_user = ''

    for name_film in films_dict:
        if name_film["original_title"].lower() == user_film.lower():
            genres_user = name_film["genres"]
            break
    if not genres_user:
        return ('The film is not found!')

    for film in films_dict:
        film_name = film["original_title"]
        genres = film["genres"]

        for elem_genres in genres:
            for elem_genres_user in genres_user:
                if (elem_genres['name'] == elem_genres_user['name']):
                    production_countries = film['production_countries']
                    if (name_film["production_countries"] == production_countries):
                        list_film.append(film_name)

    if not list_film:
        return("No recommendations")
    else:
        return (list_film)

if __name__ == '__main__':
    print("Enter for your film:")
    user_film = input()
    films_dict = get_object_from_file('films_2.json')
    print(get_recommendations(user_film, films_dict))
