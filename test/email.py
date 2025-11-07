from datetime import datetime

#1. Создайте словарь email
email = {
    "subject": "Quarterly Report",
    "from": "Alice.Cooper@Company. ",
    "to": " bob_smith@Gmail.com ",
    "body": "Hello Bob,\n\tHere is the quarterly report.\n\tPlease review and let me know your feedback.\n\nBest,\nAlice"
}


#2. Добавьте дату отправки
email["date"] = send_date = datetime.now().strftime("%Y-%m-%d")


#3. Нормализуйте e-mail адреса
email["from"] = email["from"].strip().lower()
email["to"] = email["to"].strip().lower()


#Извлеките логин и домен отправителя
login = email["from"].split("@")[0]
domain = email["from"].split("@")[1]


#5. Создайте сокращённую версию текста
sharped = email["body"][:10] + "..."
email["short_body"] = sharped
#print(email)


#6. Списки доменов
self_domains = ['gmail.com', 'list.ru', 'yahoo.com', 'outlook.com', 'hotmail.com', 'icloud.com', 'yandex.ru',
        'mail.ru','list.ru', 'bk.ru', 'inbox.ru']
corporate_domains = ['company.ru','corporation.com','university.edu','organization.org','company.ru', 'business.net']


#7. Проверьте что в списке личных и корпоративных доменов нет пересечений
self = list(set(self_domains))
corporate = list(set(corporate_domains))
test_inter = intersection = set(self) & set(corporate)
#print(test)                                                                    #--получаем 0, значит пересечений нет


#8. Проверьте «корпоративность» отправителя
is_corporate = domain in corporate_domains
#print(bool(is_corporate))                                                     #проверка корпоративности домена


#9. Соберите «чистый» текст сообщения
email["clean_body"] = clean_body = email["body"].replace("\n", " ").replace("\t", " ")


#10. Сформируйте текст отправленного письма
email["sent_text"] = f'''Кому: {email["to"]}, от: {email["from"]} 
Тема: {email["subject"]}, дата: {email["date"]} {email["clean_body"]}'''

#11. Рассчитайте количество страниц печати
pages = (len(email["sent_text"]) + 499) // 500


#12. Проверьте пустоту темы и тела письма
is_subject_empty = not bool(email["subject"])
is_body_empty = not bool(email["clean_body"])


#13. Создайте «маску» e-mail отправителя
email["masked_from"] = login[:2] + "***@" + domain


#14. Удалите из списка личных доменов значения "list.ru" и "bk.ru".
self_domains.remove("list.ru")
self_domains.remove("bk.ru")


print(email)
print(is_corporate, is_subject_empty, is_body_empty, pages)

