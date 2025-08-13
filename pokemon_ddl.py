import ZODB, ZODB.FileStorage
import persistent
from typing import List, Tuple, Set
import random



class Move(persistent.Persistent):
    """
    holds data about a move for reference when needed
    """
    def __init__(self, name: str, power: int, accuracy: float, category: str, moveType: str):
        self.name = name
        self.power = power
        self.accuracy = accuracy
        self.category = category
        self.moveType = moveType


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
    def __init__(self, starting: list[str], childrenMatrix: dict[str, List[str]]):
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

class PokemonIndiv:
    def __init__(self):
        self.name = 'Venusaur'
        self.gender = '(F)'
        self.item = 'Life Orb'
        self.ability = 'Overgrow'
        self.nature = 'Serious'
        self.level = 50
        self.shiny = 'No'
        self.hpIV = 31
        self.atkIV = 31
        self.defIV = 31
        self.spaIV = 31
        self.spdIV = 31
        self.speIV = 31
        self.moves = ['Protect', 'Sunny Day', 'Synthesis', 'Solarbeam']


    def toString(self):
        attacks = ''
        for move in self.moves:
            attacks += f'- {move}\n'
        return f'''{self.name} {self.gender} @ {self.item}
Ability: {self.ability}
Level: {self.level}
Shiny: {self.shiny}
{self.nature} Nature
IVs: {self.hpIV} HP / {self.atkIV} Atk / {self.defIV} Def / {self.spaIV} SpA / {self.spdIv} SpD / {self.speIV} / Spe
{attacks}'''

class PokemonSet(persistent.Persistent):
    def __init__(self, name: str, species: str, abilities: Tuple[str, ...], pkTypes: Tuple[str, ...], sets: Tuple[MoveSet, ...], baseStats: Tuple[int, int, int, int, int, int], genders: Tuple[str, ...], images: Tuple[str, str, str] = ('qqq.png', 'qqq.png', 'qqq.png')):
        self.name = name
        self.species = species
        self.abilities = abilities
        self.pkTypes = pkTypes
        self.sets = sets
        self.baseStats = baseStats
        self.hpIV = 31
        self.attIV = 31
        self.defIV = 31
        self.spAttIV = 31
        self.spDefIV = 31
        self.spdIV = 31
        self.nature = 'Bashful'
        self.gender = random.choice(genders)
        self.indiv = PokemonIndiv
        self.moves = []
        self.images = images
        pass

    def chooseMoves(self) -> List:
        this_set = random.choice(self.sets)
        node_stack = []
        chosen_moves, seen_moves = [], set()
        chosen_moves.append(random.choice(this_set.starting))
        seen_moves.add(chosen_moves[0])
        node_stack.append(chosen_moves[0])
        hidden_powers = {'Hidden Power [Dragon]', 'Hidden Power [Ice]', 'Hidden Power [Fighting]',
                         'Hidden Power [Dark]', 'Hidden Power [Fire]',
                         'Hidden Power [Ghost]', 'Hidden Power [Steel]', 'Hidden Power [Electric]',
                         'Hidden Power [Rock]', 'Hidden Power [Poison]',
                         'Hidden Power [Ground]', 'Hidden Power [Bug]', 'Hidden Power [Grass]',
                         'Hidden Power [Psychic]', 'Hidden Power [Flying]',
                         'Hidden Power [Normal]', 'Hidden Power [Water]'}

        while len(chosen_moves) < 4:
            if not node_stack:
                break
            choose_from = this_set.childrenMatrix.get(node_stack[-1], []).copy()
            is_choose_from_empty = not choose_from
            node_under_consideration = ''

            while choose_from:
                node_under_consideration = random.choice(choose_from)
                choose_from.remove(node_under_consideration)
                if node_under_consideration in seen_moves:
                    is_choose_from_empty = not choose_from
                elif node_under_consideration in hidden_powers:
                    seen_moves = seen_moves.union(hidden_powers)
                else:
                    break

            if is_choose_from_empty:
                node_stack.pop(-1)
                continue
            chosen_moves.append(node_under_consideration)
            seen_moves.add(node_under_consideration)
            node_stack.append(node_under_consideration)

        return chosen_moves

    def chooseItem(self) -> str:
        return ''

    def chooseEV(self) -> Tuple[str, str, str]:
        return ('', '', '')

    def chooseNature(self) -> str:
        return ''

    def buildSet(self) -> type[PokemonIndiv]:
        self.indiv.name = self.name
        self.indiv.gender = self.gender
        self.indiv.shiny = random.choices(['Yes', 'No'], [1, 15])[0]
        self.moves = self.chooseMoves()
        return self.indiv

    def toString(self) -> str:
        movesetString = ''
        for moveset in self.sets:
            parser = '\n\t'.join(moveset.toString().split('\n'))
            movesetString += f'\n\t{parser}'

        return f'{self.name}: {self.pkTypes}{movesetString}\n{self.baseStats}'

