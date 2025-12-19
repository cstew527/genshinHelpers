from collections import defaultdict
from statistics import mean

weapon_data = """
1. TheFirstGreatMagic, AstralVulturesCrimsonPlumage
2. AquaSimulacra
3. ThunderingPulse
4. SkywardHarp
5. AmosBow
6. PolarStar, SongOfStillness, PrototypeCrescent
"""

weapon_list = []
for line in weapon_data.strip().split('\n'):
    try:
        parts = line.split('. ', 1)  # Split into rank and weapons
        rank = int(parts[0])
        # Split weapon string by commas and strip whitespace
        weapons = [w.strip() for w in parts[1].split(',')]
        for weapon in weapons:
            weapon_list.append((rank, weapon))
    except (ValueError, IndexError):
        print(f"Skipping malformed line: {line}")
        continue

weapon_ranks = defaultdict(list)
for rank, weapon in weapon_list:
    weapon_ranks[weapon].append(rank)

averages = {weapon: mean(ranks) for weapon, ranks in weapon_ranks.items()}
sorted_weapons = sorted(averages.items(), key=lambda item: item[1])

for weapon, avg_rank in sorted_weapons:
    print(f"{weapon}: {avg_rank:.2f}")