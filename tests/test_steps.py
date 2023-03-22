import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

URL_GITHUB = 'https://github.com'
REPO_NAME = 'wombatoff/qa_guru_python_4_9'
ISSUE_NUMBER = '#1'


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'wombatoff')
@allure.feature(f'Проверка наличия Issue {ISSUE_NUMBER} на github')
@allure.story('Лямбда шаги через with allure.step')
@allure.link(URL_GITHUB, name='Testing')
def test_search_github_issue():
    with allure.step('Открываем главную страницу'):
        browser.open(URL_GITHUB)

    with allure.step(f'Поиск репозитория {REPO_NAME}'):
        s('.header-search-input').click()
        s('.header-search-input').send_keys(REPO_NAME)
        s('.header-search-input').submit()

    with allure.step(f'Переход по ссылке репозитория {REPO_NAME}'):
        s(by.link_text(REPO_NAME)).click()

    with allure.step('Открытие tab Issues'):
        s('#issues-tab').click()

    with allure.step(f'Проверка наличие Issue с номером {ISSUE_NUMBER}'):
        s(by.partial_text(ISSUE_NUMBER)).should(be.visible)

    browser.quit()
