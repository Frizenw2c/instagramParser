from time import sleep
from selenium import webdriver
from keyboard import write
from keyboard import send
import shutil
from os import path
from ConfigData import ConfigInit
from selenium.webdriver.chrome.options import Options
"""
---------------TODO---------------
1.Переписать под общий функционал
"""
class saveJson():
    def __init__(self,loadedData):
        self.options = webdriver.FirefoxOptions()
        self.options.add_argument('-headless')
        #self.loadedData=loadedData.get
        initObj=ConfigInit()
        self.usersSrc=initObj.get_path_jsons()
        self.
    def save(self):
        try:

            f=open("users/sort.txt","r")
            users=[]
            check=False
            number_string=0
            full_data=[]
            for name in f:
                if name[:-1]!='--------------------------' and name[:-1]!='---------------------------':
                    full_data.append(name)
                    if name[:-1]=="++++++++++++++++++++++++++++++++++":
                        check=True
                        check_string=number_string
                    if check and name[:-1]!="++++++++++++++++++++++++++++++++++":
                        users.append(name[:-1])
                    number_string+=1
            print(users)
            print(full_data,len(full_data)-check_string)
            f.close()
            count_iterations=0
            number_string=check_string

            for user in users:
                print(user)
                print(count_iterations)
                if count_iterations==0:
                    global browser
                    browser = webdriver.Firefox(executable_path="F:\WORK\instagramParser\geckodriver.exe",options=options)
                    browser.implicitly_wait(5)

                    browser.get('https://www.instagram.com/'+user+'/?__a=1')
                    sleep(2)

                    username_input = browser.find_element_by_css_selector("input[name='username']")
                    password_input = browser.find_element_by_css_selector("input[name='password']")

                    username_input.send_keys("instbober")
                    password_input.send_keys("$reset->name")

                    login_button = browser.find_element_by_xpath("//button[@type='submit']")
                    login_button.click()

                    sleep(5)

                browser.get('https://www.instagram.com/'+user+'/?__a=1')
                sleep(2)
                browser.find_element_by_id('rawdata-tab').click()
                sleep(2)
                browser.find_element_by_css_selector("button.prettyprint").click()
                sleep(2)
                content = browser.find_elements_by_css_selector('pre.data')
                for el in content:
                    contentJson=(el.text)
                js = open("D:\\searchdisaner\\jsons\\"+user+".json", 'w',encoding='utf-8')
                js.write(contentJson)
                js.close()
                #browser.close()
                if path.exists("C:\\Users\\User\\Downloads\\"+user+".json"):
                    shutil.move("C:\\Users\\User\\Downloads\\"+user+".json", "D:\\searchdisaner\\jsons\\"+user+".json")
                else:
                    sleep(5)
                    shutil.move("C:\\Users\\User\\Downloads\\" + user + ".json", "D:\\searchdisaner\\jsons\\" + user + ".json")


                count_iterations+=1
                if count_iterations==30:
                    count_iterations=0
                    browser.close()
                number_string += 1

        except:

            full_data[number_string],full_data[check_string]=full_data[check_string],full_data[number_string]
            #print(full_data)
            f=open("users/sort.txt",'w')
            for data in full_data:
                f.write(data)
            f.close()
            browser.close()

        else:

            full_data[number_string], full_data[check_string] = full_data[check_string], full_data[number_string]
            # print(full_data)
            f = open("users/sort.txt", 'w')
            for data in full_data:
                f.write(data)
            f.close()



if __name__=='__main__':
    print(saveJson.save(''))