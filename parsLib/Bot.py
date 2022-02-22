from time import sleep
from selenium import webdriver

class hastagScraper():
    def __init__(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        try:

            f = open("users/sortconc.txt", "r")
            users = []
            check = False
            number_string = 0
            full_data = []
            for name in f:
                if name[:-1] != '--------------------------' and name[:-1] != '---------------------------':
                    full_data.append(name)
                    if name[:-1] == "++++++++++++++++++++++++++++++++++":
                        check = True
                        check_string = number_string
                    if check and name[:-1] != "++++++++++++++++++++++++++++++++++":
                        users.append(name[:-1])
                    number_string += 1
            f.close()
            count_iterations = 0
            number_string = check_string

            for user in users:
                print(user)
                print(count_iterations)
                if count_iterations == 0:
                    global browser
                    browser = webdriver.Firefox(executable_path="C:\driverfox\geckodriver.exe", options=options)
                    browser.implicitly_wait(5)

                    browser.get('https://www.instagram.com/' + user + '/?__a=1')
                    sleep(2)

                    username_input = browser.find_element_by_css_selector("input[name='username']")
                    password_input = browser.find_element_by_css_selector("input[name='password']")

                    username_input.send_keys(self.login_pass[self.index_acc])
                    password_input.send_keys(self.login_pass[self.index_acc + 1])

                    login_button = browser.find_element_by_xpath("//button[@type='submit']")
                    login_button.click()

                    sleep(5)

                browser.get('https://www.instagram.com/' + user + '/?__a=1')
                sleep(2)
                browser.find_element_by_id('rawdata-tab').click()
                sleep(2)
                browser.find_element_by_css_selector("button.prettyprint").click()
                sleep(2)
                content = browser.find_elements_by_css_selector('pre.data')
                for el in content:
                    contentJson = (el.text)
                js = open("jsons_conc\\" + user + ".json", 'w', encoding='utf-8')
                js.write(contentJson)
                js.close()
                count_iterations += 1
                if count_iterations == 30:
                    count_iterations = 0
                    browser.close()
                number_string += 1


    def main

if __name__ =="__main__" :
    hastagScraper()