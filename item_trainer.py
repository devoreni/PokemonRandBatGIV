import ZODB, ZODB.FileStorage
import functions
import csv
import os
import pokemon_ddl
import random

STORAGE = ZODB.FileStorage.FileStorage('./data/PokeData.fs')
DB = ZODB.DB(STORAGE)
CONNECTION = DB.open()
DB_ROOT = CONNECTION.root

def generateMode():
    while True:
        pk_name, chosen_pk = functions.getPokemonTeam(1, DB_ROOT)
        indiv_in_list = functions.createIndivPokemon(chosen_pk, DB_ROOT)
        indiv = indiv_in_list[0]
        print(indiv.toString())
        print(indiv.hpStat, indiv.atkStat, indiv.defStat, indiv.spaStat, indiv.spdStat, indiv.speStat)
        types_hit_super_effectively = set()
        already_hit = set()
        for move_name in indiv.moves:
            move = DB_ROOT.moves[move_name]
            if move.category not in {'Phys', 'Spec'}:
                continue
            for target_type in DB_ROOT.pokeprobability['type_names']:
                if target_type in already_hit:
                    continue
                damage_modifier = functions.getDamageModifier(move.moveType, target_type)
                if damage_modifier == 2:
                    types_hit_super_effectively.add(target_type)
                    already_hit.add(target_type)
        num_super_effective_hits = len(types_hit_super_effectively)
        print(num_super_effective_hits)

        while (chosen_item := input('Item: ')) not in DB_ROOT.items['items']:
            if chosen_item == 'Skip':
                break
            print('Item not found')
        if chosen_item == 'Skip':
            print('\n\n')
            continue
        not_exists = False
        header_row = []
        if not os.path.exists(f'./item_files/{chosen_item}.csv'):
            not_exists = True

        with open(f'./item_files/{chosen_item}.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            input_layer = []

            pk_types = set(DB_ROOT.pokeprobability['pokemon_to_types_map'][pk_name[0]])
            for l_type in DB_ROOT.pokeprobability['type_names']:
                input_layer.append(0 if l_type not in pk_types else 1)
                if not_exists:
                    header_row.append(l_type)

            for ability in DB_ROOT.pokeprobability['abilities']:
                input_layer.append(0 if ability != indiv.ability else 1)
                if not_exists:
                    header_row.append(ability)

            input_layer.append(indiv.hpStat)
            input_layer.append(indiv.atkStat)
            input_layer.append(indiv.defStat)
            input_layer.append(indiv.spaStat)
            input_layer.append(indiv.spdStat)
            input_layer.append(indiv.speStat)

            if not_exists:
                header_row.append('HP Stat')
                header_row.append('Atk Stat')
                header_row.append('Def Stat')
                header_row.append('SpA Stat')
                header_row.append('SpD Stat')
                header_row.append('Spe Stat')
            for move in list(DB_ROOT.moves.values()):
                input_layer.append(0 if move.name not in indiv.moves else 1)
                if not_exists:
                    header_row.append(move.name)

            move_categories = {'Phys': 0, 'Spec': 0, 'Stat': 0}
            move_types = {'Dragon': 0, 'Ice': 0, 'Fighting': 0, 'Dark': 0, 'Fire': 0, 'Ghost': 0, 'Steel': 0, 'Electric': 0,
                          'Rock': 0, 'Poison': 0, 'Ground': 0, 'Bug': 0, 'Grass': 0, 'Psychic': 0, 'Flying': 0, 'Normal': 0,
                          'Water': 0}
            setup_moves = {'HP': 0, 'Atk': 0, 'Def': 0, 'SpA': 0, 'SpD': 0, 'Spe': 0, 'Evasion': 0}
            other_moves = {'Draining Moves': 0, 'Baton Pass': 0, 'Trapping Moves': 0, 'Item Bestowing': 0, 'Multi Hit': 0, 'Screens': 0,
                           'High Crit Ratio': 0, 'Self Stat Drop': 0, 'Low Accuracy': 0, 'Two Turn Attack': 0, 'Multi Target': 0}
            for move_name in indiv.moves:
                move = DB_ROOT.moves[move_name]
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
                if move.name in {'Acid Armor', 'Barrier', 'Bulk Up', 'Coil', 'Cosmic Power', 'Curse', 'Defend Order', 'Defense Curl',
                                 'Harden', 'Iron Defense', 'Skull Bash', 'Stockpile', 'Withdraw'}:
                    setup_moves['Def'] += 1
                if move.name in {'Calm Mind', 'Growth', 'Nasty Plot', 'Tail Glow', 'Work Up'}:
                    setup_moves['SpA'] += 1
                if move.name in {'Amnesia', 'Calm Mind', 'Cosmic Power', 'Defend Order', 'Stockpile'}:
                    setup_moves['SpD'] += 1
                if move.name in {'Agility', 'Dragon Dance', 'Rock Polish'}:
                    setup_moves['Spe'] += 1
                if move.name in {'Double Team', 'Minimize', 'Flash', 'Kinesis', 'Mud-Slap', 'Muddy Water', 'Octazooka', 'Sand Attack', 'Smokescreen'}:
                    setup_moves['Evasion'] += 1
                if move.name in {'Absorb', 'Drain Punch', 'Dream Eater', 'Giga Drain', 'Leech Seed', 'Leech Life', 'Ingrain',
                                 'Mega Drain', 'Aqua Ring'}:
                    other_moves['Draining Moves'] += 1
                if move.name == 'Baton Pass':
                    other_moves['Baton Pass'] += 1
                if move.name in {'Bind', 'Clamp', 'Fire Spin', 'Magma Storm', 'Sand Tomb', 'Whirlpool', 'Wrap'}:
                    other_moves['Trapping Moves'] += 1
                if move.name in {'Fling', 'Trick', 'Switcheroo'}:
                    other_moves['Item Bestowing'] += 1
                if move.name in {'Arm Thrust', 'Barrage', 'Bone Rush', 'Bullet Seed', 'Comet Punch', 'Double Slap', 'Fury Attack',
                                 'Fury Swipes', 'Icicle Spear', 'Pin Missile', 'Rock Blast', 'Tail Slap', 'Bonemerang', 'Double Hit',
                                 'Double Kick', 'Twineedle', 'Beat Up'}:
                    other_moves['Multi Hit'] += 1
                if move.name in {'Light Screen', 'Reflect'}:
                    other_moves['Screens'] += 1
                if move.name in {'Aeroblast', 'Air Cutter', 'Attack Order', 'Blaze Kick', 'Crabhammer', 'Cross Chop', 'Cross Poison',
                                 'Karate Chop', 'Leaf Blade', 'Night Slash', 'Poison Tail', 'Psycho Cut', 'Razor Leaf', 'Razor Wind',
                                 'Shadow Claw', 'Sky Attack', 'Slash', 'Spacial Rend', 'Stone Edge'}:
                    other_moves['High Crit Ratio'] += 1
                if move.name in {'Overheat', 'Leaf Storm', 'Draco Meteor', 'Psycho Boost', 'Superpower', 'Close Combat',
                                 'Hammer Arm'}:
                    other_moves['Self Stat Drop'] += 1
                if move.accuracy < 1:
                    other_moves['Low Accuracy'] += 1
                if move.name in {'Bounce', 'Dig', 'Dive', 'Fly', 'Shadow Force', 'Razor Wind', 'Skull Bash', 'Sky Attack'}:
                    other_moves['Two Turn Attack'] += 1
                if move.name in {'Discharge', 'Earthquake', 'Lava Plume', 'Magnitude', 'Surf', 'Acid', 'Air Cutter', 'Blizzard',
                                 'Bubble', 'Eruption', 'Heat Wave', 'Hyper Voice', 'Icy Wind', 'Muddy Water', 'Poison Gas',
                                 'Powder Snow', 'Razor Leaf', 'Razor Wind', 'Rock Slide', 'Swift', 'Twister', 'Water Spout'}:
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

            if not_exists:
                header_row.extend(list(move_categories.keys()))
                header_row.extend(list(move_types.keys()))
                setup_header = [f'{i} Boost' for i in list(setup_moves.keys())]
                header_row.extend(setup_header)
                header_row.extend(list(other_moves.keys()))


            input_layer.append(num_super_effective_hits)
            if not_exists:
                header_row.append('Coverage')

            num_weaknesses = 0
            num_quad_weaknesses = 0
            num_resistances = 0
            num_quad_resistances = 0

            for attacking_type in DB_ROOT.pokeprobability['type_names']:
                multiplier = 1
                for defensive_types in DB_ROOT.pokesets[pk_name[0]].pkTypes:
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
            if not_exists:
                header_row.extend(['Weaknesses', 'Quad Weaknesses', 'Resistance', 'Quad Resistances'])

            bulk_score = ((indiv.hpStat + indiv.defStat + indiv.spdStat)
                          * ((num_resistances + num_quad_resistances + 1)
                          / (num_weaknesses + 2 * num_quad_weaknesses + 1))
                          * (((other_moves['Draining Moves'] + setup_moves['HP'] + setup_moves['Def'] + setup_moves['SpD']) + 2) / 2))
            input_layer.append(bulk_score)
            if not_exists:
                header_row.append('Bulk Score')

            total_power = 0
            for move in indiv.moves:
                total_power += DB_ROOT.moves[move].power
            offence_score = (max(indiv.atkStat, indiv.spaStat) + 0.5 * min(indiv.atkStat, indiv.spaStat)) * max(num_super_effective_hits, 1) * (total_power / 10)
            input_layer.append(offence_score)
            if not_exists:
                header_row.append('Offence Score')

            if not_exists:
                writer.writerow(header_row)
            writer.writerow(input_layer)
            print('\n\n')

def createMode():
    while True:
        while (poke_name := input('Pokemon Name: ')) not in DB_ROOT.pokeprobability['pokemon_to_types_map'].keys():
            print('Name not recognized\n')
        pokemon = DB_ROOT.pokesets[poke_name]
        new_guy = pokemon_ddl.PokemonIndiv()
        new_guy.name = poke_name
        g = random.choice(pokemon.genders)
        g = f'({g})' if g else g
        new_guy.gender = g
        while (poke_ability := input('Ability: ')) not in DB_ROOT.pokeprobability['abilities']:
            print('Ability not recognized\n')
        new_guy.ability = poke_ability
        moves = []
        for i in range(4):
            while (move_name := input(f'Move {i}: ')) not in set(DB_ROOT.moves.keys()).union({''}):
                print('Move name not recognized')
            if move_name == '':
                break
            moves.append(move_name)
        new_guy.moves = moves
        new_guy.hpIV, new_guy.atkIV, new_guy.defIV, new_guy.spaIV, new_guy.spdIV, new_guy.speIV = pokemon.chooseIV(
            new_guy.moves, DB_ROOT)
        pokemon.chooseEVsAndNature(new_guy, DB_ROOT)

        while (item_name := input('Held Item: ')) not in DB_ROOT.items['items']:
            print('Item not recognized')

        types_hit_super_effectively = set()
        already_hit = set()
        for move_name in new_guy.moves:
            move = DB_ROOT.moves[move_name]
            if move.category not in {'Phys', 'Spec'}:
                continue
            for target_type in DB_ROOT.pokeprobability['type_names']:
                if target_type in already_hit:
                    continue
                damage_modifier = functions.getDamageModifier(move.moveType, target_type)
                if damage_modifier == 2:
                    types_hit_super_effectively.add(target_type)
                    already_hit.add(target_type)
        num_super_effective_hits = len(types_hit_super_effectively)

        not_exists = False
        header_row = []
        if not os.path.exists(f'./item_files/{item_name}.csv'):
            not_exists = True

        with open(f'./item_files/{item_name}.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            input_layer = []

            pk_types = set(DB_ROOT.pokeprobability['pokemon_to_types_map'][poke_name])
            for l_type in DB_ROOT.pokeprobability['type_names']:
                input_layer.append(0 if l_type not in pk_types else 1)
                if not_exists:
                    header_row.append(l_type)

            for ability in DB_ROOT.pokeprobability['abilities']:
                input_layer.append(0 if ability != new_guy.ability else 1)
                if not_exists:
                    header_row.append(ability)

            input_layer.append(new_guy.hpStat)
            input_layer.append(new_guy.atkStat)
            input_layer.append(new_guy.defStat)
            input_layer.append(new_guy.spaStat)
            input_layer.append(new_guy.spdStat)
            input_layer.append(new_guy.speStat)

            if not_exists:
                header_row.append('HP Stat')
                header_row.append('Atk Stat')
                header_row.append('Def Stat')
                header_row.append('SpA Stat')
                header_row.append('SpD Stat')
                header_row.append('Spe Stat')

            for move in list(DB_ROOT.moves.values()):
                input_layer.append(0 if move.name not in new_guy.moves else 1)
                if not_exists:
                    header_row.append(move.name)

            move_categories = {'Phys': 0, 'Spec': 0, 'Stat': 0}
            move_types = {'Dragon': 0, 'Ice': 0, 'Fighting': 0, 'Dark': 0, 'Fire': 0, 'Ghost': 0, 'Steel': 0, 'Electric': 0,
                          'Rock': 0, 'Poison': 0, 'Ground': 0, 'Bug': 0, 'Grass': 0, 'Psychic': 0, 'Flying': 0, 'Normal': 0,
                          'Water': 0}
            setup_moves = {'HP': 0, 'Atk': 0, 'Def': 0, 'SpA': 0, 'SpD': 0, 'Spe': 0, 'Evasion': 0}
            other_moves = {'Draining Moves': 0, 'Baton Pass': 0, 'Trapping Moves': 0, 'Item Bestowing': 0, 'Multi Hit': 0, 'Screens': 0,
                           'High Crit Ratio': 0, 'Self Stat Drop': 0, 'Low Accuracy': 0, 'Two Turn Attack': 0, 'Multi Target': 0}
            for move_name in new_guy.moves:
                move = DB_ROOT.moves[move_name]
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
                if move.name in {'Acid Armor', 'Barrier', 'Bulk Up', 'Coil', 'Cosmic Power', 'Curse', 'Defend Order', 'Defense Curl',
                                 'Harden', 'Iron Defense', 'Skull Bash', 'Stockpile', 'Withdraw'}:
                    setup_moves['Def'] += 1
                if move.name in {'Calm Mind', 'Growth', 'Nasty Plot', 'Tail Glow', 'Work Up'}:
                    setup_moves['SpA'] += 1
                if move.name in {'Amnesia', 'Calm Mind', 'Cosmic Power', 'Defend Order', 'Stockpile'}:
                    setup_moves['SpD'] += 1
                if move.name in {'Agility', 'Dragon Dance', 'Rock Polish'}:
                    setup_moves['Spe'] += 1
                if move.name in {'Double Team', 'Minimize', 'Flash', 'Kinesis', 'Mud-Slap', 'Muddy Water', 'Octazooka', 'Sand Attack', 'Smokescreen'}:
                    setup_moves['Evasion'] += 1
                if move.name in {'Absorb', 'Drain Punch', 'Dream Eater', 'Giga Drain', 'Leech Seed', 'Leech Life', 'Ingrain',
                                 'Mega Drain', 'Aqua Ring'}:
                    other_moves['Draining Moves'] += 1
                if move.name == 'Baton Pass':
                    other_moves['Baton Pass'] += 1
                if move.name in {'Bind', 'Clamp', 'Fire Spin', 'Magma Storm', 'Sand Tomb', 'Whirlpool', 'Wrap'}:
                    other_moves['Trapping Moves'] += 1
                if move.name in {'Fling', 'Trick', 'Switcheroo'}:
                    other_moves['Item Bestowing'] += 1
                if move.name in {'Arm Thrust', 'Barrage', 'Bone Rush', 'Bullet Seed', 'Comet Punch', 'Double Slap', 'Fury Attack',
                                 'Fury Swipes', 'Icicle Spear', 'Pin Missile', 'Rock Blast', 'Tail Slap', 'Bonemerang', 'Double Hit',
                                 'Double Kick', 'Twineedle', 'Beat Up'}:
                    other_moves['Multi Hit'] += 1
                if move.name in {'Light Screen', 'Reflect'}:
                    other_moves['Screens'] += 1
                if move.name in {'Aeroblast', 'Air Cutter', 'Attack Order', 'Blaze Kick', 'Crabhammer', 'Cross Chop', 'Cross Poison',
                                 'Karate Chop', 'Leaf Blade', 'Night Slash', 'Poison Tail', 'Psycho Cut', 'Razor Leaf', 'Razor Wind',
                                 'Shadow Claw', 'Sky Attack', 'Slash', 'Spacial Rend', 'Stone Edge'}:
                    other_moves['High Crit Ratio'] += 1
                if move.name in {'Overheat', 'Leaf Storm', 'Draco Meteor', 'Psycho Boost', 'Superpower', 'Close Combat',
                                 'Hammer Arm'}:
                    other_moves['Self Stat Drop'] += 1
                if move.accuracy < 1:
                    other_moves['Low Accuracy'] += 1
                if move.name in {'Bounce', 'Dig', 'Dive', 'Fly', 'Shadow Force', 'Razor Wind', 'Skull Bash', 'Sky Attack'}:
                    other_moves['Two Turn Attack'] += 1
                if move.name in {'Discharge', 'Earthquake', 'Lava Plume', 'Magnitude', 'Surf', 'Acid', 'Air Cutter', 'Blizzard',
                                 'Bubble', 'Eruption', 'Heat Wave', 'Hyper Voice', 'Icy Wind', 'Muddy Water', 'Poison Gas',
                                 'Powder Snow', 'Razor Leaf', 'Razor Wind', 'Rock Slide', 'Swift', 'Twister', 'Water Spout'}:
                    other_moves['Multi Target'] += 1

            if new_guy.ability in {'Dry Skin', 'Ice Body', 'Poison Heal', 'Rain Dish'}:
                setup_moves['HP'] += 1
            elif new_guy.ability in {'Flower Gift', 'Guts', 'Huge Power', 'Hustle', 'Pure Power'}:
                setup_moves['Atk'] += 1
            elif new_guy.ability in {'Marvel Scale'}:
                setup_moves['Def'] += 1
            elif new_guy.ability in {'Flower Gift'}:
                setup_moves['SpD'] += 1
            elif new_guy.ability in {'Solar Power'}:
                setup_moves['SpA'] += 1
            elif new_guy.ability in {'Chlorophyll', 'Minus', 'Plus', 'Quick Feet', 'Swift Swim', 'Unburden'}:
                setup_moves['Spe'] += 1
            elif new_guy.ability in {'Sand Veil', 'Snow Cloak', 'Tangled Feet'}:
                setup_moves['Evasion'] += 1
            elif new_guy.ability in {'Blaze', 'Flash Fire', 'Overgrow', 'Swarm', 'Torrent'}:
                setup_moves['Atk'] += 1
                setup_moves['SpA'] += 1

            input_layer.extend(list(move_categories.values()))
            input_layer.extend(list(move_types.values()))
            input_layer.extend(list(setup_moves.values()))
            input_layer.extend(list(other_moves.values()))

            if not_exists:
                header_row.extend(list(move_categories.keys()))
                header_row.extend(list(move_types.keys()))
                setup_header = [f'{i} Boost' for i in list(setup_moves.keys())]
                header_row.extend(setup_header)
                header_row.extend(list(other_moves.keys()))

            input_layer.append(num_super_effective_hits)
            if not_exists:
                header_row.append('Coverage')

            num_weaknesses = 0
            num_quad_weaknesses = 0
            num_resistances = 0
            num_quad_resistances = 0

            for attacking_type in DB_ROOT.pokeprobability['type_names']:
                multiplier = 1
                for defensive_types in DB_ROOT.pokesets[poke_name].pkTypes:
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
            if not_exists:
                header_row.extend(['Weaknesses', 'Quad Weaknesses', 'Resistance', 'Quad Resistances'])

            bulk_score = ((new_guy.hpStat + new_guy.defStat + new_guy.spdStat)
                          * ((num_resistances + num_quad_resistances + 1)
                             / (num_weaknesses + 2 * num_quad_weaknesses + 1))
                          * (((other_moves['Draining Moves'] + setup_moves['HP'] + setup_moves['Def'] + setup_moves[
                        'SpD']) + 2) / 2))
            input_layer.append(bulk_score)
            if not_exists:
                header_row.append('Bulk Score')

            total_power = 0
            for move in new_guy.moves:
                total_power += DB_ROOT.moves[move].power
            offence_score = (max(new_guy.atkStat, new_guy.spaStat) + 0.5 * min(new_guy.atkStat, new_guy.spaStat)) * max(
                num_super_effective_hits, 1) * (total_power / 10)
            input_layer.append(offence_score)
            if not_exists:
                header_row.append('Offence Score')

            if not_exists:
                writer.writerow(header_row)
            writer.writerow(input_layer)
            print(len(input_layer))
            print(f'Added:\n{new_guy.toString()}\nto {item_name}.csv')





def main():
    while (mode := input('Select Mode:\n1 - generate mode\n2 - create mode\n')) not in {'1', '2'}:
        print('mode not recognized\n')
    if mode == '1':
        generateMode()
    elif mode == '2':
        createMode()

if __name__ == '__main__':
    main()