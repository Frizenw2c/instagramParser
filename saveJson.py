from time import sleep
from selenium import webdriver
from keyboard import write
from keyboard import send
import shutil
from os import path
import os
from ConfigData import ConfigInit
from ConfigData import PublicOptions
from selenium.webdriver.chrome.options import Options
"""
---------------TODO---------------
1.Переписать под общий функционал
"""
class saveJson():
    def __init__(self,loadedData):
        self.options = webdriver.FirefoxOptions()
        #self.options.add_argument('-headless')
        #self.loadedData=loadedData.get
        initObj=ConfigInit()
        publicObj=PublicOptions()

        self.usersSrc=initObj.get_path_jsons()
        self.driverSrc=initObj.get_path_driver()
        self.userPc=os.environ.get("USERNAME")
        self.max_count_iterations=publicObj.get_count_iterations()


    def get_users(self):
        """
        Обработчик файла sort.txt (не использую класс loadData так как только в этом куске кода мне необходимо использовать
        еще и разделение списка на до и после отметки загруженных файлов

        :return:
        users
        number_string
        full_data
        check_string
        """
        f = open("users/sort.txt", "r")
        users = []
        check = False
        check_string =0
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
        print(users)

        f.close()

        self.check_string=check_string
        self.full_data=full_data
        self.users=users
        self.number_string = number_string

    def openBrowser(self):
        self.browser = webdriver.Firefox(executable_path=self.driverSrc, options=self.options)
        self.browser.implicitly_wait(5)


    def closeBrowser(self):
        self.browser.close()
        del(self.browser)


    def saveUsersProgress(self):
        print(self.full_data[self.number_string],self.full_data[self.check_string],self.full_data[self.check_string],self.full_data[self.number_string])
        self.full_data[self.number_string], self.full_data[self.check_string] = self.full_data[self.check_string], \
                                                                                self.full_data[self.number_string]
        # print(full_data)
        f = open("users/sort.txt", 'w')
        for data in self.full_data:
            f.write(data)
        f.close()


    def auth(self,login,password):
        self.browser.get('https://www.instagram.com/accounts/login/')
        sleep(2)

        username_input = self.browser.find_element_by_css_selector("input[name='username']")
        password_input = self.browser.find_element_by_css_selector("input[name='password']")

        username_input.send_keys(login)
        password_input.send_keys(password)

        login_button = self.browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()

        sleep(5)

    def save(self,login,password):
        count_iterations = 0
        self.get_users()
        self.openBrowser()
        self.auth(login,password)
        try:


       #Начало скачивания файлов
            for user in self.users:
                print(user)
                print(count_iterations)
                self.browser.get('https://www.instagram.com/'+user+'/?__a=1')
                sleep(2)
                self.browser.find_element_by_id('rawdata-tab').click()
                sleep(2)
                self.browser.find_element_by_css_selector("button.prettyprint").click()
                sleep(2)
                content = self.browser.find_elements_by_css_selector('pre.data')
                for el in content:
                    contentJson=(el.text)
                print(self.usersSrc+user+".json")
                js = open(self.usersSrc+user+".json", 'w',encoding='utf-8')
                js.write(contentJson)
                js.close()


                count_iterations+=1
                self.number_string += 1
                if count_iterations==self.max_count_iterations:
                    count_iterations=0
                    self.closeBrowser()
                    #self.saveUsersProgress()
                    break

        except:
            self.saveUsersProgress()
            self.closeBrowser()

        else:
            self.saveUsersProgress()


if __name__=='__main__':
    from loadData import loadData
    loaded=loadData()
    loaded.loadAll()
    jsons=saveJson(loaded)
    for _ in range(2):
        jsons.save("instbober","$reset->name")
