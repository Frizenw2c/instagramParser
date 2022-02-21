import requests

class taplinkSearch():
    def __init__(self):
        pass
    def getRequest(self,site):
        """
        Делает запрос к сайту,возращает контент сайта
        :param site:
        :return:
        """
        response = requests.get(site)
        if response.status_code==200:
            response.encoding = 'utf-8'
            text=response.text
            return text
        else:
            print("Не получилось подключиться")

    def searchInText(self,data):
        if "api.whatsapp.com" in data:

            finded_index = data.find('api.whatsapp.com/')
            if finded_index != -1:
                string_data=data[finded_index:finded_index + 45]
                return string_data

        elif "wa.me/" in data:

            finded_index=data.find('wa.me/')
            if finded_index != -1 :
                string_data=data[finded_index:finded_index+25]
                return string_data
        elif "type\":\"phone\"" in data:

            finded_index=data.find("type\":\"phone\"")
            if finded_index !=-1:
                string_data=data[finded_index+20:finded_index+40]
                return string_data
    def clearNumber(self,dirty_number):
        finded_index=dirty_number.find('7')
        string=dirty_number[finded_index:finded_index+11]
        if string.isdigit():
            return string
    def controller(self,site):

        data=self.getRequest(site)
        dirty_number=self.searchInText(data)
        if dirty_number!=None:
            return self.clearNumber(dirty_number)
if __name__ == "__main__":
    """
    Пример работы с классом
    taplink_obj=taplinkSearch()
    sites=['https://taplink.cc/kverk.ru','https://taplink.cc/nata.vindi','https://taplink.cc/bukvadel.kz','https://taplink.cc/natalya_navita',
           'https://taplink.cc/asdesign_studio','https://taplink.cc/shtory.aksamit','https://taplink.cc/svetlana_bulda_design','https://taplink.cc/v_kobzev']
    for site in sites:
        print(taplink_obj.controller(site))
    """
