# CLI Dex
A CLI program that pulls information from Pokémon in the Kanto Region (1-151)

## Concept
This program allows a user to search for a Pokémon (by either name or number) and pull information such as Evolution Information, Height, Weight, etc. All data is retrieved from PokéAPI (https://pokeapi.co/) (https://github.com/PokeAPI).

### Available Pokémon
Pokémon 1-151 (Bulbasaur - Mew) will have data available to be retrieved. Data will be pulled from the "Let's Go" games as they are the latest Kanto games. Functionality to choose which game to pull data from will come later, and more Pokémon will be able to searched for.

### Format
Name: {name} <br>
Dex #: {nat_dex_num} <br>
Abilities: {list_of_abilities} <br>
Types: {list_of_types} <br>
Moveset: {list_of_moves}

## Installation
Create a Python Virtual Environment using:
```
python3 -m venv .env
```

Activate it on Mac using:
```
source env/bin/activate 
```

On Windows:
```
env/Scripts/activate.bat //In CMD
env/Scripts/Activate.ps1 //In Powershell
```

Install the dependencies using:
```
pip install -r requirements.txt
```

## Notices
PokéAPI was created by Paul Hallett (https://github.com/phalt) and others. Pokémon and Pokémon character names are trademarks of Nintendo.