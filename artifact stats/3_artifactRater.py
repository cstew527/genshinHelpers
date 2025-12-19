import json
import csv
import ratings_defs_2 as sim
from tqdm import tqdm

# --- Configuration ---
TARGET_SCORE = 75.0  # The specific score threshold we want to check the probability for

# --- Weight Definitions ---
# 4 STAR PYRO
amber_melt_dps = {'main_stats': {'sands': {'atk_': 1, 'eleMas': 1}, 'goblet': {'pyro_dmg_': 1}, 'circlet': {'critDMG_': 1}}, 'sub_stats': {'hp': 0, 'hp_': 0, 'def': 0, 'def_': 0, 'atk': 0.175, 'atk_': 0.9, 'enerRech_': 0, 'eleMas': 0.8, 'critRate_': 0, 'critDMG_': 1.0}}
amber_buff_support = {'main_stats': {'sands': {'enerRech_': 1, 'atk_': 1}, 'goblet': {'pyro_dmg_': 1}, 'circlet': {'critRate_': 1, 'critDMG_': 1}}, 'sub_stats': {'hp': 0, 'hp_': 0, 'def': 0, 'def_': 0, 'atk': 0.15, 'atk_': 0.8, 'enerRech_': 1.0, 'eleMas': 0.7, 'critRate_': 0.9, 'critDMG_': 0.9}}
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
dehya_support = {"main_stats": {"sands": {"hp_": 1}, "goblet": {"hp_": 1}, "circlet": {"hp_": 1, "critRate_": 1}}, "sub_stats": {"hp": 0.225, "hp_": 1.0, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.7, "enerRech_": 0, "eleMas": 0.8, "critRate_": 0, "critDMG_": 0}}
dehya_reaction_dps = {"main_stats": {"sands": {"eleMas": 1}, "goblet": {"eleMas": 1}, "circlet": {"eleMas": 1}}, "sub_stats": {"hp": 0.2, "hp_": 0.9, "def": 0, "def_": 0, "atk": 0, "atk_": 0, "enerRech_": 0, "eleMas": 1.0, "critRate_": 0.7, "critDMG_": 0}}
lyney_dps = {"main_stats": {"sands": {"atk_": 1}, "goblet": {"pyro_dmg_": 1}, "circlet": {"critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.175, "atk_": 0.9, "enerRech_": 0.8, "eleMas": 0, "critRate_": 1.0, "critDMG_": 1.0}}
arlecchino_dps = {"main_stats": {"sands": {"atk_": 1, "eleMas": 1}, "goblet": {"pyro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.175, "atk_": 0.8, "enerRech_": 0, "eleMas": 0.9, "critRate_": 1.0, "critDMG_": 1.0}}
mavuika_dps_and_buff_support = {"main_stats": {"sands": {"eleMas": 1, "atk_": 1}, "goblet": {"pyro_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.175, "atk_": 0.9, "enerRech_": 0, "eleMas": 0.8, "critRate_": 1.0, "critDMG_": 1.0}}
durin_vaporize_melt_offField_dps = {'main_stats': {'sands': {'atk_': 1}, 'goblet': {'pyro_dmg_': 1, 'atk_': 1}, 'circlet': {'critRate_': 1, 'critDMG_': 1}}, 'sub_stats': {'hp': 0, 'hp_': 0, 'def': 0, 'def_': 0, 'atk': 0.15, 'atk_': 0.9, 'enerRech_': 0.7, 'eleMas': 0.8, 'critRate_': 1.0, 'critDMG_': 1.0}}
durin_buff_support_and_offField_dps = {'main_stats': {'sands': {'atk_': 1}, 'goblet': {'pyro_dmg_': 1, 'atk_': 1}, 'circlet': {'critRate_': 1, 'critDMG_': 1}}, 'sub_stats': {'hp': 0, 'hp_': 0, 'def': 0, 'def_': 0, 'atk': 0.175, 'atk_': 0.9, 'enerRech_': 0.8, 'eleMas': 0, 'critRate_': 1.0, 'critDMG_': 1.0}}
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
varesa_dps = {'main_stats': {'sands': {'atk_': 1}, 'goblet': {'electro_dmg_': 1}, 'circlet': {'critRate_': 1, 'critDMG_': 1}}, 'sub_stats': {'hp': 0, 'hp_': 0, 'def': 0, 'def_': 0, 'atk': 0.175, 'atk_': 0.8, 'enerRech_': 1.0, 'eleMas': 0, 'critRate_': 0.9, 'critDMG_': 0.9}}
ineffa_offField_dps_support = {"main_stats": {"sands": {"atk_": 1, "enerRech_": 1}, "goblet": {"atk_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.175, "atk_": 0.8, "enerRech_": 1.0, "eleMas": 0.8, "critRate_": 0.9, "critDMG_": 0.9}}
flins_dps = {'main_stats': {'sands': {'atk_': 1}, 'goblet': {'atk_': 1}, 'circlet': {'critRate_': 1, 'critDMG_': 1}}, 'sub_stats': {'hp': 0, 'hp_': 0, 'def': 0, 'def_': 0, 'atk': 0.175, 'atk_': 0.8, 'enerRech_': 1.0, 'eleMas': 0.8, 'critRate_': 0.9, 'critDMG_': 0.9}}
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
nefer_dps = {'main_stats': {'sands': {'eleMas': 1}, 'goblet': {'eleMas': 1}, 'circlet': {'critRate_': 1, 'critDMG_': 1}}, 'sub_stats': {'hp': 0, 'hp_': 0, 'def': 0, 'def_': 0, 'atk': 0, 'atk_': 0, 'enerRech_': 0, 'eleMas': 0.9, 'critRate_': 1.0, 'critDMG_': 1.0}}
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
jahoda_offField_reaction_dps_and_heal_support = {'main_stats': {'sands': {'enerRech_': 1, 'atk_': 1}, 'goblet': {'atk_': 1}, 'circlet': {'heal_': 1, 'atk_': 1, 'critRate_': 1}}, 'sub_stats': {'hp': 0, 'hp_': 0, 'def': 0, 'def_': 0, 'atk': 0.15, 'atk_': 0.9, 'enerRech_': 1.0, 'eleMas': 0.7, 'critRate_': 0.8, 'critDMG_': 0}}
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
kachina_buff_and_reaction_support = {'main_stats': {'sands': {'def_': 1, 'enerRech_': 1}, 'goblet': {'geo_dmg_%': 1, 'def_': 1}, 'circlet': {'critRate_': 1, 'critDMG_': 1}}, 'sub_stats': {'hp': 0, 'hp_': 0, 'def': 0.175, 'def_': 0.8, 'atk': 0, 'atk_': 0, 'enerRech_': 1.0, 'eleMas': 0, 'critRate_': 0.9, 'critDMG_': 0.9}}
# 5 STAR GEO
geo_traveler_geo_dps = {"main_stats": {"sands": {"atk_": 1}, "goblet": {"geo_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.175, "atk_": 0.9, "enerRech_": 0.8, "eleMas": 0, "critRate_": 1.0, "critDMG_": 1.0}}
zhongli_shield_support = {"main_stats": {"sands": {"hp_": 1}, "goblet": {"hp_": 1}, "circlet": {"hp_": 1, "critRate_": 1}}, "sub_stats": {"hp": 0.225, "hp_": 1.0, "def": 0, "def_": 0, "atk": 0, "atk_": 0, "enerRech_": 0.8, "eleMas": 0, "critRate_": 0, "critDMG_": 0}}
zhongli_burst_support = {"main_stats": {"sands": {"atk_": 1, "hp_": 1}, "goblet": {"geo_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0.125, "hp_": 0.8, "def": 0, "def_": 0, "atk": 0.15, "atk_": 0.9, "enerRech_": 0.7, "eleMas": 0, "critRate_": 1.0, "critDMG_": 1.0}}
albedo_offField_dps = {"main_stats": {"sands": {"def_": 1}, "goblet": {"geo_dmg_": 1, "def_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1, "def_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0.15, "def_": 0.9, "atk": 0.125, "atk_": 0.8, "enerRech_": 0.7, "eleMas": 0, "critRate_": 1.0, "critDMG_": 1.0}}
arataki_itto_dps = {"main_stats": {"sands": {"def_": 1}, "goblet": {"geo_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0.15, "def_": 0.8, "atk": 0.125, "atk_": 0.7, "enerRech_": 1.0, "eleMas": 0, "critRate_": 0.9, "critDMG_": 0.9}}
navia_dps = {"main_stats": {"sands": {"atk_": 1, "enerRech_": 1}, "goblet": {"geo_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0, "def_": 0, "atk": 0.175, "atk_": 0.8, "enerRech_": 1.0, "eleMas": 0, "critRate_": 0.9, "critDMG_": 0.9}}
chiori_offField_dps = {"main_stats": {"sands": {"def_": 1}, "goblet": {"geo_dmg_": 1}, "circlet": {"critRate_": 1, "critDMG_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0.175, "def_": 0.9, "atk": 0.15, "atk_": 0.8, "enerRech_": 0.5, "eleMas": 0, "critRate_": 1.0, "critDMG_": 1.0}}
xilonen_support = {"main_stats": {"sands": {"def_": 1, "enerRech_": 1}, "goblet": {"def_": 1}, "circlet": {"def_": 1, "heal_": 1, "critRate_": 1}}, "sub_stats": {"hp": 0, "hp_": 0, "def": 0.2, "def_": 0.9, "atk": 0, "atk_": 0, "enerRech_": 1.0, "eleMas": 0, "critRate_": 0.7, "critDMG_": 0}}

# --- Load Data ---
try:
    with open('artifacts.json', 'r') as f:
        artifact_db = json.load(f)
except FileNotFoundError:
    print("Error: 'artifacts.json' not found. Please ensure the file is in the same directory.")
    exit()

# --- CSV Setup ---
csv_headers = [
    'Level', 'Set', 'Slot', 'Stars', 'Main Stat', 'Main Stat Value', 'Sub Stat 1', 'Sub Stat Value 1', 'Sub Stat 2',
    'Sub Stat Value 2', 'Sub Stat 3', 'Sub Stat Value 3', 'Sub Stat 4', 'Sub Stat Value 4', 'max',
    # 4 Star Pyro
    'amber melt dps score', 'amber buff support score', 'xiangling offField dps score', 'bennett dps score',
    'bennett support score', 'xinyan physical dps score', 'xinyan pyro dps score', 'xinyan shield support score',
    'yanfei vaporize dps score', 'yanfei shield support score', 'thoma burgeon score', 'thoma shield support score',
    'chevreuse buff support score', 'chevreuse buff support and damage score', 'gaming dps score',
    # 5 Star Pyro
    'pyro traveler buff support score', 'pyro traveler dps score', 'diluc dps score', 'klee dps score',
    'hu tao dps score', 'yoimiya dps score', 'dehya onField dps score', 'dehya support score',
    'dehya reaction dps score', 'lyney dps score', 'arlecchino dps score', 'mavuika dps and buff support score',
    'durin vaporize melt offField dps score', 'durin buff support and offField dps score',
    # 4 Star Electro
    'fischl offField dps score', 'fischl offField aggravate dps score', 'beidou offField dps score',
    'lisa aggravate dps score', 'lisa offField dps score', 'lisa reaction dps score',
    'razor hyperbloom reaction dps score', 'razor physical dps score', 'kujou sara buff support and damage score',
    'kuki shinobu hyperbloom score', 'kuki shinobu aggravate offField dps score', 'kuki shinobu support score',
    'dori support score', 'sethos dps score', 'ororon offField dps score', 'iansan buff support score',
    # 5 Star Electro
    'electro traveler support score', 'keqing aggravate dps score', 'keqing quickbloom dps score',
    'raiden shogun hyperbloom score', 'raiden shogun dps score', 'yae miko offField dps score',
    'yae miko offField aggravate dps score', 'cyno quickbloom hyperbloom dps score', 'cyno aggravate dps score',
    'clorinde dps score', 'varesa dps score', 'ineffa offField dps support score', 'flins dps score',
    # 4 Star Hydro
    'xingqiu offField dps score', 'barbara support score', 'barbara bloom dps score', 'candace support score',
    'dahlia shield support score', 'aino application support score',
    # 5 Star Hydro
    'hydro traveler support score', 'hydro traveler onField dps', 'tartaglia dps score', 'mona dps score',
    'mona nuke score', 'mona burst support score', 'sangonomiya kokomi support score', 'sangonomiya kokomi dps score',
    'sangonomiya kokomi bloom dps score', 'kamisato ayato dps score', 'yelan offField dps score',
    'nilou bloom support score', 'neuvillette dps score', 'furina offField dps score', 'sigewinne support score',
    'mualani vaporize dps score',
    # 4 Star Cryo
    'diona support score', 'chongyun burst nuke score', 'chongyun infusion support score', 'kaeya freeze score',
    'kaeya reverse melt score', 'rosaria reverse melt score', 'rosaria freeze score', 'rosaria support score',
    'layla support score', 'layla support and damage score', 'mika support score', 'freminet physical dps score',
    'freminet cryo dps score', 'charlotte support score',
    # 5 Star Cryo
    'qiqi support score', 'ganyu melt dps score', 'ganyu freeze dps score', 'ganyu mono cryo dps score',
    'eula dps score', 'kamisato ayaka dps score', 'aloy burst support score', 'shenhe support score',
    'wriothesley melt dps score', 'wriothesley mono cryo freeze dps score', 'citlali support score',
    'escoffier offField dps score', 'skirk dps score',
    # 4 Star Anemo
    'sucrose em support score', 'sayu support score', 'shikanoin heizou anemo dps score',
    'shikanoin heizou reaction dps score', 'faruzan support score', 'lynette offField dps score',
    'lan yan support score', 'lan yan driver score', 'ifa reaction dps score', 'ifa anemo dps score',
    'jahoda offField reaction dps and heal support score',
    # 5 Star Anemo
    'anemo traveler anemo dps score', 'jean support and damage score', 'jean reaction dps score',
    'venti reaction offField dps score', 'venti anemo offField dps score', 'xiao dps score',
    'kaedehara kazuha reaction dps and support score', 'wanderer dps score', 'xianyun support score',
    'chasca dps score', 'yumemizuki mizuki reaction dps score',
    # 4 Star Geo
    'ningguang dps score', 'noelle dps score', 'noelle driver score', 'gorou support score', 'yun jin support score',
    'kachina buff and reaction support score',
    # 5 Star Geo
    'geo traveler geo dps score', 'zhongli shield support score', 'zhongli burst support score',
    'albedo offField dps score', 'arataki itto dps score', 'navia dps score', 'chiori offField dps score',
    'xilonen support score',
    # 4 Star Dendro
    'collei support score', 'yaoyao support score', 'kaveh bloom burgeon driver score', 'kirara shield support score',
    # 5 Star Dendro
    'dendro traveler support score', 'tighnari quick swap dps score', 'nahida dps and support score',
    'alhaitham spread dps score', 'baizhu support score', 'emilie offField dps score', 'kinich dps score',
    'lauma buff support high energy score', 'lauma buff support low energy score', 'nefer dps score'
]

with open('artifacts.csv', 'w', newline='') as outputFile:
    writer = csv.DictWriter(outputFile, fieldnames=csv_headers)
    writer.writeheader()

    print(f"Processing {len(artifact_db.get('artifacts', []))} artifacts...")
    print(f"Calculating probability of reaching {TARGET_SCORE}% score capacity...")

    for a in tqdm(artifact_db.get('artifacts', [])):
        # Safe substat extraction (handles < 4 substats)
        subs = a.get('substats', [])
        sub_data = {}
        for i in range(4):
            if i < len(subs):
                sub_data[f'Sub Stat {i + 1}'] = subs[i]['key']
                sub_data[f'Sub Stat Value {i + 1}'] = subs[i]['value']
            else:
                sub_data[f'Sub Stat {i + 1}'] = ""
                sub_data[f'Sub Stat Value {i + 1}'] = ""

        # Calculate Max Main Stat Value (Visual reference)
        # Accessing dictionary directly to avoid AttributeError if helper function is missing
        rarity = a.get('rarity', 5)
        key = a.get('mainStatKey')
        current_main_val = sim.MAX_MAINS.get(rarity, sim.MAX_MAINS[5]).get(key, 0)

        # --- Simulation ---
        # 4 Star Pyro
        amber_melt_dps_value = sim.calculate_exact_probability(a, amber_melt_dps)
        amber_buff_support_value = sim.calculate_exact_probability(a, amber_buff_support)
        xiangling_offField_dps_value = sim.calculate_exact_probability(a, xiangling_offField_dps)
        bennett_support_value = sim.calculate_exact_probability(a, bennett_support)
        bennett_dps_value = sim.calculate_exact_probability(a, bennett_dps)
        xinyan_physical_dps_value = sim.calculate_exact_probability(a, xinyan_physical_dps)
        xinyan_pyro_dps_value = sim.calculate_exact_probability(a, xinyan_pyro_dps)
        xinyan_shield_support_value = sim.calculate_exact_probability(a, xinyan_shield_support)
        yanfei_vaporize_dps_value = sim.calculate_exact_probability(a, yanfei_vaporize_dps)
        yanfei_shield_support_value = sim.calculate_exact_probability(a, yanfei_shield_support)
        thoma_burgeon_value = sim.calculate_exact_probability(a, thoma_burgeon)
        thoma_shield_support_value = sim.calculate_exact_probability(a, thoma_shield_support)
        chevreuse_buff_support_value = sim.calculate_exact_probability(a, chevreuse_buff_support)
        chevreuse_buff_support_and_damage_value = sim.calculate_exact_probability(a, chevreuse_buff_support_and_damage)
        gaming_dps_value = sim.calculate_exact_probability(a, gaming_dps)
        # 5 Star Pyro
        pyro_traveler_buff_support_value = sim.calculate_exact_probability(a, pyro_traveler_buff_support)
        pyro_traveler_dps_value = sim.calculate_exact_probability(a, pyro_traveler_dps)
        diluc_dps_value = sim.calculate_exact_probability(a, diluc_dps)
        klee_dps_value = sim.calculate_exact_probability(a, klee_dps)
        hu_tao_dps_value = sim.calculate_exact_probability(a, hu_tao_dps)
        yoimiya_dps_value = sim.calculate_exact_probability(a, yoimiya_dps)
        dehya_onField_dps_value = sim.calculate_exact_probability(a, dehya_onField_dps)
        dehya_support_value = sim.calculate_exact_probability(a, dehya_support)
        dehya_reaction_dps_value = sim.calculate_exact_probability(a, dehya_reaction_dps)
        lyney_dps_value = sim.calculate_exact_probability(a, lyney_dps)
        arlecchino_dps_value = sim.calculate_exact_probability(a, arlecchino_dps)
        mavuika_dps_and_buff_support_value = sim.calculate_exact_probability(a, mavuika_dps_and_buff_support)
        durin_vaporize_melt_offField_dps_value = sim.calculate_exact_probability(a, durin_vaporize_melt_offField_dps)
        durin_buff_support_and_offField_dps_value = sim.calculate_exact_probability(a, durin_buff_support_and_offField_dps)
        # 4 Star Electro
        fischl_offField_dps_value = sim.calculate_exact_probability(a, fischl_offField_dps)
        fischl_offField_aggravate_dps_value = sim.calculate_exact_probability(a, fischl_offField_aggravate_dps)
        beidou_offField_dps_value = sim.calculate_exact_probability(a, beidou_offField_dps)
        lisa_aggravate_dps_value = sim.calculate_exact_probability(a, lisa_aggravate_dps)
        lisa_offField_dps_value = sim.calculate_exact_probability(a, lisa_offField_dps)
        lisa_reaction_dps_value = sim.calculate_exact_probability(a, lisa_reaction_dps)
        razor_hyperbloom_reaction_dps_value = sim.calculate_exact_probability(a, razor_hyperbloom_reaction_dps)
        razor_physical_dps_value = sim.calculate_exact_probability(a, razor_physical_dps)
        kujou_sara_buff_support_and_damage_value = sim.calculate_exact_probability(a, kujou_sara_buff_support_and_damage)
        kuki_shinobu_hyperbloom_value = sim.calculate_exact_probability(a, kuki_shinobu_hyperbloom)
        kuki_shinobu_aggravate_offField_dps_value = sim.calculate_exact_probability(a, kuki_shinobu_aggravate_offField_dps)
        kuki_shinobu_support_value = sim.calculate_exact_probability(a, kuki_shinobu_support)
        dori_support_value = sim.calculate_exact_probability(a, dori_support)
        sethos_dps_value = sim.calculate_exact_probability(a, sethos_dps)
        ororon_offField_dps_value = sim.calculate_exact_probability(a, ororon_offField_dps)
        iansan_buff_support_value = sim.calculate_exact_probability(a, iansan_buff_support)
        # 5 Star Electro
        electro_traveler_support_value = sim.calculate_exact_probability(a, electro_traveler_support)
        keqing_aggravate_dps_value = sim.calculate_exact_probability(a, keqing_aggravate_dps)
        keqing_quickbloom_dps_value = sim.calculate_exact_probability(a, keqing_quickbloom_dps)
        raiden_shogun_hyperbloom_value = sim.calculate_exact_probability(a, raiden_shogun_hyperbloom)
        raiden_shogun_dps_value = sim.calculate_exact_probability(a, raiden_shogun_dps)
        yae_miko_offField_dps_value = sim.calculate_exact_probability(a, yae_miko_offField_dps)
        yae_miko_offField_aggravate_dps_value = sim.calculate_exact_probability(a, yae_miko_offField_aggravate_dps)
        cyno_quickbloom_hyperbloom_dps_value = sim.calculate_exact_probability(a, cyno_quickbloom_hyperbloom_dps)
        cyno_aggravate_dps_value = sim.calculate_exact_probability(a, cyno_aggravate_dps)
        clorinde_dps_value = sim.calculate_exact_probability(a, clorinde_dps)
        varesa_dps_value = sim.calculate_exact_probability(a, varesa_dps)
        ineffa_offField_dps_support_value = sim.calculate_exact_probability(a, ineffa_offField_dps_support)
        flins_dps_value = sim.calculate_exact_probability(a, flins_dps)
        # 4 Star Dendro
        collei_support_value = sim.calculate_exact_probability(a, collei_support)
        yaoyao_support_value = sim.calculate_exact_probability(a, yaoyao_support)
        kaveh_bloom_burgeon_driver_value = sim.calculate_exact_probability(a, kaveh_bloom_burgeon_driver)
        kirara_shield_support_value = sim.calculate_exact_probability(a, kirara_shield_support)
        # 5 Star Dendro
        dendro_traveler_support_value = sim.calculate_exact_probability(a, dendro_traveler_support)
        tighnari_quick_swap_dps_value = sim.calculate_exact_probability(a, tighnari_quick_swap_dps)
        nahida_dps_and_support_value = sim.calculate_exact_probability(a, nahida_dps_and_support)
        alhaitham_spread_dps_value = sim.calculate_exact_probability(a, alhaitham_spread_dps)
        baizhu_support_value = sim.calculate_exact_probability(a, baizhu_support)
        emilie_offField_dps_value = sim.calculate_exact_probability(a, emilie_offField_dps)
        kinich_dps_value = sim.calculate_exact_probability(a, kinich_dps)
        lauma_buff_support_high_energy_value = sim.calculate_exact_probability(a, lauma_buff_support_high_energy)
        lauma_buff_support_low_energy_value = sim.calculate_exact_probability(a, lauma_buff_support_low_energy)
        nefer_dps_value = sim.calculate_exact_probability(a, nefer_dps)
        # 4 Star Hydro
        xingqiu_offField_dps_value = sim.calculate_exact_probability(a, xingqiu_offField_dps)
        barbara_support_value = sim.calculate_exact_probability(a, barbara_support)
        barbara_bloom_dps_value = sim.calculate_exact_probability(a, barbara_bloom_dps)
        candace_support_value = sim.calculate_exact_probability(a, candace_support)
        dahlia_shield_support_value = sim.calculate_exact_probability(a, dahlia_shield_support)
        aino_application_support_value = sim.calculate_exact_probability(a, aino_application_support)
        # 5 Star Hydro
        hydro_traveler_support_value = sim.calculate_exact_probability(a, hydro_traveler_support)
        hydro_traveler_onField_dps_value = sim.calculate_exact_probability(a, hydro_traveler_onField_dps)
        tartaglia_dps_value = sim.calculate_exact_probability(a, tartaglia_dps)
        mona_dps_value = sim.calculate_exact_probability(a, mona_dps)
        mona_nuke_value = sim.calculate_exact_probability(a, mona_nuke)
        mona_burst_support_value = sim.calculate_exact_probability(a, mona_burst_support)
        sangonomiya_kokomi_support_value = sim.calculate_exact_probability(a, sangonomiya_kokomi_support)
        sangonomiya_kokomi_dps_value = sim.calculate_exact_probability(a, sangonomiya_kokomi_dps)
        sangonomiya_kokomi_bloom_dps_value = sim.calculate_exact_probability(a, sangonomiya_kokomi_bloom_dps)
        kamisato_ayato_dps_value = sim.calculate_exact_probability(a, kamisato_ayato_dps)
        yelan_offField_dps_value = sim.calculate_exact_probability(a, yelan_offField_dps)
        nilou_bloom_support_value = sim.calculate_exact_probability(a, nilou_bloom_support)
        neuvillette_dps_value = sim.calculate_exact_probability(a, neuvillette_dps)
        furina_offField_dps_value = sim.calculate_exact_probability(a, furina_offField_dps)
        sigewinne_support_value = sim.calculate_exact_probability(a, sigewinne_support)
        mualani_vaporize_dps_value = sim.calculate_exact_probability(a, mualani_vaporize_dps)
        diona_support_value = sim.calculate_exact_probability(a, diona_support)
        chongyun_burst_nuke_value = sim.calculate_exact_probability(a, chongyun_burst_nuke)
        chongyun_infusion_support_value = sim.calculate_exact_probability(a, chongyun_infusion_support)
        kaeya_freeze_value = sim.calculate_exact_probability(a, kaeya_freeze)
        kaeya_reverse_melt_value = sim.calculate_exact_probability(a, kaeya_reverse_melt)
        rosaria_reverse_melt_value = sim.calculate_exact_probability(a, rosaria_reverse_melt)
        rosaria_freeze_value = sim.calculate_exact_probability(a, rosaria_freeze)
        rosaria_support_value = sim.calculate_exact_probability(a, rosaria_support)
        layla_support_value = sim.calculate_exact_probability(a, layla_support)
        layla_support_and_damage_value = sim.calculate_exact_probability(a, layla_support_and_damage)
        mika_support_value = sim.calculate_exact_probability(a, mika_support)
        freminet_physical_dps_value = sim.calculate_exact_probability(a, freminet_physical_dps)
        freminet_cryo_dps_value = sim.calculate_exact_probability(a, freminet_cryo_dps)
        charlotte_support_value = sim.calculate_exact_probability(a, charlotte_support)
        qiqi_support_value = sim.calculate_exact_probability(a, qiqi_support)
        ganyu_melt_dps_value = sim.calculate_exact_probability(a, ganyu_melt_dps)
        ganyu_freeze_dps_value = sim.calculate_exact_probability(a, ganyu_freeze_dps)
        ganyu_mono_cryo_dps_value = sim.calculate_exact_probability(a, ganyu_mono_cryo_dps)
        eula_dps_value = sim.calculate_exact_probability(a, eula_dps)
        kamisato_ayaka_dps_value = sim.calculate_exact_probability(a, kamisato_ayaka_dps)
        aloy_burst_support_value = sim.calculate_exact_probability(a, aloy_burst_support)
        shenhe_support_value = sim.calculate_exact_probability(a, shenhe_support)
        wriothesley_melt_dps_value = sim.calculate_exact_probability(a, wriothesley_melt_dps)
        wriothesley_mono_cryo_freeze_dps_value = sim.calculate_exact_probability(a, wriothesley_mono_cryo_freeze_dps)
        citlali_support_value = sim.calculate_exact_probability(a, citlali_support)
        escoffier_offField_dps_value = sim.calculate_exact_probability(a, escoffier_offField_dps)
        skirk_dps_value = sim.calculate_exact_probability(a, skirk_dps)
        sucrose_em_support_value = sim.calculate_exact_probability(a, sucrose_em_support)
        sayu_support_value = sim.calculate_exact_probability(a, sayu_support)
        shikanoin_heizou_anemo_dps_value = sim.calculate_exact_probability(a, shikanoin_heizou_anemo_dps)
        shikanoin_heizou_reaction_dps_value = sim.calculate_exact_probability(a, shikanoin_heizou_reaction_dps)
        faruzan_support_value = sim.calculate_exact_probability(a, faruzan_support)
        lynette_offField_dps_value = sim.calculate_exact_probability(a, lynette_offField_dps)
        lan_yan_support_value = sim.calculate_exact_probability(a, lan_yan_support)
        lan_yan_driver_value = sim.calculate_exact_probability(a, lan_yan_driver)
        ifa_reaction_dps_value = sim.calculate_exact_probability(a, ifa_reaction_dps)
        ifa_anemo_dps_value = sim.calculate_exact_probability(a, ifa_anemo_dps)
        jahoda_offField_reaction_dps_and_heal_support_value = sim.calculate_exact_probability(a, jahoda_offField_reaction_dps_and_heal_support)
        anemo_traveler_anemo_dps_value = sim.calculate_exact_probability(a, anemo_traveler_anemo_dps)
        jean_support_and_damage_value = sim.calculate_exact_probability(a, jean_support_and_damage)
        jean_reaction_dps_value = sim.calculate_exact_probability(a, jean_reaction_dps)
        venti_reaction_offField_dps_value = sim.calculate_exact_probability(a, venti_reaction_offField_dps)
        venti_anemo_offField_dps_value = sim.calculate_exact_probability(a, venti_anemo_offField_dps)
        xiao_dps_value = sim.calculate_exact_probability(a, xiao_dps)
        kaedehara_kazuha_reaction_dps_and_support_value = sim.calculate_exact_probability(a, kaedehara_kazuha_reaction_dps_and_support)
        wanderer_dps_value = sim.calculate_exact_probability(a, wanderer_dps)
        xianyun_support_value = sim.calculate_exact_probability(a, xianyun_support)
        chasca_dps_value = sim.calculate_exact_probability(a, chasca_dps)
        yumemizuki_mizuki_reaction_dps_value = sim.calculate_exact_probability(a, yumemizuki_mizuki_reaction_dps)
        # 4 Star Geo
        ningguang_dps_value = sim.calculate_exact_probability(a, ningguang_dps)
        noelle_dps_value = sim.calculate_exact_probability(a, noelle_dps)
        noelle_driver_value = sim.calculate_exact_probability(a, noelle_driver)
        gorou_support_value = sim.calculate_exact_probability(a, gorou_support)
        yun_jin_support_value = sim.calculate_exact_probability(a, yun_jin_support)
        kachina_buff_and_reaction_support_value = sim.calculate_exact_probability(a, kachina_buff_and_reaction_support)
        # 5 Star Geo
        geo_traveler_geo_dps_value = sim.calculate_exact_probability(a, geo_traveler_geo_dps)
        zhongli_shield_support_value = sim.calculate_exact_probability(a, zhongli_shield_support)
        zhongli_burst_support_value = sim.calculate_exact_probability(a, zhongli_burst_support)
        albedo_offField_dps_value = sim.calculate_exact_probability(a, albedo_offField_dps)
        arataki_itto_dps_value = sim.calculate_exact_probability(a, arataki_itto_dps)
        navia_dps_value = sim.calculate_exact_probability(a, navia_dps)
        chiori_offField_dps_value = sim.calculate_exact_probability(a, chiori_offField_dps)
        xilonen_support_value = sim.calculate_exact_probability(a, xilonen_support)

        amber_melt_dps_score = sim.get_probability_greater_than(amber_melt_dps_value, TARGET_SCORE)
        amber_buff_support_score = sim.get_probability_greater_than(amber_buff_support_value, TARGET_SCORE)
        xiangling_offField_dps_score = sim.get_probability_greater_than(xiangling_offField_dps_value, TARGET_SCORE)
        bennett_support_score = sim.get_probability_greater_than(bennett_support_value, TARGET_SCORE)
        bennett_dps_score = sim.get_probability_greater_than(bennett_dps_value, TARGET_SCORE)
        xinyan_physical_dps_score = sim.get_probability_greater_than(xinyan_physical_dps_value, TARGET_SCORE)
        xinyan_pyro_dps_score = sim.get_probability_greater_than(xinyan_pyro_dps_value, TARGET_SCORE)
        xinyan_shield_support_score = sim.get_probability_greater_than(xinyan_shield_support_value, TARGET_SCORE)
        yanfei_vaporize_dps_score = sim.get_probability_greater_than(yanfei_vaporize_dps_value, TARGET_SCORE)
        yanfei_shield_support_score = sim.get_probability_greater_than(yanfei_shield_support_value, TARGET_SCORE)
        thoma_burgeon_score = sim.get_probability_greater_than(thoma_burgeon_value, TARGET_SCORE)
        thoma_shield_support_score = sim.get_probability_greater_than(thoma_shield_support_value, TARGET_SCORE)
        chevreuse_buff_support_score = sim.get_probability_greater_than(chevreuse_buff_support_value, TARGET_SCORE)
        chevreuse_buff_support_and_damage_score = sim.get_probability_greater_than(chevreuse_buff_support_and_damage_value, TARGET_SCORE)
        gaming_dps_score = sim.get_probability_greater_than(gaming_dps_value, TARGET_SCORE)
        pyro_traveler_buff_support_score = sim.get_probability_greater_than(pyro_traveler_buff_support_value, TARGET_SCORE)
        pyro_traveler_dps_score = sim.get_probability_greater_than(pyro_traveler_dps_value, TARGET_SCORE)
        diluc_dps_score = sim.get_probability_greater_than(diluc_dps_value, TARGET_SCORE)
        klee_dps_score = sim.get_probability_greater_than(klee_dps_value, TARGET_SCORE)
        hu_tao_dps_score = sim.get_probability_greater_than(hu_tao_dps_value, TARGET_SCORE)
        yoimiya_dps_score = sim.get_probability_greater_than(yoimiya_dps_value, TARGET_SCORE)
        dehya_onField_dps_score = sim.get_probability_greater_than(dehya_onField_dps_value, TARGET_SCORE)
        dehya_support_score = sim.get_probability_greater_than(dehya_support_value, TARGET_SCORE)
        dehya_reaction_dps_score = sim.get_probability_greater_than(dehya_reaction_dps_value, TARGET_SCORE)
        lyney_dps_score = sim.get_probability_greater_than(lyney_dps_value, TARGET_SCORE)
        arlecchino_dps_score = sim.get_probability_greater_than(arlecchino_dps_value, TARGET_SCORE)
        mavuika_dps_and_buff_support_score = sim.get_probability_greater_than(mavuika_dps_and_buff_support_value, TARGET_SCORE)
        durin_vaporize_melt_offField_dps_score = sim.get_probability_greater_than(durin_vaporize_melt_offField_dps_value, TARGET_SCORE)
        durin_buff_support_and_offField_dps_score = sim.get_probability_greater_than(durin_buff_support_and_offField_dps_value, TARGET_SCORE)
        fischl_offField_dps_score = sim.get_probability_greater_than(fischl_offField_dps_value, TARGET_SCORE)
        fischl_offField_aggravate_dps_score = sim.get_probability_greater_than(fischl_offField_aggravate_dps_value, TARGET_SCORE)
        beidou_offField_dps_score = sim.get_probability_greater_than(beidou_offField_dps_value, TARGET_SCORE)
        lisa_aggravate_dps_score = sim.get_probability_greater_than(lisa_aggravate_dps_value, TARGET_SCORE)
        lisa_offField_dps_score = sim.get_probability_greater_than(lisa_offField_dps_value, TARGET_SCORE)
        lisa_reaction_dps_score = sim.get_probability_greater_than(lisa_reaction_dps_value, TARGET_SCORE)
        razor_hyperbloom_reaction_dps_score = sim.get_probability_greater_than(razor_hyperbloom_reaction_dps_value, TARGET_SCORE)
        razor_physical_dps_score = sim.get_probability_greater_than(razor_physical_dps_value, TARGET_SCORE)
        kujou_sara_buff_support_and_damage_score = sim.get_probability_greater_than(kujou_sara_buff_support_and_damage_value, TARGET_SCORE)
        kuki_shinobu_hyperbloom_score = sim.get_probability_greater_than(kuki_shinobu_hyperbloom_value, TARGET_SCORE)
        kuki_shinobu_aggravate_offField_dps_score = sim.get_probability_greater_than( kuki_shinobu_aggravate_offField_dps_value, TARGET_SCORE)
        kuki_shinobu_support_score = sim.get_probability_greater_than(kuki_shinobu_support_value, TARGET_SCORE)
        dori_support_score = sim.get_probability_greater_than(dori_support_value, TARGET_SCORE)
        sethos_dps_score = sim.get_probability_greater_than(sethos_dps_value, TARGET_SCORE)
        ororon_offField_dps_score = sim.get_probability_greater_than(ororon_offField_dps_value, TARGET_SCORE)
        iansan_buff_support_score = sim.get_probability_greater_than(iansan_buff_support_value, TARGET_SCORE)
        electro_traveler_support_score = sim.get_probability_greater_than(electro_traveler_support_value, TARGET_SCORE)
        keqing_aggravate_dps_score = sim.get_probability_greater_than(keqing_aggravate_dps_value, TARGET_SCORE)
        keqing_quickbloom_dps_score = sim.get_probability_greater_than(keqing_quickbloom_dps_value, TARGET_SCORE)
        raiden_shogun_hyperbloom_score = sim.get_probability_greater_than(raiden_shogun_hyperbloom_value, TARGET_SCORE)
        raiden_shogun_dps_score = sim.get_probability_greater_than(raiden_shogun_dps_value, TARGET_SCORE)
        yae_miko_offField_dps_score = sim.get_probability_greater_than(yae_miko_offField_dps_value, TARGET_SCORE)
        yae_miko_offField_aggravate_dps_score = sim.get_probability_greater_than(yae_miko_offField_aggravate_dps_value, TARGET_SCORE)
        cyno_quickbloom_hyperbloom_dps_score = sim.get_probability_greater_than(cyno_quickbloom_hyperbloom_dps_value, TARGET_SCORE)
        cyno_aggravate_dps_score = sim.get_probability_greater_than(cyno_aggravate_dps_value, TARGET_SCORE)
        clorinde_dps_score = sim.get_probability_greater_than(clorinde_dps_value, TARGET_SCORE)
        varesa_dps_score = sim.get_probability_greater_than(varesa_dps_value, TARGET_SCORE)
        ineffa_offField_dps_support_score = sim.get_probability_greater_than(ineffa_offField_dps_support_value, TARGET_SCORE)
        flins_dps_score = sim.get_probability_greater_than(flins_dps_value, TARGET_SCORE)
        collei_support_score = sim.get_probability_greater_than(collei_support_value, TARGET_SCORE)
        yaoyao_support_score = sim.get_probability_greater_than(yaoyao_support_value, TARGET_SCORE)
        kaveh_bloom_burgeon_driver_score = sim.get_probability_greater_than(kaveh_bloom_burgeon_driver_value, TARGET_SCORE)
        kirara_shield_support_score = sim.get_probability_greater_than(kirara_shield_support_value, TARGET_SCORE)
        dendro_traveler_support_score = sim.get_probability_greater_than(dendro_traveler_support_value, TARGET_SCORE)
        tighnari_quick_swap_dps_score = sim.get_probability_greater_than(tighnari_quick_swap_dps_value, TARGET_SCORE)
        nahida_dps_and_support_score = sim.get_probability_greater_than(nahida_dps_and_support_value, TARGET_SCORE)
        alhaitham_spread_dps_score = sim.get_probability_greater_than(alhaitham_spread_dps_value, TARGET_SCORE)
        baizhu_support_score = sim.get_probability_greater_than(baizhu_support_value, TARGET_SCORE)
        emilie_offField_dps_score = sim.get_probability_greater_than(emilie_offField_dps_value, TARGET_SCORE)
        kinich_dps_score = sim.get_probability_greater_than(kinich_dps_value, TARGET_SCORE)
        lauma_buff_support_high_energy_score = sim.get_probability_greater_than(lauma_buff_support_high_energy_value, TARGET_SCORE)
        lauma_buff_support_low_energy_score = sim.get_probability_greater_than(lauma_buff_support_low_energy_value, TARGET_SCORE)
        nefer_dps_score = sim.get_probability_greater_than(nefer_dps_value, TARGET_SCORE)
        xingqiu_offField_dps_score = sim.get_probability_greater_than(xingqiu_offField_dps_value, TARGET_SCORE)
        barbara_support_score = sim.get_probability_greater_than(barbara_support_value, TARGET_SCORE)
        barbara_bloom_dps_score = sim.get_probability_greater_than(barbara_bloom_dps_value, TARGET_SCORE)
        candace_support_score = sim.get_probability_greater_than(candace_support_value, TARGET_SCORE)
        dahlia_shield_support_score = sim.get_probability_greater_than(dahlia_shield_support_value, TARGET_SCORE)
        aino_application_support_score = sim.get_probability_greater_than(aino_application_support_value, TARGET_SCORE)
        hydro_traveler_support_score = sim.get_probability_greater_than(hydro_traveler_support_value, TARGET_SCORE)
        hydro_traveler_onField_dps_score = sim.get_probability_greater_than(hydro_traveler_onField_dps_value, TARGET_SCORE)
        tartaglia_dps_score = sim.get_probability_greater_than(tartaglia_dps_value, TARGET_SCORE)
        mona_dps_score = sim.get_probability_greater_than(mona_dps_value, TARGET_SCORE)
        mona_nuke_score = sim.get_probability_greater_than(mona_nuke_value, TARGET_SCORE)
        mona_burst_support_score = sim.get_probability_greater_than(mona_burst_support_value, TARGET_SCORE)
        sangonomiya_kokomi_support_score = sim.get_probability_greater_than(sangonomiya_kokomi_support_value, TARGET_SCORE)
        sangonomiya_kokomi_dps_score = sim.get_probability_greater_than(sangonomiya_kokomi_dps_value, TARGET_SCORE)
        sangonomiya_kokomi_bloom_dps_score = sim.get_probability_greater_than(sangonomiya_kokomi_bloom_dps_value, TARGET_SCORE)
        kamisato_ayato_dps_score = sim.get_probability_greater_than(kamisato_ayato_dps_value, TARGET_SCORE)
        yelan_offField_dps_score = sim.get_probability_greater_than(yelan_offField_dps_value, TARGET_SCORE)
        nilou_bloom_support_score = sim.get_probability_greater_than(nilou_bloom_support_value, TARGET_SCORE)
        neuvillette_dps_score = sim.get_probability_greater_than(neuvillette_dps_value, TARGET_SCORE)
        furina_offField_dps_score = sim.get_probability_greater_than(furina_offField_dps_value, TARGET_SCORE)
        sigewinne_support_score = sim.get_probability_greater_than(sigewinne_support_value, TARGET_SCORE)
        mualani_vaporize_dps_score = sim.get_probability_greater_than(mualani_vaporize_dps_value, TARGET_SCORE)
        diona_support_score = sim.get_probability_greater_than(diona_support_value, TARGET_SCORE)
        chongyun_burst_nuke_score = sim.get_probability_greater_than(chongyun_burst_nuke_value, TARGET_SCORE)
        chongyun_infusion_support_score = sim.get_probability_greater_than(chongyun_infusion_support_value, TARGET_SCORE)
        kaeya_freeze_score = sim.get_probability_greater_than(kaeya_freeze_value, TARGET_SCORE)
        kaeya_reverse_melt_score = sim.get_probability_greater_than(kaeya_reverse_melt_value, TARGET_SCORE)
        rosaria_reverse_melt_score = sim.get_probability_greater_than(rosaria_reverse_melt_value, TARGET_SCORE)
        rosaria_freeze_score = sim.get_probability_greater_than(rosaria_freeze_value, TARGET_SCORE)
        rosaria_support_score = sim.get_probability_greater_than(rosaria_support_value, TARGET_SCORE)
        layla_support_score = sim.get_probability_greater_than(layla_support_value, TARGET_SCORE)
        layla_support_and_damage_score = sim.get_probability_greater_than(layla_support_and_damage_value, TARGET_SCORE)
        mika_support_score = sim.get_probability_greater_than(mika_support_value, TARGET_SCORE)
        freminet_physical_dps_score = sim.get_probability_greater_than(freminet_physical_dps_value, TARGET_SCORE)
        freminet_cryo_dps_score = sim.get_probability_greater_than(freminet_cryo_dps_value, TARGET_SCORE)
        charlotte_support_score = sim.get_probability_greater_than(charlotte_support_value, TARGET_SCORE)
        qiqi_support_score = sim.get_probability_greater_than(qiqi_support_value, TARGET_SCORE)
        ganyu_melt_dps_score = sim.get_probability_greater_than(ganyu_melt_dps_value, TARGET_SCORE)
        ganyu_freeze_dps_score = sim.get_probability_greater_than(ganyu_freeze_dps_value, TARGET_SCORE)
        ganyu_mono_cryo_dps_score = sim.get_probability_greater_than(ganyu_mono_cryo_dps_value, TARGET_SCORE)
        eula_dps_score = sim.get_probability_greater_than(eula_dps_value, TARGET_SCORE)
        kamisato_ayaka_dps_score = sim.get_probability_greater_than(kamisato_ayaka_dps_value, TARGET_SCORE)
        aloy_burst_support_score = sim.get_probability_greater_than(aloy_burst_support_value, TARGET_SCORE)
        shenhe_support_score = sim.get_probability_greater_than(shenhe_support_value, TARGET_SCORE)
        wriothesley_melt_dps_score = sim.get_probability_greater_than(wriothesley_melt_dps_value, TARGET_SCORE)
        wriothesley_mono_cryo_freeze_dps_score = sim.get_probability_greater_than(wriothesley_mono_cryo_freeze_dps_value, TARGET_SCORE)
        citlali_support_score = sim.get_probability_greater_than(citlali_support_value, TARGET_SCORE)
        escoffier_offField_dps_score = sim.get_probability_greater_than(escoffier_offField_dps_value, TARGET_SCORE)
        skirk_dps_score = sim.get_probability_greater_than(skirk_dps_value, TARGET_SCORE)
        sucrose_em_support_score = sim.get_probability_greater_than(sucrose_em_support_value, TARGET_SCORE)
        sayu_support_score = sim.get_probability_greater_than(sayu_support_value, TARGET_SCORE)
        shikanoin_heizou_anemo_dps_score = sim.get_probability_greater_than(shikanoin_heizou_anemo_dps_value, TARGET_SCORE)
        shikanoin_heizou_reaction_dps_score = sim.get_probability_greater_than(shikanoin_heizou_reaction_dps_value, TARGET_SCORE)
        faruzan_support_score = sim.get_probability_greater_than(faruzan_support_value, TARGET_SCORE)
        lynette_offField_dps_score = sim.get_probability_greater_than(lynette_offField_dps_value, TARGET_SCORE)
        lan_yan_support_score = sim.get_probability_greater_than(lan_yan_support_value, TARGET_SCORE)
        lan_yan_driver_score = sim.get_probability_greater_than(lan_yan_driver_value, TARGET_SCORE)
        ifa_reaction_dps_score = sim.get_probability_greater_than(ifa_reaction_dps_value, TARGET_SCORE)
        ifa_anemo_dps_score = sim.get_probability_greater_than(ifa_anemo_dps_value, TARGET_SCORE)
        jahoda_offField_reaction_dps_and_heal_support_score = sim.get_probability_greater_than(jahoda_offField_reaction_dps_and_heal_support_value, TARGET_SCORE)
        anemo_traveler_anemo_dps_score = sim.get_probability_greater_than(anemo_traveler_anemo_dps_value, TARGET_SCORE)
        jean_support_and_damage_score = sim.get_probability_greater_than(jean_support_and_damage_value, TARGET_SCORE)
        jean_reaction_dps_score = sim.get_probability_greater_than(jean_reaction_dps_value, TARGET_SCORE)
        venti_reaction_offField_dps_score = sim.get_probability_greater_than(venti_reaction_offField_dps_value, TARGET_SCORE)
        venti_anemo_offField_dps_score = sim.get_probability_greater_than(venti_anemo_offField_dps_value, TARGET_SCORE)
        xiao_dps_score = sim.get_probability_greater_than(xiao_dps_value, TARGET_SCORE)
        kaedehara_kazuha_reaction_dps_and_support_score = sim.get_probability_greater_than(
            kaedehara_kazuha_reaction_dps_and_support_value, TARGET_SCORE)
        wanderer_dps_score = sim.get_probability_greater_than(wanderer_dps_value, TARGET_SCORE)
        xianyun_support_score = sim.get_probability_greater_than(xianyun_support_value, TARGET_SCORE)
        chasca_dps_score = sim.get_probability_greater_than(chasca_dps_value, TARGET_SCORE)
        yumemizuki_mizuki_reaction_dps_score = sim.get_probability_greater_than(yumemizuki_mizuki_reaction_dps_value, TARGET_SCORE)
        # 4 Star Geo
        ningguang_dps_score = sim.get_probability_greater_than(ningguang_dps_value, TARGET_SCORE)
        noelle_dps_score = sim.get_probability_greater_than(noelle_dps_value, TARGET_SCORE)
        noelle_driver_score = sim.get_probability_greater_than(noelle_driver_value, TARGET_SCORE)
        gorou_support_score = sim.get_probability_greater_than(gorou_support_value, TARGET_SCORE)
        yun_jin_support_score = sim.get_probability_greater_than(yun_jin_support_value, TARGET_SCORE)
        kachina_buff_and_reaction_support_score = sim.get_probability_greater_than(kachina_buff_and_reaction_support_value, TARGET_SCORE)
        # 5 Star Geo
        geo_traveler_geo_dps_score = sim.get_probability_greater_than(geo_traveler_geo_dps_value, TARGET_SCORE)
        zhongli_shield_support_score = sim.get_probability_greater_than(zhongli_shield_support_value, TARGET_SCORE)
        zhongli_burst_support_score = sim.get_probability_greater_than(zhongli_burst_support_value, TARGET_SCORE)
        albedo_offField_dps_score = sim.get_probability_greater_than(albedo_offField_dps_value, TARGET_SCORE)
        arataki_itto_dps_score = sim.get_probability_greater_than(arataki_itto_dps_value, TARGET_SCORE)
        navia_dps_score = sim.get_probability_greater_than(navia_dps_value, TARGET_SCORE)
        chiori_offField_dps_score = sim.get_probability_greater_than(chiori_offField_dps_value, TARGET_SCORE)
        xilonen_support_score = sim.get_probability_greater_than(xilonen_support_value, TARGET_SCORE)

        # Write Row
        row = {
            'Level': a.get('level', 0),
            'Set': a.get('setKey', ''),
            'Slot': a.get('slotKey', ''),
            'Stars': a.get('rarity', 5),
            'Main Stat': a.get('mainStatKey', ''),
            'Main Stat Value': current_main_val,
            'amber melt dps score': amber_melt_dps_score,
            'amber buff support score': amber_buff_support_score,
            'xiangling offField dps score': xiangling_offField_dps_score,
            'bennett dps score': bennett_dps_score,
            'bennett support score': bennett_support_score,
            'xinyan physical dps score': xinyan_physical_dps_score,
            'xinyan pyro dps score': xinyan_pyro_dps_score,
            'xinyan shield support score': xinyan_shield_support_score,
            'yanfei vaporize dps score': yanfei_vaporize_dps_score,
            'yanfei shield support score': yanfei_shield_support_score,
            'thoma burgeon score': thoma_burgeon_score,
            'thoma shield support score': thoma_shield_support_score,
            'chevreuse buff support score': chevreuse_buff_support_score,
            'chevreuse buff support and damage score': chevreuse_buff_support_and_damage_score,
            'gaming dps score': gaming_dps_score,
            'pyro traveler buff support score': pyro_traveler_buff_support_score,
            'pyro traveler dps score': pyro_traveler_dps_score,
            'diluc dps score': diluc_dps_score,
            'klee dps score': klee_dps_score,
            'hu tao dps score': hu_tao_dps_score,
            'yoimiya dps score': yoimiya_dps_score,
            'dehya onField dps score': dehya_onField_dps_score,
            'dehya support score': dehya_support_score,
            'dehya reaction dps score': dehya_reaction_dps_score,
            'lyney dps score': lyney_dps_score,
            'arlecchino dps score': arlecchino_dps_score,
            'mavuika dps and buff support score': mavuika_dps_and_buff_support_score,
            'durin vaporize melt offField dps score': durin_vaporize_melt_offField_dps_score,
            'durin buff support and offField dps score': durin_buff_support_and_offField_dps_score,
            'fischl offField dps score': fischl_offField_dps_score,
            'fischl offField aggravate dps score': fischl_offField_aggravate_dps_score,
            'beidou offField dps score': beidou_offField_dps_score,
            'lisa aggravate dps score': lisa_aggravate_dps_score,
            'lisa offField dps score': lisa_offField_dps_score,
            'lisa reaction dps score': lisa_reaction_dps_score,
            'razor hyperbloom reaction dps score': razor_hyperbloom_reaction_dps_score,
            'razor physical dps score': razor_physical_dps_score,
            'kujou sara buff support and damage score': kujou_sara_buff_support_and_damage_score,
            'kuki shinobu hyperbloom score': kuki_shinobu_hyperbloom_score,
            'kuki shinobu aggravate offField dps score': kuki_shinobu_aggravate_offField_dps_score,
            'kuki shinobu support score': kuki_shinobu_support_score,
            'dori support score': dori_support_score,
            'sethos dps score': sethos_dps_score,
            'ororon offField dps score': ororon_offField_dps_score,
            'iansan buff support score': iansan_buff_support_score,
            'electro traveler support score': electro_traveler_support_score,
            'keqing aggravate dps score': keqing_aggravate_dps_score,
            'keqing quickbloom dps score': keqing_quickbloom_dps_score,
            'raiden shogun hyperbloom score': raiden_shogun_hyperbloom_score,
            'raiden shogun dps score': raiden_shogun_dps_score,
            'yae miko offField dps score': yae_miko_offField_dps_score,
            'yae miko offField aggravate dps score': yae_miko_offField_aggravate_dps_score,
            'cyno quickbloom hyperbloom dps score': cyno_quickbloom_hyperbloom_dps_score,
            'cyno aggravate dps score': cyno_aggravate_dps_score,
            'clorinde dps score': clorinde_dps_score,
            'varesa dps score': varesa_dps_score,
            'ineffa offField dps support score': ineffa_offField_dps_support_score,
            'flins dps score': flins_dps_score,
            'xingqiu offField dps score': xingqiu_offField_dps_score,
            'barbara support score': barbara_support_score,
            'barbara bloom dps score': barbara_bloom_dps_score,
            'candace support score': candace_support_score,
            'dahlia shield support score': dahlia_shield_support_score,
            'aino application support score': aino_application_support_score,
            'hydro traveler support score': hydro_traveler_support_score,
            'hydro traveler onField dps': hydro_traveler_onField_dps_score,
            'tartaglia dps score': tartaglia_dps_score,
            'mona dps score': mona_dps_score,
            'mona nuke score': mona_nuke_score,
            'mona burst support score': mona_burst_support_score,
            'sangonomiya kokomi support score': sangonomiya_kokomi_support_score,
            'sangonomiya kokomi dps score': sangonomiya_kokomi_dps_score,
            'sangonomiya kokomi bloom dps score': sangonomiya_kokomi_bloom_dps_score,
            'kamisato ayato dps score': kamisato_ayato_dps_score,
            'yelan offField dps score': yelan_offField_dps_score,
            'nilou bloom support score': nilou_bloom_support_score,
            'neuvillette dps score': neuvillette_dps_score,
            'furina offField dps score': furina_offField_dps_score,
            'sigewinne support score': sigewinne_support_score,
            'mualani vaporize dps score': mualani_vaporize_dps_score,
            'diona support score': diona_support_score,
            'chongyun burst nuke score': chongyun_burst_nuke_score,
            'chongyun infusion support score': chongyun_infusion_support_score,
            'kaeya freeze score': kaeya_freeze_score,
            'kaeya reverse melt score': kaeya_reverse_melt_score,
            'rosaria reverse melt score': rosaria_reverse_melt_score,
            'rosaria freeze score': rosaria_freeze_score,
            'rosaria support score': rosaria_support_score,
            'layla support score': layla_support_score,
            'layla support and damage score': layla_support_and_damage_score,
            'mika support score': mika_support_score,
            'freminet physical dps score': freminet_physical_dps_score,
            'freminet cryo dps score': freminet_cryo_dps_score,
            'charlotte support score': charlotte_support_score,
            'qiqi support score': qiqi_support_score,
            'ganyu melt dps score': ganyu_melt_dps_score,
            'ganyu freeze dps score': ganyu_freeze_dps_score,
            'ganyu mono cryo dps score': ganyu_mono_cryo_dps_score,
            'eula dps score': eula_dps_score,
            'kamisato ayaka dps score': kamisato_ayaka_dps_score,
            'aloy burst support score': aloy_burst_support_score,
            'shenhe support score': shenhe_support_score,
            'wriothesley melt dps score': wriothesley_melt_dps_score,
            'wriothesley mono cryo freeze dps score': wriothesley_mono_cryo_freeze_dps_score,
            'citlali support score': citlali_support_score,
            'escoffier offField dps score': escoffier_offField_dps_score,
            'skirk dps score': skirk_dps_score,
            'sucrose em support score': sucrose_em_support_score,
            'sayu support score': sayu_support_score,
            'shikanoin heizou anemo dps score': shikanoin_heizou_anemo_dps_score,
            'shikanoin heizou reaction dps score': shikanoin_heizou_reaction_dps_score,
            'faruzan support score': faruzan_support_score,
            'lynette offField dps score': lynette_offField_dps_score,
            'lan yan support score': lan_yan_support_score,
            'lan yan driver score': lan_yan_driver_score,
            'ifa reaction dps score': ifa_reaction_dps_score,
            'ifa anemo dps score': ifa_anemo_dps_score,
            'jahoda offField reaction dps and heal support score': jahoda_offField_reaction_dps_and_heal_support_score,
            'anemo traveler anemo dps score': anemo_traveler_anemo_dps_score,
            'jean support and damage score': jean_support_and_damage_score,
            'jean reaction dps score': jean_reaction_dps_score,
            'venti reaction offField dps score': venti_reaction_offField_dps_score,
            'venti anemo offField dps score': venti_anemo_offField_dps_score,
            'xiao dps score': xiao_dps_score,
            'kaedehara kazuha reaction dps and support score': kaedehara_kazuha_reaction_dps_and_support_score,
            'wanderer dps score': wanderer_dps_score,
            'xianyun support score': xianyun_support_score,
            'chasca dps score': chasca_dps_score,
            'yumemizuki mizuki reaction dps score': yumemizuki_mizuki_reaction_dps_score,
            # 4 Star Geo
            'ningguang dps score': ningguang_dps_score,
            'noelle dps score': noelle_dps_score,
            'noelle driver score': noelle_driver_score,
            'gorou support score': gorou_support_score,
            'yun jin support score': yun_jin_support_score,
            'kachina buff and reaction support score': kachina_buff_and_reaction_support_score,
            # 5 Star Geo
            'geo traveler geo dps score': geo_traveler_geo_dps_score,
            'zhongli shield support score': zhongli_shield_support_score,
            'zhongli burst support score': zhongli_burst_support_score,
            'albedo offField dps score': albedo_offField_dps_score,
            'arataki itto dps score': arataki_itto_dps_score,
            'navia dps score': navia_dps_score,
            'chiori offField dps score': chiori_offField_dps_score,
            'xilonen support score': xilonen_support_score,
            'collei support score': collei_support_score,
            'yaoyao support score': yaoyao_support_score,
            'kaveh bloom burgeon driver score': kaveh_bloom_burgeon_driver_score,
            'kirara shield support score': kirara_shield_support_score,
            'dendro traveler support score': dendro_traveler_support_score,
            'tighnari quick swap dps score': tighnari_quick_swap_dps_score,
            'nahida dps and support score': nahida_dps_and_support_score,
            'alhaitham spread dps score': alhaitham_spread_dps_score,
            'baizhu support score': baizhu_support_score,
            'emilie offField dps score': emilie_offField_dps_score,
            'kinich dps score': kinich_dps_score,
            'lauma buff support high energy score': lauma_buff_support_high_energy_score,
            'lauma buff support low energy score': lauma_buff_support_low_energy_score,
            'nefer dps score': nefer_dps_score,
        }
        # Merge substat data into row
        row.update(sub_data)

        writer.writerow(row)

print("Done! Results saved to artifacts.csv")