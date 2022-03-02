import json
import traceback
from loadData import loadData

"""
---------------TODO---------------
1.Добавить куски кода в pass -- V
3.Архивируем аккаунты юзеров прошедших кэш --V
4.Дополнить загрузку кэша деархивации юзеров если ключи кэша не совпадают --V
5.Чекай блок схему cache -- V
6.Создать класс для работы и контроля архивов --V
"""


class cache():
    def __init__(self, data_container=None, loaded=False):

        if loaded:
            self.stops = data_container.getOption("stops")
            self.key_words = data_container.getOption("key_words")
            self.data = data_container.getOption("data")
            self.users = data_container.getOption("users")
        self.sort_cache_path = "data/cache_data/cache_sort.json"
    def compare_cache_keys(self,cache_stops,cache_keywords,cache_data_keys,dict_keys):
        """
        3 проверки если все верны то возвращаем true
        :param cache_stops:
        :param cache_keywords:
        :param cache_data_keys:
        :param dict_keys:
        :return:
        """
        count_stops_compared=0


#Проверка stops
        for cache_stop in cache_stops:
            if  cache_stop in self.stops:
                count_stops_compared+=1

            else :
                count_stops_compared = 0
                break
        if count_stops_compared==len(self.stops):
            check_stops=True
        else:
            check_stops=False
        print(check_stops)

#Проверка keywords
        count_keywords_compared=0

        for cache_keyword in cache_keywords:
            if cache_keyword in self.key_words:
                count_keywords_compared += 1

            else:
                count_keywords_compared = 0
                break
        if count_keywords_compared == len(self.key_words):
            check_keywords = True
        else:
            check_keywords = False
        print(check_keywords)
#Проверка data_keys cache_data_keys,dict_keys
        count_data_key_compared=0

        for cache_data_key in cache_data_keys:
            if cache_data_key in dict_keys:
                count_data_key_compared += 1

            else:
                count_data_key_compared = 0
                break
        if count_data_key_compared == len(dict_keys):
            check_data_keys = True
        else:
            check_data_keys = False
        print(check_data_keys)
#Проверка результатов
        if check_stops and check_data_keys and check_keywords:
            self.result_cache_compare=True
            return True
        else:
            self.result_cache_compare =False
            return False
    def get_compare_result(self):
        return self.result_cache_compare
    def cache_load(self):
        f = open(self.sort_cache_path, 'r', encoding='utf-8')
        text = json.load(f)
        f.close()
        if text == {}:
            print('Не удалось загрузить кэш,кэш пустой')
            return False
        # Проверка на соответствие полей
        dict_keys = []
        for dict_key in self.data:
            dict_keys.append(dict_key)
        try:
            cache_stops = text["stops"]
            cache_keywords = text["key_words"]
            cache_data = text["data"]
            cache_data_keys = []
            for cache_data_key in cache_data:
                cache_data_keys.append(cache_data_key)

            print(cache_data_keys)

            if self.compare_cache_keys(cache_stops,cache_keywords,cache_data_keys,dict_keys):
                self.cache_stops = cache_stops
                self.cache_keywords = cache_keywords
                self.cache_data = cache_data

                return cache_data

            else:
                self.cache_stops, self.cache_keywords, self.cache_data = None,None,None
                return self.data
        except Exception as exc:
            print("Ошибка, не удалось загрузить кэш")
            print(traceback.format_exc())
            return False
    def get_save_data(self,data=[]):
        """
        Получает на вход дополнительные данные для дополнения кэша
        :param data:
        :return:
        """
        dict_keys = []
        data_to_save = {}
        if data != []:
            check_exist_data=True
            print(check_exist_data)
        else:
            data={"biography": [], "fullname": [], "username": [], "count_followed_by": [], "email": [], "phone": [], "site": []}
        if (self.cache_stops != None and self.cache_keywords != None  and self.cache_data != None) and self.result_cache_compare :
            print("add_save")
            for dict_key in self.data:
                dict_keys.append(dict_key)
            for key in dict_keys:
                self.cache_data[key].extend(data[key])

            self.data_to_save={
                "key_words":self.cache_keywords,
                "stops":self.cache_stops,
                "data":self.cache_data
            }
            with open(self.sort_cache_path, "w", encoding="utf-8") as write_file:
                json.dump(self.data_to_save, write_file)

        else:
            print("save!")
            self.data_to_save={
                "key_words":self.key_words,
                "stops":self.stops,
                "data":data
            }
        return self.data_to_save
    def cache_save(self,sort_data):



        self.data_to_save=self.get_save_data(sort_data)
        with open(self.sort_cache_path, "w", encoding="utf-8") as write_file:
            json.dump(self.data_to_save, write_file)




        """
        {"key_words": [], "stops": [], "data": {"biography": [], "fullname": [], "username": [], "count_followed_by": [], "email": [], "phone": [], "site": []}}

        """
    def get_cache_and_sorted_data(self,addinfo):
        """
        Перед применением использовать функцию get_save_data
        Дополняет базу номерами телефонов

        :return:
        """
        for index in range(len(self.data_to_save["data"]["username"])):
            if (self.data_to_save["data"]["phone"][index]=='' or self.data_to_save["data"]["phone"][index]==None):
                index_k=addinfo["usernames"].index(self.data_to_save["data"]["username"][index])
                if addinfo["usernames"][index_k]==self.data_to_save["data"]["username"][index]:
                    self.data_to_save["data"]["phone"][index] = addinfo["phones"][index_k]


        return self.data_to_save["data"]
    def delete_cache(self):
        data_to_save={"key_words": [], "stops": [], "data": {"biography": [], "fullname": [], "username": [], "count_followed_by": [], "email": [], "phone": [], "site": []}}
        with open(self.sort_cache_path, "w", encoding="utf-8") as write_file:
            json.dump(data_to_save, write_file)

if __name__ == "__main__":
    data_container = loadData()
    data_container.loadAll()
    loaded = data_container.checkLoad("all")
    cache_obj = cache(data_container, loaded)
    sort_data=cache_obj.cache_load()
    #print(cache_obj.delete_cache())
    save=cache_obj.get_save_data()