from functools import lru_cache
import json
from collections import defaultdict

# --- Constants ---

# Main Stat Minimums (Level 0)
MIN_MAINS = {
    5: {
        'hp': 717.0, 'atk': 47.0, 'atk_': 7.0, 'enerRech_': 7.8, 'eleMas': 28.0, 'physical_dmg_': 8.7,
        'critRate_': 4.7, 'critDMG_': 9.3, 'cryo_dmg_': 7.0, 'electro_dmg_': 7.0, 'hydro_dmg_': 7.0,
        'pyro_dmg_': 7.0, 'geo_dmg_': 7.0, 'anemo_dmg_': 7.0, 'dendro_dmg_': 7.0, 'hp_': 7.0, 'def_': 8.7,
        'heal_': 5.4
    },
    4: {
        'hp': 645.0, 'atk': 42.0, 'atk_': 6.3, 'enerRech_': 7.0, 'eleMas': 25.2, 'physical_dmg_': 7.9,
        'critRate_': 4.2, 'critDMG_': 8.4, 'cryo_dmg_': 6.3, 'electro_dmg_': 6.3, 'hydro_dmg_': 6.3,
        'pyro_dmg_': 6.3, 'geo_dmg_': 6.3, 'anemo_dmg_': 6.3, 'dendro_dmg_': 6.3, 'hp_': 6.3, 'def_': 7.9,
        'heal_': 4.8
    }
}

# Main Stat Maximums (Level 20 for 5*, Level 16 for 4*)
MAX_MAINS = {
    5: {
        'hp': 4780, 'atk': 311.0, 'atk_': 46.6, 'enerRech_': 51.8, 'eleMas': 187.0, 'physical_dmg_': 58.3,
        'critRate_': 31.1, 'critDMG_': 62.2, 'cryo_dmg_': 46.6, 'electro_dmg_': 46.6, 'hydro_dmg_': 46.6,
        'pyro_dmg_': 46.6, 'geo_dmg_': 46.6, 'anemo_dmg_': 46.6, 'dendro_dmg_': 46.6, 'hp_': 46.6,
        'def_': 58.3, 'heal_': 35.9
    },
    4: {
        'hp': 3571, 'atk': 232.0, 'atk_': 34.8, 'enerRech_': 38.7, 'eleMas': 139.3, 'physical_dmg_': 43.5,
        'critRate_': 23.2, 'critDMG_': 46.4, 'cryo_dmg_': 34.8, 'electro_dmg_': 34.8, 'hydro_dmg_': 34.8,
        'pyro_dmg_': 34.8, 'geo_dmg_': 34.8, 'anemo_dmg_': 34.8, 'dendro_dmg_': 34.8, 'hp_': 34.8,
        'def_': 43.5, 'heal_': 26.8
    }
}

# Substat Maximum Rolls
MAX_SUBS = {
    5: {
        'atk': 19.0, 'eleMas': 23.0, 'enerRech_': 6.5, 'atk_': 5.8, 'critRate_': 3.9, 'critDMG_': 7.8,
        'def': 23.0, 'hp': 299.0, 'def_': 7.3, 'hp_': 5.8
    },
    4: {
        'atk': 16.0, 'eleMas': 19.0, 'enerRech_': 5.2, 'atk_': 4.7, 'critRate_': 3.1, 'critDMG_': 6.2,
        'def': 19.0, 'hp': 239.0, 'def_': 5.8, 'hp_': 4.7
    }
}

ROLL_TIERS = [0.7, 0.8, 0.9, 1.0]


# --- Helpers ---

def get_max_level(rarity):
    return 20 if rarity == 5 else 16


def get_possible_new_substats(artifact):
    rarity = artifact.get('rarity', 5)
    existing_keys = {sub['key'] for sub in artifact['substats']}
    existing_keys.add(artifact['mainStatKey'])
    possible = []
    for key in MAX_SUBS[5].keys():
        if key not in existing_keys:
            possible.append(key)
    return possible


