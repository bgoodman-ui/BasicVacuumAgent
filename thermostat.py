from tabulate import tabulate

#rules
#Temperature < 68°F -> Heat
#Temperature > 75°F -> Cool
#Otherwise -> do nothing
#goal is for the room to be in the ideal temperature range, and for the thermostat to change to energy saving
#mode if the room is not occupied

def thermo_agent(temp):
    if temp < 68 :
        print("heat")
    elif temp > 75 :
        print("cool")
    else :
        print("do nothing")



print("Hello thermostat")
thermo_agent(65)
thermo_agent(78)
thermo_agent(70)