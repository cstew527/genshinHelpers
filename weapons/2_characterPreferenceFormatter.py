# Original list
data = """
FavoniusLance: 1.00
DragonsBane: 2.00
KitainCrossSpear: 3.00
EngulfingLightning: 4.00
"""

# Process the data
result = {}
for line in data.strip().split("\n"):
    name, value = line.split(":")
    result[name.strip()] = float(value.strip())

# Format as desired output
formatted_result = ", ".join([f'"{key}": {value}' for key, value in result.items()])

print(formatted_result)
