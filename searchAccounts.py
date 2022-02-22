from parsLib.Bot import hastagScraper
from loadData import loadData
"""
old code
    def runSearch(self,login,password):

        countUsers=0
        bot = Bot()
        bot.login(username = login ,password = password ,use_cookie=False)
        hashtags=[]
        f=open('hashtags.txt','r',encoding='utf-8')
        for line in f:
            hashtags.append(line[:-1])
        f.close()
        print (hashtags)
        for hashtag in hashtags:
            users=[]
            users.extend(bot.get_hashtag_users(hashtag))
            users_name=[]

            for user in users:
                users_name.append((bot.get_username_from_user_id(user)))

            posts_link=[]

            f = open('users/users.txt', 'a')
            f.write("--------------------------" + '\n')
            for user_name in users_name:
                f.write(user_name + '\n')
            f.close()
"""
class searchAccounts(object):
    def __init__(self,loadedData):
        self.loadedData=loadedData
        print(self.key_words)
    def runSearch(self,login,password):
        hastagScraper(loadedData)
if __name__=="__main__":
    loadedData=loadData()
    loadedData.loadKeywords()
    loadedData.loadUsers()

    searchAccounts(loadedData)
    searchAccounts.runSearch('',"todoctordoom","$reset->name")