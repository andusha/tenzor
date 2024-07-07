from ..pages.FirstScenario import FirstScenarioSearchHelper


def test_first_scenario(browser):
    first_scenario = FirstScenarioSearchHelper(browser)
    first_scenario.go_to_site()
    first_scenario.contacts_page()
    first_scenario.to_tenzor_site()
    first_scenario.driver.switch_to.window(first_scenario.driver.window_handles[-1])
    assert first_scenario.tenzor_main_page_block().is_displayed()
    first_scenario.click_on_tenzor_main_page_block_a()
    assert (
        first_scenario.check_page_url() == "https://tensor.ru/about"
        and first_scenario.check_img_size()
    )
