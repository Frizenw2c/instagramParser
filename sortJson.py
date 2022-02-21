import json
import pandas
import re
from loadData import loadData
from cache import cache
from archiveController import archive
from addionalInfoScripts.addidionalInfoController import additionallIInfoController
import os
"""
---------------TODO---------------
1.Сделать поиск с использованием кэша --V
5.Сделать выход в json --V
6.Оценка аккаунта
7.Написать тест для загрузки и сохранения кэша --F
8.Функция сброса кэша
"""

class sortJson():
    def __init__(self):
        data_container = loadData()
        data_container.loadAll()
        loaded = data_container.checkLoad("all")

        if loaded:
            self.stops = data_container.getOption("stops")
            self.key_words = data_container.getOption("key_words")
            self.data = data_container.getOption("data")
            self.users = data_container.getOption("users")
            self.addinfo = data_container.getOption("addinfo")
        self.archive_useful_items=archive(name_archive="test_archive.zip")
        self.archive_garbage_items=archive(name_archive="test_garbage_archive.zip")
        self.garbage_names=self.archive_garbage_items.get_names_archive()
        print(self.garbage_names)
        self.cache_obj = cache(data_container, loaded)
        self.cache_data=self.cache_obj.cache_load()
        print('cache_data',self.cache_data)
    def delete_file(self):
        for user in self.new_sorted_users:
            if os.path.isfile("jsons/"+user+'.json'):
                os.remove("jsons/"+user+'.json')
                print("success","jsons/"+user+".json")
            else:
                print("File doesn't exists!","jsons/"+user+".json")

        for user in self.new_garbage_users:
            if os.path.isfile("jsons/"+user+'.json'):
                os.remove("jsons/"+user+'.json')
                print("success","jsons/"+user+".json")
            else:
                print("File doesn't exists!","jsons/"+user+".json")
    def get_data(self):
        count=0
        self.new_sorted_users=[]
        self.new_garbage_users=[]
        for name in self.users:
            if name in self.cache_data['username'] or name in self.garbage_names:
                continue

            print(name)
            check_stop=False
            check_keyword=False
            array_data = []
            f=open('jsons/'+name+'.json', 'r', encoding='utf-8')
            text=json.load(f)
            f.close()
            if text=={}:
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
                    email=sortJson.mailSearch('',biograph)

            except:
                email=sortJson.mailSearch('',biograph)

            try:
                phone = text['graphql']['user']["business_phone_number"]
                if phone == None:
                    phone=sortJson.phoneSearch('',biograph)

            except:
                phone=sortJson.phoneSearch('',biograph)

            for stop in self.stops:
                if stop.lower() in biograph.lower() or stop.lower() in fullname.lower():

                    check_stop=True

            for key_word in self.key_words:
                if key_word.lower() in biograph.lower():
                    check_keyword = True
                    break
            if not check_stop and check_keyword:
                array_data=[fullname, username, biograph,count_followed_by,email,phone,external_url]
                index=0

                for key in self.data:
                    self.data[key].append(array_data[index])

                    index+=1
                self.new_sorted_users.append(name)
            else:
                self.new_garbage_users.append(name)
            count+=1
        return self.data

    def saveToexcel(self,data):
        """

        :return:
        """
        data_pandas_data = pandas.DataFrame(data)
        # Save the array to a file
        print(data_pandas_data.to_excel("data/usernames and biograph.xlsx"))
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

    def sortController(self):

        if self.cache_obj.get_compare_result():
            data=self.get_data()
            print(data)
            print(self.new_sorted_users)
            self.archive_useful_items.archivation(self.new_sorted_users)
            self.cache_obj.cache_save(data)
            self.archive_garbage_items.archivation(self.new_garbage_users)
            self.delete_file()

        else:

            self.archive_useful_items.dearchivation(key="all")
            self.archive_garbage_items.dearchivation(key="all")
            self.archive_useful_items.reload_archive()
            self.archive_garbage_items.reload_archive()
            data=self.get_data()
            print(data)
            self.cache_obj.cache_save(data)
            self.archive_useful_items.archivation(self.new_sorted_users)
            self.archive_garbage_items.archivation(self.new_garbage_users)
            self.delete_file()
        cache_and_sorted_data=self.cache_obj.get_cache_and_sorted_data(self.addinfo)
        self.saveToexcel(cache_and_sorted_data)
#        if cache_data!=False:
#            for dict_key in self.data:
#                self.data[dict_key].extend(cache_data[dict_key])



if __name__=='__main__':
    sorting=sortJson()
    sorting.sortController()

