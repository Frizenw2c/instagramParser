import json
from multipledispatch import dispatch
"""
Правила добавление новой переменной в конфиг:
1.Создать гетеры и сетеры в соотвествующих классах
2.Добавить свою переменную в test_exist и get_option
3.Добавить описание переменнойв options/readme.txt
4.Гетеры и сетеры использовать для управлением объектом
5.get_option используется если не нужно тянуть весь класс и держать в памяти ненужные объекты
6.Не добавлять set_option,установку параметров лучше делать через объекты   
"""
"""
pathExe=C:\driverfox\geckodriver.exe
path_accounts=accounts/logPass.txt
path_jsons=D:\searchdisaner\jsons_conc
index_acc=0

"""


from os import path

class ConfigInit():
    def __init__(self):
        self.pathToOptions="options/"
        self.arrayTextConfig=[]

        f=open(self.pathToOptions+"init.txt",'r',encoding='utf-8')
        for line in f:
            self.arrayTextConfig.append(line)
            if("index_acc" in line[:-1]):
                tresh,self.index_acc=line[:-1].split('=')
                self.index_acc=int(self.index_acc)

            elif("pathExe" in line[:-1]):
                tresh,self.pathExe=line[:-1].split('=')
            elif("path_accounts" in line[:-1]):
                tresh,self.path_accounts=line[:-1].split("=")
            elif("path_jsons" in line[:-1]):
                tresh,self.path_jsons=line[:-1].split('=')
            elif("time_wait" in line[:-1]):
                tresh,self.time_wait=line[:-1].split('=')
                self.time_wait=int(self.time_wait)
        self.test_exist()
        f.close()

    def test_exist(self):
        if (path.exists(self.pathExe)):
            print(self.pathExe," существует")
        else:
            print(self.pathExe," не существует,проверьте init.txt")

        if(path.exists(self.path_accounts)):
            print(self.path_accounts,' существует')
        else:
            print(self.path_accounts,'не существует,проверьте init.txt')

        if (path.exists(self.path_jsons)):
            print(self.path_jsons,' существует')
        else:
            print(self.path_jsons,' не сущесвтует,проверьте init.txt')

        if type(self.index_acc) == int or type(self.index_acc) == float:
            print(self.index_acc,' является числом')
        else:
            print(self.index_acc,' не является числом или не существует,проверьте init.txt')

        if type(self.time_wait)== int or type(self.time_wait) == float:
            print(self.time_wait,'является числом')
        else:
            print(self.time_wait,'не является числом или не существует,проверьте init.txt')

    def get_option(option):
        pathToOptions = "options/"
        array_option=["index_acc","pathExe","path_accounts","path_jsons","time_wait"]
        f = open(pathToOptions + "init.txt", 'r', encoding='utf-8')
        for line in f:
            if option in array_option:
                if (option in line[:-1]):
                    tresh, option_value = line[:-1].split('=')
                    return option_value
            else:
                print("значение ",option," неккоректно доступные значения:",array_option )
                return -1
        f.close()


    def save_init(self):
        f=open(self.pathToOptions+"init.txt",'w',encoding='utf-8')
        for line in self.arrayTextConfig:
            f.write(line)
        f.close()

    def get_path_driver(self):
        return self.pathExe

    def set_path_driver(self,newPath):
        for index in range(len(self.arrayTextConfig)):
            if("pathExe" in self.arrayTextConfig[index]):
                self.arrayTextConfig[index]="pathExe="+newPath+"\n"
                self.pathExe=newPath
        self.save_init()


    def get_path_accounts(self):
        return self.path_accounts


    def set_path_accounts(self,newPath):
        for index in range(len(self.arrayTextConfig)):
            if("path_accounts" in self.arrayTextConfig[index]):
                self.arrayTextConfig[index]="path_accounts="+newPath+"\n"
                self.path_accounts=newPath
        self.save_init()

    def get_path_jsons(self):
        return self.path_jsons

    def set_path_jsons(self,newPath):
        for index in range(len(self.arrayTextConfig)):
            if("path_jsons" in self.arrayTextConfig[index]):
                self.arrayTextConfig[index]="path_jsons="+newPath+"\n"
                self.path_jsons=newPath
        self.save_init()

    def get_index_acc(self):
        return self.index_acc

    def set_index_acc(self,newValue):
        try:
            test=int(newValue)
        except:
            print(newValue," не может быть использовано,оно должно быть ЧИСЛОМ,попробуйте ещё")
        else:
            for index in range(len(self.arrayTextConfig)):
                if("index_acc" in self.arrayTextConfig[index]):
                    self.arrayTextConfig[index]="index_acc="+str(newValue)+"\n"
                    self.index_acc=int(newValue)
            self.save_init()

    def get_time_wait(self):
        return self.time_wait

    def set_time_wait(self,newValue):
        try:
            test=int(newValue)
            del test
        except:
            print(newValue," не может быть использовано,оно должно быть ЧИСЛОМ,попробуйте ещё")
        else:
            for index in range(len(self.arrayTextConfig)):
                if("time_wait" in self.arrayTextConfig[index]):
                    self.arrayTextConfig[index]="time_wait="+str(newValue)+"\n"
                    self.time_wait=int(newValue)
            self.save_init()

