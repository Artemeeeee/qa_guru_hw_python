from python2_hw import get_correct_email, check_empty_fields, clean_body_text, create_email, add_send_date, \
     add_short_body, build_sent_text, extract_login_domain


#Часть B

def sender_email(recipient_list: list[str], subject: str, message: str, *, sender="default@study.com") -> list[dict]:
    if not recipient_list:
        return []
    # 2. Проверить корректность email отправителя и получателей
    correct_sender_list = get_correct_email([sender])
    correct_sender = correct_sender_list[0] if correct_sender_list else None
    correct_recipients = get_correct_email(recipient_list)
    if not correct_sender:
        return []

    # 3. Проверить пустоту темы и тела письма
    is_subject_empty, is_body_empty = check_empty_fields(subject, message)
    if is_subject_empty or is_body_empty:
        return []

    filtered_recipients = [recipient for recipient in correct_recipients if recipient != correct_sender]

    # 5. Нормализация данных
    clean_subject = subject.strip()
    clean_body = clean_body_text(message)
    emails: list[dict] = []
    #Создать письмо для каждого получателя
    for recipient in filtered_recipients:
        email = create_email(sender=correct_sender, recipient=recipient, subject=clean_subject, body=clean_body)
        #Добавить дату отправки
        email = add_send_date(email)
        email["date"] = email.pop("send_date")
        #8. Замаскировать email отправителя
        login, domain = extract_login_domain(email["sender"])
        email["masked_sender"] = login[:2] + "***@" + domain

        #9. Создать короткую версию тела письма
        email = add_short_body(email)
        email["shortnclean_body"] = clean_body
        #10. Сформировать итоговый текст письма
        temp_email = {
            "to": email["recipient"],
            "from": email["sender"],
            "subject": email["subject"],
            "date": email["date"],
            "clean_body": email["short_body"]
        }
        email["sent_text"] = build_sent_text(temp_email)

        emails.append(email)
    return emails

emails = sender_email(
    recipient_list=["@mail.ru", "name@.com""name@domain.comm"],
    subject="Hello!",
    message="Привет, коллега!",
    sender="default@study.com",
)

for q in emails:
    print(q["sent_text"])







