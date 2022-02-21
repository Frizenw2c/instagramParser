"""
Используется для поиска по ссылкам api whatsapp

"""
class whatsappSearch():
    def __init__(self):
        pass
    def search_in_string(self,site):
        """
        Должен искать в строке
        :return:
        """
        tresh,phone=site.split('?phone=')
        if '/' in phone:
            phone,tresh=phone.split('/')
        if "&" in phone:
            phone, tresh = phone.split('&')
        return phone

