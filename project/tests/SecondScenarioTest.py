import time
from ..pages.SecondScenario import SecondScenarioSearchHelper


def test_second_scenario(browser):
    second_scenario = SecondScenarioSearchHelper(browser)
    second_scenario.go_to_site()
    second_scenario.contacts_page()
    second_scenario.add_region_partners()
    assert (
        second_scenario.current_region().text == "Новосибирская обл."
        and second_scenario.check_region_partners()
    )
    second_scenario.click_on_region_chooser()
    second_scenario.click_in_modal()
    time.sleep(5)
    assert (
        second_scenario.current_region().text == "Камчатский край"
        and second_scenario.current_region().text in second_scenario.page_title()
        and "41-kamchatskij-kraj" in second_scenario.page_url() 
        and second_scenario.partners_compare()
    )
