from .BaseApp import BasePage
from selenium.webdriver.common.by import By


class SbisSeacrhLocators:
    LOCATOR_SBIS_NAVIGATION_CONTACTS = (By.LINK_TEXT, "Контакты")
    LOCATOR_CURRENT_REGION = (By.CLASS_NAME, "sbis_ru-Region-Chooser__text")
    LOCATOR_REGION_PARTNERS = (By.CLASS_NAME, "sbisru-Contacts-List__item")
    # LOCATOR_TENZOR_BLOCK_TITLE = (By.XPATH, "//p[contains(text(),'Сила в людях')]")
    LOCATOR_MODAL = (By.XPATH, "//span[@title='Камчатский край']")
    LOCATOR_IMAGE_BLOCK = (By.CLASS_NAME, "tensor_ru-About__block3")
    LOCATOR_IMAGE_BLOCK_IMG = (By.TAG_NAME, "img")


class SecondScenarioSearchHelper(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.partners = []

    def contacts_page(self):
        return self.find_element(
            SbisSeacrhLocators.LOCATOR_SBIS_NAVIGATION_CONTACTS, time=4
        ).click()

    def current_region(self):
        return self.find_element(SbisSeacrhLocators.LOCATOR_CURRENT_REGION, time=5)
    
    def region_partners(self):
        return self.find_elements(
            SbisSeacrhLocators.LOCATOR_REGION_PARTNERS, time=2
        )

    def add_region_partners(self):
        self.partners = self.region_partners()

    def check_region_partners(self):
        return len(self.partners) > 0

    def click_on_region_chooser(self):
        return self.current_region().click()

    def click_in_modal(self):
        return self.find_element(SbisSeacrhLocators.LOCATOR_MODAL, time=2).click()

    def page_url(self):
        return self.driver.current_url
    
    def page_title(self):
        return self.driver.title
    
    def partners_compare(self):
        if self.partners != self.region_partners():
            return True
        return False
