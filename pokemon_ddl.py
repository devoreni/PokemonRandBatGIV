import ZODB, ZODB.FileStorage
import persistent
from typing import List, Tuple, Set
import random



class Move(persistent.Persistent):
    def __init__(self, name: str, power: int, accuracy: float, category: str, moveType: str,
                 dependents: Tuple[Tuple[str, float]] = (())):
        self.name = name
        self.power = power
        self.accuracy = accuracy
        self.category = category
        self.moveType = moveType
        self.dependents = dependents

    def getDependentMoves(self, checked: Set = None) -> List:
        if checked is None:
            checked = {}
        for move in self.dependents:
            pass
        return []

    def toString(self) -> str:
        return f'{self.name}: {self.power} Att., {self.accuracy * 100}% accurate, {self.category}, {self.moveType}'


class MoveSets(persistent.Persistent):
    def __init__(self, starting, children):
        pass

class PokemonSet(persistent.Persistent):
    def __init__(self, name: str, sets):
        pass