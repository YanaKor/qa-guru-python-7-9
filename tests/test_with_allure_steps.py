import allure
from selene import browser, by, have, be


@allure.step('Открытие главной страницы')
def open_main_page():
    browser.open('/')


@allure.step('Поиск репозитория по названию: {repo_name}')
def search_repo_by_name(repo_name):
    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').type(repo_name).press_enter()


@allure.step('Переход в репозиторий по ссылке с названием {repo_name}')
def go_to_repo(repo_name):
    browser.element(by.link_text(repo_name)).click()


@allure.step('Открытие вкладки "Issues')
def go_to_issue_tab():
    browser.element('#issues-tab').click()


@allure.step('Проверка наличия задачи с номером {number} на вкладке')
def check_issue_with_number(number):
    browser.all('[aria-label=Issues][role=group]').element_by(have.text(number)).should(be.visible)


@allure.title('Проверка наличия названия Issue в репозитории')
def test_with_allure_steps():
    open_main_page()
    search_repo_by_name('eroshenkoam/allure-example')
    go_to_repo('eroshenkoam/allure-example')
    go_to_issue_tab()
    check_issue_with_number('#80')
