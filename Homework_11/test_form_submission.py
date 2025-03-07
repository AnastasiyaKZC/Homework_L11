from selene import browser, have, be, command


def test_fill_form():
    # Заполняю личные данные
    browser.open("https://demoqa.com/automation-practice-form")
    browser.element("#firstName").type("Анастасия")
    browser.element("#lastName").type("Кузнецова")
    browser.element("#userEmail").type("kuznetsova@mail.com")

    # Выбираю пол
    browser.element('[for="gender-radio-2"]').click()

    # Ввожу номер телефона
    browser.element("#userNumber").type("1234567890")

    # Выбираю дату рождения
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__year-select").type("1984")
    browser.element(".react-datepicker__month-select").type("May")
    browser.element(".react-datepicker__day--009").click()

    # Ввожу предметы
    browser.element("#subjectsInput").type("Math").press_enter() #тут повозилась - не знала, что это выпадашка, пыталась ввести свой текст

    # Выбираю хобби
    browser.element('[for="hobbies-checkbox-2"]').click()

    # Загружаю изображение
    browser.element("#uploadPicture").send_keys("/Users/kuznetsova/Desktop/download.jpg")

    # Вводим текущий адрес
    browser.element("#currentAddress").type("Ростов-на-Дону, ул.Города Волос")

    # Выбираем штат
    browser.element("#state").perform(command.js.scroll_into_view).click() # скролл к элементу
    browser.element("#state").should(be.clickable).click() # задержка до появления списка
    browser.element("#state").click()
    browser.all("div.css-11unzgr").element_by(have.text("Haryana")).click()

    # Дожидаемся загрузки списка городов
    browser.element("#city").should(be.clickable).click() # задержка до появления списка
    browser.all("div.css-11unzgr").element_by(have.text("Karnal")).click()

    # Отправляем форму
    browser.element("#submit").press_enter()

    # Проверяем, что форма отправлена (например, через проверку заголовка или успешного сообщения)
    browser.element(".modal-title").should(have.text("Thanks for submitting the form"))