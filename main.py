from user import User
from contact import Contact
from admin import Admin

# Пример использования:
user1 = User("Алиса")
user2 = User("Влад")

user1.add_friend(user2)

user1.add_phone_book('family')
user2.add_phone_book('work')

contact1 = Contact(user1, '1', '123456789')
user1.add_contact(contact1, 'family')

admin = Admin("AdminUser")  # Admin user instance
admin.add_contact_to_phone_book(contact1, user2.phone_books['work'])

user1.share_phone_book(user2, 'family')

filtered_contacts = user2.phone_books['family'].filter_by_user(user1)
print(f"Контакты получены от {user1.name}: {[(contact.country_code, contact.phone_number) for contact in filtered_contacts]}")
