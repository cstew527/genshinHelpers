from functools import lru_cache
import json

MIN_MAINS = {
    'hp': 717.0, 'atk': 47.0, 'atk_': 7.0, 'enerRech_': 7.8, 'eleMas': 28.0, 'physical_dmg_': 8.7,
    'critRate_': 4.7, 'critDMG_': 9.3, 'cryo_dmg_': 7.0, 'electro_dmg_': 7.0, 'hydro_dmg_': 7.0,
    'pyro_dmg_': 7.0, 'geo_dmg_': 7.0, 'anemo_dmg_': 7.0, 'dendro_dmg_': 7.0, 'hp_': 7.0, 'def_': 8.7,
    'heal_': 5.4
}
MAX_MAINS = {
    'hp': 4780, 'atk': 311.0, 'atk_': 46.6, 'enerRech_': 51.8, 'eleMas': 187.0, 'physical_dmg_': 58.3,
    'critRate_': 31.1, 'critDMG_': 62.2, 'cryo_dmg_': 46.6, 'electro_dmg_': 46.6, 'hydro_dmg_': 46.6,
    'pyro_dmg_': 46.6, 'geo_dmg_': 46.6, 'anemo_dmg_': 46.6, 'dendro_dmg_': 46.6, 'hp_': 46.6,
    'def_': 58.3, 'heal_': 35.9
}
MAX_SUBS = {
    'atk': 19.0, 'eleMas': 23.0, 'enerRech_': 6.5, 'atk_': 5.8, 'critRate_': 3.9, 'critDMG_': 7.8,
    'def': 23.0, 'hp': 299.0, 'def_': 7.3, 'hp_': 5.8
}


@lru_cache(maxsize=1)
def get_main_stat_db():
    with open('main_stat_data.json', 'r') as f:
        return json.load(f)


def main_stat_value(artifact):
    main_stat_db = get_main_stat_db()
    num_stars = str(artifact['rarity'])
    main_stat_key = artifact['mainStatKey']
    level = artifact['level']
    return main_stat_db[num_stars][main_stat_key][level]


def has_unactivated_substats(artifact):
    """Check if artifact has unactivated substats"""
    return ('unactivatedSubstats' in artifact and
            any(substat['key'] for substat in artifact['unactivatedSubstats']))


def process_artifact_with_unactivated_substats(artifact):
    """Process artifact with unactivated substats by treating it as level 4"""
    if not has_unactivated_substats(artifact):
        return artifact

    # Create a copy of the artifact to avoid modifying the original
    processed_artifact = artifact.copy()

    # Set level to 4 for calculation purposes
    processed_artifact['level'] = 4

    # Find the first valid unactivated substat
    unactivated_substats = artifact.get('unactivatedSubstats', [])
    valid_unactivated = None

    for substat in unactivated_substats:
        if substat['key'] and substat['key'] in MAX_SUBS:
            valid_unactivated = substat.copy()
            break

    # If we found a valid unactivated substat, add it to the 4th slot
    if valid_unactivated:
        # Create a new substats list
        new_substats = []

        # Add existing activated substats
        for substat in artifact.get('substats', []):
            if substat['key']:  # Only add if key is not empty
                new_substats.append(substat.copy())

        # Add the unactivated substat if we have less than 4 substats
        if len(new_substats) < 4:
            new_substats.append(valid_unactivated)

        processed_artifact['substats'] = new_substats

    return processed_artifact


def rate(artifact, weight):
    # validate_weights(weight)

    # Check for unactivated substats and process accordingly
    if has_unactivated_substats(artifact):
        artifact = process_artifact_with_unactivated_substats(artifact)
        # print(f"Processing artifact with unactivated substats at level {artifact['level']}")

    value = main_stat_value(artifact)
    key = artifact['mainStatKey']
    level = artifact['level']

    # Main stat score
    main_score = 0.0
    sub_score = 0.0
    sub_weight = 0.0
    main_weight = 3 + level / 4

    # Get the slot type (goblet, sands, circlet)
    slot_type = artifact['slotKey'].lower()

    # Handle fixed main stats for flower and plume
    if slot_type == 'flower':
        main_stat_weight = 1.0  # Flower always has HP
    elif slot_type == 'plume':
        main_stat_weight = 1.0  # Plume always has ATK
    else:
        main_stat_weight = weight['main_stats'][slot_type].get(key, 0)

    # Calculate main stat score
    max_main = MAX_MAINS[key] - (MAX_MAINS[key] - MIN_MAINS[key]) * (1 - level / 20.0)
    main_score = (value / max_main) * main_stat_weight * main_weight
    main_weight = main_weight * main_stat_weight if key in ['atk', 'hp'] else main_weight

    # Rest of your substat calculation remains the same
    count = 0
    for k, v in sorted(weight['sub_stats'].items(), key=lambda item: item[1], reverse=True):
        if k == key or k not in MAX_SUBS:
            continue
        sub_weight += v * (1 + level / 4) if count == 0 else v
        count += 1
        if count == 4:
            break

    for sub in artifact['substats']:
        sub_key = sub['key']
        sub_value = sub['value']
        if sub_key in MAX_SUBS:
            sub_score += (sub_value / MAX_SUBS[sub_key]) * weight['sub_stats'].get(sub_key, 0)

    # Final score calculation
    total_weight = main_weight + sub_weight
    score = ((main_score + sub_score) / total_weight * 100) if total_weight > 0 else 100
    score = min(score, 100)  # Cap score at 100

    # Normalize main and sub scores for display
    main_score = min((main_score / main_weight * 100) if main_weight > 0 else 100, 100)
    sub_score = min((sub_score / sub_weight * 100) if sub_weight > 0 else 100, 100)

    # Print or return as needed
    # print(f'Gear Score: {score:.2f}% (main {main_score:.2f}% {main_weight}, sub {sub_score:.2f}% {sub_weight})')
    print(score, main_stat_value(artifact))
    return score, main_stat_value(artifact)


def validate_weights(weights):
    # Valid main stat keys for each slot
    valid_main_stats = {
        'flower': ['hp'],
        'plume': ['atk'],
        'sands': ['hp_', 'atk_', 'def_', 'eleMas', 'enerRech_'],
        'goblet': ['hp_', 'atk_', 'def_', 'eleMas', 'physical_dmg_', 'pyro_dmg_',
                   'hydro_dmg_', 'cryo_dmg_', 'electro_dmg_', 'anemo_dmg_',
                   'geo_dmg_', 'dendro_dmg_'],
        'circlet': ['hp_', 'atk_', 'def_', 'eleMas', 'critRate_', 'critDMG_', 'heal_']
    }

    # Valid substat keys
    valid_sub_stats = ['hp', 'hp_', 'atk', 'atk_', 'def', 'def_', 'eleMas',
                       'enerRech_', 'critRate_', 'critDMG_']

    # Check if required top-level keys exist
    if not all(key in weights for key in ['main_stats', 'sub_stats']):
        raise ValueError("Weights must contain 'main_stats' and 'sub_stats' keys")

    # Validate main stats
    for slot in weights['main_stats']:
        if slot not in valid_main_stats:
            raise ValueError(f"Invalid slot type: {slot}")

        for stat in weights['main_stats'][slot]:
            if stat not in valid_main_stats[slot]:
                raise ValueError(f"Invalid main stat '{stat}' for slot '{slot}'")

    # Validate sub stats
    for stat in weights['sub_stats']:
        if stat not in valid_sub_stats:
            raise ValueError(f"Invalid sub stat: {stat}")

    return True