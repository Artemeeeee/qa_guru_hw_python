import os
from pathlib import Path

from selene import browser, by, have, command


#Пишу что-то подобное впервые, так же практически впервые работаю с вебом, не судите строго...
#Заполняю поля
def test_form_fill():
    browser.open('https://demoqa.com/automation-practice-form')

    browser.element('#firstName').type('Artem')
    browser.element('#lastName').type('Shmakov')
    browser.element('#userEmail').type('A.Shmakov@mail.ru')
    browser.element(by.text('Male')).click()
    browser.element('#userNumber').type('1234567890')
    browser.element('#subjectsInput').type('ma').press_enter()
    browser.element('#submit').perform(command.js.scroll_into_view)
    browser.element('label[for="hobbies-checkbox-1"]').click()       #не уверен
    #Картинка
    browser.element('#currentAddress').type('Улица колотушкина 10')

    #город и штат
    browser.element('#state').click()
    browser.element('#react-select-3-input').type('nc').press_enter()
    browser.element('#city').click()
    browser.element('#react-select-4-input').type('d').press_enter()


    #фото
    test_image_path = str(Path(__file__).parent.parent.joinpath('test_files', 'photo.jpg').resolve())
    browser.element('#uploadPicture').set_value(test_image_path)


    #блок даты рождения
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click().element(by.text('2003')).click()
    browser.element('.react-datepicker__month-select').click().element(by.text('January')).click()
    browser.element('.react-datepicker__day--028').click()

    browser.element('#submit').click()

    #проверки
    browser.all('.modal-body tr td:last-child').should(have.texts(
        'Artem Shmakov',
        'A.Shmakov@mail.ru',
        'Male',
        '1234567890',
        '28 January,2003',
        'Maths',
        'Sports',
        '',  # Picture - пустое
        'Улица колотушкина 10',
        'NCR Delhi'
    ))













