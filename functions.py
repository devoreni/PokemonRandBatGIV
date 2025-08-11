from typing import List, Tuple, Set
import pokemon_ddl
import random
import ZODB, ZODB.FileStorage

def getFullPokemon(num: int) -> list:
    storage = ZODB.FileStorage.FileStorage('PokeData.fs')
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root

    counts = {'Dragon': 0, 'Ice': 0, 'Fighting': 0, 'Dark': 0, 'Fire': 0, 'Ghost': 0, 'Steel': 0, 'Electric': 0,
              'Rock': 0, 'Poison': 0, 'Ground': 0,
              'Bug': 0, 'Grass': 0, 'Psychic': 0, 'Flying': 0, 'Normal': 0, 'Water': 0}
    setup = root.pokeprobability['pokemon']
    chosen = []

    for i in range(num):
        selected = None
        for j in range(50):
            selected = random.choices(setup[0], setup[1])[0]
            selected_types = root.pokeprobability['pokemon_to_types_map'][selected]
            odds = 1
            for p_type in selected_types:
                if counts[p_type] < max(num // 4, 2):
                    odds *= 1
                elif counts[p_type] == max(num // 4, 2):
                    odds *= 0.25
                else:
                    odds = 0
            if odds < random.random():
                continue

            for pokemon in chosen:
                if pokemon.species == selected.species:
                    continue

            if j == 49:
                return chosen
            chosen.append(selected)
            for p_type in selected_types:
                counts[p_type] += 1
            break
    return chosen


if __name__ == '__main__':
    counts = {'Dragon': 0, 'Ice': 0, 'Fighting': 0, 'Dark': 0, 'Fire': 0, 'Ghost': 0, 'Steel': 0, 'Electric': 0,
              'Rock': 0, 'Poison': 0, 'Ground': 0,
              'Bug': 0, 'Grass': 0, 'Psychic': 0, 'Flying': 0, 'Normal': 0, 'Water': 0}

    print(getFullPokemon(1))