import json
from contact import Contact

# with open('Phone_book.json', "r") as outfile:
#     Phone_book = json.load(outfile)

commands = {'/help': 'Покажи все команды', '/add': 'Добавить контакт', '/search': 'Поиск по контактам', '/remove': 'Удалить контакт', '/show': 'Показать все контакты', '/quit': 'Закрыть книгу'}

print('Добро пожаловать в телефонную книгу!')
print('Введите одну из представленных ниже команд для работы:')
[print(f'{key} - {value}') for key, value in commands.items()]

Phone_book = []
Phone_book.append(Contact('Зоя', '+77863546', '21/10/2000', 'dfgh@sg.ru', '190000 SPb'))
Phone_book.append(Contact('Клава', '546', '14/10/2000', 'spb@sg.ru', '190000 SPb'))

command = input('Введите искомую команду: ')

while(command != '/quit'):
    if command == '/help':
        [print(f'{key} - {value}') for key, value in commands.items()]

    elif command == '/add':
        print('Введите нужную информацию о контакте')
        name = input('Введите имя контакта: ')
        phone = input('Введите телефонный номер контакта: ')
        birthday = input('Введите дату рождения контакта: ') 
        email = input('Введите почту контакта: ')
        adress = input('Введите адрес контакта: ')

        Phone_book.append(Contact(name, phone, birthday, email, adress))
#        Contact.save(name, phone, birthday, email, adress)

    elif command == '/search':
        data = input('Введите данные для поиска: ')
        for person in Phone_book:
            Contact.search(person, data)

    elif command == '/remove':
        rm = input('Введите данные для удаления: ')
        for person in Phone_book:
            flag = Contact.search(person, rm)
            if flag == True:
                answer = input('Вы хотите удалить этого человека? Yes/No ')
                if answer.lower() == 'yes':
                    Phone_book.remove(person)
                    break

    elif command == '/show':
         for person in Phone_book:
            Contact.print(person)   

    else:
        print('Введите одну из представленных ниже команд для работы:')
        [print(f'{key} - {value}') for key, value in commands.items()]
        
    command = input('Введите искомую команду: ')