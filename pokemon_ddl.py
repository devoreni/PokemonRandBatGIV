import ZODB, ZODB.FileStorage
import persistent
from typing import List, Tuple, Set
import random
import os
import pickle
import sys

import config
import functions


def arcDrag():
    return 'Draco Plate'
def arcIce():
    return 'Icicle Plate'
def arcFight():
    return 'Fist Plate'
def arcFire():
    return 'Flame Plate'
def arcWater():
    return 'Splash Plate'
def arcGrass():
    return 'Meadow Plate'
def arcElec():
    return 'Zap Plate'
def arcPsychic():
    return 'Mind Plate'
def arcPoison():
    return 'Toxic Plate'
def arcGround():
    return 'Earth Plate'
def arcFly():
    return 'Sky Plate'
def arcBug():
    return 'Insect Plate'
def arcRock():
    return 'Stone Plate'
def arcGhost():
    return 'Spooky Plate'
def arcDark():
    return 'Dread Plate'
def arcSteel():
    return 'Iron Plate'
def lati():
    return 'Soul Dew'
def dialga():
    return 'Adamant Orb'
def palkia():
    return 'Lustrous Orb'
def farf():
    return 'Stick'
def maro():
    return 'Thick Club'
def pika():
    return 'Light Ball'


ITEM_LOGIC_REGISTRY = {
    'arcDrag': arcDrag,
    'arcIce': arcIce,
    'arcFight': arcFight,
    'arcFire': arcFire,
    'arcWater': arcWater,
    'arcGrass': arcGrass,
    'arcElec': arcElec,
    'arcPsychic': arcPsychic,
    'arcPoison': arcPoison,
    'arcGround': arcGround,
    'arcFly': arcFly,
    'arcBug': arcBug,
    'arcRock': arcRock,
    'arcGhost': arcGhost,
    'arcDark': arcDark,
    'arcSteel': arcSteel,
    'lati': lati,
    'dialga': dialga,
    'palkia': palkia,
    'farf': farf,
    'maro': maro,
    'pika': pika
}

# Arceus getEvsandNature function
def arcStat(self_obj, indiv_obj, root=None):
    if root is None:
        storage = ZODB.FileStorage.FileStorage(config.DB_FILE)
        db = ZODB.DB(storage)
        connection = db.open()
        root = connection.root

    points = {'HP': 2, 'Atk': 0.9, 'Def': 1, 'SpA': 1, 'SpD': 1, 'Spe': 1}
    phys, spec, stat = 0, 0, 0
    ppow, spow = 0, 0
    for move_name in indiv_obj.moves:
        move = root.moves[move_name]
        if move.category == 'Phys':
            phys += 1
            ppow += move.power
        elif move.category == 'Spec':
            spec += 1
            spow += move.power
        elif move.category == 'Stat':
            stat += 1
    if {'Gyro Ball', 'Trick Room'}.intersection(set(indiv_obj.moves)):
        points['Spe'] = -10
    if phys == 0:
        points['Atk'] = -7
    else:
        points['Atk'] += phys
    if spec == 0:
        points['SpA'] = -5
    else:
        points['SpA'] += spec
    if phys > 0 and spow > 0:
        if ppow > spow + 30:
            points['SpA'] = -5
        elif spow > ppow + 30:
            points['Atk'] = -10
        else:
            points['Def'] = -3

    sorted_stats = sorted(points.items(), key=lambda item: item[1], reverse=True)
    top_five_names = [sorted_stats[0][0], sorted_stats[1][0], sorted_stats[2][0], sorted_stats[3][0],
                      sorted_stats[4][0]]
    stat_order = ['HP', 'Atk', 'Def', 'SpA', 'SpD', 'Spe']
    ordered_top_five = sorted(top_five_names, key=lambda high_stat: stat_order.index(high_stat))

    h1 = ordered_top_five[0]
    h2 = ordered_top_five[1]
    h3 = ordered_top_five[2]
    h4 = ordered_top_five[3]
    h5 = ordered_top_five[4]
    indiv_obj.EVs = f'100 {h1} / 100 {h2} / 100 {h3} / 100 {h4} / 100 {h5}'

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

    indiv_obj.nature = nature_list[plus][minus]
    stat_list = [h1, h2, h3, h4, h5]

    indiv_obj.hpStat = int((2 * self_obj.baseStats[0] + indiv_obj.hpIV + (
        100 if 'HP' in stat_list else 0) / 4) * indiv_obj.level / 100 + indiv_obj.level + 10)
    indiv_obj.atkStat = int(((2 * self_obj.baseStats[1] + indiv_obj.atkIV + (
        100 if 'Atk' in stat_list else 0) / 4) * indiv_obj.level / 100 + 5) * (
                             1.1 if plus == "Atk" else 0.9 if minus == "Atk" else 1))
    indiv_obj.defStat = int(((2 * self_obj.baseStats[2] + indiv_obj.defIV + (
        100 if 'Def' in stat_list else 0) / 4) * indiv_obj.level / 100 + 5) * (
                             1.1 if plus == "Def" else 0.9 if minus == "Def" else 1))
    indiv_obj.spaStat = int(((2 * self_obj.baseStats[3] + indiv_obj.spaIV + (
        100 if 'SpA' in stat_list else 0) / 4) * indiv_obj.level / 100 + 5) * (
                             1.1 if plus == "SpA" else 0.9 if minus == "SpA" else 1))
    indiv_obj.spdStat = int(((2 * self_obj.baseStats[4] + indiv_obj.spdIV + (
        100 if 'SpD' in stat_list else 0) / 4) * indiv_obj.level / 100 + 5) * (
                             1.1 if plus == "SpD" else 0.9 if minus == "SpD" else 1))
    indiv_obj.speStat = int(((2 * self_obj.baseStats[5] + indiv_obj.speIV + (
        100 if 'Spe' in stat_list else 0) / 4) * indiv_obj.level / 100 + 5) * (
                             1.1 if plus == "Spe" else 0.9 if minus == "Spe" else 1))
    return indiv_obj
