from selene import browser, by, have, be


def test_issues():
    browser.open('/')

    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').type('eroshenkoam/allure-example').press_enter()
    browser.element(by.link_text('eroshenkoam/allure-example')).click()
    browser.element('#issues-tab').click()

    browser.all('[aria-label=Issues][role=group]').element_by(
        have.text('#80')
    ).should(be.visible)

