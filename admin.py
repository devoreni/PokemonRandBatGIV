import ZODB, ZODB.FileStorage
import persistent
from persistent.mapping import PersistentMapping
from BTrees.OOBTree import OOBTree

if __name__ == '__main__':
    # db = ZODB.DB('PokeData.fs')
    # connection = db.open()
    # root = connection.root
#
    # tester = root.moves['Stockpile']
    # print(tester.toString())
    # print(tester.getDependentMoves(root))
#
    # connection.close()

    typeNames = ['Dragon', 'Ice', 'Fighting', 'Dark', 'Fire', 'Ghost', 'Steel', 'Electric', 'Rock', 'Poison', 'Ground', 'Bug', 'Grass', 'Psychic', 'Flying', 'Normal', 'Water']
    beforeWeights = [12, 14, 15, 16, 16, 17, 18, 19, 20, 21, 23, 26, 26, 34, 40, 41, 48]
    afterWeights = []
    for i, x in enumerate(a):
        afterWeights.append(((sum(a)/len(a)) - x)*.4 + x)

