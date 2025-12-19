# Original list
data = """
TheFirstGreatMagic: 1.00
AstralVulturesCrimsonPlumage: 1.00
AquaSimulacra: 2.00
ThunderingPulse: 3.00
SkywardHarp: 4.00
AmosBow: 5.00
PolarStar: 6.00
SongOfStillness: 6.00
PrototypeCrescent: 6.00
"""

# Process the data
result = {}
for line in data.strip().split("\n"):
    name, value = line.split(":")
    result[name.strip()] = float(value.strip())

# Format as desired output
formatted_result = ", ".join([f'"{key}": {value}' for key, value in result.items()])

print(formatted_result)
