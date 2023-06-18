phone_book = {}
path: str = 'fons.txt'

def open_fail(): # поставили по умолчанию наш файл
    phone_book.clear()
    fail = open(path, 'r', encoding='UTF-8') #fail это сущность
    data = fail.readlines() # data - это куда мы будем считывать информацию
    fail.close()
    for contact in data:
        nc = contact.strip().split(':')
        phone_book[int(nc[0])] = ({'name': nc[1],'phone': nc[2], 'comment': nc[3]})
    print('\nТелефонная книга успешно загружена.')



def save_file():
    data = []
    for i, contact in phone_book.items():
        new = ':'.join([str(i), contact.get('name'),contact.get('phone'),contact.get('comment')])
        data.append(new)
    data = '\n'.join(data)
    with open(path, 'w', encoding= 'UTF-8') as file:
        file.write(data)
    print('\nТелефонная книга успешно сохранена.')
    print('=' * 100 + "\n")



def show_contacts(book: dict[int,dict]):
    print('\n' + '=' * 100)
    for i, cnt in book.items():
        print(f'{i:>3}. {cnt.get("name"):<20}{cnt.get("phone"):<20}{cnt.get("comment"):<20}')
    print('=' * 100 + "\n")

def add_contact():
    uid = max(list(phone_book.keys())) + 1
    name = input('Введите имя контакты: ')
    phone = input('Введите телефон контакта: ')
    comment = input('Введите комментарий к контакту: ')
    phone_book[uid] = {'name': name, 'phone': phone, 'comment': comment}

    print(f'\nКонтакт {name} успешно добавлен в телефонную книгу!')
    print('=' * 100 + "\n")


def search():
    result = {}
    count = 0
    word = input('Введите слово по которому будет осуществляться поиск: ').lower()
    for i, contact in phone_book.items():
        if word in ' '.join(list(contact.values())).lower():
            result[i] = contact
            count += 1
    if count == 0:
        print('='*100)
        print('='*100)
        print(f'В вашей телефонной книге нет ничего похожего на {word}')
    return result

def del_contact():
    result = search()
    show_contacts(result)
    if result != {}:
        index = int(input('Введите ID контакта, который хотим удалить: '))
        del_cnt = phone_book.pop(index)
        print(f'\nКонтакт {del_cnt.get("name")} успешно удален из телефонной книги!')
        print('=' * 100 + "\n")


def change_contact():
    result = search()
    show_contacts(result)
    if result != {}:
        index = int(input('Введите ID контакта, который хотим изменить: '))
        phone_book[index] = {'name': input('Внести изменения в поле имя: '), 'phone': input('Внести изменения в поле номер: '), 'comment': input('Внести изменения в комментарии: ')}


def menu() -> int:
    main_menu = '''Главное меню: 
    1. Открыть файл
    2. Сохранить файл
    3. Показать все контакты
    4. Создать контакт
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход'''
    print(main_menu)
    while True:
        select = input('Выберите пункт меню: ')
        if select.isdigit() and 0 < int(select) < 9:
            return int(select)
        else:
            print('Ошибка ввода, введите число от 1 до 8.')



open_fail()
while True:
    select = menu()
    match select:  # типо что у нас за селект? спрашиваем
        case 1:   # если 1, то делай этот код, если 2 то другой
            open_fail()
        case 2:
            save_file()
        case 3:
            show_contacts(phone_book)
        case 4:
            add_contact()
        case 5:
            result = search()
            show_contacts(result)
        case 6:
            change_contact()
        case 7:
            del_contact()
        case 8:
            print('До свидания! До новых встреч')
            break


