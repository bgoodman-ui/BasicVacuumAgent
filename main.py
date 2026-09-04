from tabulate import tabulate
import random

rows = [
    ["A","dirty"],
    ["B","clean"],
    ["A","clean"],
    ["B","dirty"]
]


RamdomRowNumber = random.randint(1,38)
locations = ["A","B"]
statuses = ["clean", "dirty"]
RandomRows = [[random.choice(locations),random.choice(statuses)]for _ in range(RamdomRowNumber)]

headers = ["location","status"]


#test print starting tables
#print(tabulate(rows, headers = headers,tablefmt="fancy_grid"))
#print(tabulate(RandomRows, headers = headers,tablefmt="fancy_grid"))


def vacuum_agent(location, status) :
    if location == "A":
        if status == "dirty":
            status = "clean"
            action = "suck"

        else:
            location = "B"
            action = "right"


    elif location == "B":
        if status == "dirty":
            status = "clean"
            action = "suck"
        else:
            location = "A"
            action = "left"
    else:
        raise Exception("Invalid location")
    return location, status, action


table = []
table2 = []
#still compiles if variables are just named location, status but gives a warning
for row_location,row_status in rows:
    new_location,new_status,new_action = vacuum_agent(row_location,row_status)
    table.append([row_location,row_status,new_action])

for row_location,row_status in RandomRows:
    new_location,new_status,new_action = vacuum_agent(row_location,row_status)
    table2.append([row_location,row_status,new_action])

def test_agent() :
    print(vacuum_agent("A","dirty"))
    print(vacuum_agent("A", "clean"))
    print(vacuum_agent("B", "dirty"))
    print(vacuum_agent("B", "clean"))

    print(tabulate(table,headers = ["location","status","action"],tablefmt="fancy_grid"))
    print(tabulate(table2,headers = ["location","status","action"],tablefmt="fancy_grid"))


test_agent()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
