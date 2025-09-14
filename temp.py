import ZODB.FileStorage
import ZODB, ZODB.FileStorage
from typing import List

storage = ZODB.FileStorage.FileStorage('./data/PokeData.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root

def main():
    abilities_list = []
    for pk in list(root.pokesets.values()):
        for ability in pk.abilities:
            if ability not in abilities_list:
                abilities_list.append(ability)
    print(abilities_list)

if __name__ == '__main__':
    main()