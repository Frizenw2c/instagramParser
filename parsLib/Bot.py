from time import sleep
import json
from selenium import webdriver
from ConfigData import AccountsConfig
from ConfigData import PublicOptions

class hastagScraper():
    def __init__(self,loadData):
        self.loadData=loadData
        self.options = webdriver.FirefoxOptions()
        #self.options.add_argument()
        self.max_count_files=int(PublicOptions.get_public_option('max_count_files'))
        self.maxIndexOptionKeywords=loadData.getMaxIndexOption("key_words")
        self.indexOptionKeywords=0
        self.count_files=0

    def openBrowser(self):
        self.browser = webdriver.Firefox(executable_path="C:\driverfox\geckodriver.exe", options=self.options)
        self.browser.implicitly_wait(5)

    def closeBroser(self):
        self.browser.close()
        del(self.browser)
        self.indexOptionKeywords=0
        self.count_files=0
        self.posts=[]

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

    def searchPosts(self):
        self.browser.get('https://www.instagram.com/explore/tags/'+self.loadData.getOption('key_words',self.indexOptionKeywords)+'/')
        self.indexOptionKeywords=self.indexOptionKeywords+1 if self.maxIndexOptionKeywords>=self.indexOptionKeywords+1 else 0

        posts=[]
        while self.max_count_files >= self.count_files:
            self.browser.execute_script("window.scrollBy(0,3200);")
            elements = self.browser.find_elements_by_tag_name('a')
            for el in elements:
                try:
                    if 'com/p/' in el.get_attribute('href'):
                        posts.append(el.get_attribute('href'))
                except:
                    self.browser.execute_script("window.scrollBy(0,1000);")
            sleep(50)
            self.count_files = len(posts)
            self.posts=posts
    def checkAuthorPost(self):
        count_index=0
        for route in self.posts:
            print(count_index, route)
            count_index += 1
            self.browser.get(route + '?__a=1')
            sleep(2)
            self.browser.find_element_by_id('rawdata-tab').click()
            sleep(2)
            self.browser.find_element_by_css_selector("button.prettyprint").click()
            sleep(2)
            content = self.browser.find_elements_by_css_selector('pre.data')
            for el in content:
                contentJson = (el.text)

            js = open("data.json", 'w', encoding='utf-8')
            js.write(contentJson)
            js.close()
            js = open("data.json", 'r', encoding='utf-8')
            text = json.load(js)
            js.close()
            try:
                username = text['items'][0]['user']['username']
            except:
                continue
            f = open('users/users.txt', 'a', encoding='utf-8')
            f.write(username + '\n')
            f.close

if __name__ =="__main__" :
    hastagScraper()