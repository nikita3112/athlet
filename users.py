import uuid
from config import SQLite


db = SQLite('sochi_athletes.sqlite3')

def main():
    print('Введите ваши данные')
    ids = []
    if db.get_ids():
        for i in db.get_ids():
            ids.append(i[0])
        user_id = max(ids) + 1
    else:
        user_id = 1
    name = input('Ваше имя: ')
    surname = input('Ваша фамилия: ')
    gender = input('Ваш пол (Male/Female): ')
    email = input('Ваш email: ')
    b_date = input('Ваша дата рождения (в формате гггг-мм-дд): ')
    height = input('Ваш рост: ')
    db.add_user(user_id=user_id, name=name, surname=surname, gender=gender, email=email, b_date=b_date, height=height)

if __name__ == "__main__":
    main()