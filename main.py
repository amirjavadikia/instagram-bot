from time import sleep
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver

class Bot:
    def __init__(self):
        self.login("testbot396","a123456789")

    def login(self,username,password):
        self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.driver.get("https://insagram.com")

        sleep(3)

        username_input = self.driver.find_element_by_css_selector("input[name='username']")
        username_input.send_keys(username)

        password_input = self.driver.find_element_by_css_selector("input[name='password']")
        password_input.send_keys(password)

        sleep(2)

        login_btn = self.driver.find_element_by_xpath("//button[@type='submit']")
        login_btn.click()

        sleep(4)
        self.driver.get("https://www.instagram.com/accounts/access_tool/current_follow_requests")
        sleep(3)

        # num_scroll = 0
        # while nums in num_scroll < 1:
        #     self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/main/button').click()
        #     sleep(1)
        #     num_scroll += 1


        name_list = []

        for name in self.driver.find_elements_by_class_name('-utLf'):
            name_list.append(name.text)

        for user in name_list:
            self.driver.get(f"https://instagram.com/{user}")
            sleep(1)

            self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/button/div').click()
            sleep(1)

            self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[1]').click()

myBot = Bot()

myBot
