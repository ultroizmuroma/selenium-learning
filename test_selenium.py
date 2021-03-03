from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())


def test_something():
    rosbank = go_to_page("https://www.rosbank-auto.ru/")
    assert rosbank[1] < 100

    go_to_page("https://www.gosuslugi.ru/")
    search_in_yandex("Поиск раз")
    search_in_yandex("Поиск два")


def go_to_page(url) -> list:
    browser.get(url)
    return calculate_for_page(url)


def search_in_yandex(search_string):
    go_to_page("https://yandex.ru")
    search_field = browser.find_element(By.ID, "text")
    search_field.send_keys(search_string)
    search_field.send_keys(Keys.RETURN)
    calculate_for_page(f"https://yandex.ru/ and {search_string}")


def calculate_for_page(url) -> list:
    navigation_start = browser.execute_script("return window.performance.timing.navigationStart")
    response_start = browser.execute_script("return window.performance.timing.responseStart")
    dom_complete = browser.execute_script("return window.performance.timing.domComplete")

    backend_performance_calc = response_start - navigation_start
    frontend_performance_calc = dom_complete - response_start

    print(f"{url}, Back End: %s" % backend_performance_calc)
    print(f"{url}, Front End: %s" % frontend_performance_calc)

    return [backend_performance_calc, frontend_performance_calc]