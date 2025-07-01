from handlers.is_valid_phone import is_valid_phone
from handlers.input_error import input_error

@input_error
def change_contact(args, contacts):
    name, phone = args
    if not is_valid_phone(phone):
        return "❌ Invalid phone number. Use only digits, 10–15 characters. May start with '+'❌"
    if name in contacts:
        contacts[name] = phone
        return f"🔁 Contact '{name}' updated with new phone 📞 {phone}"
    else:
        return "Contact not found 😭"
