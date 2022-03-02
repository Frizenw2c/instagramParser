"""
------------------TODOOLD------------------
1.Собрать список необходимых файлов --- V
2.Создание файлов ---V
3.Установка geckodriver из архива ---V
4.Установка firefox --- V
5.Закончить ---V
6.Запуск скрипта parseConc в режиме теста
6.1.Пробежаться с работой скрипта в разных режимах
6.2.Если есть ошибки то попытаться пофиксить и вывести результат
"""
"""
------------------TODO------------------
1.Класс для устнановки на новом компьютере для разработки
2.Методы установки класса для разработки должны быть наследуемы в класс для установки для пользователя
3.Переопределение путей к текущему каталогу
4.Создание документации по установке  
"""
"""
------------------FILES------------------
--------CREATE--------
users/sortconc.txt
users/usersconc.txt
jsons_conc/
data/
users/
accounts/
options/
--------CREATE&EDIT--------
accounts/logPass.txt
options/resetfile.txt
options/publicOptions.txt
options/init.txt
--------DEARCHIVE--------
options/readme.txt
stop words.txt
key words.txt
parseConc.py
hastags.txt
reset.py
"""
import os
import zipfile
from os import path
from time import sleep
from ConfigData import ConfigInit
"""
Класс для установки парсера конкурента на прод
"""
class installParser():

    def createDirectories(self,directories):
        for directory in directories:
            if not(path.exists(directory)):
                try:
                    os.mkdir(directory)
                    print('создание директории',directory,'прошло успешно')
                except:
                    print('ошибка')
            else:
                print(directory,'уже существует')

    def createFiles(self,files):
        for file in files:
            if not(path.exists(file)):
                try:
                    f=open(file,'w',encoding='utf-8')
                    if file=="users/sortconc.txt":
                        f.write('++++++++++++++++++++++++++++++++++\n')
                    else:
                        f.write('')
                    f.close()
                    print(file,'создан')
                except:
                    print(file, 'не создан')
            else:
                print(file,'уже сущестувует')

    def deArchive(self):
        archive_path="arc.zip"
        archive = zipfile.ZipFile(archive_path, "r")
        archive.extractall('')

    def editFiles(self,files):
        initObj=ConfigInit()
        for file in files:
            if file=="accounts/logPass.txt":
                print("Сейчас нужно будет ввести логин и пароли к аккаунтам инстаграмма используемые для сбора")
                try:
                    count_logs=int(input('Введите количество используемых аккаунтов(позже можно будет изменить вручную):').strip(' '))
                    for _ in range(count_logs):
                        login=str(input('Введите логин:')).strip(' ')
                        password=str(input('Введите пароль:')).strip(' ')
                        f=open(file,'a',encoding='utf-8')
                        f.write(login+'\n')
                        f.write(password + '\n')
                        f.close()
                except:
                    print('Ошибка при сохраненнии акаунтов,необходимо самостоятельно добавить аккаунты в accounts/logPass.txt')
            elif file=="options/publicOptions.txt":
                print("Заполнение данных файла publicOptions,так же можно будет позже отредактировать,рекомендуется оставить стандартные настройки")
                options_check=str(input('Введите "yes" если вы хотите самостоятельно настроить,если хотите использовать стандартные настройки введите"no":')).strip(' ').lower()
                if options_check=="yes":
                    count_iterations=int(input("Введите максимальное количество действий для одного аккаунта(рекомендуется число больше 30 и меньше 100):").strip(' '))
                    max_count_files=int(input("Введите максимальное количество собранных постов у конкурента(рекомендуется больше 150.чем больше число тем дольше будет идти сбор):").strip(' '))
                else:
                    count_iterations=35
                    max_count_files=250
                f=open(file,'w',encoding='utf-8')
                f.write("count_iterations="+str(count_iterations)+'\n')
                f.write("max_count_files="+str(max_count_files))
                f.close
            elif file=="options/init.txt":
                pathExe="geckodriver.exe"
                path_accounts="accounts/logPass.txt"
                path_jsons=path.join(os.getcwd(),'jsons')
                index_acc= 0
                initObj.set_path_driver(pathExe)
                initObj.set_path_jsons(path_jsons)
                initObj.set_path_accounts(path_accounts)
                initObj.set_index_acc(index_acc)

    def installFirefox(self):
        print('Необходимо установить Firefox')
        os.startfile('Firefox Installer.exe')


class installDevNewPc(installParser):
    def __init__(self):

        self.installFirefox()
        sleep(15)
        checkInstall = str(input('Введите "yes" когда установка Firefox будет законченна:')).strip(' ').lower()
        if checkInstall == 'yes':
            self.createDirectories(["jsons/", "users/"])
            sleep(15)
            self.createFiles(files=["users/sort.txt","users/users.txt"])
            sleep(15)
            self.editFiles(files=["accounts/logPass.txt","options/resetfile.txt","options/publicOptions.txt","options/init.txt"])
            sleep(15)
        print('Установка прошла успешно')
        input('Нажмите enter чтобы закрыть программу')


if __name__=='__main__':
    """
    Старая установка
    install=installParser()
    install.deArchive()
    sleep(15)
    install.installFirefox()
    sleep(15)
    checkInstall=str(input('Введите "yes" когда установка Firefox будет законченна:')).strip(' ').lower()
    if checkInstall=='yes':
        install.createDirectories()
        sleep(15)
        install.createFiles(["jsons_conc/","data/","users/","accounts/","options/"])
        sleep(15)
        install.editFiles()
        sleep(15)
    print('Установка прошла успешно')
    input('Нажмите enter чтобы закрыть программу')
    """
    installDevNewPc()