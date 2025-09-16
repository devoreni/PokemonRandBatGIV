from typing import List, Tuple, Set
import pokemon_ddl
import random
import ZODB, ZODB.FileStorage
import pprint

def getPokemonTeam(num: int, root = None) -> Tuple[list, list]:
    if not root:
        storage = ZODB.FileStorage.FileStorage('./data/PokeData.fs')
        db = ZODB.DB(storage)
        connection = db.open()
        root = connection.root

    local_type_counts = {'Dragon': 0, 'Ice': 0, 'Fighting': 0, 'Dark': 0, 'Fire': 0, 'Ghost': 0, 'Steel': 0, 'Electric': 0,
              'Rock': 0, 'Poison': 0, 'Ground': 0,
              'Bug': 0, 'Grass': 0, 'Psychic': 0, 'Flying': 0, 'Normal': 0, 'Water': 0}
    setup = root.pokeprobability['pokemon']
    chosen_names, chosen_objects = [], []

    for i in range(num):
        for j in range(50):
            selected_name = random.choices(setup[0], setup[1])[0]
            selected_species = root.pokesets[selected_name]
            selected_types = root.pokeprobability['pokemon_to_types_map'][selected_name]
            odds = 1
            for p_type in selected_types:
                if local_type_counts[p_type] < max(num // 4, 2):
                    odds *= 1
                elif max(num // 4, 2) <= local_type_counts[p_type] <= max(num // 3.3, 2):
                    odds *= 0.25
                else:
                    odds = 0
            if odds < random.random():
                continue

            dupe = False
            for pokemon in chosen_objects:
                if pokemon.species == selected_species.species:
                    dupe = True
                    break
            if dupe:
                continue

            chosen_names.append(selected_name)
            chosen_objects.append(selected_species)
            for p_type in selected_types:
                local_type_counts[p_type] += 1
            break
    return chosen_names, chosen_objects

def createIndivPokemon(team: list, root = None) -> list:
    created_indivs = []
    for pk_set in team:
        created_pokemon = pk_set.buildSet(root)
        created_indivs.append(created_pokemon)
    return created_indivs

def getDamageModifier(attacker: str, defender: str) -> int:
    str_to_num = {'Normal': 0, 'Fire': 1, 'Water': 2, 'Electric': 3, 'Grass': 4, 'Ice': 5, 'Fighting': 6, 'Poison': 7,
                  'Ground': 8, 'Flying': 9, 'Psychic': 10, 'Bug': 11, 'Rock': 12, 'Ghost': 13, 'Dragon': 14, 'Dark': 15, 'Steel': 16}
    type_chart = [
        # Normal (0) vs.
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0.5, 0, 1, 1, 0.5],
        # Fire (1) vs.
        [1, 0.5, 0.5, 1, 2, 2, 1, 1, 1, 1, 1, 2, 0.5, 1, 0.5, 1, 2],
        # Water (2) vs.
        [1, 2, 0.5, 1, 0.5, 1, 1, 1, 2, 1, 1, 1, 2, 1, 0.5, 1, 1],
        # Electric (3) vs.
        [1, 1, 2, 0.5, 0.5, 1, 1, 1, 0, 2, 1, 1, 1, 1, 0.5, 1, 1],
        # Grass (4) vs.
        [1, 0.5, 2, 1, 0.5, 1, 1, 0.5, 2, 0.5, 1, 0.5, 2, 1, 0.5, 1, 0.5],
        # Ice (5) vs.
        [1, 0.5, 0.5, 1, 2, 0.5, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, 0.5],
        # Fighting (6) vs.
        [2, 1, 1, 1, 1, 2, 1, 0.5, 1, 0.5, 0.5, 0.5, 2, 0, 1, 2, 2],
        # Poison (7) vs.
        [1, 1, 1, 1, 2, 1, 1, 0.5, 0.5, 1, 1, 1, 0.5, 0.5, 1, 1, 0],
        # Ground (8) vs.
        [1, 2, 1, 2, 0.5, 1, 1, 2, 1, 0, 1, 0.5, 2, 1, 1, 1, 2],
        # Flying (9) vs.
        [1, 1, 1, 0.5, 2, 1, 2, 1, 1, 1, 1, 2, 0.5, 1, 1, 1, 0.5],
        # Psychic (10) vs.
        [1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 0.5, 1, 1, 1, 1, 0, 0.5],
        # Bug (11) vs.
        [1, 0.5, 1, 1, 2, 1, 0.5, 0.5, 1, 0.5, 2, 1, 1, 0.5, 1, 2, 0.5],
        # Rock (12) vs.
        [1, 2, 1, 1, 1, 2, 0.5, 1, 0.5, 2, 1, 2, 1, 1, 1, 1, 0.5],
        # Ghost (13) vs.
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 0.5, 0.5],
        # Dragon (14) vs.
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 0.5],
        # Dark (15) vs.
        [1, 1, 1, 1, 1, 1, 0.5, 1, 1, 1, 2, 1, 1, 2, 1, 0.5, 0.5],
        # Steel (16) vs.
        [1, 0.5, 0.5, 0.5, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 0.5]
    ]

    return type_chart[str_to_num[attacker]][str_to_num[defender]]



if __name__ == '__main__':
    storage = ZODB.FileStorage.FileStorage('./data/PokeData.fs')
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root

    '''_, before = getPokemonTeam(50, root)
    team = createIndivPokemon(before, root)
    '''

    pk1 = root.pokesets['Lopunny']
    pk2 = root.pokesets['Lopunny']
    pk3 = root.pokesets['Lopunny']
    pk4 = root.pokesets['Lopunny']
    pk5 = root.pokesets['Lopunny']
    pk6 = root.pokesets['Lopunny']
    pk7 = root.pokesets['Lopunny']
    pk8 = root.pokesets['Lopunny']
    pk9 = root.pokesets['Lopunny']
    pk0 = root.pokesets['Lopunny']
    team = createIndivPokemon([pk1, pk2, pk3, pk4, pk5, pk6, pk7, pk8, pk9, pk0], root)

    for pk in team:
        print(pk.toString())
