def send_email(a, b, *, sender="university.help@gmail.com"):               # Создаем принимающую функцию
    recipient = b                                                          # Присваиваем значение b пересенной recipient
    m1 = 'Невозможно отправить письмо с адреса '                           #
    m2 = 'Письмо успешно отправлено с адреса '                             # Создаем перечень сообщений для вывода
    m3 = 'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! '                                     # в консоль
    m4 = 'Письмо отправлено с адреса '                                     #

    if "@" not in sender or not sender.endswith((".com", ".ru", ".net")):        # Проверяем правильность адреса
                                                                                 # отправителя
        print(f"{m1} {sender} на адрес {recipient}")                           # Если адрес верный,
        return                                                                   # выходим из функции
    if "@" not in recipient or not recipient.endswith((".com", ".ru", ".net")):  # Проверяем правильность адреса
        print(f"{m1} {sender} на адрес {recipient}")                             # получателя. Если адрес верный,
        return                                                                   # выходим из функции

    if sender == recipient:                                       # Проверяем совпадение адреса отправителя и получателя
        print("Нельзя отправить письмо самому себе!")             # При совпадении адресов выводим сообщение и
        return                                                    # выходим из функции

    if sender == "university.help@gmail.com":                     # Если адрес отправителя по умолчанию совпадает
                                                                  # с адресом university.help@gmail.com
        print(f"{m2} {sender} на адрес {recipient}")              # Выводим сообщение m2
    else:
        print(f"{m3} {m4} {sender} на адрес {recipient}")         # Если адреса не совпали выводим сообщения m3 и m4


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
