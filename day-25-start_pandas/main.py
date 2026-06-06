# with open("weather_data.csv") as data_file:
#     data = data_file.read()
#     print(data)

# import csv
#
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)


import pandas

data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
temp_list = data["temp"].to_list()

# print(data["temp"].mean())
# print(data["temp"].max())
#
#get data in column
# print(data.condition)

#get data in row
print(data[data.day == "Monday"])

# # print(data[data.temp == data["temp"].max()])
#
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp*9/5+32
# print(monday_temp_F)


#create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("student_data.csv", index=False)

# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260516.csv")
# fur_data =data["Primary Fur Color"]
# fur_list = fur_data.to_list()
# gray = 0
# cinnamon = 0
# black = 0
#
# for color in fur_list:
#     if color == "Black":
#         black += 1
#     elif color == "Gray":
#         gray += 1
#     elif color == "Cinnamon":
#         cinnamon += 1
#
# fur_dict = {
#     "Fur Color": ["Black", "Gray", "Cinnamon"],
#     "Count": [black, gray, cinnamon],
# }
# new_data = pandas.DataFrame(data=fur_dict)
# new_data.to_csv("Fur Color.csv")
