from phonebook import PhoneBook


class User:
    def __init__(self, name):
        self.name = name
        self.friends = []
        self.phone_books = {}

    def add_friend(self, friend):
        self.friends.append(friend)

    def remove_friend(self, friend):
        self.friends.remove(friend)

    def add_contact(self, contact, tag):
        if tag in self.phone_books:
            self.phone_books[tag].add_contact(contact)
        else:
            print(f"Нет телефонной книги с тегом '{tag}' для пользователя '{self.name}'")

    def remove_contact(self, contact, tag):
        if tag in self.phone_books:
            self.phone_books[tag].remove_contact(contact)
        else:
            print(f"Нет телефонной книги с тегом '{tag}' для пользователя '{self.name}'")

    def add_phone_book(self, tag):
        if tag not in self.phone_books:
            self.phone_books[tag] = PhoneBook(tag)
        else:
            raise ValueError(f"Данная телефонная книга {tag} уже существует")

    def share_phone_book(self, friend, tag):
        if friend in self.friends:
            if tag in self.phone_books:
                friend.phone_books[tag] = self.phone_books[tag]
            else:
                print(f"Нет телефонной книги с тегом '{tag}' для пользователя '{self.name}'")
        else:
            print(f"{friend.name} - не Ваш друг")