def calculate_score_components(artifact, weights, target_level):
    key = artifact['mainStatKey']
    rarity = artifact.get('rarity', 5)

    main_weight = 3 + target_level / 4
    slot_type = artifact['slotKey'].lower()

    if slot_type == 'flower':
        main_stat_weight = 1.0
    elif slot_type == 'plume':
        main_stat_weight = 1.0
    else:
        main_stat_weight = weights['main_stats'][slot_type].get(key, 0)

    main_weight = main_weight * main_stat_weight if key in ['atk', 'hp'] else main_weight

    sub_weight = 0.0
    count = 0
    valid_sub_keys = MAX_SUBS[5].keys()

    for k, v in sorted(weights['sub_stats'].items(), key=lambda item: item[1], reverse=True):
        if k == key or k not in valid_sub_keys:
            continue
        sub_weight += v * (1 + target_level / 4) if count == 0 else v
        count += 1
        if count == 4:
            break

    total_weight = main_weight + sub_weight
    if total_weight == 0: total_weight = 1

    min_v = MIN_MAINS.get(rarity, MIN_MAINS[5]).get(key, 0)
    max_v = MAX_MAINS.get(rarity, MAX_MAINS[5]).get(key, 0)
    val_at_max = max_v

    max_lvl_denom = 20.0 if rarity == 5 else 16.0
    max_main_denom = max_v - (max_v - min_v) * (1 - target_level / max_lvl_denom)
    if max_main_denom == 0: max_main_denom = 1

    main_score_val = (val_at_max / max_main_denom) * main_stat_weight * main_weight

    return main_score_val, total_weight


def calculate_current_sub_score_raw(artifact, weights):
    rarity = artifact.get('rarity', 5)
    sub_score = 0.0
    for sub in artifact['substats']:
        sub_key = sub['key']
        sub_value = sub['value']
        max_sub_val = MAX_SUBS.get(rarity, MAX_SUBS[5]).get(sub_key)
        if max_sub_val:
            sub_score += (sub_value / max_sub_val) * weights['sub_stats'].get(sub_key, 0)
    return sub_score


def get_upgrade_options(artifact, weights):
    rarity = artifact.get('rarity', 5)
    options = []
    for idx, sub in enumerate(artifact['substats']):
        key = sub['key']
        weight = weights['sub_stats'].get(key, 0)
        max_val = MAX_SUBS.get(rarity, MAX_SUBS[5]).get(key)
        if max_val:
            for tier in ROLL_TIERS:
                val_increase = max_val * tier
                score_increase = (val_increase / max_val) * weight
                options.append((score_increase, idx))
    return options


# --- Core Probability Engine ---

