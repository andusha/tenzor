from .BaseApp import BasePage
from selenium.webdriver.common.by import By


class SbisSeacrhLocators:
    LOCATOR_SBIS_NAVIGATION_CONTACTS = (By.LINK_TEXT, "Контакты")
    LOCATOR_TENZOR_BANNER = (By.CLASS_NAME, "sbisru-Contacts__logo-tensor")
    LOCATOR_TENZOR_BLOCK = (By.CLASS_NAME, "tensor_ru-Index__block4-content")
    # LOCATOR_TENZOR_BLOCK_TITLE = (By.XPATH, "//p[contains(text(),'Сила в людях')]")
    LOCATOR_TENZOR_BLOCK_A = (By.LINK_TEXT, "Подробнее")
    LOCATOR_IMAGE_BLOCK = (By.CLASS_NAME, "tensor_ru-About__block3")
    LOCATOR_IMAGE_BLOCK_IMG = (By.TAG_NAME, "img")


class FirstScenarioSearchHelper(BasePage):

    def contacts_page(self):
        return self.find_element(
            SbisSeacrhLocators.LOCATOR_SBIS_NAVIGATION_CONTACTS, time=4
        ).click()

    def to_tenzor_site(self):
        return self.find_element(
            SbisSeacrhLocators.LOCATOR_TENZOR_BANNER, time=2
        ).click()

    def tenzor_main_page_block(self):
        return self.find_element(SbisSeacrhLocators.LOCATOR_TENZOR_BLOCK, time=10)

    def click_on_tenzor_main_page_block_a(self):
        block = self.tenzor_main_page_block()
        element = block.find_element(*SbisSeacrhLocators.LOCATOR_TENZOR_BLOCK_A)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        return element.click()

    def check_page_url(self):
        return self.driver.current_url

    def check_img_size(self):
        image_block = self.find_element(SbisSeacrhLocators.LOCATOR_IMAGE_BLOCK, time=3)
        images = image_block.find_elements(*SbisSeacrhLocators.LOCATOR_IMAGE_BLOCK_IMG)

        size = []
        for img in images:
            size.append((img.get_attribute("width"), img.get_attribute("height")))

        first_img_res = size[0]
        for res in size:
            if first_img_res != res:
                return False

        return True
