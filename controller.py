from searchAccounts import searchAccounts
from saveJson import saveJson
from sortJson import sortJson
from editUsers import sortUsers
from time import sleep
from ConfigData import ConfigInit
from ConfigData import AccountsConfig
from ConfigData import PublicOptions
from loadData import loadData

class searchController():
    def __init__(self,count_iterations,CheckSearchAcc):
        # config data
        self.accounts=AccountsConfig()


        self.count_iterations = count_iterations
        self.CheckSearchAcc = CheckSearchAcc


        #---------------------------
        self.max_count_iterations_save = PublicOptions.get_public_option("count_iterations")
        self.max_index_iteration = PublicOptions.get_public_option("max_index_iteration")
        self.time_wait = ConfigInit.get_option("time_wait")  # sec
        # --------------------------
        self.data=loadData()
        self.data.loadAll()
        #Точка входа
        #------------------------
        self.saveJsonObj= saveJson(self.data)
        self.main_control()
        #------------------------

    def main_control(self):
        indexAccount = 0
        index_iteration = 0
        count_iterations_save = 0


        for _ in range( self.count_iterations):
            if index_iteration==self.max_index_iteration:
                print('Слишком много итераций работа программы приостановлена на:',self.time_wait//60,'минут')
                sleep(self.time_wait)
                index_iteration=0
            login,password=self.accounts.get_auti_data(indexAccount)
            if self.CheckSearchAcc=='yes':
                search=searchAccounts(self.data)
                search.runSearch(login,password)

            sortUsers.sort('')
            full_data = self.data.loadUsers()
            while full_data[-1]!="++++++++++++++++++++++++++++++++++\n":
                if [-1]=="++++++++++++++++++++++++++++++++++\n":break
                self.saveJsonObj.save(login,password)
                full_data = self.data.loadUsers()


            indexAccount += 1
            index_iteration+=1
            if indexAccount + 1 >= len(self.accounts.get_auti_data()):
                indexAccount = 0

#sortJson.sort('')


if __name__ == "__main__":
    count_iterations = int(input('Введите количество итераций сбора '))
    CheckSearchAcc = str(input('Искать новвые аккаунты yes/no ').lower())
    controller=searchController(count_iterations,CheckSearchAcc)