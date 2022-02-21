import re
import json
import pyexcel
def get_clean_word(word: str) -> str:
    word = re.sub('[^a-zа-яё-]', '', word, flags=re.IGNORECASE)
    word = word.strip('-')
    word = word.lower()
    return word
def insertion_sort(countWords):
    for i in range(1, len(countWords)):
        item_to_insert = countWords[i]
        j = i - 1
        while j >= 0 and countWords[j]['countWords'] > item_to_insert['countWords']:
            countWords[j + 1] = countWords[j]
            j -= 1
        countWords[j + 1] = item_to_insert
    return countWords
#Config data
count=0
max_count=10000
count_chars=2
array_ignor=['по','на','для','не','из','за','все','всей','более','цены','пиши','под','нет','нас','доставка','до',
'от','лет','наличии','как','вопросам','работаем','здесь','привет','пишите','ссылку','со','или','без','in','and','всем','жизни'
'подход','вашего','мы','надзор','наш','только','день','твой','миру','запись','года','всему','решения','ваш','вас','нами','нам'
'ссылке','вы','ул','тут','for','of',]
#End config data
f= open('key words.txt','r',encoding='utf-8')
key_words=[]
for line in f:
    key_words.append(line[:-1])
print(key_words)
f.close()
stops = ['\u0491', '\u0454', '\u0456', '\u0457']
f = open('stop words.txt', 'r', encoding='utf-8')
for line in f:
    stops.append(line[:-1])

f.close()
print(stops)
f=open('users/sort.txt','r')
users=[]
all_words=[]
check_words=[]
for name in f:
    if name[:-1]!='--------------------------' and name[:-1]!='---------------------------':
        if name[:-1]=="++++++++++++++++++++++++++++++++++":
            break
        if name[:-1] != "++++++++++++++++++++++++++++++++++":
                users.append(name[:-1])
                count+=1
        if count==max_count:
            break

f.close

for user in users:
    array_data = []
    f = open('jsons/' + user + '.json', 'r', encoding='utf-8')
    text = json.load(f)
    f.close()
    if text == {}:
        continue
    try:
        biograph = text['graphql']['user']['biography']
        fullname = text['graphql']['user']['full_name']
        username = text['graphql']['user']['username']
    except:
        continue
    check_stop=False
    check_keyword=False
    for stop in stops:
        if stop.lower() in biograph.lower() or stop.lower() in fullname.lower():
            check_stop = True
            break
    for key_word in key_words:
        if key_word.lower() in biograph.lower():
            check_keyword=True
            break
    if not check_stop and check_keyword:
        words = biograph.replace('\n',' ').split(' ')
        words = [get_clean_word(word) for word in words]
        words=[word for word in words if not (word in array_ignor)  and not (len(word) <count_chars)]

        all_words.extend(words)
countWords=[]
for word in all_words:
    if word not in check_words:
        countWords.append({'word':word,'countWords':all_words.count(word)})
        check_words.append(word)


countWords=insertion_sort(countWords)[::-1]
data=[['word','count']]


for i in range(len(countWords)):
    if countWords[i]['countWords']<=10:
        break
    for j in range(i+1,len(countWords)):
        if countWords[i]['word'] in countWords[j]['word'] and str(countWords[i]['word'])!='тел' :
            countWords[i]['countWords']+=countWords[j]['countWords']
            countWords[j]['countWords']=0
            countWords[j]['word']=''
countWords=insertion_sort(countWords)[::-1]
for line in countWords:
    if line['word']!='' and line['countWords']!=0:
        data.append([line['word'],line['countWords']])
pyexcel.save_as(array=data, dest_file_name="data/vizualize.xlsx")