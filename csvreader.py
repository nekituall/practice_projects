

# csv reader
# @nekituall

names = {}

with open("Export.csv", "r") as f:
    for data in f:
        datarow = data.strip().split(",")
        # print(datarow)
        names[datarow[0]] = datarow[1:]

print(names)

city = input("Input city => ")
state = input("Input state => ")

for value in names.values():
    if value[8] == city and value[9] == state:
        print("Market:", value[0], "- has coordinates:", value[19:21])

