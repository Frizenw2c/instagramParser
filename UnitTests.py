from sortJson import sortJson
class unitCacheTest():
    def test0(self):
        """
        Проверка создания объекта sortJson test
        :return:
        """
        try:
            self.sortJsonTest = sortJson()
        except:
            return False
        else:
            return True
    def test1(self):
        """
        Открытие файла self.cache
        :return:
        """
        try:
            self.sortJsonTest.setDirectoryCache()
        except:
            return False
        else:
            return True
    def test2(self):
        """
        Открытие файла key words.txt
        :return:

        """
        try:
            f = open('key words.txt', 'r', encoding='utf-8')
        except:
            return False
        else:
            return True
    def test3(self):
        """
        Считывание из файла key words.txt
        :return:
        """
        try:
            self.key_words,bo=self.sortJsonTest.loadKeywords()
            if self.key_words!=[] and bo:
                return True
            else:
                return False
        except:
            return False
    def test4(self):
        """
        Открытие файла stops
        :return:
        """
        try:
            f = open('stop words.txt', 'r', encoding='utf-8')
        except:
            return False
        else:
            return True
    def test5(self):
        """
        Считывание файла stops
        :return:
        """
        try:
            f = open('stop words.txt', 'r', encoding='utf-8')

            self.stops,bo=self.sortJsonTest.loadStops()
            if self.stops!=[] and bo:
                return True
            else:
                return False
        except:
            return False
    def test6(self):
        """
        Открытие файла sort.txt
        :return:
        """
        try:
            f=open('users/sort.txt','r')
        except:
            return False
        else:
            return True
    def test7(self):
        """
        Считывание файла sort.txt
        :return:
        """
        try:

            self.users=self.sortJsonTest.loadUsers()
            if self.users != []:
                return True
            else:
                return False
        except:
            return False
    def test8(self):
        """
        Загрузка ключей
        :return:
        """
        self.data=self.sortJsonTest.loadDataKeys()
        try:
            if self.data!=[]:
                return True
            else:
                return False
        except:
            return False
    def test9(self):
        """
        Тест функции cache_load
        :return:
        """
        self.sortJsonTest.cache_load()
if __name__=='__main__':
    cacheTest=unitCacheTest()
    if cacheTest.test0():
        print("Тест 0(Создание объекта) выполнен")
    else:
        print("Тест 0(Создание объекта) закончен ошибкой")

    if cacheTest.test1():
        print("Тест 1(Откытие файла cache) выполнен")
    else:
        print("Тест 1(Открытие файла cache) закончен ошибкой")

    if cacheTest.test2():
        print("Тест 2(Открытие файла key words.txt) выполнен")
    else:
        print("Тест 2(Открытие файла key words.txt) закончен ошибкой")

    if cacheTest.test3():
        print("Тест 3(Считывание из файла key words.txt) выполнен")
    else:
        print("Тест 3(Считывание из файла key words.txt) закончен ошибкой")

    if cacheTest.test4():
        print("Тест 4(Открытие файла stops) выполнен")
    else:
        print("Тест 4(Открытие файла stops) закончен ошибкой")

    if cacheTest.test5():
        print("Тест 5(Считывание из файла stops.txt) выполнен")
    else:
        print("Тест 5(Считывание из файла stops.txt) закончен ошибкой")

    if cacheTest.test6():
        print("Тест 6(Открытие файла sort.txt) выполнен")
    else:
        print("Тест 6(Открытие файла sort.txt) закончен ошибкой")

    if cacheTest.test7():
        print("Тест 7(Считывание файла sort.txt) выполнен")
    else:
        print("Тест 7(Считывание файла sort.txt) закончен ошибкой")
    if cacheTest.test8():
        print("Тест 8(Загрузка ключей) выполнен")
    else:
        print("Тест 8(Загрузка ключей) закончен ошибкой")
    if cacheTest.test9():
        print("Тест 9(Тест функции cache_load) выполнен")
    else:
        print("Тест 9(Тест функции cache_load) закончен ошибкой")
