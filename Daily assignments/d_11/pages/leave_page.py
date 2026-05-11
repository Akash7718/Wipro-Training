from components.side_menu_component import SideMenuComponent


class LeavePage:

    def __init__(self, driver):
        self.driver = driver

        # Include Sidebar Component
        self.side_menu = SideMenuComponent(driver)