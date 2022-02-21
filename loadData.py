"""
---------------TODO---------------
1.Файлы stops,key words не должны содержать дубликатов,необходимо проверять это

"""
import json
class loadData():
    def __init__(self,
                 users_path="users/sort.txt",
                 key_words_path="key words.txt",
                 stops_path="stop words.txt",
                 addinfo_path="D:\searchdisaner\data\\additional_info\\add_data.json"
                 ):
        self.users_path=users_path
        self.key_words_path=key_words_path
        self.stops_path=stops_path
        self.addInfo_path=addinfo_path

    def loadUsers(self):
        f=open(self.users_path,'r')
        users=[]
        for name in f:
            if name[:-1]!='--------------------------' and name[:-1]!='---------------------------':

                if name[:-1]=="++++++++++++++++++++++++++++++++++":
                    break
                if name[:-1] != "+++++++++++++++++++++++++++++++++":
                    users.append(name[:-1])

        self.users=users
        f.close
        return users
    def loadDataKeys(self):
        self.data = {'fullname': [], 'username': [], 'biography': [], 'count_followed_by': [], 'email': [], 'phone': [],
                'site': []}
        return self.data

    def loadKeywords(self):
        f = open(self.key_words_path, 'r', encoding='utf-8')
        key_words = []
        for line in f:
            key_words.append(line[:-1])

        f.close()
        self.key_words=key_words
        return key_words
    def loadStops(self):
        stops=['\u0491', '\u0454', '\u0456', '\u0457']
        f = open(self.stops_path, 'r', encoding='utf-8')
        for line in f:
            stops.append(line[:-1])
        f.close()
        self.stops=stops
        return stops


    def loadAddInfo(self):
        f = open(self.addInfo_path,'r',encoding='utf-8')
        text = json.load(f)
        f.close()
        if text == {}:
            print('Не удалось загрузить кэш,кэш пустой')
            return False
        return text
    def loadAll(self):
        self.data=self.loadDataKeys()
        self.users=self.loadUsers()
        self.key_words=self.loadKeywords()
        self.stops=self.loadStops()
        self.addInfo=self.loadAddInfo()
    def checkLoad(self,option):
        """
        Функция проверяет загруженны ли данные
        :param option data,users,key_words,stops,all:
        :return:Возвращает True или False в зависимости от существует ли загруженная информация
        """
        if option=="data":
            if (self.data)!={}:
                return True
            else:
                return False
        elif option=="users":
            if (self.users)!=[]:
                return True
            else:
                return False
        elif option=="key_words":
            if self.key_words!=[]:
                return True
            else:
                return False
        elif option=="stops":
            if self.stops!=[]:
                return True
            else:
                return False
        elif option=='addInfo':
            if self.addInfo!=[]:
                return True
            else:
                return False
        elif option=="all":
            if (self.data)!={} and (self.users)!=[] and self.key_words!=[] and self.stops!=[] and self.addInfo!=[]:
                return True
            else:
                return False

    def getOption(self,option):
        if option=="data":
            return self.data
        elif option=="users":
            return self.users
        elif option=="key_words":
            return self.key_words
        elif option=="stops":
            return self.stops
        elif option=="addinfo":
            return self.addInfo


if __name__=="__main__":
    data_container=loadData()
    data_container.loadAll()
