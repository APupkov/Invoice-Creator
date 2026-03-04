import smtplib
from email.message import EmailMessage

def send_email_gmail(sender_email, sender_password, recipient_email, subject, body):
    """
    Отправляет электронное письмо через SMTP-сервер Gmail.

    :param sender_email: Адрес отправителя (почта Gmail)
    :param sender_password: Пароль или пароль приложения Gmail
    :param recipient_email: Адрес получателя
    :param subject: Заголовок письма
    :param body: Текст письма
    """
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, sender_password)
        server.send_message(msg)

# Пример использования:
sender_email = "your_email@gmail.com"
sender_password = "your_gmail_app_password_or_account_password"
recipient_email = "receiver@example.com"
subject = "Тестовая тема письма"
body = "Привет!\n\nЭто тестовое письмо."

send_email_gmail(sender_email, sender_password, recipient_email, subject, body)