"""
instbober
$reset->name
todoctordoom
<dcae><4315>

"""
"""

@dispatch -перегрузка функции в зависимости от того есть параметр index или нет, get_auti_data без индекса возращает массив, 
с индексом только логин и пароль соответствующего индекса,использовать 0,1,2,3,4...n
---------------------------------------------------------------------------------------------------------------
|Временное или вечное:                                                                                        |
|Удалять с осторожностью,резервное хранение на данный момент 24.01.2022 не реализовано,придется заново вводить|
---------------------------------------------------------------------------------------------------------------
"""
class AccountsConfig():
    def __init__(self):
        self.path_accounts=ConfigInit.get_option("path_accounts")
        self.accounts=[]
        f = open(self.path_accounts, 'r', encoding='utf-8')
        for line in f:
            self.accounts.append(line[:-1])
        f.close()
        self.accounts_to_dict()

    def accounts_to_dict(self):
        index=0
        dict_acc={"login":[],"password":[]}
        while (index<len(self.accounts)):
            dict_acc["login"].append(self.accounts[index])
            dict_acc["password"].append(self.accounts[index+1])
            index+=2
        self.dict_accounts=dict_acc

    def save_accounts(self):
        f=open(self.path_accounts,'w',encoding='utf-8')
        print(self.accounts,self.dict_accounts)
        for line in self.accounts:
            f.write(line+"\n")
        f.close()

    @dispatch()
    def get_auti_data(self):
        return self.dict_accounts

    @dispatch(int)
    def get_auti_data(self,index):
        return [self.dict_accounts["login"][index],self.dict_accounts["password"][index]]

    def add_auti_data(self,login,password):
        self.dict_accounts["login"].append(login)
        self.dict_accounts["password"].append(password)
        self.accounts.extend([login,password])
        self.save_accounts()

    def del_auti_data(self,login):
        if login in self.dict_accounts["login"]:
            pos=self.dict_accounts["login"].index(login)
            if pos!=-1:
                self.dict_accounts["login"].pop(pos)
                self.dict_accounts["password"].pop(pos)
        if login in self.accounts:
            pos=self.accounts.index(login)
            if pos!=-1:
                self.accounts.pop(pos+1)
                self.accounts.pop(pos)
        self.save_accounts()
"""
count_iterations=35
max_count_files=1000
"""
class PublicOptions():

    def __init__(self):
        self.pathToOptions = "options/"
        self.arrayTextConfig = []

        f = open(self.pathToOptions + "publicOptions.txt", 'r', encoding='utf-8')
        for line in f:
            self.arrayTextConfig.append(line)
            if("count_iterations" in line[:-1]):
                tresh,self.count_iterations=line[:-1].split('=')
                self.count_iterations=int(self.count_iterations)
            elif("max_count_files") in line[:-1]:
                tresh,self.max_count_files=line[:-1].split("=")
                self.max_count_files=int(self.max_count_files)
            elif("max_index_iteration") in line[:-1]:
                tresh,self.max_index_iteration=line[:-1].split("=")
                self.max_index_iteration=int(self.max_index_iteration)

    def test_exist(self):
        if type(self.max_count_files) == int or type(self.max_count_files) == float:
            print(self.max_count_files,' является числом')
        else:
            print(self.max_count_files,' не является числом или не существует,проверьте publicOptions.txt')
        if type(self.count_iterations) == int or type(self.count_iterations) == float:
            print(self.count_iterations,' является числом')
        else:
            print(self.count_iterations,' не является числом или не существует,проверьте publicOptions.txt')

        if type(self.max_index_iteration)==int or type(self.max_index_iteration) == float:
            print(self.max_index_iteration,' не является числом или не сущуествует,проверьте publicOptions.txt')
        else:
            print(self.max_index_iteration,'не является числом или не существует,проверьте publicOptions.txt')

    def get_count_iterations(self):
        return self.count_iterations

    def get_max_count_files(self):
        return self.max_count_files

    def set_count_iterations(self,newValue):
        for index in range(len(self.arrayTextConfig)):
            if ("count_iterations" in self.arrayTextConfig[index]):
                self.arrayTextConfig[index] = "count_iterations=" + str(newValue) + "\n"
                self.count_iterations = int(newValue)
        self.save_public_options()

    def set_max_count_files(self,newValue):
        for index in range(len(self.arrayTextConfig)):
            if ("max_count_files" in self.arrayTextConfig[index]):
                self.arrayTextConfig[index] = "max_count_files=" + str(newValue) + "\n"
                self.max_count_files = int(newValue)
        self.save_public_options()

    def get_max_index_iteration(self):
        return self.max_index_iteration

    def set_max_index_iteration(self,newValue):
        for index in range(len(self.arrayTextConfig)):
            if ("max_index_iteration" in self.arrayTextConfig[index]):
                self.arrayTextConfig[index] = "max_index_iteration=" + str(newValue) + "\n"
                self.max_index_iteration = int(newValue)
        self.save_public_options()

    def save_public_options(self):
        f = open(self.pathToOptions + "publicOptions.txt", 'w', encoding='utf-8')
        for line in self.arrayTextConfig:
            f.write(line)
        f.close()

    def get_public_option(option):
        pathToOptions = "options/"
        array_option=["max_count_files","count_iterations","max_index_iteration"]
        f = open(pathToOptions + "publicOptions.txt", 'r', encoding='utf-8')
        for line in f:
            if option in array_option:
                if (option in line[:-1]):
                    tresh, option_value = line[:-1].split('=')
                    return option_value
            else:
                print("значение ",option," неккоректно доступные значения:",array_option )
                return -1
        f.close()

#-----------------------------------------

if __name__ == "__main__":
    #config=ConfigPaths()
    #configAcc=AccountsConfig()
    public_options=PublicOptions()