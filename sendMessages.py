from time import sleep
from selenium import webdriver
from keyboard import send
from keyboard import write
import pyexcel
from pyexcel._compact import OrderedDict

def sendTab(count):
    for _ in range(count):
        send('TAB', do_press="TAB")
        sleep(0.4)


def sendMassage(users, login, password):

    browser = webdriver.Firefox(executable_path="F:\WORK\instagramParser\geckodriver.exe")
    browser.implicitly_wait(5)
    browser.get('https://www.instagram.com/instbober/?__a=1')
    sleep(2)
    username_input = browser.find_element_by_css_selector("input[name='username']")
    password_input = browser.find_element_by_css_selector("input[name='password']")
    username_input.send_keys(login)
    password_input.send_keys(password)
    login_button = browser.find_element_by_xpath("//button[@type='submit']")
    login_button.click()
    sleep(5)
    # valentine_painting
    browser.get('https://www.instagram.com/direct/new')
    sleep(5)
    # Пропуск всплывающей подсказки
    sendTab(2)
    send('ENTER', do_press="ENTER")
    for user in users:
        browser.get('https://www.instagram.com/direct/new')
        sleep(0.2)
        write(user)
        sleep(1)
        # Выбор адрессата
        sendTab(2)
        sleep(3)
        send('ENTER', do_press="ENTER")
        sleep(0.2)
        # Фокус на кнопку next
        sendTab(2)
        sleep(2)
        send('ENTER', do_press="ENTER")
        sleep(4
              )
        # Пишем сообщение
        # write(generateMessage())
        # send('ENTER',do_press="ENTER")
    browser.close()


def generateMessage():
    pass


def searchUser(keyWords):
    allUsers = pyexcel.get_dict(file_name="data/usernames and biograph.xlsx", name_columns_by_row=0)
    checkedUsers=[]
    for index in range(len(allUsers['fullname'])):
        flagCheckUser=False
        for keyWord in keyWords:
            if keyWord in allUsers['fullname'][index] or keyWord in allUsers['username'][index]\
                or keyWord in allUsers['biography'][index]:
                flagCheckUser=True
                break
        if flagCheckUser:
            checkedUsers.append(allUsers['username'][index])
    return checkedUsers
def getAccounts():
    f = open('accounts\\logPass.txt', 'r', encoding='utf-8')
    accounts = []
    logPass = []
    for line in f:
        accounts.append(line[:-1])
    for index in range(0, len(accounts), 2):
        logPass.append({'log': accounts[index], 'pass': accounts[index + 1]})
    f.close()
    return logPass


def getKeyWords():
    keyWords = []
    f = open('key words.txt', 'r', encoding='utf-8')
    for line in f:
        keyWords.append(line[:-1])

    f.close()
    return keyWords



keyWords = getKeyWords()
accounts = getAccounts()
users=searchUser(keyWords)
indexAccounts=0
idUsers=0
stepUsers=10
while stepUsers<=20:

    sendMassage(users[idUsers:stepUsers], accounts[indexAccounts]['log'], accounts[indexAccounts]['pass'])
    idUsers+=10
    stepUsers+=10
    indexAccounts+=1
    if indexAccounts+1>=len(accounts):
        indexAccounts=0
