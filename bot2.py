def parse_input(user_input):
    """Розбиває введення користувача на команду та аргументи."""
    parts = user_input.strip().split()
    command = parts[0].lower()
    args = parts[1:]
    return command, args

def add_contact(args, contacts):
    """Додає новий контакт до словника."""
    if len(args) != 2:
        return "Неправильний формат. Введіть команду як: add [ім'я] [номер]"
    name, phone = args
    contacts[name] = phone
    return "Контакт додано."

def change_contact(args, contacts):
    """Змінює існуючий контакт у словнику."""
    if len(args) != 2:
        return "Неправильний формат. Введіть команду як: change [ім'я] [новий номер]"
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Контакт оновлено."
    else:
        return "Контакт не знайдено."

def show_phone(args, contacts):
    """Показує номер телефону за заданим ім'ям."""
    if len(args) != 1:
        return "Неправильний формат. Введіть команду як: phone [ім'я]"
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Контакт не знайдено."

def show_all(contacts):
    """Показує всі контакти."""
    if contacts:
        return '\n'.join([f'{name}: {phone}' for name, phone in contacts.items()])
    else:
        return "Контактів немає."

def handle_command(command, args, contacts):
    """Обробляє команду введену користувачем."""
    if command == "add":
        return add_contact(args, contacts)
    elif command == "change":
        return change_contact(args, contacts)
    elif command == "phone":
        return show_phone(args, contacts)
    elif command == "all":
        return show_all(contacts)
    elif command in ["exit", "close"]:
        return "exit"
    else:
        return "Невідома команда."

def main():
    """Основна функція, що управляє циклом запитів від користувача."""
    contacts = {}
    print("Ласкаво просимо до бота-асистента!")

    while True:
        user_input = input("Введіть команду: ")
        command, args = parse_input(user_input)
        response = handle_command(command, args, contacts)
        if response == "exit":
            print("До побачення!")
            break
        print(response)

if __name__ == "__main__":
    main()









def input_error(func):
    """Декоратор для обробки помилок введення користувача."""
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Контакт не знайдено."
        except ValueError as e:
            return str(e)
        except IndexError:
            return "Будь ласка, введіть правильні аргументи."
    return inner

@input_error
def add_contact(args, contacts):
    """Додає контакт, якщо отримано ім'я та номер."""
    if len(args) != 2:
        raise ValueError("Необхідно вказати ім'я та номер телефону.")
    name, phone = args
    contacts[name] = phone
    return "Контакт додано."

@input_error
def change_contact(args, contacts):
    """Змінює існуючий контакт у словнику."""
    if len(args) != 2:
        raise ValueError("Необхідно вказати ім'я та новий номер телефону.")
    name, new_phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = new_phone
    return "Контакт оновлено."

@input_error
def show_phone(args, contacts):
    """Виводить номер телефону за ім'ям."""
    if len(args) != 1:
        raise ValueError("Необхідно вказати ім'я для пошуку.")
    name = args[0]
    if name not in contacts:
        raise KeyError
    return contacts[name]

@input_error
def show_all(contacts):
    """Виводить всі контакти."""
    if not contacts:
        return "Контакти відсутні."
    return '\n'.join([f'{name}: {phone}' for name, phone in contacts.items()])

def handle_command(command, args, contacts):
    """Обробляє команду введену користувачем."""
    if command == "add":
        return add_contact(args, contacts)
    elif command == "change":
        return change_contact(args, contacts)
    elif command == "phone":
        return show_phone(args, contacts)
    elif command == "all":
        return show_all(contacts)
    elif command in ["exit", "close"]:
        return "exit"
    else:
        return "Невідома команда."

def main():
    """Основна функція, що управляє циклом запитів від користувача."""
    contacts = {}
    print("Ласкаво просимо до бота-асистента!")

    while True:
        user_input = input("Введіть команду: ")
        command, *args = parse_input(user_input)
        response = handle_command(command, args, contacts)
        if response == "exit":
            print("До побачення!")
            break
        print(response)

if __name__ == "__main__":
    main()
