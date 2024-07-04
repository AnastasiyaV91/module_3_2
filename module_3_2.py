sender = "university.help@gmail.com"  # Создаем глобальные переменные sender и recipient
recipient = "vasyok1337@gmail.com"


def send_email(a, b):                                                   # Создаем функцию send_email с двумя аргументами
    if "@" in recipient:                                                # Ищем @ в адресе получателя
        var = (".com",".ru",".net")                                     # Создаем список разрешенных окончаний
        if recipient.endswith(var):                                     # Ищем совпадение с именем получателя
            message1 = "Письмо успешно отправлено с адреса"
            print(f"{message1} {sender} на адрес {recipient}")          # Выводим сообщение об успешном отправлении
        else:
            message = "Невозможно отправить письмо"
            print(message)                                              # Сообщение об ошибке отправления

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
print()


def send_email(a, b, sender):                                           # Создаем функцию send_email с двумя аргументами
    if "gmail.com" not in b:                                            # Если в адресе не верно разрешенное окончание
        message1 = "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!"
        message2 = "Письмо успешно отправлено с адреса"
    print(f"{message1} {message2} {b} на адрес {sender}")               # Вывод сообщения в консоль


send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
print()


def send_email(a, b, sender):                                           # Создаем функцию send_email с двумя аргументами
    if ".ru" not in sender:                                             # Если окончание не нашли в адресе отправителя
        message = "Невозможно отправить письмо"                         # Выводим сообщение об ошибке в адресе
        print(f"{message} с адреса {sender} на адрес {b}")

send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
print()


def send_email(a, b, sender):                                           # Создаем функцию send_email с двумя аргументами
    if b == sender:                                                     # Сравниваем адрес получателя и отправителя
        message = "Нельзя отправить письмо самому себе!"                # Если адреса сравнились, то выводим сообщение об ошибке
        print(message)


send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
print()