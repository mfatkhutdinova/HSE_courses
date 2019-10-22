import sqlite3
from random import randint
from helpers import delete_punctuations

KEYS = ['имя', 'фамилия', 'возраст', 'должность', 'компания', 'знакомство']
DB_PATH = r"users.db"


def create_db() -> None:
    session = sqlite3.connect(DB_PATH)
    cursor = session.cursor()
    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT,"
                   "chat_id INT , firstName VARCHAR(100), "
                   "secondName VARCHAR(30), Age INT, "
                   "Position VARCHAR(100), Company VARCHAR(100), "
                   "Meet VARCHAR(200))")
    session.commit()
    session.close()


def edit_user(user_data: dict):
    session = sqlite3.connect(DB_PATH)

    for key in KEYS:
        if key not in user_data:
            user_data[key] = None

    with session:
        cursor = session.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()

        user_id = None
        for row in rows:
            user_id = row[0]
            if user_data['chat_id'] == row[1]:
                cursor.execute(
                    "UPDATE users SET firstName = ?, secondName = ?, Age = ?, "
                    "Position = ?, Company = ?, Meet = ? WHERE id = ?",
                    (user_data[KEYS[0]], user_data[KEYS[1]],
                     user_data[KEYS[2]], user_data[KEYS[3]],
                     user_data[KEYS[4]], user_data[KEYS[5]], user_id))
                break
            else:
                user_id = None

    session.commit()
    cursor.close()
    session.close()
    if user_id:
        return user_id


def add_user(user_data):
    is_user_id = edit_user(user_data)

    if is_user_id:
        return read_from_db(is_user_id, user_data[KEYS[-1]])

    session = sqlite3.connect(DB_PATH)
    cursor = session.cursor()

    # @TODO: add validation
    for key in KEYS:
        if key not in user_data:
            user_data[key] = None

    cursor.execute(
        f"INSERT INTO users (id, chat_id, firstName, secondName, Age, "
        f"Position, Company, Meet) VALUES(NULL, '{user_data['chat_id']}', "
        f"{user_data[KEYS[0]]}', '{user_data[KEYS[1]]}', "
        f"{user_data[KEYS[2]]}', '{user_data[KEYS[3]]}', "
        f"{user_data[KEYS[4]]}', '{user_data[KEYS[5]]}')")
    cursor.execute("SELECT last_insert_rowid()")
    user_id = cursor.fetchall()[0][0]

    session.commit()
    cursor.close()
    session.close()
    return read_from_db(user_id, user_data[KEYS[-1]])


def delete_current_user(id, data_from_db):
    index = 0
    for data_dict in data_from_db:
        if str(data_dict['id']) == str(id):
            data_from_db.pop(index)
            break
        index += 1

    return data_from_db


def delete_id_and_none(data_from_db, keys):
    for data in data_from_db:
        data.pop('id')
        data.pop('chat_id')

        for key in keys:
            if data[key] == "None":
                data.pop(key)

    return data_from_db


def create_random_users(data_from_db):
    random_users = []

    if len(data_from_db) > 3:
        while len(random_users) < 3:
            data = data_from_db[randint(0, len(data_from_db) - 1)]
            if data not in random_users:
                random_users.append(data)
    else:
        for data in data_from_db:
            random_users.append(data)

    return random_users


def read_from_db(id, meet):
    meet_user = delete_punctuations(meet).lower().split()
    if not meet_user:
        return "К сожалению, мы ничего не можем Вам предложить"

    session = sqlite3.connect(DB_PATH)
    keys = ['id', 'chat_id']
    keys.extend(KEYS)

    with session:
        cursor = session.cursor()
        cursor.execute("SELECT id, chat_id, firstName, secondName, Age, "
                       "Position, Company, Meet FROM users")
        rows = cursor.fetchall()

        data_from_db = []
        for row in rows:
            for one_user_data in row:
                one_user_data = delete_punctuations(str(one_user_data)).split()

                for user_info in one_user_data:
                    if user_info.lower() in meet_user:
                        data_from_db.append(dict(zip(keys, row)))
                        break

        data_from_db = delete_current_user(id, data_from_db)

        if not data_from_db:
            return 'К сожалению, мы ничего не можем Вам предложить.'

        random_users = create_random_users(data_from_db)

        random_users = delete_id_and_none(random_users, keys)

    cursor.close()
    session.close()

    return random_users


if __name__ == '__main__':
    create_db()