def calculate_exact_probability(start_artifact, weights, target_score=None):
    rarity = start_artifact.get('rarity', 5)
    max_level = get_max_level(rarity)

    # 1. Base Configs
    configurations = []

    def generate_configs(current_art, current_prob):
        num_subs = len(current_art['substats'])
        if num_subs >= 4:
            configurations.append((current_art, current_prob))
            return

        if 'unactivatedSubstats' in current_art and current_art['unactivatedSubstats']:
            next_stat = current_art['unactivatedSubstats'][0]
            new_art = current_art.copy()
            new_art['substats'] = list(current_art['substats']) + [next_stat]
            new_art['unactivatedSubstats'] = current_art['unactivatedSubstats'][1:]
            generate_configs(new_art, current_prob)
            return

        possible_keys = get_possible_new_substats(current_art)
        if not possible_keys:
            configurations.append((current_art, current_prob))
            return

        branch_prob = current_prob * (1.0 / len(possible_keys)) * 0.25

        for key in possible_keys:
            for tier in ROLL_TIERS:
                new_art = current_art.copy()
                max_val = MAX_SUBS.get(rarity, MAX_SUBS[5]).get(key)
                val = max_val * tier
                new_art['substats'] = list(current_art['substats']) + [{'key': key, 'value': val}]
                generate_configs(new_art, branch_prob)

    generate_configs(start_artifact, 1.0)

    # 2. DP
    final_results = defaultdict(lambda: {'total_prob': 0.0, 'variations': defaultdict(float)})

    for idx, (config_art, config_prob) in enumerate(configurations):
        total_intervals = 5 if max_level == 20 else 4
        actions_remaining = total_intervals - (start_artifact['level'] // 4)
        lines_added = len(config_art['substats']) - len(start_artifact['substats'])
        upgrades_remaining = actions_remaining - lines_added

        if upgrades_remaining < 0: upgrades_remaining = 0

        main_score, total_weight = calculate_score_components(config_art, weights, max_level)
        current_raw_sub = calculate_current_sub_score_raw(config_art, weights)

        options = get_upgrade_options(config_art, weights)

        # DP State: { (raw_sub_score, (c0, c1, c2, c3)): probability }
        initial_counts = (0, 0, 0, 0)
        dp = {(current_raw_sub, initial_counts): 1.0}

        for step in range(upgrades_remaining):
            new_dp = defaultdict(float)
            for (score, counts), prob in dp.items():
                for (delta, slot_idx) in options:
                    ns = score + delta

                    # Update counts tuple
                    new_counts_list = list(counts)
                    new_counts_list[slot_idx] += 1
                    new_counts = tuple(new_counts_list)

                    new_dp[(ns, new_counts)] += prob * (1.0 / 16.0)

            # Optimization: Round score in key
            rounded_dp = defaultdict(float)
            for (s, c), p in new_dp.items():
                rounded_dp[(round(s, 6), c)] += p
            dp = rounded_dp

        # Aggregate Results
        # original_keys logic missing in the user snippet, but needed for proper variations logic
        # We'll just skip detailed variation string logic here to keep it compatible with the logic requested

        for (raw_sub, counts), prob in dp.items():
            final_pct = ((main_score + raw_sub) / total_weight) * 100
            final_pct = min(final_pct, 100.0)
            display_score = round(final_pct, 2)

            # Sum total prob for this score
            final_results[display_score]['total_prob'] += prob * config_prob

    return final_results


# --- API Helpers for CSV scripts ---

def get_probability_greater_than(results, target_score):
    """
    Sums the probabilities in results where score >= target_score.
    Returns float (0.0 to 100.0).
    """
    total = 0.0
    for score, data in results.items():
        if score >= target_score - 0.001:  # Epsilon
            total += data['total_prob']
    return total * 100.0


def get_max_main_stat_value(artifact):
    """Returns the main stat value this artifact will have at max level."""
    key = artifact['mainStatKey']
    rarity = artifact.get('rarity', 5)
    return MAX_MAINS.get(rarity, MAX_MAINS[5]).get(key, 0)


def print_report(final_results):
    """
    Prints a formatted table of the simulation results.
    """
    print(f"\n{'Score':<10} | {'Probability':<12}")
    print("-" * 120)

    sorted_scores = sorted(final_results.items(), key=lambda x: x[0], reverse=True)

    for score, data in sorted_scores:
        total_prob = data['total_prob'] * 100.0
        if total_prob < 0.001: continue

        print(f"{score:.2f}%     | {total_prob:.4f}%     |")


# --- Example Usage ---

if __name__ == "__main__":
    # Test Case
    test_artifact = {
        'level': 0,
        'rarity': 4,
        'slotKey': 'plume',
        'mainStatKey': 'atk',
        'substats': [
            {'key': 'def', 'value': 13},
            {'key': 'enerRech_', 'value': 3.6}
        ],
        'unactivatedSubstats': []
    }

    test_weights = {
        'main_stats': {
            'flower': {'hp': 1}, 'plume': {'atk': 1}, 'sands': {'atk_': 1},
            'goblet': {'pyro_dmg_': 1}, 'circlet': {'critRate_': 1}
        },
        'sub_stats': {
            'critRate_': 1.0, 'critDMG_': 1.0, 'atk_': 1.0, 'eleMas': 0.0,
            'enerRech_': 0.0, 'hp': 0, 'hp_': 0, 'def': 0, 'def_': 0, 'atk': 0
        }
    }

    results = calculate_exact_probability(test_artifact, test_weights)
    print_report(results)