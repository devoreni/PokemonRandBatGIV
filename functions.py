from typing import List, Tuple, Set
import pokemon_ddl
import random

def getSixPokemon() -> List:
    typeNames = ['Dragon', 'Ice', 'Fighting', 'Dark', 'Fire', 'Ghost', 'Steel', 'Electric', 'Rock', 'Poison', 'Ground',
                 'Bug', 'Grass', 'Psychic', 'Flying', 'Normal', 'Water']
    weights = [12, 14, 15, 16, 16, 17, 18, 19, 20, 21, 23, 26, 26, 34, 40, 41, 48]
    """
    afterWeights = []
    for i, x in enumerate(beforeWeights):
        afterWeights.append(((sum(beforeWeights) / len(beforeWeights)) - x) * .4 + x)
    weights = afterWeights
    """
    counts = {'Dragon': 2, 'Ice': 2, 'Fighting': 2, 'Dark': 2, 'Fire': 2, 'Ghost': 2, 'Steel': 2, 'Electric': 2, 'Rock': 2, 'Poison': 2, 'Ground': 2,
                 'Bug': 2, 'Grass': 2, 'Psychic': 2, 'Flying': 2, 'Normal': 2, 'Water': 2}

    def isTypeAvailable(typeName: str) -> bool:
        if counts[typeName] > 0:
            counts[typeName] -= 1
            return True
        return False

    chosenTypes = []
    for i in range(6):
        currType = ''
        for j in range(50):
            if j >= 48 and isTypeAvailable('Dragon'):
                currType = 'Dragon'
                break
            elif j >= 46 and isTypeAvailable('Ice'):
                currType = 'Ice'
                break
            elif j >= 44 and isTypeAvailable('Fighting'):
                currType = 'Fighting'
                break
            currType = random.choices(typeNames, weights)[0]
            if isTypeAvailable(currType):
                break
        chosenTypes.append(currType)

    return chosenTypes

if __name__ == '__main__':
    counts = {'Dragon': 0, 'Ice': 0, 'Fighting': 0, 'Dark': 0, 'Fire': 0, 'Ghost': 0, 'Steel': 0, 'Electric': 0,
              'Rock': 0, 'Poison': 0, 'Ground': 0,
              'Bug': 0, 'Grass': 0, 'Psychic': 0, 'Flying': 0, 'Normal': 0, 'Water': 0}

    for i in range(2000):
        for x in getSixPokemon():
            counts[x] = counts[x] + 1

    print(counts.values())
    seen = list(counts.values())
    weights = [12, 14, 15, 16, 16, 17, 18, 19, 20, 21, 23, 26, 26, 34, 40, 41, 48]
    for i, x in enumerate(seen):
        seen[i] = x/weights[i]
    print(seen)