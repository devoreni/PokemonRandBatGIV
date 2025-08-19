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

        return f'{self.name}: {self.power} Att., {self.accuracy * 100}% accurate, {self.category}, {self.moveType}'


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
        self.moves = ['Protect', 'Sunny Day', 'Synthesis', 'SolarBeam']
        self.EVs = '252 HP / 252 SpA'


    def toString(self):
        attacks = ''
        for move in self.moves:
            attacks += f'- {move}\n'
        return f'''{self.name} {self.gender} @ {self.item}
Ability: {self.ability}
Level: {self.level}
Shiny: {self.shiny}
{self.nature} Nature
EVs: {self.EVs}
IVs: {self.hpIV} HP / {self.atkIV} Atk / {self.defIV} Def / {self.spaIV} SpA / {self.spdIV} SpD / {self.speIV} Spe
{attacks}'''

class PokemonSet(persistent.Persistent):
    def __init__(self, name: str, species: str, abilities: Tuple[str, ...], pkTypes: Tuple[str, ...], sets: Tuple[MoveSet, ...], baseStats: Tuple[int, int, int, int, int, int], genders: Tuple[str, ...], images: Tuple[str, str, str] = ('qqq.png', 'qqq.png', 'qqq.png'), ability_weights = None):
        self.name = name
        self.species = species
        self.abilities = abilities
        if not ability_weights:
            self.ability_weights = [1 for ability in self.abilities]
        else:
            self.ability_weights = ability_weights
        self.pkTypes = pkTypes
        self.sets = sets
        self.baseStats = baseStats
        self.genders = genders
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
                    break
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

    def chooseEVsAndNature(self, detail, base, root=None) -> PokemonIndiv:
        if root is None:
            storage = ZODB.FileStorage.FileStorage('./data/PokeData.fs')
            db = ZODB.DB(storage)
            connection = db.open()
            root = connection.root

        points = {'HP': 0.0, 'Atk': 0.0, 'Def': 0.0, 'SpA': 0.0, 'SpD': 0.0, 'Spe': 0.0}

        points['HP'] += (100 / base[0]) * (base[2] / 13 + base[4] / 13)
        points['Atk'] += base[1] / 10
        points['Def'] += base[2] / 10
        points['SpA'] += base[3] / 10
        points['SpD'] += base[4] / 10
        points['Spe'] += base[5] / 6.5
        phys, spec = 0, 0
        for attack in detail.moves:
            move_data = root.moves[attack]
            if move_data.category == 'Phys' and attack not in {'Seismic Toss', 'Counter', 'Metal Burst', 'Fissure',
                                                                 'Guillotine', 'Horn Drill', 'Super Fang', 'Endeavor', 'Bide'}:
                points['Atk'] += min(3.2, move_data.power / 32) if 200 > move_data.power > 10 else 1
                points['Spe'] += min(2.0, move_data.power / 60)
                phys += 1
            elif move_data.category == 'Spec' and attack not in {'Night Shade', 'Mirror Coat', 'Dragon Rage', 'Sonic Boom', 'Sheer Cold'}:
                points['SpA'] += min(3.2, move_data.power / 32) if move_data.power > 10 else 1
                points['Spe'] += min(2.0, move_data.power / 60)
                spec += 1
            elif move_data.category == 'Stat' and move_data.name != 'Protect':
                points['HP'] += 0.5
                points['Spe'] += 1
                points['Def'] += 2.1
                points['SpD'] += 2.1

            if move_data.power < 40:
                points['Def'] += 1
                points['SpD'] += 1
                points['HP'] += 0.5

        if phys == 0:
            points['Atk'] = -1
        else:
            points['Atk'] += 3 * phys
            points['Spe'] += 0.6 * phys
        if spec == 0:
            points['SpA'] = 0
        else:
            points['SpA'] += 3 * spec
            points['Spe'] += 0.6 * spec

        if phys > 0 and spec > 0 and self.baseStats[5] < 60:
            points['Spe'] -= 10
        if self.baseStats[5] <= 40:
            points['Spe'] -= 10

        attacks = set(detail.moves)
        if 'Endeavor' in attacks:
            points['HP'] -= 10
            points['Spe'] += 3
        if 'Perish Song' in attacks:
            points['HP'] += 6
            points['Def'] += 5
            points['SpD'] += 5
        if 'Destiny Bond' in attacks:
            points['HP'] -= 5
            points['Def'] -= 5
            points['SpD'] -= 5
            points['Spe'] += 3
        if {'Swords Dance', 'Dragon Dance', 'Howl', 'Bulk Up', 'Curse'}.intersection(attacks):
            points['Atk'] += 3
        if {'Calm Mind', 'Nasty Plot', 'Tail Glow'}.intersection(attacks):
            points['SpA'] += 3
        if {'Iron Defense', 'Bulk Up', 'Curse', 'Cosmic Power', 'Sheer Cold', 'Fissure', 'Guillotine', 'Horn Drill'}.intersection(attacks):
            points['Def'] += 3
        if {'Calm Mind', 'Amnesia', 'Cosmic Power', 'Sheer Cold', 'Fissure', 'Guillotine', 'Horn Drill'}.intersection(attacks):
            points['SpD'] += 3
        if {'Rock Polish', 'Agility', 'Dragon Dance'}.intersection(attacks):
            points['Spe'] += 3
        if {'Curse', 'Recover', 'Sheer Cold', 'Fissure', 'Guillotine', 'Horn Drill', 'Substitute'}.intersection(attacks):
            points['HP'] += 3


        if 'Trick Room' in attacks or 'Gyro Ball' in attacks:
            points['Spe'] = -10
        if detail.ability == 'Huge Power' or detail.ability == 'Pure Power':
            points['Atk'] = points['Atk'] + 8.0


        sorted_stats = sorted(points.items(), key=lambda item: item[1], reverse=True)
        top_two_names = [sorted_stats[0][0], sorted_stats[1][0]]
        stat_order = ['HP', 'Atk', 'Def', 'SpA', 'SpD', 'Spe']

        ordered_top_two = sorted(top_two_names, key=lambda stat: stat_order.index(stat))

        high_stat_1 = ordered_top_two[0]
        high_stat_2 = ordered_top_two[1]
        detail.EVs = f'252 {high_stat_1} / 252 {high_stat_2}'

        if sorted_stats[0][0] != 'HP':
            plus = sorted_stats[0][0]
        else:
            plus = sorted_stats[1][0]
        if sorted_stats[5][0] != 'HP':
            minus = sorted_stats[5][0]
        else:
            minus = sorted_stats[4][0]
        nature_list = {
            'Atk': {'Def': 'Lonely', 'SpA': 'Adamant', 'SpD': 'Naughty', 'Spe': 'Brave'},
            'Def': {'Atk': 'Bold', 'SpA': 'Impish', 'SpD': 'Lax', 'Spe': 'Relaxed'},
            'SpA': {'Atk': 'Modest', 'Def': 'Mild', 'SpD': 'Rash', 'Spe': 'Quiet'},
            'SpD': {'Atk': 'Calm', 'Def': 'Gentle', 'SpA': 'Careful', 'Spe': 'Sassy'},
            'Spe': {'Atk': 'Timid', 'Def': 'Hasty', 'SpA': 'Jolly', 'SpD': 'Naive'}
        }

        detail.nature = nature_list[plus][minus]

        return detail

    def chooseIV(self, attacks: list, root = None) -> (int, int, int, int, int, int):
        hp, att, phd, spa, spd, spe = 31, 31, 31, 31, 31, 31
        attacks_set = set(attacks)
        if 'Gyro Ball' in attacks_set or 'Trick Room' in attacks_set or self.baseStats[5] < 40:
            spe = 0
        has_phys_att = False
        if root is None:
            storage = ZODB.FileStorage.FileStorage('./data/PokeData.fs')
            db = ZODB.DB(storage)
            connection = db.open()
            root = connection.root
        for attack in attacks:
            if root.moves[attack].category == 'Phys':
                has_phys_att = True
        if not has_phys_att:
            att = 0
        if 'Hidden Power [Fire]' in attacks_set:
            hp, att, phd, spa, spd, spe = 31, 30, 31, 30, 31, 30
        elif 'Hidden Power [Ice]' in attacks_set:
            hp, att, phd, spa, spd, spe = 31, 30, 30, 31, 31, 31
        elif 'Hidden Power [Grass]' in attacks_set:
            hp, att, phd, spa, spd, spe = 31, 30, 31, 30, 31, 31
        elif 'Hidden Power [Ground]' in attacks_set:
            hp, att, phd, spa, spd, spe = 31, 31, 31, 30, 30, 31
        elif 'Hidden Power [Fighting]' in attacks_set:
            hp, att, phd, spa, spd, spe = 31, 30, 31, 30, 30, 30
        elif 'Hidden Power [Water]' in attacks_set:
            hp, att, phd, spa, spd, spe = 31, 30, 30, 30, 31, 31
        elif 'Hidden Power [Electric]' in attacks_set:
            hp, att, phd, spa, spd, spe = 31, 31, 31, 30, 31, 31
        elif 'Hidden Power [Poison]' in attacks_set:
            hp, att, phd, spa, spd, spe = 31, 31, 30, 30, 30, 31
        elif 'Hidden Power [Flying]' in attacks_set:
            hp, att, phd, spa, spd, spe = 30, 30, 30, 30, 30, 31
        elif 'Hidden Power [Psychic]' in attacks_set:
            hp, att, phd, spa, spd, spe = 31, 30, 31, 31, 31, 30
        elif 'Hidden Power [Bug]' in attacks_set:
            hp, att, phd, spa, spd, spe = 31, 30, 30, 31, 30, 31
        elif 'Hidden Power [Rock]' in attacks_set:
            hp, att, phd, spa, spd, spe = 31, 31, 30, 31, 30, 30
        elif 'Hidden Power [Ghost]' in attacks_set:
            hp, att, phd, spa, spd, spe = 31, 31, 30, 31, 30, 31
        elif 'Hidden Power [Dragon]' in attacks_set:
            hp, att, phd, spa, spd, spe = 31, 30, 31, 31, 31, 31
        elif 'Hidden Power [Dark]' in attacks_set:
            hp, att, phd, spa, spd, spe = 31, 31, 31, 31, 31, 31
        elif 'Hidden Power [Steel]' in attacks_set:
            hp, att, phd, spa, spd, spe = 31, 31, 31, 31, 30, 31

        return hp, att, phd, spa, spd, spe

    def choosePokeball(self) -> str:
        pokeball_options = (
            'cherish', 'dive', 'dusk', 'fast', 'friend', 'great', 'heal', 'heavy',
            'level', 'love', 'lure', 'luxury', 'master', 'moon', 'nest', 'net',
            'park', 'poke', 'premier', 'quick', 'repeat', 'safari', 'sport',
            'timer', 'ultra'
        )
        chosen_ball = random.choice(pokeball_options)
        return f"{chosen_ball}.png"

    def buildSet(self, root = None) -> PokemonIndiv:
        new_guy = PokemonIndiv()
        new_guy.name = self.name
        new_guy.gender = random.choice(self.genders)
        new_guy.ability = random.choices(self.abilities, self.ability_weights)[0]
        new_guy.shiny = random.choices(['Yes', 'No'], [1, 15])[0]
        new_guy.pokeball = self.choosePokeball()
        try:
            new_guy.moves = self.chooseMoves()
        except Exception as e:
            pass
        new_guy.hpIV, new_guy.atkIV, new_guy.defIV, new_guy.spaIV, new_guy.spdIV, new_guy.speIV = self.chooseIV(new_guy.moves, root)
        self.chooseEVsAndNature(new_guy, self.baseStats, root)
        return new_guy

    def toString(self) -> str:
        movesetString = ''
        for moveset in self.sets:
            parser = '\n\t'.join(moveset.toString().split('\n'))
            movesetString += f'\n\t{parser}'

        return f'{self.name}: {self.pkTypes}{movesetString}\n{self.baseStats}'

