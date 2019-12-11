import random
import string
from time import sleep, time

from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from css_selectors import Selectors

BASE_URL = 'http://automationpractice.com/index.php'


def create_address(d):
    address_name = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])

    link_addresses = d.find_element_by_css_selector(Selectors.LINK_ADDRESSES)
    link_addresses.click()

    link_add_address = d.find_element_by_css_selector(Selectors.LINK_ADD_ADDRESS)
    link_add_address.click()

    input_firstname = d.find_element_by_css_selector(Selectors.INPUT_FIRSTNAME)
    input_lastname = d.find_element_by_css_selector(Selectors.INPUT_LASTNAME)
    input_company = d.find_element_by_css_selector(Selectors.INPUT_COMPANY)
    input_address1 = d.find_element_by_css_selector(Selectors.INPUT_ADDRESS1)
    input_address2 = d.find_element_by_css_selector(Selectors.INPUT_ADDRESS2)
    input_city = d.find_element_by_css_selector(Selectors.INPUT_CITY)
    input_state = Select(d.find_element_by_css_selector(Selectors.INPUT_STATE))
    input_postcode = d.find_element_by_css_selector(Selectors.INPUT_POSTCODE)
    input_country = Select(d.find_element_by_css_selector(Selectors.INPUT_COUNTRY))
    input_phone = d.find_element_by_css_selector(Selectors.INPUT_PHONE)
    input_phone_mobile = d.find_element_by_css_selector(Selectors.INPUT_MOBILE_PHONE)
    input_other = d.find_element_by_css_selector(Selectors.INPUT_OTHER)
    input_alias = d.find_element_by_css_selector(Selectors.INPUT_ALIAS)
    button_submit = d.find_element_by_css_selector(Selectors.BUTTON_SUBMIT)

    input_firstname.clear()
    input_firstname.send_keys('John')
    input_lastname.clear()
    input_lastname.send_keys('Doe')
    input_company.send_keys('Google Inc.')
    input_address1.send_keys('1010 Rainbow Road')
    input_address2.send_keys('Apt 6')
    input_city.send_keys('Durango')
    input_state.select_by_value('1')
    input_postcode.send_keys('81301')
    input_country.select_by_value('21')
    input_phone.send_keys('970-317-8234')
    input_phone_mobile.send_keys('970-317-1231')
    input_other.send_keys('test test')
    input_alias.clear()
    input_alias.send_keys(address_name)
    button_submit.click()


if __name__ == '__main__':
    display = Display(visible=1, size=(1920, 1080))
    display.start()
    options = Options()
    options.headless = False
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)
    driver.set_window_position(0, 0)

    try:
        driver.get(BASE_URL)

        link_login = driver.find_element_by_css_selector(Selectors.LINK_LOGIN)
        link_login.click()

        input_email = driver.find_element_by_css_selector(Selectors.INPUT_EMAIL)
        input_password = driver.find_element_by_css_selector(Selectors.INPUT_PASSWORD)

        input_email.send_keys('fake-test@gmail.com')
        input_password.send_keys('password12345')
        input_password.send_keys(Keys.ENTER)

        create_address(driver)

        link_women = driver.find_element_by_css_selector(Selectors.LINK_WOMEN)
        ActionChains(driver).move_to_element(link_women).perform()
        link_summer_dresses = driver.find_element_by_css_selector(Selectors.LINK_SUMMER_DRESSES)
        link_summer_dresses.click()

        link_list = driver.find_element_by_css_selector(Selectors.LINK_LIST)
        link_list.click()

        items = driver.find_elements_by_css_selector(Selectors.LIST_ITEMS)
        item_urls = [item.get_attribute('href') for item in items]
        for url in item_urls:
            driver.get(url)
            driver.implicitly_wait(2)

            input_quantity = driver.find_element_by_css_selector(Selectors.INPUT_QUANTITY)
            input_size = Select(driver.find_element_by_css_selector(Selectors.INPUT_SIZE))
            input_quantity.clear()
            input_quantity.send_keys('5')
            input_size.select_by_visible_text('L')

            link_color = driver.find_element_by_css_selector(Selectors.LINK_COLOR)
            button_add_to_cart = driver.find_element_by_css_selector(Selectors.BUTTON_ADD_TO_CART)
            link_color.click()
            button_add_to_cart.click()

            driver.implicitly_wait(3)
            button_continue = driver.find_element_by_css_selector(Selectors.BUTTON_CONTINUE)
            button_continue.click()

        link_cart = driver.find_element_by_css_selector(Selectors.LINK_CART)
        ActionChains(driver).move_to_element(link_cart).perform()
        link_checkout = driver.find_element_by_css_selector(Selectors.LINK_CHECKOUT)
        link_checkout.click()

        link_proceed_checkout = driver.find_element_by_css_selector(Selectors.LINK_PROCEED_CHECKOUT)
        link_proceed_checkout.click()

        link_proceed_checkout2 = driver.find_element_by_css_selector(Selectors.LINK_PROCEED_CHECKOUT2)
        link_proceed_checkout2.click()

        input_tos = driver.find_element_by_css_selector(Selectors.INPUT_TOS)
        link_proceed_checkout2 = driver.find_element_by_css_selector(Selectors.LINK_PROCEED_CHECKOUT2)
        input_tos.click()
        link_proceed_checkout2.click()

        link_bankwire = driver.find_element_by_css_selector(Selectors.LINK_BANKWIRE)
        link_bankwire.click()

        button_confirm_order = driver.find_element_by_css_selector(Selectors.BUTTON_CONFIRM_ORDER)
        button_confirm_order.click()

        link_account = driver.find_element_by_css_selector(Selectors.LINK_ACCOUNT)
        link_account.click()

        link_orders = driver.find_element_by_css_selector(Selectors.LINK_ORDERS)
        link_orders.click()

        driver.implicitly_wait(3)
        driver.save_screenshot('./screenshots/{}.png'.format(int(time())))

        link_logout = driver.find_element_by_css_selector(Selectors.LINK_LOGOUT)
        link_logout.click()
        sleep(3)

        driver.quit()
        display.stop()
    except Exception as e:
        driver.quit()
        display.stop()
        raise e
