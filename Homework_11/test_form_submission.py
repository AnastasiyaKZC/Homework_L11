import allure
from selene import browser, have, be, command

@allure.title("done")
def test_fill_form(setup_browser):
    browser = setup_browser  # Явно передаём фикстурный браузер

    with allure.step("open"):
        browser.open("https://demoqa.com/automation-practice-form")
        browser.element("#firstName").type("Анастасия")
        browser.element("#lastName").type("Кузнецова")
        browser.element("#userEmail").type("kuznetsova@mail.com")

    with allure.step("state"):
        browser.element('[for="gender-radio-2"]').click()

    with allure.step("tel_number"):
        browser.element("#userNumber").type("1234567890")

    with allure.step("date"):
        browser.element("#dateOfBirthInput").click()
        browser.element(".react-datepicker__year-select").type("1984")
        browser.element(".react-datepicker__month-select").type("May")
        browser.element(".react-datepicker__day--009").click()

    with allure.step("pred"):
        browser.element("#subjectsInput").type("Math").press_enter() #тут повозилась - не знала, что это выпадашка, пыталась ввести свой текст

    with allure.step("hobbies"):
        browser.element('[for="hobbies-checkbox-2"]').click()

    with allure.step("picture"):
        browser.element("#uploadPicture").send_keys("/Users/kuznetsova/Desktop/download.jpg")

    with allure.step("adress"):
        browser.element("#currentAddress").type("Ростов-на-Дону, ул.Города Волос")

    with allure.step("statee"):
        browser.element("#state").perform(command.js.scroll_into_view).click() # скролл к элементу
        browser.element("#state").should(be.clickable).click() # задержка до появления списка
        browser.element("#state").click()
        browser.all("div.css-11unzgr").element_by(have.text("Haryana")).click()

    with allure.step("list"):
        browser.element("#city").should(be.clickable).click() # задержка до появления списка
        browser.all("div.css-11unzgr").element_by(have.text("Karnal")).click()

    with allure.step("form"):
        browser.element("#submit").press_enter()

    with allure.step("should"):
        browser.element(".modal-title").should(have.text("Thanks for submitting the form"))