from user import User


class Admin(User):
    def __init__(self, name):
        super().__init__(name)

    @staticmethod
    def add_contact_to_phone_book(contact, phone_book):
        phone_book.add_contact(contact)

    @staticmethod
    def remove_contact_from_phone_book(contact, phone_book):
        phone_book.remove_contact(contact)