def shedStat(self_obj, indiv_obj, root=None):
    indiv_obj.hpStat = 1
    indiv_obj.nature = 'Lonely'
    indiv_obj.EVs = f'252 Atk / 252 Spe'
    plus, minus = 'Atk', 'Def'

    indiv_obj.atkStat = int(((2 * self_obj.baseStats[1] + indiv_obj.atkIV + 252 / 4) * indiv_obj.level / 100 + 5) * (
                                1.1 if plus == "Atk" else 0.9 if minus == "Atk" else 1))
    indiv_obj.defStat = int(((2 * self_obj.baseStats[2] + indiv_obj.defIV + 0) * indiv_obj.level / 100 + 5) * (
                                1.1 if plus == "Def" else 0.9 if minus == "Def" else 1))
    indiv_obj.spaStat = int(((2 * self_obj.baseStats[3] + indiv_obj.spaIV + 0) * indiv_obj.level / 100 + 5) * (
                                1.1 if plus == "SpA" else 0.9 if minus == "SpA" else 1))
    indiv_obj.spdStat = int(((2 * self_obj.baseStats[4] + indiv_obj.spdIV + 0) * indiv_obj.level / 100 + 5) * (
                                1.1 if plus == "SpD" else 0.9 if minus == "SpD" else 1))
    indiv_obj.speStat = int(((2 * self_obj.baseStats[5] + indiv_obj.speIV + 0) * indiv_obj.level / 100 + 5) * (
                                1.1 if plus == "Spe" else 0.9 if minus == "Spe" else 1))

STAT_LOGIC_REGISTRY = {
    'arcStat': arcStat,
    'shedStat': shedStat
}

class Move(persistent.Persistent):
    """
    holds data about a move for reference when needed
    """
    def __init__(self, name: str, power: int, accuracy: float, category: str, moveType: str, pp: int=5):
        self.name = name
        self.power = power
        self.accuracy = accuracy
        self.category = category
        self.moveType = moveType
        self.pp = pp


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
        self.moves = ['Protect', 'Sunny Day', 'Synthesis', 'Solar Beam']
        self.EVs = '252 HP / 252 SpA'
        self.hpStat = 100
        self.atkStat = 100
        self.defStat = 100
        self.spaStat = 100
        self.spdStat = 100
        self.speStat = 100
        self.pokeball = 'poke.png'
        self.experience = 125000

    def toString(self):
        attacks = ''
        for move in self.moves:
            attacks += f'- {move}\n'
        return f'''{self.name} {self.gender} @ {self.item}
Ability: {self.ability}
Level: {self.level}
{f'Shiny: Yes\n' if self.shiny == 'Yes' else ''}{self.nature} Nature
EVs: {self.EVs}
IVs: {self.hpIV} HP / {self.atkIV} Atk / {self.defIV} Def / {self.spaIV} SpA / {self.spdIV} SpD / {self.speIV} Spe
{attacks}'''.strip()

