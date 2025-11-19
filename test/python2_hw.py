#Взял грязное письмо из четвертого урока
from datetime import date
from time import strftime

email = {
    "subject": "Quarterly Report",
    "from": "Alice.Cooper@Company. ",
    "to": " bob_smith@Gmail.com ",
    "body": "Hello Bob,\n\tHere is the quarterly report.\n\tPlease review and let me know your feedback.\n\nBest,\nAlice",
    "date": "2025.11.16"
}


##Часть A. Функции
#1. Нормализация email адресов
def normalize_addresses(email: dict) -> dict:
    normalized_email = email.copy()
    normalized_email["from"] = normalized_email["from"].strip().lower()
    normalized_email["to"] = normalized_email["to"].strip().lower()
    return normalized_email

normalized_email = normalize_addresses(email)
#print(normalized_email)

#2. Сокращенная версия тела письма
def add_short_body(email: dict) -> dict:
    short_email = email.copy()
    short_email["short_body"] = short_email["body"][:10] + "..."
    return short_email
email_short = add_short_body(email)
#print(email_short)

#3. Очистка текста письма
def clean_body_text(body: str) -> str:
    body = body.replace("\n", " ")
    body = body.replace("\t", " ")
    return body
email["clean_body"] = clean_body_text(email["body"])
#print(clean_body_text(body=email["body"]))

#4. Формирование итогового текста письма

def build_sent_text(email: dict) -> str:
    beauty_email = f"Кому: {email['to']}, от: {email['from']} Тема: {email['subject']}, дата: {email['date']} {email['clean_body']}"
    return beauty_email
email["beauty body"] = build_sent_text(email)
#print(email["beauty body"])

#5. Проверка пустоты темы и тела
def check_empty_fields(subject: str, body: str) -> tuple[bool, bool]:
    is_subject_empty = not email["subject"].strip()
    is_body_empty = not email["clean_body"].strip()
    return is_subject_empty, is_body_empty
is_subject_empty, is_body_empty = check_empty_fields(email["subject"], email["body"])
#print("Пустая тема письма:", is_subject_empty)
#print("Пустое тело письма:", is_body_empty)

#6. Маска email отправителя

def mask_sender_email(email: dict) -> dict:
    email_copy = email.copy()
    login, domain = email["from"].strip().split('@')
    email_copy["from"] = login[:2] + "***@" + domain.strip()
    return email_copy

#masked = mask_sender_email(email)
#print(masked["from"])

#7. Проверка корректности email
def get_correct_email(email_list: list[str]) -> list[str]:
    correct_email_list = []
    valid_domains = ['.com', '.ru', '.net']
    for email in email_list:
        clean_email = email.strip().lower()
        if clean_email and '@' in clean_email:
            domain_part = clean_email.split('@')[1]
            if any(domain_part.endswith(domain) for domain in valid_domains):
                correct_email_list.append(clean_email)
    return correct_email_list

test_emails = [
    # Корректные адреса
    "user@gmail.com",
    "admin@company.ru",
    "test_123@service.net",
    "Example.User@domain.com",
    "default@study.com",
    " hello@corp.ru  ",
    "user@site.NET",
    "user@domain.coM",
    "user.name@domain.ru",
    "usergmail.com",
    "user@domain",
    "user@domain.org",
    "@mail.ru",
    "name@.com",
    "name@domain.comm",
    "",
    "   ",
    ]
#correct_list = get_correct_email(test_emails)
#print( correct_list)


#8. Создание словаря письма
def create_email(sender: str, recipient: str, subject: str, body: str) -> dict:
    auto_email = {
        "sender": sender,
        "recipient": recipient,
        "subject": subject,
        "body": body
    }
    return auto_email

#test_auto_email = create_email(sender="tema", recipient="ktoto", subject="Test Email", body="Test trst test")
#print(test_auto_email)


#9. Добавление даты отправки
def add_send_date(email: dict) -> dict:
    send_date = date.today().strftime("%Y-%m-%d")
    email["send_date"] = send_date
    return email

#email_with_date = add_send_date({'test_email': ''})
#print(email_with_date)

#10Получение логина и домена - разделяет email на логин и домен
def extract_login_domain(address: str) -> tuple[str, str]:
    login, domain = address.split('@')
    return login, domain
# parted = extract_login_domain(email["from"])
# print(parted)