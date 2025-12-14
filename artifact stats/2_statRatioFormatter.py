import json
import re
import sys
import pyperclip


def read_file(filepath):
    """Safely reads a file and returns lines."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        sys.exit(1)


def calculate_weight(rank, is_flat):
    """
    Calculates weight based on rank (1-10).
    Normal: 1.0 down to 0.1
    Flat: 0.25 down to 0.025
    """
    # Convert string rank to integer (0-based index)
    index = int(rank) - 1

    # Base calculation
    if is_flat:
        return round(0.25 - (index * 0.025), 3)
    else:
        return round(1.0 - (index * 0.1), 1)


def parse_artifact_stats(lines):
    # Initialize the structure
    data = {
        "main_stats": {
            "sands": {},
            "goblet": {},
            "circlet": {}
        },
        "sub_stats": {
            # Pre-filling common keys ensures JSON consistency,
            # though not strictly necessary if dynamic is preferred.
            "hp": 0, "hp_": 0, "def": 0, "def_": 0,
            "atk": 0, "atk_": 0, "enerRech_": 0,
            "eleMas": 0, "critRate_": 0, "critDMG_": 0
        }
    }

    # Regex patterns for safer parsing
    # Captures "Category - Stat1 / Stat2"
    main_stat_pattern = re.compile(r"(Sands|Goblet|Circlet)\s*-\s*(.*)", re.IGNORECASE)

    # Captures "1. Stat1 / flat_Stat2"
    sub_stat_pattern = re.compile(r"^(\d+)\.\s*(.*)")

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # 1. Check for Main Stats
        main_match = main_stat_pattern.search(line)
        if main_match:
            category = main_match.group(1).lower()  # e.g., 'sands'
            raw_stats = main_match.group(2)

            # Split stats by '/' and clean them
            stats_list = [s.strip().replace('*', '') for s in raw_stats.split('/')]

            for stat in stats_list:
                data["main_stats"][category][stat] = 1
            continue  # Skip to next line

        # 2. Check for Sub Stats (Weighted)
        sub_match = sub_stat_pattern.search(line)
        if sub_match:
            rank = sub_match.group(1)  # The number at the start (e.g., "1")
            raw_stats = sub_match.group(2)

            stats_list = [s.strip().replace('*', '') for s in raw_stats.split('/')]

            for stat in stats_list:
                # Detect if it's a flat stat
                is_flat = "flat_" in stat

                # Clean the name (remove 'flat_' for the key)
                stat_key = stat.replace('flat_', '')

                # Calculate weight
                weight = calculate_weight(rank, is_flat)

                # Assign (or add) to dictionary
                # Use .get() default to 0 just in case a new stat appears
                current_val = data["sub_stats"].get(stat_key, 0)
                data["sub_stats"][stat_key] = max(current_val, weight)

    return data


if __name__ == "__main__":
    INPUT_FILE = '1_stats.txt'

    # 1. Read
    file_lines = read_file(INPUT_FILE)

    # 2. Parse
    result = parse_artifact_stats(file_lines)

    # 3. Output
    # json_output = json.dumps(result, indent=2)  # indent makes it readable

    try:
        pyperclip.copy(result)
        print("Success! JSON copied to clipboard.")
        # Optional: Print to console to verify
        # print(json_output)
    except Exception as e:
        print(f"Error copying to clipboard: {e}")
        print("Here is the output instead:")
        print(result)