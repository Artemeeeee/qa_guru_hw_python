from selene import browser, have
from selene.core.condition import Condition


def test_visible_after_5_seconds_text_selene_v2():

    browser.open('https://www.tutorialspoint.com/selenium/practice/dynamic-prop.php')
    browser.element('#colorChange').click()
    browser.element('#visibleAfter').with_(timeout=browser.config.timeout * 2).should(Condition.by_and(
        have.text('Visible'),
        (have.text('5 Seconds')
         )
    )
    )
