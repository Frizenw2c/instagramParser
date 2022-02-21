from os import path
f=open("users/sort.txt","r")
users=[]
miss_users=[]
exist_users=[]
check=False
number_string=0
for name in f:
    if name[:-1]=="++++++++++++++++++++++++++++++++++":
            check=True
            check_string=number_string
    if not(check) and name[:-1]!="++++++++++++++++++++++++++++++++++":
            users.append(name[:-1])

print(users)

f.close()
count=0
for user in users:
    if not (path.exists("D:\\searchdisaner\\jsons\\" + user + ".json")):
        print(user)
        count+=1
        miss_users.append(user)
    else:
        exist_users.append(user)
print(count)
f=open("users/repair_sort.txt",'w')
for exist_user in exist_users:
    f.write(exist_user+'\n')
f.write("++++++++++++++++++++++++++++++++++\n")
for miss_user in miss_users:
    f.write(miss_user+'\n')
