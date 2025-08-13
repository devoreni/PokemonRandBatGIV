from typing import List, Tuple, Set
import pokemon_ddl
import random
import ZODB, ZODB.FileStorage
import pprint

def getPokemonTeam(num: int, root = None) -> Tuple[list, list]:
    if not root:
        storage = ZODB.FileStorage.FileStorage('PokeData.fs')
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

def createIndivPokemon(team: list) -> list:
    created_indivs = []
    for pk_set in team:
        pk_set.buildSet()
        created_indivs.append(pk_set.moves)
    return created_indivs



if __name__ == '__main__':
    storage = ZODB.FileStorage.FileStorage('PokeData.fs')
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root

    pk1 = root.pokesets['Heracross']
    pk2 = root.pokesets['Heracross']
    pk3 = root.pokesets['Heracross']
    pk4 = root.pokesets['Heracross']
    pk5 = root.pokesets['Heracross']
    pk6 = root.pokesets['Heracross']
    pk7 = root.pokesets['Heracross']
    pk8 = root.pokesets['Heracross']
    pk9 = root.pokesets['Heracross']
    pk0 = root.pokesets['Heracross']

    pprint.pprint(createIndivPokemon([pk1, pk2, pk3, pk4, pk5, pk6, pk7, pk8, pk9, pk0]))