# Original list
data = """
KagurasVerity: 1.00
LostPrayerToTheSacredWinds: 1.00
SurfsUp: 2.00
TomeOfTheEternalFlow: 3.00
CashflowSupervision: 3.00
SkywardAtlas: 4.00
MemoryOfDust: 5.00
TulaytullahsRemembrance: 5.00
TheWidsith: 5.00
SolarPearl: 6.00
CranesEchoingCall: 6.00
FlowingPurity: 7.00
DodocoTales: 8.00
"""

# Process the data
result = {}
for line in data.strip().split("\n"):
    name, value = line.split(":")
    result[name.strip()] = float(value.strip())

# Format as desired output
formatted_result = ", ".join([f'"{key}": {value}' for key, value in result.items()])

print(formatted_result)
