"""
---------------TODO---------------
2.Из ссылок wa.me ,api.watsapp доставать номера телефонов ----V
3.из ссылки taplink можно вытащить номера телефонов,почту и сайт,необходимо детально изучить все веб страницы в поисках алгоритма ----V
4.contact-me можно достать ссылки,телефон через href ---V




-----------------------------------
 {"usernames": ['avr.print','gusaktv84','sofiadoors','asanova.interior.designer','kverk.ru','nata.vindi','bukvadel.kz'],
                            "phones": ['','','','','','',''],
                            "sites": ['http://wa.me/77777263300/','https://wa.me/79264702236',
                                      'https://api.whatsapp.com/send/?phone=79771667785&app_absent=0','https://api.whatsapp.com/send?phone=79112271992',
                                      'https://taplink.cc/kverk.ru',
                                      'https://taplink.cc/nata.vindi', 'https://taplink.cc/bukvadel.kz',
                                      ]}#Временное решение для тестов
"""
from regex import regex as re
from cache import cache
from loadData import loadData
from addionalInfoScripts.wame_scripts import wameSearch
from addionalInfoScripts.whatsapp_scripts import whatsappSearch
from addionalInfoScripts.taplink_scripts import taplinkSearch
import json
import os
class additionallIInfoController():
    def __init__(self):
        self.path_to_addInfo_json="data\\additional_info\\add_data.json"
        if not os.path.exists(self.path_to_addInfo_json):
            js=open(self.path_to_addInfo_json,mode="w")
            js.close()
        data_container = loadData()
        data_container.loadAll()
        loaded = data_container.checkLoad("all")
        if loaded:
            self.stops = data_container.getOption("stops")
            self.key_words = data_container.getOption("key_words")
            self.data = data_container.getOption("data")
            self.users = data_container.getOption("users")
            """
            добавить загрузку доп инфы 
            self.addinfo={"usernames":[],"phones":[],"sites":[]}
            """
            self.addinfo =data_container.getOption("addinfo")


        self.cache_obj = cache(data_container, loaded)
        self.cache_data = self.cache_obj.cache_load()
        print('cache_data', self.cache_data)
        self.wameSearch_obj=wameSearch()
        self.whatsapp_obj=whatsappSearch()
        self.taplink_obj=taplinkSearch()
    def saveAddInfo(self):
        with open(self.path_to_addInfo_json, "w", encoding="utf-8") as write_file:
            json.dump(self.addinfo, write_file)
    def regex_check(self):
        regex=re.compile('^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$')
        for index in range(len(self.addinfo["usernames"])):
            if self.addinfo['sites'][index]!=None:
                regex_result=re.fullmatch(pattern=regex,string=str(self.addinfo["phones"][index]))#
                if regex_result:
                    print("YES",regex_result.string)
                else:
                    self.addinfo["phones"][index]=''
    def addinfo_add_cache(self):
        self.addinfo['usernames'].extend(self.cache_data['username'])
        self.addinfo['phones'].extend(self.cache_data['phone'])
        self.addinfo['sites'].extend(self.cache_data['site'])
    def controller(self):
        self.addinfo_add_cache()
        for index in range(len(self.addinfo["usernames"])):
            if self.addinfo["phones"][index]=='' and self.addinfo['sites'][index]!=None:
                if "wa.me" in self.addinfo['sites'][index]:
                    self.addinfo["phones"][index]=self.wameSearch_obj.search_in_string(self.addinfo['sites'][index])

                elif "api.whatsapp" in self.addinfo["sites"][index] and self.addinfo['sites'][index]!=None:
                    self.addinfo["phones"][index]=self.whatsapp_obj.search_in_string(self.addinfo['sites'][index])
                elif "taplink" in self.addinfo['sites'][index] and self.addinfo['sites'][index]!=None:
                    self.addinfo["phones"][index]=self.taplink_obj.controller(self.addinfo["sites"][index])
        print(self.addinfo)
        self.regex_check()
        self.saveAddInfo()
if __name__=="__main__":
    test_obj=additionallIInfoController()
    print()