class PokemonSet(persistent.Persistent):
    def __init__(self, name: str, species: str, abilities: Tuple[str, ...], pkTypes: Tuple[str, ...], sets: Tuple[MoveSet, ...], baseStats: Tuple[int, int, int, int, int, int], genders: Tuple[str, ...], images: Tuple[str, str, str] = ('qqq.png', 'qqq.png', 'qqq.png'), ability_weights = None, item_key = None, stat_key = None):
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
        self.item_key = item_key
        self.stat_key = stat_key
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

    def chooseItem(self, indiv, root=None, debug = False) -> str:
        if not os.path.exists(config.PICKLE_MODEL_FILE) or not root:
            return 'Big Nugget'
        packed = open(config.PICKLE_MODEL_FILE, 'rb')
        unpacked = pickle.load(packed)
        packed.close()
        model = unpacked['model']
        keys = unpacked['keys']
        input_layer = []

        types_hit_super_effectively = set()
        already_hit = set()
        for move_name in indiv.moves:
            move = root.moves[move_name]
            if move.category not in {'Phys', 'Spec'}:
                continue
            for target_type in root.pokeprobability['type_names']:
                if target_type in already_hit:
                    continue
                damage_modifier = functions.getDamageModifier(move.moveType, target_type)
                if damage_modifier == 2:
                    types_hit_super_effectively.add(target_type)
                    already_hit.add(target_type)
        num_super_effective_hits = len(types_hit_super_effectively)

        pk_types = set(root.pokeprobability['pokemon_to_types_map'][indiv.name])
        for l_type in root.pokeprobability['type_names']:
            input_layer.append(0 if l_type not in pk_types else 1)

        for ability in root.pokeprobability['abilities']:
            input_layer.append(0 if ability != indiv.ability else 1)

        input_layer.append(indiv.hpStat)
        input_layer.append(indiv.atkStat)
        input_layer.append(indiv.defStat)
        input_layer.append(indiv.spaStat)
        input_layer.append(indiv.spdStat)
        input_layer.append(indiv.speStat)

        for move in list(root.moves.values()):
            input_layer.append(0 if move.name not in indiv.moves else 1)

        move_categories = {'Phys': 0, 'Spec': 0, 'Stat': 0}
        move_types = {'Dragon': 0, 'Ice': 0, 'Fighting': 0, 'Dark': 0, 'Fire': 0, 'Ghost': 0, 'Steel': 0, 'Electric': 0,
                      'Rock': 0, 'Poison': 0, 'Ground': 0, 'Bug': 0, 'Grass': 0, 'Psychic': 0, 'Flying': 0, 'Normal': 0,
                      'Water': 0}
        setup_moves = {'HP': 0, 'Atk': 0, 'Def': 0, 'SpA': 0, 'SpD': 0, 'Spe': 0, 'Evasion': 0}
        other_moves = {'Draining Moves': 0, 'Baton Pass': 0, 'Trapping Moves': 0, 'Item Bestowing': 0, 'Multi Hit': 0,
                       'Screens': 0,
                       'High Crit Ratio': 0, 'Self Stat Drop': 0, 'Low Accuracy': 0, 'Two Turn Attack': 0,
                       'Multi Target': 0}
        for move_name in indiv.moves:
            move = root.moves[move_name]
            if move.category == 'Phys':
                move_categories['Phys'] += 1
                move_types[move.moveType] += 1
            elif move.category == 'Spec':
                move_categories['Spec'] += 1
                move_types[move.moveType] += 1
            elif move.category == 'Stat' and move.name not in {'Protect', 'Detect'}:
                move_categories['Stat'] += 1
            if move.name in {'Slack Off', 'Rest', 'Recover', 'Roost'}:
                setup_moves['HP'] += 1
            if move.name in {'Dragon Dance', 'Swords Dance', 'Bulk Up', 'Howl', 'Belly Drum', 'Coil', 'Curse', 'Growth',
                             'Hone Claws', 'Meditate', 'Work Up'}:
                setup_moves['Atk'] += 1
            if move.name in {'Acid Armor', 'Barrier', 'Bulk Up', 'Coil', 'Cosmic Power', 'Curse', 'Defend Order',
                             'Defense Curl',
                             'Harden', 'Iron Defense', 'Skull Bash', 'Stockpile', 'Withdraw'}:
                setup_moves['Def'] += 1
            if move.name in {'Calm Mind', 'Growth', 'Nasty Plot', 'Tail Glow', 'Work Up'}:
                setup_moves['SpA'] += 1
            if move.name in {'Amnesia', 'Calm Mind', 'Cosmic Power', 'Defend Order', 'Stockpile'}:
                setup_moves['SpD'] += 1
            if move.name in {'Agility', 'Dragon Dance', 'Rock Polish'}:
                setup_moves['Spe'] += 1
            if move.name in {'Double Team', 'Minimize', 'Flash', 'Kinesis', 'Mud-Slap', 'Muddy Water', 'Octazooka',
                             'Sand Attack', 'Smokescreen'}:
                setup_moves['Evasion'] += 1
            if move.name in {'Absorb', 'Drain Punch', 'Dream Eater', 'Giga Drain', 'Leech Seed', 'Leech Life',
                             'Ingrain',
                             'Mega Drain', 'Aqua Ring'}:
                other_moves['Draining Moves'] += 1
            if move.name == 'Baton Pass':
                other_moves['Baton Pass'] += 1
            if move.name in {'Bind', 'Clamp', 'Fire Spin', 'Magma Storm', 'Sand Tomb', 'Whirlpool', 'Wrap'}:
                other_moves['Trapping Moves'] += 1
            if move.name in {'Fling', 'Trick', 'Switcheroo'}:
                other_moves['Item Bestowing'] += 1
            if move.name in {'Arm Thrust', 'Barrage', 'Bone Rush', 'Bullet Seed', 'Comet Punch', 'Double Slap',
                             'Fury Attack',
                             'Fury Swipes', 'Icicle Spear', 'Pin Missile', 'Rock Blast', 'Tail Slap', 'Bonemerang',
                             'Double Hit',
                             'Double Kick', 'Twineedle', 'Beat Up'}:
                other_moves['Multi Hit'] += 1
            if move.name in {'Light Screen', 'Reflect'}:
                other_moves['Screens'] += 1
            if move.name in {'Aeroblast', 'Air Cutter', 'Attack Order', 'Blaze Kick', 'Crabhammer', 'Cross Chop',
                             'Cross Poison',
                             'Karate Chop', 'Leaf Blade', 'Night Slash', 'Poison Tail', 'Psycho Cut', 'Razor Leaf',
                             'Razor Wind',
                             'Shadow Claw', 'Sky Attack', 'Slash', 'Spacial Rend', 'Stone Edge'}:
                other_moves['High Crit Ratio'] += 1
            if move.name in {'Overheat', 'Leaf Storm', 'Draco Meteor', 'Psycho Boost', 'Superpower', 'Close Combat',
                             'Hammer Arm'}:
                other_moves['Self Stat Drop'] += 1
            if move.accuracy < 1:
                other_moves['Low Accuracy'] += 1
            if move.name in {'Bounce', 'Dig', 'Dive', 'Fly', 'Shadow Force', 'Razor Wind', 'Skull Bash', 'Sky Attack'}:
                other_moves['Two Turn Attack'] += 1
            if move.name in {'Discharge', 'Earthquake', 'Lava Plume', 'Magnitude', 'Surf', 'Acid', 'Air Cutter',
                             'Blizzard',
                             'Bubble', 'Eruption', 'Heat Wave', 'Hyper Voice', 'Icy Wind', 'Muddy Water', 'Poison Gas',
                             'Powder Snow', 'Razor Leaf', 'Razor Wind', 'Rock Slide', 'Swift', 'Twister',
                             'Water Spout'}:
                other_moves['Multi Target'] += 1
        if indiv.ability in {'Dry Skin', 'Ice Body', 'Poison Heal', 'Rain Dish'}:
            setup_moves['HP'] += 1
        elif indiv.ability in {'Flower Gift', 'Guts', 'Huge Power', 'Hustle', 'Pure Power'}:
            setup_moves['Atk'] += 1
        elif indiv.ability in {'Marvel Scale'}:
            setup_moves['Def'] += 1
        elif indiv.ability in {'Flower Gift'}:
            setup_moves['SpD'] += 1
        elif indiv.ability in {'Solar Power'}:
            setup_moves['SpA'] += 1
        elif indiv.ability in {'Chlorophyll', 'Minus', 'Plus', 'Quick Feet', 'Swift Swim', 'Unburden'}:
            setup_moves['Spe'] += 1
        elif indiv.ability in {'Sand Veil', 'Snow Cloak', 'Tangled Feet'}:
            setup_moves['Evasion'] += 1
        elif indiv.ability in {'Blaze', 'Flash Fire', 'Overgrow', 'Swarm', 'Torrent'}:
            setup_moves['Atk'] += 1
            setup_moves['SpA'] += 1

        input_layer.extend(list(move_categories.values()))
        input_layer.extend(list(move_types.values()))
        input_layer.extend(list(setup_moves.values()))
        input_layer.extend(list(other_moves.values()))

        input_layer.append(num_super_effective_hits)

        num_weaknesses = 0
        num_quad_weaknesses = 0
        num_resistances = 0
        num_quad_resistances = 0

        for attacking_type in root.pokeprobability['type_names']:
            multiplier = 1
            for defensive_types in root.pokesets[indiv.name].pkTypes:
                multiplier *= functions.getDamageModifier(attacking_type, defensive_types)
            if multiplier >= 2:
                num_weaknesses += 1
            if multiplier == 4:
                num_quad_weaknesses += 1
            if multiplier <= 0.5:
                num_resistances += 1
            if multiplier == 0.25:
                num_quad_resistances += 1
        input_layer.extend([num_weaknesses, num_quad_weaknesses, num_resistances, num_quad_resistances])

        bulk_score = ((indiv.hpStat + indiv.defStat + indiv.spdStat)
                      * ((num_resistances + num_quad_resistances + 1)
                         / (num_weaknesses + 2 * num_quad_weaknesses + 1))
                      * (((other_moves['Draining Moves'] + setup_moves['HP'] + setup_moves['Def'] + setup_moves[
                    'SpD']) + 2) / 2))
        input_layer.append(bulk_score)

        total_power = 0
        for move in indiv.moves:
            total_power += root.moves[move].power
        offence_score = (max(indiv.atkStat, indiv.spaStat) + 0.5 * min(indiv.atkStat, indiv.spaStat)) * max(
            num_super_effective_hits, 1) * (total_power / 10)
        input_layer.append(offence_score)

        probs = model.predict_proba([input_layer])[0]
        class_probs = dict(zip([keys[i] for i in model.classes_], [float(j) for j in probs]))

        sorted_probs = sorted(class_probs.items(), key=lambda x: x[1], reverse=True)

        results = {}
        choices = []
        item_weights = []

        for label, prob in sorted_probs:
            if prob >= 0.1 and sum(item_weights) < 0.5:
                choices.append(label)
                item_weights.append(prob)
            if prob > 0:
                results[label] = prob
        if debug:
            print(results)
            print(list(zip(choices, item_weights)), '\n')

        berries = []
        berry_weights = []
        attacking_types = {'Dragon': 1, 'Ice': 1, 'Fighting': 1, 'Dark': 1, 'Fire': 1, 'Ghost': 1, 'Steel': 1, 'Electric': 1,
         'Rock': 1, 'Poison': 1, 'Ground': 1,
         'Bug': 1, 'Grass': 1, 'Psychic': 1, 'Flying': 1, 'Normal': 1, 'Water': 1}
        super_effective_berry = {'Dragon': 'Haban Berry', 'Ice': 'Yache Berry', 'Fighting': 'Chople Berry', 'Dark': 'Colbur Berry',
                                 'Fire': 'Occa Berry', 'Ghost': 'Kasib Berry', 'Steel': 'Babiri Berry', 'Electric': 'Wacan Berry',
                                 'Rock': 'Charti Berry', 'Poison': 'Kebia Berry', 'Ground': 'Shuca Berry', 'Bug': 'Tanga Berry',
                                 'Grass': 'Rindo Berry', 'Psychic': 'Payapa Berry', 'Flying': 'Coba Berry', 'Water': 'Passho Berry',
                                 'Normal': 'Chilan Berry'}

        for defensive_type in self.pkTypes:
            for attack in attacking_types.keys():
                attacking_types[attack] *= functions.getDamageModifier(attack, defensive_type)
        for key, value in attacking_types.items():
            if value == 2:
                if sum(item_weights) <= 0.5:
                    if (key == 'Fire' and indiv.ability == 'Flash Fire') or \
                            (key == 'Water' and indiv.ability in {'Water Absorb', 'Dry Skin'}) or \
                            (key == 'Electric' and indiv.ability in {'Motor Drive', 'Volt Absorb'}) or \
                            (key == 'Ground' and indiv.ability in {'Levitate'}):
                        continue
                    berries.append(super_effective_berry[key])
                    berry_weights.append(1)
            elif value == 4:
                berries.append(super_effective_berry[key])
                if sum(item_weights) <= 0.5:
                    berry_weights.append(4)
                else:
                    berry_weights.append(1)

        item_weights = [i * 14 if i <= 0.7 else 10 for i in item_weights]
        item_weights.extend(berry_weights)
        choices.extend(berries)
        if choices:
            return random.choices(choices, item_weights)[0]
        return 'Chilan Berry'


    def chooseEVsAndNature(self, detail, root=None, debug=False) -> PokemonIndiv:
        if root is None:
            storage = ZODB.FileStorage.FileStorage(os.path.join(os.path.dirname(__file__), 'data', 'PokeData.fs'))
            db = ZODB.DB(storage)
            connection = db.open()
            root = connection.root

        # usually between 5 and 15
        points = {'HP': self.baseStats[0] / 10.0 + self.baseStats[2] / 100.0 + self.baseStats[4] / 100.0,
                  'Atk': self.baseStats[1] / 10.0,
                  'Def': self.baseStats[2] / 10.0,
                  'SpA': self.baseStats[3] / 10.0,
                  'SpD': self.baseStats[4] / 10.0,
                  'Spe': max(self.baseStats[5] / (0.01 * (self.baseStats[5] - 90)**2 + 3.75), 9.0) if 45 <= self.baseStats[5] <= 135 else 2}

        if detail.ability in {'Huge Power', 'Pure Power'}:
            points['Atk'] *= 3

        if self.baseStats[0] + self.baseStats[2] >= 240:
            points['HP'] += 6
            points['Def'] += 6
        if self.baseStats[0] + self.baseStats[4] >= 240:
            points['HP'] += 6
            points['SpD'] += 6

        # look at moves
        phys, spec, stat = 0, 0, 0
        for move in detail.moves:
            if (root.moves[move].category == 'Phys'
                    or move in {'Dragon Dance', 'Swords Dance', 'Bulk Up', 'Howl', 'Belly Drum',
                                                      'Coil', 'Curse', 'Growth', 'Hone Claws', 'Meditate', 'Work Up'})\
                    and move not in {'Bide', 'Counter', 'Endeavor', 'Metal Burst', 'Seismic Toss', 'Super Fang',
                                     'Explosion', 'Selfdestruct', 'Fissure', 'Guillotine', 'Horn Drill'}:
                phys += 1
                points['Atk'] += min(3, root.moves[move].power / 35)
                points['Spe'] += 0.5

            if (root.moves[move].category == 'Spec'
                    or move in {'Calm Mind', 'Growth', 'Nasty Plot', 'Tail Glow', 'Work Up'})\
                    and move not in {'Dragon Rage', 'Mirror Coat', 'Night Shade', 'Sonic Boom', 'Psywave', 'Sheer Cold'}:
                spec += 1
                points['SpA'] += min(3, root.moves[move].power / 35)
                points['Spe'] += 0.5
            if root.moves[move].category == 'Stat' and move not in {'Protect', 'Dragon Dance', 'Swords Dance', 'Bulk Up', 'Howl', 'Belly Drum',
                                                      'Coil', 'Curse', 'Growth', 'Hone Claws', 'Meditate', 'Shell Smash',
                                                      'Work Up', 'Calm Mind', 'Nasty Plot', 'Tail Glow'}:
                stat += 1
                points['HP'] += 1
                points['Def'] += 1
                points['SpD'] += 1
                points['Spe'] += 1
            if move in {'Avalanche', 'Counter', 'Mirror Coat', 'Payback', 'Roar', 'Whirlwind'}:
                points['HP'] += 3
                points['Spe'] -= 1
            if move in {'Perish Song', 'Horn Drill', 'Fissure', 'Guillotine', 'Sheer Cold', 'Recover', 'Roost',
                        'Moonlight', 'Morning Sun', 'Substitute', 'Wish', 'Ingrain', 'Heal Order', 'Milk Drink',
                        'Slack Off', 'Soft-Boiled', 'Synthesis'}:
                points['HP'] += 3
                points['Def'] += 3
                points['SpD'] += 3
        # End Loop

        if (self.baseStats[2] + self.baseStats[4]) - (self.baseStats[0] * 2) > 60:
            points['HP'] += ((self.baseStats[2] + self.baseStats[4]) - (self.baseStats[0] * 2)) / 10

        points['HP'] += stat
        if points['HP'] >= 25:
            points['Def'] += 2
            points['SpD'] += 2
        if self.baseStats[5] >= 80:
            points['Spe'] += phys + spec
        moves_as_set = set(detail.moves)

        points['HP'] += len(moves_as_set.intersection({'Stealth Rock', 'Roar', 'Spikes', 'Toxic Spikes', 'Knock Off', 'Icy Wind', 'Follow Me', 'Mud Shot'}))
        points['Def'] += len(moves_as_set.intersection({'Stealth Rock', 'Roar', 'Spikes', 'Toxic Spikes', 'Knock Off', 'Icy Wind', 'Follow Me', 'Mud Shot'}))
        points['SpD'] += len(moves_as_set.intersection({'Stealth Rock', 'Roar', 'Spikes', 'Toxic Spikes', 'Knock Off', 'Icy Wind', 'Follow Me', 'Mud Shot'}))

        if phys + spec == len(moves_as_set.intersection({'Fake Out', 'Extreme Speed', 'Feint', 'Aqua Jet', 'Bide', 'Bullet Punch',
                                                     'Ice Shard', 'Mach Punch', 'Quick Attack', 'Shadow Sneak',
                                                     'Sucker Punch', 'Dragon Dance', 'Swords Dance', 'Bulk Up', 'Howl', 'Belly Drum',
                                                      'Coil', 'Curse', 'Growth', 'Hone Claws', 'Meditate', 'Shell Smash',
                                                      'Work Up', 'Calm Mind', 'Nasty Plot', 'Tail Glow'})):
            points['Spe'] -= 3
            points['HP'] += 2
            points['Def'] += 2
            points['SpD'] += 2

        if points['Atk'] >= max(points['HP'], points['Def'], points['SpD'], points['Spe'])\
                and points['SpA'] >= max(points['HP'], points['Def'], points['SpD'], points['Spe']):
            if self.baseStats[5] <= 70:
                points['Spe'] = 0
            else:
                if points['Atk'] <= points['SpA']:
                    points['Atk'] = max(points['HP'], points['Def'], points['SpD'], points['Spe']) - 1
                else:
                    points['SpA'] = max(points['HP'], points['Def'], points['SpD'], points['Spe']) - 1
                if max(points['Atk'], points['SpA']) - points['Spe'] < 3.3:
                    points['Spe'] += 3.3

        if points['HP'] - max(points['Atk'], points['Def'], points['SpA'], points['SpD'], points['Spe']) > 5\
                and self.baseStats[0] - min(self.baseStats[2], self.baseStats[4]) > 80:
            if points['Def'] < points['SpD']:
                points['Def'] = points['HP']
            else:
                points['SpD'] = points['HP']

        if points['Def'] >= max(points['Atk'], points['SpA'], points['SpD'], points['Spe'])\
                and moves_as_set.intersection({'Will-O-Wisp', 'Tri-Attack', 'Sacred Fire', 'Lava Plume', 'Heat Wave',
                                               'Flare Blitz', 'Flamethrower', 'Flame Wheel', 'Fire Punch', 'Fire Fang',
                                               'Fire Blast', 'Ember', 'Blaze Kick'})\
                and abs(self.baseStats[2] - self.baseStats[4]) < 30:
            temp = points['Def']
            points['Def'] = points['SpD']
            points['SpD'] = temp + 0.01

        if points['Def'] <= min(points['Atk'], points['HP'], points['SpA'], points['SpD'], points['Spe'])\
                and (points['HP'] > max(points['Atk'], points['Def'], points['SpA'], points['SpD'], points['Spe'])
                or points['SpD'] > max(points['Atk'], points['Def'], points['SpA'], points['HP'], points['Spe'])):
            points['Spe'] = 0
        elif points['SpD'] <= min(points['Atk'], points['HP'], points['SpA'], points['Def'], points['Spe'])\
                and (points['HP'] > max(points['Atk'], points['Def'], points['SpA'], points['SpD'], points['Spe'])
                or points['Def'] > max(points['Atk'], points['SpD'], points['SpA'], points['HP'], points['Spe'])):
            points['Spe'] = 0

        if (points['Def'] < points['HP'] + 3 or points['SpD'] < points['HP'] + 3)\
                    and (4 <= len([i for i in points.values() if i < points['Def']]) or 4 <= len([i for i in points.values() if i < points['SpD']])):
            points['HP'] += 3

        if phys == 0 or (phys == 1 and {'Fake Out', 'Aqua Jet', 'Quick Attack', 'Mach Punch', 'Ice Shard', 'Bullet Punch', 'Swords Dance'}.intersection(moves_as_set)):
            points['Atk'] = -10
        elif phys == len({"Swords Dance", "Extreme Speed"}.intersection(moves_as_set)):
            points['Spe'] -= 10
            points['Atk'] += 3
            points['HP'] += 3
        if spec == 0:
            points['SpA'] = -1
        if set(moves_as_set).intersection({'Trick Room', 'Gyro Ball'}):
            points['Spe'] = -100



        sorted_stats = sorted(points.items(), key=lambda item: item[1], reverse=True)
        top_two_names = [sorted_stats[0][0], sorted_stats[1][0]]
        stat_order = ['HP', 'Atk', 'Def', 'SpA', 'SpD', 'Spe']

        ordered_top_two = sorted(top_two_names, key=lambda high_stat: stat_order.index(high_stat))

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
        detail.hpStat = int((2 * self.baseStats[0] + detail.hpIV + (
            252 if sorted_stats[0][0] == 'HP' or sorted_stats[1][0] == 'HP' else 0) / 4) * detail.level / 100 + detail.level + 10)
        detail.atkStat = int(((2 * self.baseStats[1] + detail.atkIV + (
            252 if sorted_stats[0][0] == 'Atk' or sorted_stats[1][0] == 'Atk' else 0) / 4) * detail.level / 100 + 5) * (
                                1.1 if plus == "Atk" else 0.9 if minus == "Atk" else 1))
        detail.defStat = int(((2 * self.baseStats[2] + detail.defIV + (
            252 if sorted_stats[0][0] == 'Def' or sorted_stats[1][0] == 'Def' else 0) / 4) * detail.level / 100 + 5) * (
                                 1.1 if plus == "Def" else 0.9 if minus == "Def" else 1))
        detail.spaStat = int(((2 * self.baseStats[3] + detail.spaIV + (
            252 if sorted_stats[0][0] == 'SpA' or sorted_stats[1][0] == 'SpA' else 0) / 4) * detail.level / 100 + 5) * (
                                 1.1 if plus == "SpA" else 0.9 if minus == "SpA" else 1))
        detail.spdStat = int(((2 * self.baseStats[4] + detail.spdIV + (
            252 if sorted_stats[0][0] == 'SpD' or sorted_stats[1][0] == 'SpD' else 0) / 4) * detail.level / 100 + 5) * (
                                 1.1 if plus == "SpD" else 0.9 if minus == "SpD" else 1))
        detail.speStat = int(((2 * self.baseStats[5] + detail.speIV + (
            252 if sorted_stats[0][0] == 'Spe' or sorted_stats[1][0] == 'Spe' else 0) / 4) * detail.level / 100 + 5) * (
                                 1.1 if plus == "Spe" else 0.9 if minus == "Spe" else 1))


        # ---------------- Debug -------
        if debug:
            print(detail.toString())
            import pprint
            print(f"\n--- DEBUG: {self.name} | Moves: {detail.moves} ---")
            pprint.pprint(sorted(points.items(), key=lambda item: item[1], reverse=True))
            # -----------------End Debug --------

        return detail

    def chooseIV(self, attacks: list, root = None) -> (int, int, int, int, int, int):
        hp, att, phd, spa, spd, spe = 31, 31, 31, 31, 31, 31
        attacks_set = set(attacks)
        if 'Gyro Ball' in attacks_set or 'Trick Room' in attacks_set\
                or (self.baseStats[5] < 40
                and len(set(attacks).intersection({'Rock Polish', 'Agility', 'Dragon Dance', 'Shell Smash', 'Acupressure',})) == 0):
            spe = 0
        has_phys_att = False
        if root is None:
            storage = ZODB.FileStorage.FileStorage(os.path.join(os.path.dirname(__file__), 'data', 'PokeData.fs'))
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

    def buildSet(self, root = None, debug = False) -> PokemonIndiv:
        new_guy = PokemonIndiv()
        new_guy.name = self.name
        g = random.choice(self.genders)
        g = f'({g})' if g else g
        new_guy.gender = g
        new_guy.ability = random.choices(self.abilities, self.ability_weights)[0]
        new_guy.shiny = random.choices(['Yes', 'No'], [1, 19])[0]
        new_guy.pokeball = self.choosePokeball()
        try:
            new_guy.moves = self.chooseMoves()
        except Exception as e:
            pass
        new_guy.hpIV, new_guy.atkIV, new_guy.defIV, new_guy.spaIV, new_guy.spdIV, new_guy.speIV = self.chooseIV(new_guy.moves, root)
        if stat_func := STAT_LOGIC_REGISTRY.get(self.stat_key):
            stat_func(self, new_guy, root)
        else:
            self.chooseEVsAndNature(new_guy, root)
        if item_func := ITEM_LOGIC_REGISTRY.get(self.item_key):
            new_guy.item = item_func()
        else:
            new_guy.item = self.chooseItem(new_guy, root, debug)
        return new_guy

    def toString(self) -> str:
        movesetString = ''
        for moveset in self.sets:
            parser = '\n\t'.join(moveset.toString().split('\n'))
            movesetString += f'\n\t{parser}'

        return f'{self.name}: {self.pkTypes}{movesetString}\n{self.baseStats}'

