# Original list
data = """
VividNotions: 1.00
ReliquaryOfTruth: 2.00
KagurasVerity: 3.00
LostPrayerToTheSacredWinds: 4.00
CranesEchoingCall: 5.00
TomeOfTheEternalFlow: 6.00
SurfsUp: 6.00
CashflowSupervision: 6.00
TulaytullahsRemembrance: 7.00
TheWidsith: 8.00
SkywardAtlas: 8.00
SacrificialJade: 9.00
SolarPearl: 10.00
BlackcliffAgate: 10.00
DawningFrost: 10.00
FlowingPurity: 10.00
"""

# Process the data
result = {}
for line in data.strip().split("\n"):
    name, value = line.split(":")
    result[name.strip()] = float(value.strip())

# Format as desired output
formatted_result = ", ".join([f'"{key}": {value}' for key, value in result.items()])

print(formatted_result)
