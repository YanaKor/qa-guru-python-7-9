import allure
from selene import browser, by, have, be


def test_issues_with_dynamic_steps():
    with allure.step('Открытие главной страницы'):
        browser.open('/')

    with allure.step('Поиск репозитория по названию: eroshenkoam/allure-example'):
        browser.element('.header-search-button').click()
        browser.element('#query-builder-test').type('eroshenkoam/allure-example').press_enter()

    with allure.step('Переход в репозиторий по ссылке'):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Открытие вкладки "Issues"'):
        browser.element('#issues-tab').click()

    with allure.step('Проверка наличия задачи с номером 80 на вкладке'):
        browser.all('[aria-label=Issues][role=group]').element_by(have.text('#80')).should(be.visible)

