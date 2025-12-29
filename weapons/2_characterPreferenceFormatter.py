# Original list
data = """
SerpentSpine: 1.00
RedhornStonethresher: 1.00
AThousandBlazingSuns: 1.00
Verdict: 1.00
BeaconOfTheReedSea: 2.00
FruitfulHook: 3.00
WolfsGravestone: 3.00
Rainslasher: 3.00
MailedFlower: 4.00
LithicBlade: 4.00
TheUnforged: 4.00
TidalShadow: 5.00
UltimateOverlordsMegaMagicSword: 5.00
MakhairaAquamarine: 5.00
"""

# Process the data
result = {}
for line in data.strip().split("\n"):
    name, value = line.split(":")
    result[name.strip()] = float(value.strip())

# Format as desired output
formatted_result = ", ".join([f'"{key}": {value}' for key, value in result.items()])

print(formatted_result)
