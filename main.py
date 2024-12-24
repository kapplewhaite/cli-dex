"""
CLI Dex
Kaiden Applewhaite
12/22/2024
"""

from requests import get as g

def get_data(pokémon:int|str) -> dict:
    response = g(f"https://pokeapi.co/api/v2/{pokémon}")
    data = response.json()

    return data

def get_ability_list(pdict:dict) -> list:
    ability_list = []

    for key in pdict['abilities']:
        ability_str = ""
        ability_str += pdict[key]['ability']['name']

        if pdict[key]['ability']['is_hidden']:
            ability_str += "(Hidden)"

        ability_list.append(ability_str)

    return ability_list

def get_type(pdict:dict) -> str:
    type_1 = ""
    type_2 = ""

    type_1 += pdict['types'][0]['type']['name']

    try:
        type_2 += pdict['types'][1]['type']['name']
    except:
        type_2 = ""
    
    return f"{type_1}, {type_2}"

def get_moveset_list(pdict:dict) -> list[tuple]:
    moveset_list = []

    for key in pdict['moves']:
        move_data = pdict['moves'][key]['version_group_details']

        for game in move_data:
            if move_data[game]['version_group']['name'] == 'scarlet-violet':
                move = pdict['moves'][key]['name']
                level = move_data['level_learned_at']

        moveset_list.append((level, move))

    moveset_list.sort()
    return moveset_list


