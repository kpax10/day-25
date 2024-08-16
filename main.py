# with open("weather_data.csv", 'r') as data_file:
#     data = data_file.read().splitlines()
#     print(data)

# import csv
#
# with open("weather_data.csv", 'r') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data['condition'])

# data_dict = data.to_dict()
# print(data_dict)

# print(data["temp"].tolist())

# temp_data = data["temp"].to_list()
# average = sum(temp_data) / len(temp_data)
# print(average)

# temps = pandas.Series(temp_data)
# print(temps.mean())

# max_temp = data["temp"].max()
# print(max_temp)

# print(data[data.day == 'Monday'])

# print(data['temp'].max())
# max_temp_row = data[data.temp == data.temp.max()]
# print(max_temp_row)

# monday = data[data.day == 'Monday']
# monday_temp = monday.temp
# monday_in_f = (monday.temp * 1.8) + 32
# print(monday_in_f)

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("students.csv")