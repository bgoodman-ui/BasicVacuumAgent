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


def vacuum_agent(location, status,points) :

    if location == "A":
        if status == "dirty":
            status = "clean"
            action = "suck"
            points += 10
        else:
            location = "B"
            action = "right"
            points -= 1


    elif location == "B":
        if status == "dirty":
            status = "clean"
            action = "suck"
            points +=  10
        else:
            location = "A"
            action = "left"
            points -= 1
    else:
        raise Exception("Invalid location")
    return location, status, action, points

def run_table(input_rows,use_new_location=False):
    #local declaration for points so it can be reset running the function
    points = 0
    tableg = []
    for row_location, row_status in input_rows:
        new_location, new_status, new_action, points = vacuum_agent(row_location, row_status,points)
        out_location = new_location if use_new_location else row_location
        out_status = new_status if use_new_location else row_status
        tableg.append([out_location, out_status, new_action, points])
        print("Total Points:", points)
    return tableg


table = run_table(rows)
table2 = run_table(RandomRows)
table3 = run_table(RandomRows,use_new_location=True)

def test_agent() :
    print(vacuum_agent("A","dirty",0))
    print(vacuum_agent("A", "clean",0))
    print(vacuum_agent("B", "dirty",0))
    print(vacuum_agent("B", "clean",0))

    print(tabulate(table,headers = ["location","status","action","points"],tablefmt="fancy_grid"))
    print(tabulate(table2,headers = ["location","status","action","points"],tablefmt="fancy_grid"))
    print(tabulate(table3, headers=["location", "status", "action","points"], tablefmt="fancy_grid"))



test_agent()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
