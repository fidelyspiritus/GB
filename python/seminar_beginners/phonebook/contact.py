import json

class Contact:
    def __init__(self, name, phone, birthday, email, adress):
        self.name = name
        self.phone_number = phone
        self.birthday = birthday
        self.mail = email
        self.adress = adress
#        Contact.print(self)
    
    def search(person, data):
        if data in person.name or data in person.phone_number:
            Contact.print(person)
            return True

    def print(self):
        print(f'ФИО: {self.name}, Телефонный номер: {self.phone_number}, Дата рождения: {self.birthday}, Почта: {self.mail}, Адрес: {self.adress}')

    def save(self):
        with open('Phone_book.json', "w", encoding = 'utf-8') as outfile:
            json.dump(self, outfile)
        print("Контакт сохранен")       
    
    def remove(self):
        pass
