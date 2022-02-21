"""
Используется для поиска по ссылкам wa.me

"""
class wameSearch():
    def __init__(self):
        pass
    def search_in_string(self,site):
        """
        Должен искать в строке
        :return:
        """
        tresh,phone=site.split('wa.me/')
        if '/' in phone:
            phone,tresh=phone.split('/')
        return phone

