# Original list
data = """
VividNotions: 1.00
ReliquaryOfTruth: 2.00
TomeOfTheEternalFlow: 3.00
SurfsUp: 3.00
KagurasVerity: 4.00
LostPrayerToTheSacredWinds: 5.00
CashflowSupervision: 5.00
CranesEchoingCall: 6.00
TulaytullahsRemembrance: 7.00
TheWidsith: 8.00
SacrificialJade: 8.00
FlowingPurity: 9.00
"""

# Process the data
result = {}
for line in data.strip().split("\n"):
    name, value = line.split(":")
    result[name.strip()] = float(value.strip())

# Format as desired output
formatted_result = ", ".join([f'"{key}": {value}' for key, value in result.items()])

print(formatted_result)
