from tabulate import tabulate
import pandas
import random




#global for calculating global score across tables
total_score = 0

rows = [
    ["A","dirty"],
    ["B","clean"],
    ["A","clean"],
    ["B","dirty"]
]


RamdomRowNumber = random.randint(1,12)
locations = ["A","B"]
statuses = ["clean", "dirty"]
RandomRows = [[random.choice(locations),random.choice(statuses)]for _ in range(RamdomRowNumber)]

headers = ["location","status"]


#test print starting tables
#print(tabulate(rows, headers = headers,tablefmt="fancy_grid"))
#print(tabulate(RandomRows, headers = headers,tablefmt="fancy_grid"))


def vacuum_agent(location, status,points) :
    global total_score
    if location == "A":
        if status == "dirty":
            status = "clean"
            action = "suck"
            points += 10
            total_score += 10
        else:
            location = "B"
            action = "right"
            points -= 1
            total_score -= 1


    elif location == "B":
        if status == "dirty":
            status = "clean"
            action = "suck"
            points +=  10
            total_score += 10
        else:
            location = "A"
            action = "left"
            points -= 1
            total_score -= 1
    else:
        raise Exception("Invalid location")
    return location, status, action, points

def run_table(input_rows,use_new_location=False):
    #local declaration for points so it can be reset running the function
    points = 0
    #resets everytime run_table is called
    table_score = 0
    tableg = []
    for row_location, row_status in input_rows:
        new_location, new_status, new_action, points = vacuum_agent(row_location, row_status,points)
        out_location = new_location if use_new_location else row_location
        out_status = new_status if use_new_location else row_status
        tableg.append([out_location, out_status, new_action, points])
        table_score = points
    return tableg, table_score

#check if all room in table are clean
def check_rooms(input_rows):
    #room status column number
    roomcheck = 1
    all_clean = all(row[roomcheck] == "clean" for row in input_rows)
    return "all clean" if all_clean else "not all clean"





def test_agent() :
    print(vacuum_agent("A","dirty",0))
    print(vacuum_agent("A", "clean",0))
    print(vacuum_agent("B", "dirty",0))
    print(vacuum_agent("B", "clean",0))

    table, table_score = run_table(rows)
    print(tabulate(table,headers = ["location","status","action","points"],tablefmt="fancy_grid"))
    print("Table score", table_score)
    print("Total Score: ", total_score)
    print(check_rooms(table))

    table2, table_score = run_table(rows,use_new_location=True)
    print(tabulate(table2, headers=["location", "status", "action", "points"], tablefmt="fancy_grid"))
    print("Table score", table_score)
    print("Total Score: ", total_score)
    print(check_rooms(table2))

    table3, table_score = run_table(RandomRows)
    print(tabulate(table3, headers = ["location","status","action","points"],tablefmt="fancy_grid"))
    print("Table score", table_score)
    print("Total Score: ", total_score)
    print(check_rooms(table3))

    #doing what it is supposed to table to technically run again so total score is calculated again
    table4, table_score = run_table(RandomRows,use_new_location=True)
    print(tabulate(table4, headers=["location", "status", "action","points"], tablefmt="fancy_grid"))
    print("Table score", table_score)
    print("Total Score: ", total_score)
    print(check_rooms(table4))


test_agent()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
