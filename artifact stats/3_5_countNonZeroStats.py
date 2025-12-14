# Recursive function to count non-zero stats in nested dictionaries
def count_unique_non_zero_stats(dictionary):
    unique_stats = set()  # Use a set to avoid duplicates

    def traverse(data):
        for key, value in data.items():
            if isinstance(value, dict):  # Recurse into nested dictionaries
                traverse(value)
            elif isinstance(value, (int, float)) and value > 0:  # Add only non-zero numeric values
                unique_stats.add(key)

    traverse(dictionary)
    return len(unique_stats)


# 4 STAR PYRO
amber_melt_dps = {"main_stats": {"sands": {"atk_": 1, "eleMas": 1}, "goblet": {"pyro_dmg_": 1}, "circlet": {"critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.175, "atk_": 0.9, "enerRech_": 0, "eleMas": 0.8, "critRate_": 0, "critDMG_": 1.0}}
amber_buff_support = {"main_stats": {"sands": {"enerRech_": 1, "atk_": 1}, "goblet": {"pyro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.8, "enerRech_": 1.0, "eleMas": 0.7, "critRate_": 0.9, "critDMG_": 0.9}}
xiangling_offField_dps = {"main_stats": {"sands": {"enerRech_": 1, "atk_": 1, "eleMas": 1}, "goblet": {"pyro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.8, "enerRech_": 1.0, "eleMas": 0.7, "critRate_": 0.9, "critDMG_": 0.9}}
bennett_support = {"main_stats": {"sands": {"enerRech_": 1, "atk_": 1, "hp_": 1}, "goblet": {"pyro_dmg_": 1, "hp_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1, "hp_": 1, "heal_": 1}}, "sub_stats": {"hp": 0.2, "hp_": 0.9, "def": 0, "def_": 0, "atk": 0.175, "atk_": 0.8, "enerRech_": 1.0, "eleMas": 0, "critRate_": 0.9, "critDMG_": 0.9}}
bennett_dps = {"main_stats": {"sands": {"atk_": 1, "eleMas": 1}, "goblet": {"pyro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.8, "enerRech_": 1.0, "eleMas": 0.7, "critRate_": 0.9, "critDMG_": 0.9}}
xinyan_physical_dps = {"main_stats": {"sands": {"atk_": 1, "enerRech_": 1}, "goblet": {"physical_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0.125, "def_": 0.7, "atk": 0.15, "atk_": 0.9, "enerRech_": 0.8, "eleMas": 0, "critRate_": 1.0, "critDMG_": 1.0}}
xinyan_pyro_dps = {"main_stats": {"sands": {"atk_": 1}, "goblet": {"pyro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0.125, "def_": 0.7, "atk": 0.15, "atk_": 0.9, "enerRech_": 0.8, "eleMas": 0, "critRate_": 1.0, "critDMG_": 1.0}}
xinyan_shield_support = {"main_stats": {"sands": {"def_": 1, "enerRech_": 1}, "goblet": {"def_": 1}, "circlet": {"def_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0.175, "def_": 0.9, "atk": 0.175, "atk_": 0.9, "enerRech_": 1.0, "eleMas": 0, "critRate_": 0.8, "critDMG_": 0.8}}
yanfei_vaporize_dps = {"main_stats": {"sands": {"atk_": 1, "eleMas": 1}, "goblet": {"pyro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.9, "enerRech_": 0.7, "eleMas": 0.8, "critRate_": 1.0, "critDMG_": 1.0}}
yanfei_shield_support = {"main_stats": {"sands": {"enerRech_": 1, "hp_": 1}, "goblet": {"hp_": 1}, "circlet": {"hp_": 1}}, "sub_stats": {"hp": 0.2, "hp_": 0.9, "def": 0, "def_": 0, "atk": 0, "atk_": 0, "enerRech_": 1.0, "eleMas": 0, "critRate_": 0, "critDMG_": 0}}
thoma_burgeon = {"main_stats": {"sands": {"enerRech_": 1, "eleMas": 1}, "goblet": {"eleMas": 1}, "circlet": {"eleMas": 1}}, "sub_stats": {"hp": 0.175, "hp_": 0.8, "def": 0, "def_": 0, "atk": 0, "atk_": 0, "enerRech_": 1.0, "eleMas": 0.9, "critRate_": 0.6, "critDMG_": 0}}
thoma_shield_support = {"main_stats": {"sands": {"enerRech_": 1, "hp_": 1}, "goblet": {"hp_": 1}, "circlet": {"hp_": 1, "critRate_": 1}}, "sub_stats": {"hp": 0.175, "hp_": 0.9, "def": 0, "def_": 0, "atk": 0, "atk_": 0, "enerRech_": 1.0, "eleMas": 0, "critRate_": 0.8, "critDMG_": 0}}
chevreuse_buff_support = {"main_stats": {"sands": {"hp_": 1, "enerRech_": 1}, "goblet": {"hp_": 1}, "circlet": {"hp_": 1, "heal_": 1}}, "sub_stats": {"hp": 0.175, "hp_": 0.9, "def": 0, "def_": 0, "atk": 0, "atk_": 0, "enerRech_": 1.0, "eleMas": 0.6, "critRate_": 0.8, "critDMG_": 0}}
chevreuse_buff_support_and_damage = {"main_stats": {"sands": {"atk_": 1, "enerRech_": 1}, "goblet": {"pyro_dmg_%": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0.1, "hp_": 0.7, "def": 0, "def_": 0, "atk": 0.125, "atk_": 0.8, "enerRech_": 1.0, "eleMas": 0.6, "critRate_": 0.9, "critDMG_": 0.9}}
gaming_dps = {"main_stats": {"sands": {"eleMas": 1, "atk_": 1, "enerRech_": 1}, "goblet": {"pyro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.7, "enerRech_": 1.0, "eleMas": 0.8, "critRate_": 0.9, "critDMG_": 0.9}}
# 5 STAR PYRO
pyro_traveler_buff_support = {"main_stats": {"sands": {"enerRech_": 1, "atk_": 1}, "goblet": {"pyro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.175, "atk_": 0.8, "enerRech_": 1.0, "eleMas": 0, "critRate_": 0.9, "critDMG_": 0.9}}
pyro_traveler_dps = {"main_stats": {"sands": {"enerRech_": 1, "atk_": 1, "eleMas": 1}, "goblet": {"pyro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.7, "enerRech_": 1.0, "eleMas": 0.8, "critRate_": 0.9, "critDMG_": 0.9}}
diluc_dps = {"main_stats": {"sands": {"eleMas": 1, "atk_": 1}, "goblet": {"pyro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.9, "enerRech_": 0.7, "eleMas": 0.8, "critRate_": 1.0, "critDMG_": 1.0}}
klee_dps = {"main_stats": {"sands": {"atk_": 1}, "goblet": {"pyro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.8, "enerRech_": 1.0, "eleMas": 0.7, "critRate_": 0.9, "critDMG_": 0.9}}
hu_tao_dps = {"main_stats": {"sands": {"hp_": 1, "eleMas": 1}, "goblet": {"pyro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0.15, "hp_": 0.8, "def": 0, "def_": 0, "atk": 0.125, "atk_": 0.7, "enerRech_": 0, "eleMas": 0.9, "critRate_": 1.0, "critDMG_": 1.0}}
yoimiya_dps = {"main_stats": {"sands": {"atk_": 1, "eleMas": 1}, "goblet": {"pyro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.9, "enerRech_": 0.7, "eleMas": 0.8, "critRate_": 1.0, "critDMG_": 1.0}}
dehya_onField_dps = {"main_stats": {"sands": {"atk_": 1, "enerRech_": 1}, "goblet": {"pyro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0.6, "def": 0.1, "def_": 0, "atk": 0.125, "atk_": 0.8, "enerRech_": 1.0, "eleMas": 0.7, "critRate_": 0.9, "critDMG_": 0.9}}
dehya_tank_support = {"main_stats": {"sands": {"hp_": 1}, "goblet": {"hp_": 1}, "circlet": {"hp_": 1, "critRate_": 1}}, "sub_stats": {"hp": 0.225, "hp_": 1.0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.7, "enerRech_": 0, "eleMas": 0.8, "critRate_": 0, "critDMG_": 0}}
dehya_burgeon = {"main_stats": {"sands": {"eleMas": 1}, "goblet": {"eleMas": 1}, "circlet": {"eleMas": 1}}, "sub_stats": {"hp": 0.2, "hp_": 0.9, "def": 0, "def_": 0, "atk": 0, "atk_": 0, "enerRech_": 0, "eleMas": 1.0, "critRate_": 0.7, "critDMG_": 0}}
lyney_dps = {"main_stats": {"sands": {"atk_": 1}, "goblet": {"pyro_dmg_": 1}, "circlet": {"critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.175, "atk_": 0.9, "enerRech_": 0.8, "eleMas": 0, "critRate_": 1.0, "critDMG_": 1.0}}
arlecchino_dps = {"main_stats": {"sands": {"atk_": 1, "eleMas": 1}, "goblet": {"pyro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.175, "atk_": 0.8, "enerRech_": 0, "eleMas": 0.9, "critRate_": 1.0, "critDMG_": 1.0}}
mavuika_dps_and_buff_support = {"main_stats": {"sands": {"eleMas": 1, "atk_": 1}, "goblet": {"pyro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.175, "atk_": 0.9, "enerRech_": 0, "eleMas": 0.8, "critRate_": 1.0, "critDMG_": 1.0}}
# 4 STAR ELECTRO
fischl_offField_dps = {"main_stats": {"sands": {"atk_": 1}, "goblet": {"electro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.8, "enerRech_": 1.0, "eleMas": 0.7, "critRate_": 0.9, "critDMG_": 0.9}}
fischl_offField_aggravate_dps = {"main_stats": {"sands": {"atk_": 1, "eleMas": 1}, "goblet": {"electro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.175, "atk_": 0.8, "enerRech_": 1.0, "eleMas": 0.8, "critRate_": 0.9, "critDMG_": 0.9}}
beidou_offField_dps = {"main_stats": {"sands": {"atk_": 1, "enerRech_": 1}, "goblet": {"electro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.8, "enerRech_": 1.0, "eleMas": 0.7, "critRate_": 0.9, "critDMG_": 0.9}}
lisa_aggravate_dps = {"main_stats": {"sands": {"eleMas": 1, "atk_": 1}, "goblet": {"electro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.175, "atk_": 0.9, "enerRech_": 0.8, "eleMas": 0.9, "critRate_": 1.0, "critDMG_": 1.0}}
lisa_offField_dps = {"main_stats": {"sands": {"enerRech_": 1, "atk_": 1, "eleMas": 1}, "goblet": {"electro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.8, "enerRech_": 1.0, "eleMas": 0.7, "critRate_": 0.9, "critDMG_": 0.9}}
lisa_reaction_dps = {"main_stats": {"sands": {"eleMas": 1, "enerRech_": 1}, "goblet": {"eleMas": 1}, "circlet": {"eleMas": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.8, "enerRech_": 1.0, "eleMas": 0.9, "critRate_": 0.7, "critDMG_": 0.7}}
razor_hyperbloom_reaction_dps = {"main_stats": {"sands": {"eleMas": 1}, "goblet": {"eleMas": 1}, "circlet": {"eleMas": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0, "atk_": 0, "enerRech_": 0.9, "eleMas": 1.0, "critRate_": 0.8, "critDMG_": 0}}
razor_physical_dps = {"main_stats": {"sands": {"atk_": 1}, "goblet": {"physical_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.9, "enerRech_": 0.8, "eleMas": 0.7, "critRate_": 1.0, "critDMG_": 1.0}}
kujou_sara_buff_support_and_damage = {"main_stats": {"sands": {"enerRech_": 1, "atk_": 1}, "goblet": {"electro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.175, "atk_": 0.8, "enerRech_": 1.0, "eleMas": 0, "critRate_": 0.9, "critDMG_": 0.9}}
kuki_shinobu_hyperbloom = {"main_stats": {"sands": {"eleMas": 1}, "goblet": {"eleMas": 1}, "circlet": {"eleMas": 1}}, "sub_stats": {"hp": 0.2, "hp_": 0.9, "def": 0, "def_": 0, "atk": 0, "atk_": 0, "enerRech_": 0.7, "eleMas": 1.0, "critRate_": 0, "critDMG_": 0}}
kuki_shinobu_aggravate_offField_dps = {"main_stats": {"sands": {"enerRech_": 1, "eleMas": 1}, "goblet": {"electro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0.15, "hp_": 0.7, "def": 0, "def_": 0, "atk": 0, "atk_": 0, "enerRech_": 1.0, "eleMas": 0.8, "critRate_": 0.9, "critDMG_": 0.9}}
kuki_shinobu_support = {"main_stats": {"sands": {"hp_": 1}, "goblet": {"hp_": 1}, "circlet": {"heal_": 1, "hp_": 1, "critRate_": 1}}, "sub_stats": {"hp": 0.2, "hp_": 1.0, "def": 0, "def_": 0, "atk": 0, "atk_": 0, "enerRech_": 0, "eleMas": 0.8, "critRate_": 0.9, "critDMG_": 0}}
dori_support = {"main_stats": {"sands": {"enerRech_": 1, "hp_": 1, "eleMas": 1}, "goblet": {"hp_": 1, "eleMas": 1}, "circlet": {"heal_": 1, "hp_": 1, "eleMas": 1}}, "sub_stats": {"hp": 0.15, "hp_": 0.8, "def": 0, "def_": 0, "atk": 0, "atk_": 0, "enerRech_": 0.9, "eleMas": 0.7, "critRate_": 1.0, "critDMG_": 0}}
sethos_dps = {"main_stats": {"sands": {"eleMas": 1, "enerRech_": 1}, "goblet": {"electro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.7, "enerRech_": 1.0, "eleMas": 0.8, "critRate_": 0.9, "critDMG_": 0.9}}
ororon_offField_dps = {"main_stats": {"sands": {"atk_": 1, "enerRech_": 1}, "goblet": {"electro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.8, "enerRech_": 1.0, "eleMas": 0.7, "critRate_": 0.9, "critDMG_": 0.9}}
iansan_buff_support = {"main_stats": {"sands": {"atk_": 1, "enerRech_": 1}, "goblet": {"atk_": 1}, "circlet": {"atk_": 1, "critRate_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.175, "atk_": 0.9, "enerRech_": 1.0, "eleMas": 0, "critRate_": 0.8, "critDMG_": 0}}
# 5 STAR ELECTRO
electro_traveler_support = {"main_stats": {"sands": {"enerRech_": 1}, "goblet": {"electro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.175, "atk_": 0.9, "enerRech_": 1.0, "eleMas": 0, "critRate_": 0.8, "critDMG_": 0.8}}
keqing_aggravate_dps = {"main_stats": {"sands": {"atk_": 1, "eleMas": 1}, "goblet": {"electro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.175, "atk_": 0.9, "enerRech_": 0.6, "eleMas": 0.9, "critRate_": 1.0, "critDMG_": 1.0}}
keqing_quickbloom_dps = {"main_stats": {"sands": {"eleMas": 1, "atk_": 1}, "goblet": {"electro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.7, "enerRech_": 1.0, "eleMas": 0.8, "critRate_": 0.9, "critDMG_": 0.9}}
raiden_shogun_hyperbloom = {"main_stats": {"sands": {"eleMas": 1}, "goblet": {"eleMas": 1}, "circlet": {"eleMas": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.9, "enerRech_": 0.8, "eleMas": 1.0, "critRate_": 0.7, "critDMG_": 0.7}}
raiden_shogun_dps = {"main_stats": {"sands": {"enerRech_": 1, "atk_": 1}, "goblet": {"electro_dmg_": 1, "atk_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.9, "enerRech_": 0.8, "eleMas": 0.7, "critRate_": 1.0, "critDMG_": 1.0}}
yae_miko_offField_dps = {"main_stats": {"sands": {"enerRech_": 1, "atk_": 1}, "goblet": {"electro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.9, "enerRech_": 0.8, "eleMas": 0.7, "critRate_": 1.0, "critDMG_": 1.0}}
yae_miko_offField_aggravate_dps = {"main_stats": {"sands": {"enerRech_": 1, "eleMas": 1, "atk_": 1}, "goblet": {"electro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.8, "enerRech_": 0.7, "eleMas": 0.9, "critRate_": 1.0, "critDMG_": 1.0}}
cyno_quickbloom_hyperbloom_dps = {"main_stats": {"sands": {"eleMas": 1}, "goblet": {"electro_dmg_": 1, "eleMas": 1}, "circlet": {"critRate_": 1, "critDMG_": 1, "eleMas": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.7, "enerRech_": 1.0, "eleMas": 0.9, "critRate_": 0.8, "critDMG_": 0.8}}
cyno_aggravate_dps = {"main_stats": {"sands": {"eleMas": 1, "atk_": 1}, "goblet": {"electro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.175, "atk_": 0.8, "enerRech_": 1.0, "eleMas": 0.8, "critRate_": 0.9, "critDMG_": 0.9}}
clorinde_dps = {"main_stats": {"sands": {"atk_": 1, "eleMas": 1}, "goblet": {"electro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.9, "enerRech_": 0.7, "eleMas": 0.8, "critRate_": 1.0, "critDMG_": 1.0}}
varesa_dps = {"main_stats": {"sands": {"atk_": 1}, "goblet": {"electro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.8, "enerRech_": 1.0, "eleMas": 0.7, "critRate_": 0.9, "critDMG_": 0.9}}
ineffa_offField_dps_support = {"main_stats": {"sands": {"atk_": 1, "enerRech_": 1}, "goblet": {"atk_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.175, "atk_": 0.8, "enerRech_": 1.0, "eleMas": 0.8, "critRate_": 0.9, "critDMG_": 0.9}}
# 4 STAR DENDRO
collei_support = {"main_stats": {"sands": {"enerRech_": 1, "atk_": 1, "eleMas": 1}, "goblet": {"dendro_dmg_": 1, "eleMas": 1}, "circlet": {"critRate_": 1, "critDMG_": 1, "eleMas": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.175, "atk_": 0.8, "enerRech_": 1.0, "eleMas": 0.8, "critRate_": 0.9, "critDMG_": 0.9}}
yaoyao_support = {"main_stats": {"sands": {"hp_": 1, "enerRech_": 1}, "goblet": {"hp_": 1}, "circlet": {"heal_": 1}}, "sub_stats": {"hp": 0.175, "hp_": 0.9, "def": 0, "def_": 0, "atk": 0, "atk_": 0, "enerRech_": 1.0, "eleMas": 0, "critRate_": 0.8, "critDMG_": 0,}}
kaveh_bloom_burgeon_driver = {"main_stats": {"sands": {"enerRech_": 1, "eleMas": 1}, "goblet": {"eleMas": 1}, "circlet": {"eleMas": 1, "critRate_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0, "atk_": 0, "enerRech_": 1.0, "eleMas": 0.9, "critRate_": 0.8, "critDMG_": 0}}
kirara_shield_support = {"main_stats": {"sands": {"hp_": 1, "enerRech_": 1}, "goblet": {"hp_": 1}, "circlet": {"hp_": 1, "critRate_": 1}}, "sub_stats": {"hp": 0.175, "hp_": 0.9, "def": 0, "def_": 0, "atk": 0, "atk_": 0, "enerRech_": 1.0, "eleMas": 0, "critRate_": 0.8, "critDMG_": 0}}
# 5 STAR DENDRO
dendro_traveler_support = {"main_stats": {"sands": {"enerRech_": 1, "atk_": 1, "eleMas": 1}, "goblet": {"dendro_dmg_": 1, "eleMas": 1}, "circlet": {"critRate_": 1, "critDMG_": 1, "eleMas": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.175, "atk_": 0.8, "enerRech_": 1.0, "eleMas": 0.8, "critRate_": 0.9, "critDMG_": 0.9}}
tighnari_quick_swap_dps = {"main_stats": {"sands": {"atk_": 1, "eleMas": 1, "enerRech_": 1}, "goblet": {"dendro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.175, "atk_": 0.9, "enerRech_": 0.8, "eleMas": 0.9, "critRate_": 1.0, "critDMG_": 1.0}}
nahida_dps_and_support = {"main_stats": {"sands": {"eleMas": 1}, "goblet": {"eleMas": 1, "dendro_dmg_": 1}, "circlet": {"eleMas": 1, "critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.175, "atk_": 0.8, "enerRech_": 1.0, "eleMas": 0.9, "critRate_": 0.9, "critDMG_": 0.9}}
alhaitham_spread_dps = {"main_stats": {"sands": {"eleMas": 1, "atk_": 1}, "goblet": {"dendro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.7, "enerRech_": 1.0, "eleMas": 0.8, "critRate_": 0.9, "critDMG_": 0.9}}
baizhu_support = {"main_stats": {"sands": {"hp_": 1, "enerRech_": 1}, "goblet": {"hp_": 1}, "circlet": {"hp_": 1, "heal_": 1}}, "sub_stats": {"hp": 0.2, "hp_": 0.9, "def": 0, "def_": 0, "atk": 0, "atk_": 0, "enerRech_": 1.0, "eleMas": 0, "critRate_": 0.7, "critDMG_": 0}}
emilie_offField_dps = {"main_stats": {"sands": {"atk_": 1}, "goblet": {"dendro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.175, "atk_": 0.9, "enerRech_": 0.8, "eleMas": 0, "critRate_": 1.0, "critDMG_": 1.0}}
kinich_dps = {"main_stats": {"sands": {"atk_": 1}, "goblet": {"dendro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.175, "atk_": 0.9, "enerRech_": 0.8, "eleMas": 0, "critRate_": 1.0, "critDMG_": 1.0}}
lauma_buff_support_high_energy = {"main_stats": {"sands": {"enerRech_": 1, "eleMas": 1}, "goblet": {"eleMas": 1}, "circlet": {"eleMas": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0, "atk_": 0, "enerRech_": 1.0, "eleMas": 0.9, "critRate_": 0.8, "critDMG_": 0.8}}
lauma_buff_support_low_energy = {"main_stats": {"sands": {"eleMas": 1}, "goblet": {"eleMas": 1}, "circlet": {"eleMas": 1, "critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0, "atk_": 0, "enerRech_": 1.0, "eleMas": 0.9, "critRate_": 0.8, "critDMG_": 0.8}}
# 4 STAR HYDRO
xingqiu_offField_dps = {"main_stats": {"sands": {"enerRech_": 1, "atk_": 1}, "goblet": {"hydro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.9, "enerRech_": 0.8, "eleMas": 0.7, "critRate_": 1.0, "critDMG_": 1.0}}
barbara_support = {"main_stats": {"sands": {"hp_": 1}, "goblet": {"hp_": 1}, "circlet": {"heal_": 1}}, "sub_stats": {"hp": 0.225, "hp_": 1.0, "def": 0, "def_": 0, "atk": 0, "atk_": 0, "enerRech_": 0, "eleMas": 0, "critRate_": 0, "critDMG_": 0}}
barbara_bloom_dps = {"main_stats": {"sands": {"eleMas": 1}, "goblet": {"eleMas": 1}, "circlet": {"eleMas": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0, "atk_": 0, "enerRech_": 0.9, "eleMas": 1.0, "critRate_": 0, "critDMG_": 0}}
candace_support = {"main_stats": {"sands": {"enerRech_": 1, "hp_": 1}, "goblet": {"hp_": 1, "hydro_dmg_": 1}, "circlet": {"hp_": 1, "critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0.175, "hp_": 0.8, "def": 0, "def_": 0, "atk": 0, "atk_": 0, "enerRech_": 1.0, "eleMas": 0, "critRate_": 0.9, "critDMG_": 0}}
dahlia_shield_support = {"main_stats": {"sands": {"enerRech_": 1, "hp_": 1}, "goblet": {"hp_": 1}, "circlet": {"hp_": 1}}, "sub_stats": {"hp": 0.175, "hp_": 0.9, "def": 0, "def_": 0, "atk": 0, "atk_": 0, "enerRech_": 1.0, "eleMas": 0, "critRate_": 0.8, "critDMG_": 0}}
aino_application_support = {"main_stats": {"sands": {"enerRech_": 1, "eleMas": 1}, "goblet": {"eleMas": 1}, "circlet": {"eleMas": 1, "critRate_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0, "atk_": 0, "enerRech_": 1.0, "eleMas": 0.9, "critRate_": 0.8, "critDMG_": 0}}
# 5 STAR HYDRO
hydro_traveler_support = {"main_stats": {"sands": {"enerRech_": 1, "atk_": 1}, "goblet": {"hydro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1, "heal_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.175, "atk_": 0.8, "enerRech_": 1.0, "eleMas": 0, "critRate_": 0.9, "critDMG_": 0.9}}
hydro_traveler_onField_dps = {"main_stats": {"sands": {"enerRech_": 1, "atk_": 1}, "goblet": {"hydro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0.125, "hp_": 0.7, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.8, "enerRech_": 1.0, "eleMas": 0, "critRate_": 0.9, "critDMG_": 0.9}}
tartaglia_dps = {"main_stats": {"sands": {"atk_": 1}, "goblet": {"hydro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.9, "enerRech_": 0.7, "eleMas": 0.8, "critRate_": 1.0, "critDMG_": 1.0}}
mona_dps = {"main_stats": {"sands": {"atk_": 1}, "goblet": {"hydro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.9, "enerRech_": 0.7, "eleMas": 0.8, "critRate_": 1.0, "critDMG_": 1.0}}
mona_nuke = {"main_stats": {"sands": {"atk_": 1, "enerRech_": 1, "eleMas": 1}, "goblet": {"hydro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.8, "enerRech_": 0.9, "eleMas": 0.7, "critRate_": 1.0, "critDMG_": 1.0}}
mona_burst_support = {"main_stats": {"sands": {"enerRech_": 1, "atk_": 1}, "goblet": {"hydro_dmg_": 1, "atk_": 1}, "circlet": {"critRate_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.175, "atk_": 0.8, "enerRech_": 1.0, "eleMas": 0, "critRate_": 0.9, "critDMG_": 0}}
sangonomiya_kokomi_support = {"main_stats": {"sands": {"enerRech_": 1, "hp_": 1}, "goblet": {"hp_": 1}, "circlet": {"heal_": 1, "hp_": 1}}, "sub_stats": {"hp": 0.175, "hp_": 0.9, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.8, "enerRech_": 1.0, "eleMas": 0, "critRate_": 0, "critDMG_": 0}}
sangonomiya_kokomi_dps = {"main_stats": {"sands": {"hp_": 1, "enerRech_": 1}, "goblet": {"hydro_dmg_": 1}, "circlet": {"heal_": 1}}, "sub_stats": {"hp": 0.2, "hp_": 1.0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.8, "enerRech_": 0.9, "eleMas": 0.7, "critRate_": 0, "critDMG_": 0}}
sangonomiya_kokomi_bloom_dps = {"main_stats": {"sands": {"eleMas": 1}, "goblet": {"eleMas": 1}, "circlet": {"eleMas": 1}}, "sub_stats": {"hp": 0.175, "hp_": 0.8, "def": 0, "def_": 0, "atk": 0, "atk_": 0, "enerRech_": 0.9, "eleMas": 1.0, "critRate_": 0, "critDMG_": 0}}
kamisato_ayato_dps = {"main_stats": {"sands": {"atk_": 1}, "goblet": {"hydro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0.1, "hp_": 0.7, "def": 0, "def_": 0, "atk": 0.125, "atk_": 0.9, "enerRech_": 0.8, "eleMas": 0.6, "critRate_": 1.0, "critDMG_": 1.0}}
yelan_offField_dps = {"main_stats": {"sands": {"enerRech_": 1, "hp_": 1}, "goblet": {"hydro_dmg_": 1, "hp_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1, "hp_": 1}}, "sub_stats": {"hp": 0.2, "hp_": 0.9, "def": 0, "def_": 0, "atk": 0, "atk_": 0, "enerRech_": 1.0, "eleMas": 0, "critRate_": 0.9, "critDMG_": 0.9}}
nilou_bloom_support = {"main_stats": {"sands": {"hp_": 1}, "goblet": {"hp_": 1}, "circlet": {"hp_": 1}}, "sub_stats": {"hp": 0.225, "hp_": 1.0, "def": 0, "def_": 0, "atk": 0, "atk_": 0, "enerRech_": 0, "eleMas": 0.8, "critRate_": 0, "critDMG_": 0}}
neuvillette_dps = {"main_stats": {"sands": {"hp_": 1}, "goblet": {"hydro_dmg_": 1, "hp_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1, "hp_": 1}}, "sub_stats": {"hp": 0.2, "hp_": 0.9, "def": 0, "def_": 0, "atk": 0, "atk_": 0, "enerRech_": 1.0, "eleMas": 0, "critRate_": 0.9, "critDMG_": 0.9}}
furina_offField_dps = {"main_stats": {"sands": {"enerRech_": 1, "hp_": 1}, "goblet": {"hp_": 1, "hydro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0.2, "hp_": 0.9, "def": 0, "def_": 0, "atk": 0, "atk_": 0, "enerRech_": 1.0, "eleMas": 0, "critRate_": 0.9, "critDMG_": 0.9}}
sigewinne_support = {"main_stats": {"sands": {"hp_": 1}, "goblet": {"hp_": 1}, "circlet": {"hp_": 1, "critRate_": 1}}, "sub_stats": {"hp": 0.225, "hp_": 1.0, "def": 0, "def_": 0, "atk": 0, "atk_": 0, "enerRech_": 0, "eleMas": 0, "critRate_": 0.8, "critDMG_": 0}}
mualani_vaporize_dps = {"main_stats": {"sands": {"hp_": 1, "eleMas": 1}, "goblet": {"hydro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1, "hp_": 1, "eleMas": 1}}, "sub_stats": {"hp": 0.2, "hp_": 0.9, "def": 0, "def_": 0, "atk": 0, "atk_": 0, "enerRech_": 0, "eleMas": 0.9, "critRate_": 1.0, "critDMG_": 1.0}}
# 4 STAR CRYO
diona_support = {"main_stats": {"sands": {"enerRech_": 1, "hp_": 1}, "goblet": {"hp_": 1}, "circlet": {"hp_": 1, "heal_": 1}}, "sub_stats": {"hp": 0.175, "hp_": 0.9, "def": 0, "def_": 0, "atk": 0, "atk_": 0, "enerRech_": 1.0, "eleMas": 0, "critRate_": 0.8, "critDMG_": 0}}
chongyun_burst_nuke = {"main_stats": {"sands": {"atk_": 1, "enerRech_": 1, "eleMas": 1}, "goblet": {"cryo_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.9, "enerRech_": 0.7, "eleMas": 0.8, "critRate_": 1.0, "critDMG_": 1.0}}
chongyun_infusion_support = {"main_stats": {"sands": {"atk_": 1, "enerRech_": 1}, "goblet": {"cryo_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.9, "enerRech_": 0.7, "eleMas": 0.8, "critRate_": 1.0, "critDMG_": 1.0}}
kaeya_freeze = {"main_stats": {"sands": {"atk_": 1}, "goblet": {"cryo_dmg_": 1}, "circlet": {"critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.9, "enerRech_": 0.8, "eleMas": 0, "critRate_": 0.7, "critDMG_": 1.0}}
kaeya_reverse_melt = {"main_stats": {"sands": {"enerRech_": 1, "atk_": 1}, "goblet": {"cryo_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.8, "enerRech_": 1.0, "eleMas": 0.7, "critRate_": 0.9, "critDMG_": 0.9}}
rosaria_reverse_melt = {"main_stats": {"sands": {"eleMas": 1, "atk_": 1}, "goblet": {"cryo_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.8, "enerRech_": 0.7, "eleMas": 0.8, "critRate_": 1.0, "critDMG_": 0.9}}
rosaria_freeze = {"main_stats": {"sands": {"atk_": 1}, "goblet": {"cryo_dmg_": 1}, "circlet": {"critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.9, "enerRech_": 0.8, "eleMas": 0, "critRate_": 0.7, "critDMG_": 1.0}}
rosaria_support = {"main_stats": {"sands": {"atk_": 1, "enerRech_": 1}, "goblet": {"cryo_dmg_": 1}, "circlet": {"critRate_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.7, "enerRech_": 0.9, "eleMas": 0, "critRate_": 1.0, "critDMG_": 0.8}}
layla_support = {"main_stats": {"sands": {"hp_": 1, "enerRech_": 1}, "goblet": {"hp_": 1}, "circlet": {"hp_": 1, "critRate_": 1}}, "sub_stats": {"hp": 0.175, "hp_": 0.9, "def": 0, "def_": 0, "atk": 0, "atk_": 0, "enerRech_": 1.0, "eleMas": 0, "critRate_": 0.8, "critDMG_": 0}}
layla_support_and_damage = {"main_stats": {"sands": {"hp_": 1, "enerRech_": 1}, "goblet": {"cryo_dmg_": 1, "hp_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1, "hp_": 1}}, "sub_stats": {"hp": 0.175, "hp_": 0.9, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.8, "enerRech_": 1.0, "eleMas": 0, "critRate_": 0.9, "critDMG_": 0.9}}
mika_support = {"main_stats": {"sands": {"enerRech_": 1, "hp_": 1}, "goblet": {"hp_": 1}, "circlet": {"heal_": 1, "critRate_": 1}}, "sub_stats": {"hp": 0.175, "hp_": 0.8, "def": 0, "def_": 0, "atk": 0, "atk_": 0, "enerRech_": 1.0, "eleMas": 0, "critRate_": 0.9, "critDMG_": 0}}
freminet_physical_dps = {"main_stats": {"sands": {"atk_": 1}, "goblet": {"physical_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.8, "enerRech_": 1.0, "eleMas": 0.7, "critRate_": 0.9, "critDMG_": 0.9}}
freminet_cryo_dps = {"main_stats": {"sands": {"atk_": 1}, "goblet": {"cryo_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.8, "enerRech_": 1.0, "eleMas": 0.7, "critRate_": 0.9, "critDMG_": 0.9}}
charlotte_support = {"main_stats": {"sands": {"enerRech_": 1, "atk_": 1}, "goblet": {"atk_": 1}, "circlet": {"heal_": 1, "atk_": 1, "critRate_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.175, "atk_": 0.9, "enerRech_": 1.0, "eleMas": 0, "critRate_": 0.8, "critDMG_": 0.6}}
# 5 STAR CRYO
qiqi_support = {"main_stats": {"sands": {"atk_": 1, "enerRech_": 1}, "goblet": {"atk_": 1}, "circlet": {"heal_": 1, "atk_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.2, "atk_": 1.0, "enerRech_": 0.9, "eleMas": 0, "critRate_": 0, "critDMG_": 0}}
ganyu_melt_dps = {"main_stats": {"sands": {"eleMas": 1, "atk_": 1}, "goblet": {"cryo_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.175, "atk_": 0.8, "enerRech_": 0, "eleMas": 0.9, "critRate_": 1.0, "critDMG_": 1.0}}
ganyu_freeze_dps = {"main_stats": {"sands": {"atk_": 1}, "goblet": {"cryo_dmg_": 1}, "circlet": {"critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.175, "atk_": 0.9, "enerRech_": 0.8, "eleMas": 0, "critRate_": 1.0, "critDMG_": 1.0}}
ganyu_mono_cryo_dps = {"main_stats": {"sands": {"atk_": 1}, "goblet": {"cryo_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.175, "atk_": 0.9, "enerRech_": 0.8, "eleMas": 0, "critRate_": 1.0, "critDMG_": 1.0}}
eula_dps = {"main_stats": {"sands": {"atk_": 1}, "goblet": {"physical_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.175, "atk_": 0.8, "enerRech_": 0.9, "eleMas": 0, "critRate_": 1.0, "critDMG_": 1.0}}
kamisato_ayaka_dps = {"main_stats": {"sands": {"atk_": 1}, "goblet": {"cryo_dmg_": 1}, "circlet": {"critDMG_": 1, "atk_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.9, "enerRech_": 0.8, "eleMas": 0, "critRate_": 0.7, "critDMG_": 1.0}}
aloy_burst_support = {"main_stats": {"sands": {"atk_": 1, "eleMas": 1}, "goblet": {"cryo_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.9, "enerRech_": 0.7, "eleMas": 0.8, "critRate_": 1.0, "critDMG_": 1.0}}
shenhe_support = {"main_stats": {"sands": {"atk_": 1, "enerRech_": 1}, "goblet": {"atk_": 1}, "circlet": {"atk_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.175, "atk_": 0.9, "enerRech_": 1.0, "eleMas": 0, "critRate_": 0.8, "critDMG_": 0.8}}
wriothesley_melt_dps = {"main_stats": {"sands": {"atk_": 1, "eleMas": 1}, "goblet": {"cryo_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.2, "atk_": 0.9, "enerRech_": 0, "eleMas": 0.9, "critRate_": 1.0, "critDMG_": 1.0}}
wriothesley_mono_cryo_freeze_dps = {"main_stats": {"sands": {"atk_": 1}, "goblet": {"cryo_dmg_": 1}, "circlet": {"critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.2, "atk_": 0.9, "enerRech_": 0.7, "eleMas": 0, "critRate_": 1.0, "critDMG_": 1.0}}
citlali_support = {"main_stats": {"sands": {"eleMas": 1, "enerRech_": 1}, "goblet": {"eleMas": 1}, "circlet": {"eleMas": 1, "critRate_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0, "atk_": 0, "enerRech_": 1.0, "eleMas": 0.9, "critRate_": 0.8, "critDMG_": 0}}
escoffier_offField_dps = {"main_stats": {"sands": {"atk_": 1, "enerRech_": 1}, "goblet": {"cryo_dmg_": 1, "atk_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.175, "atk_": 0.8, "enerRech_": 1.0, "eleMas": 0, "critRate_": 0.9, "critDMG_": 0.9}}
skirk_dps = {"main_stats": {"sands": {"atk_": 1}, "goblet": {"cryo_dmg_": 1, "atk_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.2, "atk_": 0.9, "enerRech_": 0, "eleMas": 0, "critRate_": 1.0, "critDMG_": 1.0}}
# 4 STAR ANEMO
sucrose_em_support = {"main_stats": {"sands": {"eleMas": 1}, "goblet": {"eleMas": 1}, "circlet": {"eleMas": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.8, "enerRech_": 0.9, "eleMas": 1.0, "critRate_": 0.7, "critDMG_": 0.7}}
sayu_support = {"main_stats": {"sands": {"enerRech_": 1, "eleMas": 1}, "goblet": {"eleMas": 1, "atk_": 1}, "circlet": {"heal_": 1, "eleMas": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.8, "enerRech_": 1.0, "eleMas": 0.9, "critRate_": 0.7, "critDMG_": 0}}
shikanoin_heizou_anemo_dps = {"main_stats": {"sands": {"atk_": 1}, "goblet": {"anemo_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.9, "enerRech_": 0.8, "eleMas": 0.7, "critRate_": 1.0, "critDMG_": 1.0}}
shikanoin_heizou_reaction_dps = {"main_stats": {"sands": {"eleMas": 1}, "goblet": {"eleMas": 1}, "circlet": {"eleMas": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.9, "enerRech_": 0.8, "eleMas": 1.0, "critRate_": 0.7, "critDMG_": 0}}
faruzan_support = {"main_stats": {"sands": {"enerRech_": 1}, "goblet": {"anemo_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.7, "enerRech_": 1.0, "eleMas": 0, "critRate_": 0.9, "critDMG_": 0.8}}
lynette_offField_dps = {"main_stats": {"sands": {"enerRech_": 1, "atk_": 1}, "goblet": {"anemo_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.7, "enerRech_": 1.0, "eleMas": 0, "critRate_": 0.9, "critDMG_": 0.8}}
lan_yan_support = {"main_stats": {"sands": {"atk_": 1, "enerRech_": 1}, "goblet": {"atk_": 1}, "circlet": {"atk_": 1, "critRate_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.9, "enerRech_": 1.0, "eleMas": 0.8, "critRate_": 0.7, "critDMG_": 0}}
lan_yan_driver = {"main_stats": {"sands": {"eleMas": 1, "atk_": 1, "enerRech_": 1}, "goblet": {"eleMas": 1, "atk_": 1}, "circlet": {"eleMas": 1, "atk_": 1, "critRate_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.9, "enerRech_": 1.0, "eleMas": 0.8, "critRate_": 0.7, "critDMG_": 0}}
ifa_reaction_dps = {"main_stats": {"sands": {"eleMas": 1, "enerRech_": 1}, "goblet": {"eleMas": 1}, "circlet": {"eleMas": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.8, "enerRech_": 1.0, "eleMas": 0.9, "critRate_": 0.7, "critDMG_": 0.7}}
ifa_anemo_dps = {"main_stats": {"sands": {"atk_": 1}, "goblet": {"anemo_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.9, "enerRech_": 0.7, "eleMas": 0.8, "critRate_": 1.0, "critDMG_": 1.0}}
# 5 STAR ANEMO
anemo_traveler_anemo_dps = {"main_stats": {"sands": {"eleMas": 1, "atk_": 1, "enerRech_": 1}, "goblet": {"eleMas": 1, "anemo_dmg_": 1}, "circlet": {"eleMas": 1, "critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.8, "enerRech_": 0.9, "eleMas": 1.0, "critRate_": 0.7, "critDMG_": 0.7}}
jean_support_and_damage = {"main_stats": {"sands": {"atk_": 1, "enerRech_": 1}, "goblet": {"anemo_dmg_": 1, "atk_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1, "heal_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.8, "enerRech_": 1.0, "eleMas": 0.7, "critRate_": 0.9, "critDMG_": 0.9}}
jean_reaction_dps = {"main_stats": {"sands": {"enerRech_": 1, "eleMas": 1}, "goblet": {"eleMas": 1}, "circlet": {"eleMas": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.175, "atk_": 0.8, "enerRech_": 1.0, "eleMas": 0.9, "critRate_": 0, "critDMG_": 0}}
venti_reaction_offField_dps = {"main_stats": {"sands": {"eleMas": 1}, "goblet": {"eleMas": 1}, "circlet": {"eleMas": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.8, "enerRech_": 0.9, "eleMas": 1.0, "critRate_": 0.7, "critDMG_": 0.7}}
venti_anemo_offField_dps = {"main_stats": {"sands": {"atk_": 1}, "goblet": {"atk_": 1, "anemo_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.8, "enerRech_": 0.9, "eleMas": 0.7, "critRate_": 1.0, "critDMG_": 1.0}}
xiao_dps = {"main_stats": {"sands": {"atk_": 1}, "goblet": {"anemo_dmg_": 1, "atk_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.175, "atk_": 0.8, "enerRech_": 1.0, "eleMas": 0.7, "critRate_": 0.9, "critDMG_": 0.9}}
kaedehara_kazuha_reaction_dps_and_support = {"main_stats": {"sands": {"eleMas": 1, "enerRech_": 1}, "goblet": {"eleMas": 1}, "circlet": {"eleMas": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0, "atk_": 0, "enerRech_": 1.0, "eleMas": 0.9, "critRate_": 0.8, "critDMG_": 0}}
wanderer_dps = {"main_stats": {"sands": {"atk_": 1}, "goblet": {"anemo_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.2, "atk_": 0.9, "enerRech_": 0.6, "eleMas": 0.7, "critRate_": 1.0, "critDMG_": 1.0}}
xianyun_support = {"main_stats": {"sands": {"atk_": 1, "enerRech_": 1}, "goblet": {"atk_": 1}, "circlet": {"atk_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.2, "atk_": 0.9, "enerRech_": 1.0, "eleMas": 0, "critRate_": 0.7, "critDMG_": 0}}
chasca_dps = {"main_stats": {"sands": {"atk_": 1}, "goblet": {"atk_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.9, "enerRech_": 0.7, "eleMas": 0.8, "critRate_": 1.0, "critDMG_": 1.0}}
yumemizuki_mizuki_reaction_dps = {"main_stats": {"sands": {"eleMas": 1, "enerRech_": 1}, "goblet": {"eleMas": 1}, "circlet": {"eleMas": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0, "atk_": 0, "enerRech_": 1.0, "eleMas": 0.9, "critRate_": 0.8, "critDMG_": 0}}
# 4 STAR GEO
ningguang_dps = {"main_stats": {"sands": {"atk_": 1}, "goblet": {"geo_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.175, "atk_": 0.9, "enerRech_": 0.8, "eleMas": 0, "critRate_": 1.0, "critDMG_": 1.0}}
noelle_dps = {"main_stats": {"sands": {"def_": 1, "atk_": 1}, "goblet": {"geo_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0.175, "def_": 0.8, "atk": 0, "atk_": 0, "enerRech_": 0.9, "eleMas": 0, "critRate_": 1.0, "critDMG_": 1.0}}
noelle_driver = {"main_stats": {"sands": {"def_": 1}, "goblet": {"geo_dmg_": 1, "def_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1, "def_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0.175, "def_": 0.8, "atk": 0, "atk_": 0, "enerRech_": 0.9, "eleMas": 0, "critRate_": 1.0, "critDMG_": 1.0}}
gorou_support = {"main_stats": {"sands": {"enerRech_": 1}, "goblet": {"geo_dmg_": 1, "def_": 1}, "circlet": {"critRate_": 1, "def_": 1, "heal_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0.175, "def_": 0.9, "atk": 0, "atk_": 0, "enerRech_": 1.0, "eleMas": 0, "critRate_": 0.8, "critDMG_": 0}}
yun_jin_support = {"main_stats": {"sands": {"def_": 1, "enerRech_": 1}, "goblet": {"def_": 1}, "circlet": {"def_": 1, "critRate_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0.2, "def_": 1.0, "atk": 0, "atk_": 0, "enerRech_": 0.9, "eleMas": 0, "critRate_": 0.7, "critDMG_": 0}}
kachina_support_and_offField_dps = {"main_stats": {"sands": {"def_": 1, "enerRech_": 1}, "goblet": {"geo_dmg_": 1, "def_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0.175, "def_": 0.8, "atk": 0, "atk_": 0, "enerRech_": 1.0, "eleMas": 0, "critRate_": 0.9, "critDMG_": 0.9}}
# 5 STAR GEO
geo_traveler_geo_dps = {"main_stats": {"sands": {"atk_": 1}, "goblet": {"geo_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.175, "atk_": 0.9, "enerRech_": 0.8, "eleMas": 0, "critRate_": 1.0, "critDMG_": 1.0}}
zhongli_shield_support = {"main_stats": {"sands": {"hp_": 1}, "goblet": {"hp_": 1}, "circlet": {"hp_": 1, "critRate_": 1}}, "sub_stats": {"hp": 0.225, "hp_": 1.0, "def": 0, "def_": 0, "atk": 0, "atk_": 0, "enerRech_": 0.8, "eleMas": 0, "critRate_": 0, "critDMG_": 0}}
zhongli_burst_support = {"main_stats": {"sands": {"atk_": 1, "hp_": 1}, "goblet": {"geo_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0.125, "hp_": 0.8, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.9, "enerRech_": 0.7, "eleMas": 0, "critRate_": 1.0, "critDMG_": 1.0}}
albedo_offField_dps = {"main_stats": {"sands": {"def_": 1}, "goblet": {"geo_dmg_": 1, "def_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1, "def_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0.15, "def_": 0.9, "atk": 0.125, "atk_": 0.8, "enerRech_": 0.7, "eleMas": 0, "critRate_": 1.0, "critDMG_": 1.0}}
arataki_itto_dps = {"main_stats": {"sands": {"def_": 1}, "goblet": {"geo_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0.15, "def_": 0.8, "atk": 0.125, "atk_": 0.7, "enerRech_": 1.0, "eleMas": 0, "critRate_": 0.9, "critDMG_": 0.9}}
navia_dps = {"main_stats": {"sands": {"atk_": 1, "enerRech_": 1}, "goblet": {"geo_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.175, "atk_": 0.8, "enerRech_": 1.0, "eleMas": 0, "critRate_": 0.9, "critDMG_": 0.9}}
chiori_offField_dps = {"main_stats": {"sands": {"def_": 1}, "goblet": {"geo_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0.175, "def_": 0.9, "atk": 0.15, "atk_": 0.8, "enerRech_": 0.5, "eleMas": 0, "critRate_": 1.0, "critDMG_": 1.0}}
xilonen_support = {"main_stats": {"sands": {"def_": 1, "enerRech_": 1}, "goblet": {"def_": 1}, "circlet": {"def_": 1, "heal_": 1, "critRate_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0.2, "def_": 0.9, "atk": 0, "atk_": 0, "enerRech_": 1.0, "eleMas": 0, "critRate_": 0.7, "critDMG_": 0}}


character_builds = {
        'amber_melt_dps': amber_melt_dps,
'amber_buff_support': amber_buff_support,
'xiangling_offField_dps': xiangling_offField_dps,
'bennett_support': bennett_support,
'bennett_dps': bennett_dps,
'xinyan_physical_dps': xinyan_physical_dps,
'xinyan_pyro_dps': xinyan_pyro_dps,
'xinyan_shield_support': xinyan_shield_support,
'yanfei_vaporize_dps': yanfei_vaporize_dps,
'yanfei_shield_support': yanfei_shield_support,
'thoma_burgeon': thoma_burgeon,
'thoma_shield_support': thoma_shield_support,
'chevreuse_buff_support': chevreuse_buff_support,
'chevreuse_buff_support_and_damage': chevreuse_buff_support_and_damage,
'gaming_dps': gaming_dps,
'pyro_traveler_buff_support': pyro_traveler_buff_support,
'pyro_traveler_dps': pyro_traveler_dps,
'diluc_dps': diluc_dps,
'klee_dps': klee_dps,
'hu_tao_dps': hu_tao_dps,
'yoimiya_dps': yoimiya_dps,
'dehya_onField_dps': dehya_onField_dps,
'dehya_support': dehya_tank_support,
'dehya_reaction_dps': dehya_burgeon,
'lyney_dps': lyney_dps,
'arlecchino_dps': arlecchino_dps,
'mavuika_dps_and_buff_support': mavuika_dps_and_buff_support,
'fischl_offField_dps': fischl_offField_dps,
'fischl_offField_aggravate_dps': fischl_offField_aggravate_dps,
'beidou_offField_dps': beidou_offField_dps,
'lisa_aggravate_dps': lisa_aggravate_dps,
'lisa_offField_dps': lisa_offField_dps,
'lisa_reaction_dps': lisa_reaction_dps,
'razor_hyperbloom_reaction_dps': razor_hyperbloom_reaction_dps,
'razor_physical_dps': razor_physical_dps,
'kujou_sara_buff_support_and_damage': kujou_sara_buff_support_and_damage,
'kuki_shinobu_hyperbloom': kuki_shinobu_hyperbloom,
'kuki_shinobu_aggravate_offField_dps': kuki_shinobu_aggravate_offField_dps,
'kuki_shinobu_support': kuki_shinobu_support,
'dori_support': dori_support,
'sethos_dps': sethos_dps,
'ororon_offField_dps': ororon_offField_dps,
'iansan_buff_support': iansan_buff_support,
'electro_traveler_support': electro_traveler_support,
'keqing_aggravate_dps': keqing_aggravate_dps,
'keqing_quickbloom_dps': keqing_quickbloom_dps,
'raiden_shogun_hyperbloom': raiden_shogun_hyperbloom,
'raiden_shogun_dps': raiden_shogun_dps,
'yae_miko_offField_dps': yae_miko_offField_dps,
'yae_miko_offField_aggravate_dps': yae_miko_offField_aggravate_dps,
'cyno_quickbloom_hyperbloom_dps': cyno_quickbloom_hyperbloom_dps,
'cyno_aggravate_dps': cyno_aggravate_dps,
'clorinde_dps': clorinde_dps,
'varesa_dps': varesa_dps,
'ineffa_offField_dps_support': ineffa_offField_dps_support,
'collei_support': collei_support,
'yaoyao_support': yaoyao_support,
'kaveh_bloom_burgeon_driver': kaveh_bloom_burgeon_driver,
'kirara_shield_support': kirara_shield_support,
'dendro_traveler_support': dendro_traveler_support,
'tighnari_quick_swap_dps': tighnari_quick_swap_dps,
'nahida_dps_and_support': nahida_dps_and_support,
'alhaitham_spread_dps': alhaitham_spread_dps,
'baizhu_support': baizhu_support,
'emilie_offField_dps': emilie_offField_dps,
'kinich_dps': kinich_dps,
'lauma_buff_support_high_energy': lauma_buff_support_high_energy,
'lauma_buff_support_low_energy': lauma_buff_support_low_energy,
'xingqiu_offField_dps': xingqiu_offField_dps,
'barbara_support': barbara_support,
'barbara_bloom_dps': barbara_bloom_dps,
'candace_support': candace_support,
'dahlia_shield_support': dahlia_shield_support,
'aino_application_support': aino_application_support,
'hydro_traveler_support': hydro_traveler_support,
'hydro_traveler_onField_dps': hydro_traveler_onField_dps,
'tartaglia_dps': tartaglia_dps,
'mona_dps': mona_dps,
'mona_nuke': mona_nuke,
'mona_burst_support': mona_burst_support,
'sangonomiya_kokomi_support': sangonomiya_kokomi_support,
'sangonomiya_kokomi_dps': sangonomiya_kokomi_dps,
'sangonomiya_kokomi_bloom_dps': sangonomiya_kokomi_bloom_dps,
'kamisato_ayato_dps': kamisato_ayato_dps,
'yelan_offField_dps': yelan_offField_dps,
'nilou_bloom_support': nilou_bloom_support,
'neuvillette_dps': neuvillette_dps,
'furina_offField_dps': furina_offField_dps,
'sigewinne_support': sigewinne_support,
'mualani_vaporize_dps': mualani_vaporize_dps,
'diona_support': diona_support,
'chongyun_burst_nuke': chongyun_burst_nuke,
'chongyun_infusion_support': chongyun_infusion_support,
'kaeya_freeze': kaeya_freeze,
'kaeya_reverse_melt': kaeya_reverse_melt,
'rosaria_reverse_melt': rosaria_reverse_melt,
'rosaria_freeze': rosaria_freeze,
'rosaria_support': rosaria_support,
'layla_support': layla_support,
'layla_support_and_damage': layla_support_and_damage,
'mika_support': mika_support,
'freminet_physical_dps': freminet_physical_dps,
'freminet_cryo_dps': freminet_cryo_dps,
'charlotte_support': charlotte_support,
'qiqi_support': qiqi_support,
'ganyu_melt_dps': ganyu_melt_dps,
'ganyu_freeze_dps': ganyu_freeze_dps,
'ganyu_mono_cryo_dps': ganyu_mono_cryo_dps,
'eula_dps': eula_dps,
'kamisato_ayaka_dps': kamisato_ayaka_dps,
'aloy_burst_support': aloy_burst_support,
'shenhe_support': shenhe_support,
'wriothesley_melt_dps': wriothesley_melt_dps,
'wriothesley_mono_cryo_freeze_dps': wriothesley_mono_cryo_freeze_dps,
'citlali_support': citlali_support,
'escoffier_offField_dps': escoffier_offField_dps,
'skirk_dps': skirk_dps,
'sucrose_em_support': sucrose_em_support,
'sayu_support': sayu_support,
'shikanoin_heizou_anemo_dps': shikanoin_heizou_anemo_dps,
'shikanoin_heizou_reaction_dps': shikanoin_heizou_reaction_dps,
'faruzan_support': faruzan_support,
'lynette_offField_dps': lynette_offField_dps,
'lan_yan_support': lan_yan_support,
'lan_yan_driver': lan_yan_driver,
'ifa_reaction_dps': ifa_reaction_dps,
'ifa_anemo_dps': ifa_anemo_dps,
'anemo_traveler_anemo_dps': anemo_traveler_anemo_dps,
'jean_support_and_damage': jean_support_and_damage,
'jean_reaction_dps': jean_reaction_dps,
'venti_reaction_offField_dps': venti_reaction_offField_dps,
'venti_anemo_offField_dps': venti_anemo_offField_dps,
'xiao_dps': xiao_dps,
'kaedehara_kazuha_reaction_dps_and_support': kaedehara_kazuha_reaction_dps_and_support,
'wanderer_dps': wanderer_dps,
'xianyun_support': xianyun_support,
'chasca_dps': chasca_dps,
'yumemizuki_mizuki_reaction_dps': yumemizuki_mizuki_reaction_dps,
'ningguang_dps': ningguang_dps,
'noelle_dps': noelle_dps,
'noelle_driver': noelle_driver,
'gorou_support': gorou_support,
'yun_jin_support': yun_jin_support,
'kachina_support_and_offField_dps': kachina_support_and_offField_dps,
'geo_traveler_geo_dps': geo_traveler_geo_dps,
'zhongli_shield_support': zhongli_shield_support,
'zhongli_burst_support': zhongli_burst_support,
'albedo_offField_dps': albedo_offField_dps,
'arataki_itto_dps': arataki_itto_dps,
'navia_dps': navia_dps,
'chiori_offField_dps': chiori_offField_dps,
'xilonen_support': xilonen_support,

}

for name, build in character_builds.items():
    count = count_unique_non_zero_stats(build)
    print(f"{name}: {count}")