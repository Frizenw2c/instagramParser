import zipfile
import os.path
class archive():
    def __init__(self,name_archive):
        self.path_to_users="jsons\\"
        path_to_archive_dump="archive_dump\\"
        self.name_archive=name_archive
        if os.path.exists(path_to_archive_dump+self.name_archive):
            self.path_to_archive=path_to_archive_dump+self.name_archive
        else:
            archive=zipfile.ZipFile(path_to_archive_dump + self.name_archive,mode="w")
            archive.close()
            self.path_to_archive = path_to_archive_dump + self.name_archive
    def get_archived_names(self):
        filenames=[]
        try:
            archive= zipfile.ZipFile(self.path_to_archive,mode='r')
        except:
            print("Неудалось открыть архив")

        for file_info in archive.infolist():
            filename, tresh = file_info.filename.split('.json')
            tresh, filename = filename.split('jsons/')
            filenames.append(filename)

        archive.close()
        return filenames

    def check_exist_in_archive(self,names):
        not_exist_names=[]
        filenames=[]
        print('names',names)
        try:
            archive= zipfile.ZipFile(self.path_to_archive,mode='r')
        except:
            print("Неудалось открыть архив")

        for file_info in archive.infolist():
            filename, tresh = file_info.filename.split('.json')
            tresh, filename = filename.split('jsons/')
            filenames.append(filename)
        for name in names:
            if not(name in filenames):
                not_exist_names.append(name)
        archive.close()

        return not_exist_names
    def archivation(self,names=[]):
        names=self.check_exist_in_archive(names)

        try:
            archive= zipfile.ZipFile(self.path_to_archive,mode='a')
        except:
            archive = zipfile.ZipFile(self.path_to_archive, mode='w')
        for name in names:
            archive.write(self.path_to_users+name+".json")
        archive.close()
    def dearchivation(self,key,names=[]):
        """
        :param key:all/names
        :param names:array names
        :return:

        """
        archive= zipfile.ZipFile(self.path_to_archive,mode='r')
        info_list=archive.infolist()
        if key=="all":
            for file_info in info_list:
                print("extract:", file_info.filename)
                print(archive.extract(member=file_info))
        elif key=="names":
            for file_info in info_list:
                filename, tresh = file_info.filename.split('.json')
                tresh, filename = filename.split('jsons/')
                if filename in names:
                    print("extract:",filename)
                    print(archive.extract(member=file_info))
        else:
            print("key,Ключ неверен")
    def get_names_archive(self):
        """
        :return:Выдает список имен находящихся в архиве
        """
        print(self.path_to_archive)
        archive=zipfile.ZipFile(self.path_to_archive,mode='r')
        info_list=archive.infolist()
        filenames=[]
        for file_info in info_list:
            filename, tresh = file_info.filename.split('.json')
            tresh, filename = filename.split('jsons/')
            filenames.append(filename)
        return filenames
    def reload_archive(self):
        if os.path.isfile(self.path_to_archive):
            os.remove(self.path_to_archive)
            print("success", self.path_to_archive)
        else:
            print("File doesn't exists!", self.path_to_archive)
        archive = zipfile.ZipFile(self.path_to_archive, mode="w")
        archive.close()
if __name__ == "__main__":
    """
    @Пример инициализации класса
    archive=archive("big_dump.zip")
    """
    """
    @Пример использования archivation
    archive.archivation(["abkartun","abmokeeva.design","aboitajikistan"])
    """
    """
    @Пример использования dearchivation
    :param key:names
    archive.dearchivation(key="names",names=["abkartun","abmokeeva.design"])
    """
    """
    @Пример использования dearchivation
    :param key:all
    archive.dearchivation(key="all")
    """
    """
    @Пример использования  get_names_archive()
    :return: array[name0,name1,...]
    filenames=archive_garbage.get_names_archive()
    """
    archive_useful_items = archive(name_archive="test_archive.zip")
    archive_garbage_items = archive(name_archive="test_garbage_archive.zip")
    archive_garbage_items.dearchivation(key="all")
    archive_useful_items.dearchivation(key="all")