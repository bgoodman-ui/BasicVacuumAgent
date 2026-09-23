from tabulate import tabulate

#rules
#Temperature < 68°F -> Heat
#Temperature > 75°F -> Cool
#Otherwise -> do nothing
#goal is for the room to be in the ideal temperature range, and for the thermostat to change to energy saving
#mode if the room is not occupied

#actuators-adjust heat, activate heat,turn air conditioning on, turn air conditioning off
#sensors-occupancy status, temp sensor, humidity sensor.

#1 means the room is occupied and 0 means unoccupied
#third column is humidity 30% to 50% is healthy after 50 is when the dehumidifier needs to be turned on
thermo_rows = [
    [1,89,33],
    [0,53,58],
    [1,70,52],
    [0,79,37]
]


def thermo_agent(occupancy_status,temp,humidity):
    if temp < 68 :
        print("heat")
    elif temp > 75 :
        print("cool")
    else :
        print("do nothing")



print("Hello thermostat")
thermo_agent(1,65)
thermo_agent(0,78)
thermo_agent(1,70)