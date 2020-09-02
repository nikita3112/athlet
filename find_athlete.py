import datetime
from config import SQLite


db = SQLite('sochi_athletes.sqlite3')

def nearest_value_b_date(items, value):
    found = datetime.datetime.toordinal(datetime.datetime.strptime(items[0][2], '%Y-%m-%d'))
    for item in items:
        date = datetime.datetime.toordinal(datetime.datetime.strptime(item[2], '%Y-%m-%d'))
        if abs(date - value) < abs(found - value):
            found = date
            man = item
    return man

def nearest_value(items, value):
    found = items[0][4]
    for item in items:
        if item[4] is not None:
            height = item[4]
            if abs(height - value) < abs(found - value):
                found = height
                man = item
    return man

def printl(header, text):
    print('=' * 100)
    print(f'{header}')
    print(
        f'ID: {text[0]}\n'
        f'AGE: {text[1]}\n'
        f'Birthdate: {text[2]}\n'
        f'Gender: {text[3]}\n'
        f'Height: {text[4]}\n'
        f'Name: {text[5]}\n'
        f'Weight: {text[6]}\n'
        f'Gold_medals: {text[7]}\n'
        f'Silver_medals: {text[8]}\n'
        f'Bronze_medals: {text[9]}\n'
        f'Total_medals: {text[10]}\n'
        f'Sport: {text[11]}\n'
        f'Country: {text[12]}\n'
    )

def main():
    user_id = input('Введите id пользователя: ')
    if db.find_id(user_id=user_id):
        item = db.get_set(user_id=user_id)
        b_date = datetime.datetime.toordinal(datetime.datetime.strptime(item[0], '%Y-%m-%d'))
        height = item[1]
        printl('По дате рождения', nearest_value_b_date(db.find_athlete(), b_date))
        printl('По росту', nearest_value(db.find_athlete(), height))
    else:
        print('Такого пользователя нет')

if __name__ == "__main__":
    main()