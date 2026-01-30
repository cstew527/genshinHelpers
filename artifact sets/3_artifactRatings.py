def update_rating(artifact_rating, artifact, ranking):
    set_types = {'1p': 0.5, '2p': 1, '4p': 2}
    set_type = next(set_type for set_type in set_types if set_type in artifact)
    artifact_rating[artifact] = set_types[set_type] / 2 ** (ranking - 1)
    return artifact_rating


def print_highest_rating(artifact_rating, artifact1, artifact2):
    print(max(artifact_rating[artifact1], artifact_rating[artifact2]))


def rank_artifacts(filename="2_artifactsMerged.txt"):
    artifacts = [
        "Prayers for Wisdom (1p)",
        "Prayers for Destiny (1p)",
        "Prayers for Illumination (1p)",
        "Prayers to Springtime (1p)",
        "ATK +18% (2p)",
        "Elemental Mastery +80 (2p)",
        "Elemental Burst DMG +20% (2p)",
        "Physical DMG Bonus +25% (2p)",
        "Healing Bonus +15% (2p)",
        "Anemo DMG Bonus +15% (2p)",
        "Geo DMG Bonus +15% (2p)",
        "Shield Strength +35% (2p)",
        "Electro RES +40% (2p)",
        "Electro DMG Bonus +15% (2p)",
        "Pyro RES +40% (2p)",
        "Pyro DMG Bonus +15% (2p)",
        "Cryo DMG Bonus +15% (2p)",
        "Hydro DMG Bonus +15% (2p)",
        "HP +20% (2p)",
        "Energy Recharge +20% (2p)",
        "DEF +30% (2p)",
        "Dendro DMG Bonus +15% (2p)",
        "Normal/Charged Attack DMG +15% (2p)",
        "Elemental Skill DMG +20% (2p)",
        "Nightsoul Burst: Elemental Energy +6 (2p)",
        "Nightsoul's Blessing: DMG +15% (2p)",
        "Plunging Attack DMG +25% (2p)",
        "All Elemental RES +20% (2p)",
        "CRIT Rate +12% (2p)",
        "HP +1000 (2p)",
        "DEF +100 (2p)",
        "Incoming Healing Bonus +20% (2p)",
        "Gladiator's Finale (4p)",
        "Wanderer's Troupe (4p)",
        "Noblesse Oblige (4p)",
        "Bloodstained Chivalry (4p)",
        "Maiden Beloved (4p)",
        "Viridescent Venerer (4p)",
        "Archaic Petra (4p)",
        "Retracing Bolide (4p)",
        "Thundersoother (4p)",
        "Thundering Fury (4p)",
        "Lavawalker (4p)",
        "Crimson Witch of Flames (4p)",
        "Blizzard Strayer (4p)",
        "Heart of Depth (4p)",
        "Tenacity of the Millelith (4p)",
        "Pale Flame (4p)",
        "Shimenawa's Reminiscence (4p)",
        "Emblem of Severed Fate (4p)",
        "Husk of Opulent Dreams (4p)",
        "Ocean-Hued Clam (4p)",
        "Vermillion Hereafter (4p)",
        "Echoes of an Offering (4p)",
        "Deepwood Memories (4p)",
        "Gilded Dreams (4p)",
        "Desert Pavilion Chronicle (4p)",
        "Flower of Paradise Lost (4p)",
        "Nymph's Dream (4p)",
        "Vourukasha's Glow (4p)",
        "Marechaussee Hunter (4p)",
        "Golden Troupe (4p)",
        "Song of Days Past (4p)",
        "Nighttime Whispers in the Echoing Woods (4p)",
        "Fragment of Harmonic Whimsy (4p)",
        "Unfinished Reverie (4p)",
        "Scroll of the Hero of Cinder City (4p)",
        "Obsidian Codex (4p)",
        "Long Night's Oath (4p)",
        "Finale of the Deep Galleries (4p)",
        "Night of the Sky's Unveiling (4p)",
        "Silken Moon's Serenade (4p)",
        "Aubade of Morningstar and Moon (4p)",
        "A Day Carved From Rising Winds (4p)",
        "Resolution of Sojourner (4p)",
        "Tiny Miracle (4p)",
        "Berserker (4p)",
        "Instructor (4p)",
        "The Exile (4p)",
        "Defender's Will (4p)",
        "Brave Heart (4p)",
        "Martial Artist (4p)",
        "Gambler (4p)",
        "Scholar (4p)",
    ]

    artifact_rating = dict.fromkeys(artifacts, 0)
    # num_rankings = int(input("Enter the number of rankings: "))
    #
    # for i, artifact in enumerate(artifacts):
    #     print(i + 1, artifact)
    #
    # for ranking in range(num_rankings, 0, -1):
    #     print("Select artifacts for ranking", ranking)
    #     selected_artifacts = input("Enter the numbers of the selected artifacts, separated by commas: ").split(',')
    #     selected_artifacts = [artifacts[int(x) - 1] for x in selected_artifacts]
    #
    #     for artifact in selected_artifacts:
    #         artifact_rating = update_rating(artifact_rating, artifact, ranking)

    entries = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(".")
            ranking = int(parts[0])   # number before the "."
            selected_numbers = parts[1].split(",")
            selected_artifacts = [artifacts[int(x) - 1] for x in selected_numbers if x.strip().isdigit()]
            entries.append((ranking, selected_artifacts))

    # Sort by ranking descending → apply worst first, best last
    entries.sort(reverse=True, key=lambda x: x[0])

    for ranking, selected_artifacts in entries:
        for artifact in selected_artifacts:
            artifact_rating = update_rating(artifact_rating, artifact, ranking)


    print("\nFinal Ratings:")
    for artifact, rating in artifact_rating.items():
        print(artifact, ":", rating)

    comparisons_before_blank_line = [
        ("A Day Carbed From Rising Winds (4p)", "ATK +18% (2p)"),
        ("Aubade of Morningstar and Moon (4p)", "Elemental Mastery +80 (2p)"),
        ("Silken Moon's Serenade (4p)", "Energy Recharge +20% (2p)"),
        ("Night of the Sky's Unveiling (4p)", "Elemental Mastery +80 (2p)"),
        ("Finale of the Deep Galleries (4p)", "Cryo DMG Bonus +15% (2p)"),
        ("Long Night's Oath (4p)", "Plunging Attack DMG +25% (2p)"),
        ("Obsidian Codex (4p)", "Nightsoul Burst: Elemental Energy +6 (2p)"),
        ("Scroll of the Hero of Cinder City (4p)", "Nightsoul's Blessing: DMG +15% (2p)"),
        ("Unfinished Reverie (4p)", "ATK +18% (2p)"),
        ("Fragment of Harmonic Whimsy (4p)", "ATK +18% (2p)"),
        ("Nighttime Whispers in the Echoing Woods (4p)", "ATK +18% (2p)"),
        ("Song of Days Past (4p)", "Healing Bonus +15% (2p)"),
        ("Golden Troupe (4p)", "Elemental Skill DMG +20% (2p)"),
        ("Marechaussee Hunter (4p)", "Normal/Charged Attack DMG +15% (2p)"),
        ("Vourukasha's Glow (4p)", "HP +20% (2p)"),
        ("Nymph's Dream (4p)", "Hydro DMG Bonus +15% (2p)"),
        ("Flower of Paradise Lost (4p)", "Elemental Mastery +80 (2p)"),
        ("Desert Pavilion Chronicle (4p)", "Anemo DMG Bonus +15% (2p)"),
        ("Gilded Dreams (4p)", "Elemental Mastery +80 (2p)"),
        ("Deepwood Memories (4p)", "Dendro DMG Bonus +15% (2p)"),
        ("Echoes of an Offering (4p)", "ATK +18% (2p)"),
        ("Vermillion Hereafter (4p)", "ATK +18% (2p)"),
        ("Ocean-Hued Clam (4p)", "Healing Bonus +15% (2p)"),
        ("Husk of Opulent Dreams (4p)", "DEF +30% (2p)"),
        ("Emblem of Severed Fate (4p)", "Energy Recharge +20% (2p)"),
        ("Shimenawa's Reminiscence (4p)", "ATK +18% (2p)"),
        ("Pale Flame (4p)", "Physical DMG Bonus +25% (2p)"),
        ("Tenacity of the Millelith (4p)", "HP +20% (2p)"),
        ("Heart of Depth (4p)", "Hydro DMG Bonus +15% (2p)"),
        ("Blizzard Strayer (4p)", "Cryo DMG Bonus +15% (2p)"),
        ("Crimson Witch of Flames (4p)", "Pyro DMG Bonus +15% (2p)"),
        ("Lavawalker (4p)", "Pyro RES +40% (2p)"),
        ("Thundering Fury (4p)", "Electro DMG Bonus +15% (2p)"),
        ("Thundersoother (4p)", "Electro RES +40% (2p)"),
        ("Retracing Bolide (4p)", "Shield Strength +35% (2p)"),
        ("Archaic Petra (4p)", "Geo DMG Bonus +15% (2p)"),
        ("Viridescent Venerer (4p)", "Anemo DMG Bonus +15% (2p)"),
        ("Maiden Beloved (4p)", "Healing Bonus +15% (2p)"),
        ("Bloodstained Chivalry (4p)", "Physical DMG Bonus +25% (2p)"),
        ("Noblesse Oblige (4p)", "Elemental Burst DMG +20% (2p)"),
        ("Wanderer's Troupe (4p)", "Elemental Mastery +80 (2p)"),
        ("Gladiator's Finale (4p)", "ATK +18% (2p)"),
    ]

    # Build the output string for the comparisons
    output_lines = []
    for comp in comparisons_before_blank_line:
        value = max(artifact_rating[comp[0]], artifact_rating[comp[1]])
        output_lines.append(str(value))

    output_str = "\n".join(output_lines)

    # Copy to clipboard using pyperclip if available, otherwise provide instructions
    try:
        import pyperclip
        pyperclip.copy(output_str)
        print("\nComparison results have been copied to your clipboard!")
    except ImportError:
        print(
            "\npyperclip module not available. Please install it with 'pip install pyperclip' for clipboard functionality.")
        print("Alternatively, manually copy the following output:\n")
        print(output_str)
    except Exception as e:
        print(f"\nAn error occurred while copying to clipboard: {e}")
        print("Please manually copy the following output:\n")
        print(output_str)
    #
    # print()  # This will print a blank line
    #
    # print(artifact_rating["Prayers for Destiny (1p)"])
    # print(artifact_rating["Prayers for Illumination (1p)"])
    # print(artifact_rating["Prayers for Wisdom (1p)"])
    # print(artifact_rating["Prayers to Springtime (1p)"])
    #
    # comparisons_after_blank_line = [
    #     ("Scholar (4p)", "Energy Recharge +20% (2p)"),
    #     ("Gambler (4p)", "Elemental Skill DMG +20% (2p)"),
    #     ("Martial Artist (4p)", "Normal/Charged Attack DMG +15% (2p)"),
    #     ("Brave Heart (4p)", "ATK +18% (2p)"),
    #     ("Defender's Will (4p)", "DEF +30% (2p)"),
    #     ("The Exile (4p)", "Energy Recharge +20% (2p)"),
    #     ("Instructor (4p)", "Elemental Mastery +80 (2p)"),
    #     ("Berserker (4p)", "CRIT Rate +12% (2p)"),
    #     ("Tiny Miracle (4p)", "All Elemental RES +20% (2p)"),
    #     ("Resolution of Sojourner (4p)", "ATK +18% (2p)"),
    # ]
    #
    # for comp in comparisons_after_blank_line:
    #     print_highest_rating(artifact_rating, comp[0], comp[1])


rank_artifacts()