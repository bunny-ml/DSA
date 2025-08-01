# link = "https://onedrive.live.com/?redeem=aHR0cHM6Ly8xZHJ2Lm1zL3QvYy82ZjYyNTBhOGZlZTczMTMwL0VlX0xVcl9wU2ZGRXN4ODJEZFdpbHpRQmhaTGt2U2tKVGZDSW5kdnV2TEp5MXc&cid=6F6250A8FEE73130&id=6F6250A8FEE73130%21sbf52cbef49e944f1b31f360dd5a29734&parId=6F6250A8FEE73130%21s1da8476ec71f48119cc0b3e157f90bc6&o=OneUp"

events = [
    (1, "Singing", 10),
    (2, "Painting", 8),
    (3, "Quiz", 12),
    (4, "Dance", 6)
]


class solution_to_question_1:


    def __init__(self , data ):
        self.data = data
        self.__data = []

    def convert_to_list(self):
        k = len(self.data)
        for i in range(k):
            self.__data.append(list(self.data[i]))
        return self.__data 

    def display(self, id):
        l = len(self.data)
        for i in range(l):
            if id == self.__data[i][0]:
                # print(self.data[i])
                return self.__data[i]


    def add_event(self):
        id_1 = int(input("Enter the ID number"))
        event_name = str(input("Enter the event Name"))
        participants = int(input("Enter the number of participants"))
        if id_1 and  event_name and participants :
            self.__data.append((id_1 , event_name , participants))
            return self.__data
        else:
            print("Invalid input.")
            return self.__data
            
    def remove_event(self):
        id_1 = int(input("Enter the event ID: "))
        index = -1
        for i in range(len(self.__data)):
            if id_1 == self.__data[i][0]:
                index = i 
        if index != -1:
            removed = self.__data.pop(index)
        else:
            print("Error! no Element will be reomved ")
        return self.__data

sol = solution_to_question_1(events)

# converted = sol.convert_to_list()
# print(f"converted to list: ", converted)
# print("")

# displayed = sol.display(2)
# print(f"display events : {displayed}")
# print("")

# data = sol.remove_event()
# print(f"data removed and we left with :{data}")
# print("")

# added_events = sol.add_event()
# print(f"added_events in events list :{added_events}")
# print("")


"""
    sets 
"""
data_1 = {"abhi" , 'aryaman'}

class solution_to_question_2:
    def __init__(self, data):
        self.__data = data

    def add_data_to_set(self):
        name = str(input("Enter the names of participants: "))
        self.__data.add(name)
        return self.__data

    def check_if_person_in_set(self):
        value = False
        name = str(input("Enter the name of person: "))
        for i in self.__data:
            if name == i:
                value = True
        return f"person is already registered: {value}"

    def remove_participant(self):
        value = False
        name = str(input("Enter the name of participant: "))
        index = -1
        for i in self.__data:
            if i == name:
                index = i
        if index:
            value = True
            self.__data.remove(name)
        else:
                print("Error! user may not exist in set ")
        return f"user removed from set {value} and remaaining set are {self.__data}"

    def display(self):
            return (f"{self.__data}")



sol_2 = solution_to_question_2(data_1)

# print(f"added data to set: {sol_2.add_data_to_set()}")
# print("")

# print(f"{sol_2.check_if_person_in_set()}")
# print("")

# print(f"{sol_2.remove_participant()}")
# print("")

# print(sol_2.display())


data_2 = {
    1: ["Alice", "Bob"],
    2: ["Charlie"],
    3: [],
    4: ["Eve", "Mallory"]
}

class solution_to_question_3:
    def __init__(self , data):
        self.__data = data

    def add_participant(self):
        id_1 = int(input("Enter the ID: "))
        name = str(input("Enter the name: "))
        if id_1 in self.__data:
            
        self.__data[id_1] = [name]
        return self.__data

    def check_participant(self):
        value = False
        name = str(input("Enter the name: "))
        for event_id , participants in self.__data.items():
            if name in participants:
                value =True
        return f"Is name in the dictionar : {value}"

        


sol_3 = solution_to_question_3(data_2)

# print(f"{sol_3.add_participant()}")

# print(f"{sol_3.check_participant()}")
