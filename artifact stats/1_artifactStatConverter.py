def replace_strings_in_file(input_file, replacements):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    with open(input_file, 'w') as file:
        for line in lines:
            for old_string, new_string in replacements.items():
                line = line.replace(old_string, new_string)
            file.write(line)


file_path = "1_stats.txt"
string_map = {
    "Flat HP": "flat_hp",
    "HP%": "hp_",
    "Flat ATK": "flat_atk",
    "ATK%": "atk_",
    "Atk%": "atk_",
    "Flat DEF": "flat_def",
    "DEF%": "def_",
    "Elemental Mastery": "eleMas",
    "ER%": "enerRech_",
    "Energy Recharge": "enerRech_",
    "Crit Rate/ DMG": "critRate_ / critDMG_",
    "CRIT Rate / DMG": "critRate_ / critDMG_",
    "Crit Rate / DMG": "critRate_ / critDMG_",
    "CRIT Rate%": "critRate_",
    "Crit Rate%": "critRate_",
    "CRIT Rate": "critRate_",
    "Crit Rate": "critRate_",
    "CRIT DMG": "critDMG_",
    "Crit DMG": "critDMG_",
    "Physical DMG Bonus": "physical_dmg_",
    "Physical DMG": "physical_dmg_",
    "Anemo DMG Bonus": "anemo_dmg_",
    "Anemo DMG": "anemo_dmg_",
    "Anemo Damage": "anemo_dmg_",
    "Geo DMG Bonus": "geo_dmg_",
    "Geo DMG": "geo_dmg_",
    "Electro DMG Bonus": "electro_dmg_",
    "Electro DMG": "electro_dmg_",
    "Electro Damage": "electro_dmg_",
    "Hydro DMG Bonus": "hydro_dmg_",
    "Hydro DMG": "hydro_dmg_",
    "Pyro DMG Bonus": "pyro_dmg_",
    "Pyro DMG": "pyro_dmg_",
    "Cryo DMG Bonus": "cryo_dmg_",
    "Cryo DMG": "cryo_dmg_",
    "Dendro DMG Bonus": "dendro_dmg_",
    "Dendro DMG": "dendro_dmg_",
    "Healing Bonus%": "heal_",
    "Healing Bonus": "heal_"

}

replace_strings_in_file(file_path, string_map)