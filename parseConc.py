from selenium import webdriver
from time import sleep
import json
import pandas
import re
from os import path
import os
"""
------------------TODO------------------
1.Валидный поиск номера телефона в биографии---V
2.Валидный поиск почты в биографии---V
3.Загрузку инит из файлов --- V
4.Добавить собранные в ручную аккаунты --- V
5.Проверить способ связи Whatsapp--- V
6.Добавить остановку если профиль закончился ---VAZNO


"""
"""
------------------Code save------------------
self.max_count_files = 150
self.pathExe = "F:\WORK\instagramParser\geckodriver.exe"
self.path_accounts = 'accounts/logPass.txt'
self.path_jsons = 'F:\WORK\instagramParser\jsons'
self.index_acc = 0
self.count_iterations=30 # Количество итераций на аккаунте

"""
class parseConcurent():
    def __init__(self):
        pathToOptions="optionsConcurent/"
        f=open(pathToOptions+"init.txt",'r',encoding='utf-8')
        for line in f:
            line=line.replace('\n','')
            if 'pathExe' in line:
                param, pathExe = line.split('=')
                if path.exists(pathExe.strip(' ')):

                    self.pathExe=pathExe.strip(' ')
                else:
                    print('GeckoDriver.exe не найден,проверьте init.txt')
            elif 'path_accounts' in line:
                param,path_accounts= line.split('=')
                if path.exists(path_accounts.strip(' ')):
                    self.path_accounts=path_accounts
                else:
                    print('Файл с аккаунтами не найден,проверьте init.txt')
            elif 'path_jsons' in line:
                param,path_jsons=line.split('=')
                if path.exists(path_jsons.strip(' ')):
                    self.path_jsons=path_jsons
                else:
                    print('Дирректория с jsons не найдена,проверьте init.txt')
            elif 'index_acc' in line:
                param,index_acc=line.split('=')
                try :
                    index_acc=int(index_acc.strip(' '))
                    self.index_acc=index_acc
                except:
                    print('Неверно указан index_acc, проверьте init.txt')
        f.close()
        f=open(pathToOptions+"publicOptions.txt",'r',encoding='utf-8')
        for line in f:
            line=line.replace('\n','')
            if "count_iterations" in line:
                param,count_iterations=line.split('=')
                try :
                    count_iterations=int(count_iterations.strip(' '))
                    self.count_iterations=count_iterations
                except:
                    print('Неверно указан count_iterations, проверьте publicOptions.txt')
            elif "max_count_files" in line:
                param, max_count_files = line.split('=')
                try:
                    max_count_files = int(max_count_files.strip(' '))
                    self.max_count_files = max_count_files
                except:
                    print('Неверно указан count_iterations, проверьте publicOptions.txt')


        self.count_files = 0
        self.posts = []
        self.login_pass = parseConcurent.getAutiData('', self.path_accounts)
    def load_key_words(self):

        f = open('key words.txt', 'r', encoding='utf-8')
        key_words = []
        for line in f:
            key_words.append(line[:-1])
        self.key_words=key_words
        f.close()
    def load_stop_words(self):

        stops = ['\u0491', '\u0454', '\u0456', '\u0457']
        f = open('stop words.txt', 'r', encoding='utf-8')
        for line in f:
            stops.append(line[:-1])

        f.close()
        self.stops = stops
    def getAutiData(self,path_accounts):
        accData = []
        f = open(path_accounts, 'r', encoding='utf-8')
        for line in f:
            accData.append(line[:-1])
        f.close()
        return accData

    def parse(self, name):
        """
        Парсит по кнопке "отметки"
        :param name:
        :return:
        Сохраняет в файл search
        """
        # config data

        # options = webdriver.FirefoxOptions()
        # options.add_argument('-headless')

        # coreSpriteRightPaginationArrow
        check_while = False
        options = webdriver.FirefoxOptions()
        # options.add_argument('-headless')
        while not (check_while):
            browser = webdriver.Firefox(executable_path=self.pathExe, options=options)
            browser.implicitly_wait(5)
            browser.get('https://www.instagram.com/explore/tags/дизайнинтерьера/')
            sleep(2)
            username_input = browser.find_element_by_css_selector("input[name='username']")
            password_input = browser.find_element_by_css_selector("input[name='password']")
            username_input.send_keys(self.login_pass[self.index_acc])
            password_input.send_keys(self.login_pass[self.index_acc + 1])
            login_button = browser.find_element_by_xpath("//button[@type='submit']")
            login_button.click()
            sleep(5)
            browser.get('https://www.instagram.com/explore/tags/дизайнинтерьера/')
            while self.max_count_files >= self.count_files:
                browser.execute_script("window.scrollBy(0,3200);")
                elements = browser.find_elements_by_tag_name('a')
                for el in elements:
                    try:
                        if 'com/p/' in el.get_attribute('href'):
                            self.posts.append(el.get_attribute('href'))
                    except:
                        browser.execute_script("window.scrollBy(0,1000);")
                sleep(50)
                print(self.posts)
                self.count_files = len(self.posts)

            break
            self.index_acc += 2
            if self.index_acc + 1 >= len(self.login_pass):
                self.index_acc = 0

        # save post and check name author
        count_index = 0

        for route in self.posts:
            print(count_index, route)
            count_index += 1
            browser.get(route + '?__a=1')
            sleep(2)
            browser.find_element_by_id('rawdata-tab').click()
            sleep(2)
            browser.find_element_by_css_selector("button.prettyprint").click()
            sleep(2)
            content = browser.find_elements_by_css_selector('pre.data')
            for el in content:
                contentJson = (el.text)

            js = open("data.json", 'w', encoding='utf-8')
            js.write(contentJson)
            js.close()
            js = open("data.json", 'r', encoding='utf-8')
            text = json.load(js)
            js.close()
            username = text['graphql']['shortcode_media']['owner']['username']
            f = open('users/usersconc.txt', 'a', encoding='utf-8')
            f.write(username + '\n')
            f.close
        browser.close()

    def sortingData(self):
        f = open("users/usersconc.txt", 'r')
        array_names_users = []
        array_names_sort = []
        new_names = []
        for line in f:
            array_names_users.append(line[:])
        f.close()
        f = open("users/sortconc.txt", 'r')
        for line in f:
            array_names_sort.append(line[:])
        for name in array_names_users:
            if not (name in new_names) and not (name in array_names_sort):
                new_names.append(name)
        f.close
        f = open("users/sortconc.txt", 'a')

        for user_name in new_names:
            f.write(user_name)
        f.close()
    def saveJson(self):
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
                    browser = webdriver.Firefox(executable_path="F:\WORK\instagramParser\geckodriver.exe", options=options)
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

        except:

            full_data[number_string], full_data[check_string] = full_data[check_string], full_data[number_string]
            f = open("users/sortconc.txt", 'w')
            for data in full_data:
                f.write(data)
            f.close()
            browser.close()

        else:

            full_data[number_string], full_data[check_string] = full_data[check_string], full_data[number_string]
            f = open("users/sortconc.txt", 'w')
            for data in full_data:
                f.write(data)
            f.close()
    def phoneSearch(self,biography):
        biography=biography.replace('-','')
        biography=biography.replace(' ','')
        regex = re.compile('(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
        phones=regex.findall(biography)
        phones_str=''
        if phones=='':
            return 'Null'
        elif isinstance(phones,list):
            for phone in phones:
                phones_str+=phone+' '
            return phones_str
        else : return phones
    def mailSearch(self,biography):
        #biography = biography.replace('-', '')
        #biography = biography.replace(' ', '')
        regex = re.compile('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
        mails = regex.findall(biography)
        mails_str = ''
        if mails == '':
            return 'Null'
        elif isinstance(mails, list):
            for mail in mails:
                mails_str += mail + ' '
            return mails_str
        else:
            return mails
    def configurateValidUsers(self,stops='no',key_words='no'):
        data = {'fullname':[],'username':[],'biography':[],'count_followed_by':[],'email':[],'phone':[],'site':[]}
        f=open('users/sortconc.txt','r')
        users=[]
        for name in f:
            if name[:-1]!='--------------------------' and name[:-1]!='---------------------------':
                if name[:-1]=="++++++++++++++++++++++++++++++++++":
                    break
                if name[:-1] != "+++++++++++++++++++++++++++++++++":
                    users.append(name[:-1])
        f.close
        numberUser = 0
        for name in users:
            check_stop = False
            check_keyword = False
            array_data = []
            f = open('jsons_conc/' + name + '.json', 'r', encoding='utf-8')
            text = json.load(f)
            f.close()
            if text == {}:
                continue
            try:
                biograph = text['graphql']['user']['biography']
                fullname = text['graphql']['user']['full_name']
                username = text['graphql']['user']['username']
                count_followed_by=text['graphql']['user']["edge_followed_by"]['count']
                external_url=text['graphql']['user']['external_url']
            except:
                continue
            try:
                email = text['graphql']['user']['business_email']
                if email == None:
                    email=self.mailSearch(biograph)
            except:
                email=self.mailSearch(biograph)
            try:
                phone = text['graphql']['user']["business_phone_number"]
                if phone == None:
                    phone=self.phoneSearch(biograph)
            except:
                phone=self.phoneSearch(biograph)
            if stops=='y':
                for stop in self.stops:
                    if stop.lower() in biograph.lower() or stop.lower() in fullname.lower():
                        check_stop = True
            else:
                check_stop=False
            if key_words=='y':
                for key_word in self.key_words:
                    if key_word.lower() in biograph.lower():
                        check_keyword = True
                        break
            else:
                check_keyword=True

            if not check_stop and check_keyword:
                array_data=[fullname, username, biograph,count_followed_by,email,phone,external_url]
                index=0
                for key in data:
                    data[key].append(array_data[index])
                    index+=1

            numberUser += 1
            print(numberUser, name)
        print(data)
        data=pandas.DataFrame(data)
        # Save the array to a file
        data.to_excel("data/usernames and biograph concurents.xlsx")



def validate_input_name(text=''):
    validation_rules=['']
    validCheck=False
    while not(validCheck):
        name=str(input(text)).strip()
        if not(name in validation_rules):
            validCheck=True
            return name
        else:
            print('Введите корректный логин конкурента')

def validate_input_use(text=''):
    validation_rules = ['yes','y','no','n']
    while True:
        key = str(input(text)).lower().strip()
        if key in validation_rules:
            if key=='yes' or key=='y':
                return 'y'
            else:
                return 'n'
        else:
            print('Введите корректный ключ')

if __name__=='__main__':
    concurrent=parseConcurent()
    stops=validate_input_use('Использовать исключающие слова(yes/no):')
    key_words=validate_input_use('Использовать ключевые слова(yes/no):')
    saveJson =validate_input_use('Сохранять новые файлы(yes/no):')
    parseJson=validate_input_use('Парсить конкурента?(yes/no):')
    if parseJson=='y':
        name=validate_input_name('Введите имя аккаунта конкурента:')
        concurrent.parse(name)
        os.system('cls||clear')
    if key_words=='y':
        concurrent.load_key_words()
    if stops=='y':
        concurrent.load_stop_words()
    concurrent.sortingData()
    if saveJson=='y':
        concurrent.saveJson()
        os.system('cls||clear')
        concurrent.configurateValidUsers(stops,key_words)
