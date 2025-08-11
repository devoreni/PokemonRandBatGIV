import ZODB, ZODB.FileStorage
import persistent
from typing import List, Tuple, Set
import random



class Move(persistent.Persistent):
    """
    holds data about a move for reference when needed
    """
    def __init__(self, name: str, power: int, accuracy: float, category: str, moveType: str,
                 dependents: Tuple[Tuple[str, float], ...] = None):
        self.name = name
        self.power = power
        self.accuracy = accuracy
        self.category = category
        self.moveType = moveType
        self.dependents = dependents

    def getDependentMoves(self, root, checked: Set[str] = None) -> List:
        """
        gets all moves that require the parent. For example, swallow should not be run without the move stockpile.
        Each dependent has a probability associated with it ranging from 0-1, swallow has a 100% chance to add stockpile to the list, but
        rest has a 30% chance to add sleep talk and a 10% chance to add snore

        :param root: database connection
        :param checked: set containing all already checked moves
        :return:
        """
        if not self.dependents:
            return []

        if checked is None:
            checked = set()

        newMoves = []
        for move_name, probability in self.dependents:
            if move_name in checked:
                continue
            if random.random() < probability:
                checked.add(move_name)
                newMoves.append(move_name)
                grandChild = root.moves[move_name]
                newMoves.extend(grandChild.getDependentMoves(root, checked))

        return newMoves

    def toString(self) -> str:
        """
        toString function, provides information about the move object
        :return:
        """
        hasDependents = ''
        if self.dependents:
            hasDependents += ', Dependent Moves: ['
            for child, probability in self.dependents:
                hasDependents += f'{child}, '
            hasDependents = f'{hasDependents[:-2]}]'

        return f'{self.name}: {self.power} Att., {self.accuracy * 100}% accurate, {self.category}, {self.moveType}{hasDependents}'


class MoveSet(persistent.Persistent):
    """
    MoveSet is a possible moveset for a Pokemon. It involves a list of starting points and connections between them
    which represent synergies between moves. a Pokemon can have multiple movesets
    """
    def __init__(self, starting: Tuple[str, ...], childrenMatrix: dict[str, List[str]]):
        """
        :param starting: tuple of starting nodes
        :param childrenMatrix: dictionary where the key is a move and the value is a list of moves that synergize with the key
        """
        self.starting = starting
        self.childrenMatrix = childrenMatrix

    def toString(self) -> str:
        """
        uses the attributes of the MoveSet object to create a string for easy viewing of the object
        :return: returns a string in a human-readable format
        """
        graphView = '\n\t{'
        for key, value in self.childrenMatrix.items():
            graphView += f'{key}: {value},\n\t'
        if graphView[-1] != '{':
            graphView = graphView[:-3]
        graphView += '}'

        return f'{self.starting}{graphView}'


class PokemonSet(persistent.Persistent):
    def __init__(self, name: str, species: str, abilities: Tuple[str, ...], pkTypes: Tuple[str, ...], sets: Tuple[MoveSet, ...], legalMoves: Tuple[str, ...], baseStats: Tuple[int, int, int, int, int, int]):
        self.name = name
        self.species = species
        self.abilities = abilities
        self.pkTypes = pkTypes
        self.sets = sets
        self.legalMoves = legalMoves
        self.baseStats = baseStats
        self.hpIV = 31
        self.attIV = 31
        self.defIV = 31
        self.spAttIV = 31
        self.spDefIV = 31
        self.spdIV = 31
        self.nature = 'Bashful'
        pass

    def chooseMovesAndIV(self) -> List:
        return []

    def chooseItem(self) -> str:
        return ''

    def chooseEV(self) -> Tuple[str, str, str]:
        return ('', '', '')

    def chooseNature(self) -> str:
        return ''

    def buildSet(self):
        return

    def toString(self) -> str:
        movesetString = ''
        for moveset in self.sets:
            parser = '\n\t'.join(moveset.toString().split('\n'))
            movesetString += f'\n\t{parser}'

        return f'{self.name}: {self.pkTypes}{movesetString}\n{self.baseStats}'

class PokemonIndiv:
    def __init__(self):
        pass