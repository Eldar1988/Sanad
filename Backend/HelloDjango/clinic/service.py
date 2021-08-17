import telebot


bot = telebot.TeleBot('1999402722:AAFtVFNUznpQWcQJkg3bglQ7M7iGk1IYVWM')
chat_id = '-1001244151686'


def send_tg_message(appoint):
    """Заявка на прием"""
    doctor = appoint.doctor or 'Не указан'
    name = appoint.name
    phone = appoint.phone
    comment = appoint.comment or ''

    message = '=====   Заявка на прием ===== \n\n' \
           f'Доктор: {doctor} \n' \
           f'Имя: {name} \n' \
           f'Телефон: +7 {phone} \n' \
           f'Комментарий: {comment} \n'

    try:
        bot.send_message(chat_id, message)

    except:
        return
