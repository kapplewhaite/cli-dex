"""
CLI Dex
Kaiden Applewhaite
12/22/2024
"""
from pokemon import Pokémon
from requests import get as g
import os

pokédex = Pokémon()
# Clear Console command
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def get_data(pokémon:int|str) -> dict:
    url = f"https://pokeapi.co/api/v2/pokemon/{pokémon}"
    response = g(url)
    data = response.json()

    return data

def get_ability_list(pdict:dict) -> list:
    ability_list = []

    for a_dict in pdict['abilities']:
        ability_str = ""
        ability_str += a_dict['ability']['name']

        if a_dict['is_hidden']:
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

    for m_dict in pdict['moves']:

        for vgd_dict in m_dict['version_group_details']:

            if vgd_dict['version_group']['name'] == 'lets-go-pikachu-lets-go-eevee':
                move = m_dict['move']['name']
                level = vgd_dict['level_learned_at']

                moveset_list.append((level, move))

    moveset_list.sort()
    return moveset_list

def main():
    while True:

        pokémon = input("Enter a Pokémon name or Pokédex #: ")

        if not pokédex.check_query(pokémon):
            print("Please try again")
            continue

        data = get_data(pokémon)
        
        abilities = get_ability_list(data)
        types = get_type(data)
        moves = get_moveset_list(data)

        clearConsole()

        print(f"Name: {data['name']}\n")
        print(f"Dex #: {data['id']}\n")
        print(f"Abilities: {abilities}\n")
        print(f"Types: {types}\n")
        print(f"Moves: {moves}")

        run_again = input("Search again? (Y/n) ")
        
        if run_again.lower() == "n":
            break

main()