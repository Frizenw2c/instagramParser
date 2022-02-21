class sortUsers(object):
    def sort(self):
        f=open("users/users.txt",'r')
        array_names_users=[]
        array_names_sort=[]
        new_names=[]
        for line in f:
            array_names_users.append(line[:])
        f.close()
        f=open("users/sort.txt",'r')
        for line in f:
            array_names_sort.append(line[:])
        for name in array_names_users:
            if  not (name in new_names) and not(name in array_names_sort) and name!='--------------------------\n':

                new_names.append(name)
        f.close
        f=open("users/sort.txt",'a')

        for user_name in new_names:
            f.write(user_name)
        f.close()

if __name__=='__main__':
    sortUsers.sort('')