from cache import cache
from loadData import loadData
import numpy as np
import pandas
class stats():
    def __init__(self,save_data,keywords):
        self.save_data=save_data
        self.keywords=keywords

    def get_final_mark(self,result):
        total_arr={"username":[],"mark":[]}
        total_arr["username"]=result["followers"]["username"]

        foll_marks=np.array(result["followers"]["mark"])
        keys_marks=np.array(result["key_compares"]["mark"])
        full_marks=np.array(result["fullness"]["mark"])

        sum_marks=(foll_marks+keys_marks+full_marks)//3
        for mark in sum_marks:
            total_arr["mark"].append(mark)
        return total_arr

    def generate_weights_marks(self,count):
        out = []
        if count < 5:
            for index in range(count+1):
                out.append(index / count)
            while len(out)<5:
                out.insert(0,0)
        else:
            elements = []
            for index in range(count+1):
                elements.append(index / count)
            index_third = int(count / 2)
            index_second = int(count / 4)
            index_four = index_third + index_second
            out = [elements[0], elements[index_second], elements[index_third], elements[index_four],
                   elements[count]]
        return out


    def get_score_on_follower(self):
        numbers={"number":[],"username":[],"weight":[],"mark":[]}
        count_weight=[]
        for index in range(len(self.save_data["count_followed_by"])):
            if not (self.save_data["count_followed_by"][index] in numbers["number"]):
                count_numbers=self.save_data["count_followed_by"].count(self.save_data["count_followed_by"][index])
                numbers["number"].append(self.save_data["count_followed_by"][index])
                numbers["weight"].append(count_numbers)
                numbers["username"].append(self.save_data["username"][index])
            else:
                numbers["number"].append(self.save_data["count_followed_by"][index])
                numbers["weight"].append(count_numbers)
                numbers["username"].append(self.save_data["username"][index])


        length_numbers=len(numbers["number"])
        average_sum=np.average(numbers["number"],weights=numbers["weight"])
        for index in range(1,4):
            count_weight.append(int(average_sum/index))
        sorted_numbers=sorted(numbers["number"])
        count_weight.append(sorted_numbers[(length_numbers//2)-1])
        count_weight.append(sorted_numbers[(length_numbers // 4) - 1])

        for index in range(len(numbers["username"])):
            if numbers["number"][index] <=count_weight[4]:
                numbers["mark"].append(0)
            elif numbers["number"][index]<=count_weight[3] and numbers["number"][index]>count_weight[4]:
                numbers["mark"].append(1)
            elif numbers["number"][index]<=count_weight[2] and numbers["number"][index]>count_weight[3]:
                numbers["mark"].append(2)
            elif numbers["number"][index]<=count_weight[1] and numbers["number"][index]>count_weight[2]:
                numbers["mark"].append(3)
            elif numbers["number"][index]<=count_weight[0] and numbers["number"][index]>count_weight[1]:
                numbers["mark"].append(4)
            elif numbers["number"][index]>=count_weight[0]:
                numbers["mark"].append(5)
            else:print(numbers["number"][index])

        return numbers

    def get_score_fullness(self):
        """
        Проверяет заполненность информации пользователя
        :return:
        """
        score={"username":[],"mark":[]}
        weight={"biograph":1,"email":1,"phone":2,"site":1}
        for index in range(len(self.save_data["username"])):
            mark=0
            if 10<len(self.save_data["biography"][index]):
                mark+=1*weight["biograph"]
            if self.save_data["email"][index]!='':
                mark+=1*weight["email"]
            if self.save_data['phone'][index]!='':
                mark+=1*weight["phone"]
            if self.save_data['site'][index]!='':
                mark+=1*weight["site"]
            score["username"].append(self.save_data["username"][index])
            score["mark"].append(mark)

        return score
    def sortByMark(self,data):
        return data["mark"]
    def get_score_key_compares(self):
        score={
            "username":[],
            "mark":[],
            "count_user_keys":[]
        }
        count_keys=len(self.keywords)
        for index in range(len(self.save_data["username"])):
            count_user_keys=0
            for keyword in self.keywords:
                if keyword.lower() in self.save_data["biography"][index].lower():
                    count_user_keys+=1
            score["count_user_keys"].append(count_user_keys)
            score["username"].append(self.save_data["username"][index])
        weights_marks=self.generate_weights_marks(count_keys)
        weights_marks.reverse()
        for index in range(len(score["username"])):
            mark=5
            for weight_mark in weights_marks:
                if weight_mark <= score["count_user_keys"][index]/count_keys:
                    score["mark"].append(mark)
                    break;
                else:
                    mark-=1


        return score
    def saveToExcel(self,data):
        data_pandas_data = pandas.DataFrame(data)
        data_pandas_data= data_pandas_data.sort_values("mark" ,ascending=False)
        # Save the array to a file
        print(data_pandas_data.to_excel("data/fulldata with mark.xlsx"))
    def stats_controller(self):
        result={"followers":[],"fullness":[],"key_compares":[]}
        result["followers"]=self.get_score_on_follower()
        result["fullness"]=self.get_score_fullness()
        result["key_compares"]=self.get_score_key_compares()

        result_final_mark=self.get_final_mark(result)
        data={"fullname":save_data["fullname"],"username":save_data["username"],"biography":save_data["biography"],"count_followed_by":save_data["count_followed_by"],
              "email":save_data["email"],"phone":save_data["phone"],"site":save_data["site"],"mark":result_final_mark["mark"]}

        self.saveToExcel(data)
        print()
if __name__ == "__main__":
    data_container = loadData()
    data_container.loadAll()
    loaded = data_container.checkLoad("all")
    addinfo=data_container.getOption("addinfo")
    cache_obj = cache(data_container, loaded)

    sort_data=cache_obj.cache_load()

    save_data=cache_obj.get_save_data()
    save_data=cache_obj.get_cache_and_sorted_data(addinfo)

    """
    
    """
    stats_obj = stats(save_data,data_container.getOption("key_words"))
    stats_obj.stats_controller()