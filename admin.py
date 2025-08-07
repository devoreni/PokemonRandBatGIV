import ZODB, ZODB.FileStorage
import persistent
from persistent.mapping import PersistentMapping
import BTree.OOBTree

if __name__ == '__main__':
    # db = ZODB.DB('PokeData.fs')

    storage = ZODB.FileStorage.FileStorage('PokeData.fs')
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root
