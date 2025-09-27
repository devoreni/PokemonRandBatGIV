from BTrees.OOBTree import OOBTree
import ZODB, ZODB.FileStorage
import persistent
import transaction
import numpy as np
import random
import pprint
import os

import config
import pokemon_ddl
import version_control

def runDML():
    if os.path.exists(config.DB_FILE):
        os.remove(config.DB_FILE)

    storage = ZODB.FileStorage.FileStorage(config.DB_FILE)
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root

    current_dml_hash = version_control.get_dml_hash()
    if not current_dml_hash:
        connection.close()
        db.close()
        storage.close()
        return
    root.dml_version = current_dml_hash

    if not hasattr(root, 'moves'):
        root.moves = OOBTree()
    if not hasattr(root, 'pokesets'):
        root.pokesets = OOBTree()
    if not hasattr(root, 'pokeprobability'):
        root.pokeprobability = OOBTree()
    if not hasattr(root, 'items'):
        root.items = OOBTree()

    if 'Pokemon':
        # Dragon type pokemon
        if 'Dragon':
            if 'Dragonite':
                root.pokesets['Dragonite'] = pokemon_ddl.PokemonSet(
                    name='Dragonite', species='Dragonite', abilities=('Inner Focus',), pkTypes=('Dragon', 'Flying'),
                    sets=(
                        pokemon_ddl.MoveSet(['Protect'],
                                            {
                                                'Protect': ['Dragon Dance', 'Thunder Wave', 'Dragon Rush', 'Draco Meteor', 'Outrage', 'Extreme Speed', 'Aqua Tail', 'Dragon Claw'],
                                                'Dragon Dance': ['Fly', 'Outrage', 'Rock Slide'],
                                                'Aqua Tail': ['Roost', 'Attract', 'Steel Wing', 'Rain Dance'],
                                                'Roost': ['Double Team', 'Safeguard'],
                                                'Fly': ['Dragon Claw', 'Outrage', 'Iron Tail', 'Return'],
                                                'Thunder Wave': ['Dragon Claw', 'Fling', 'Light Screen', 'Haze', 'Aerial Ace'],
                                                'Dragon Claw': ['Earthquake', 'Fire Punch', 'Roar', 'Aerial Ace'],
                                                'Fire Punch': ['Thunder Punch', 'Ice Punch', 'Return'],
                                                'Dragon Rush': ['Fire Punch', 'Thunder Punch', 'Ice Punch'],
                                                'Ice Punch': ['Fire Punch', 'Thunder Punch', 'Stone Edge', 'Rock Slide'],
                                                'Draco Meteor': ['Surf', 'Thunderbolt', 'Flamethrower', 'Fire Blast', 'Blizzard'],
                                                'Surf': ['Flamethrower', 'Thunderbolt', 'Focus Blast', 'Icy Wind', 'Blizzard'],
                                                'Outrage': ['Earthquake', 'Superpower', 'Giga Impact', 'Focus Punch'],
                                                'Thunderbolt': ['Heat Wave']
                                            }),
                    ), baseStats=(91, 134, 95, 100, 100, 80), genders=('M', 'F'), images=('149.gif', '149.png', '149 (1).png')
                )
            if 'Kingdra':
                root.pokesets['Kingdra'] = pokemon_ddl.PokemonSet(
                    name='Kingdra', species='Kingdra', abilities=('Swift Swim', 'Sniper'), pkTypes=('Water', 'Dragon'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Rain Dance', 'Hydro Pump', 'Muddy Water', 'Draco Meteor', 'Dragon Pulse', 'Outrage'],
                                'Hydro Pump': ['Rain Dance', 'Signal Beam', 'Smokescreen', 'Swift'],
                                'Muddy Water': ['Rain Dance', 'Dragon Pulse', 'Yawn', 'Hidden Power [Electric]'],
                                'Draco Meteor': ['Rain Dance', 'Outrage', 'Ice Beam', 'Muddy Water'],
                                'Dragon Pulse': ['Rain Dance', 'Brine', 'Hidden Power [Electric]'],
                                'Outrage': ['Waterfall', 'Iron Head', 'Double-Edge', 'Headbutt'],
                                'Waterfall': ['Rain Dance', 'Dragon Dance'],
                                'Iron Head': ['Dragon Dance', 'Substitute'],
                                'Dragon Dance': ['Waterfall']
                            }
                        ),
                    ), baseStats=(75, 95, 95, 95, 95, 85), genders=('M', 'F'), images=('230.gif', '230.png', '230 (1).png')
                )
            if 'Flygon':
                root.pokesets['Flygon'] = pokemon_ddl.PokemonSet(
                    name='Flygon', species='Flygon', abilities=('Levitate',), pkTypes=('Ground', 'Dragon'),
                    sets=(pokemon_ddl.MoveSet(
                        ['Protect'],
                        {
                            'Protect': ['Earthquake', 'Dragon Claw', 'Roost', 'Draco Meteor'],
                            'Earthquake': ['Bug Bite', 'U-turn', 'Outrage', 'Stone Edge', 'Crunch'],
                            'Dragon Claw': ['Bug Bite', 'U-turn', 'Sandstorm', 'Thunder Punch', 'Dig'],
                            'Roost': ['Sandstorm', 'Thunder Punch', 'Stone Edge', 'Giga Drain'],
                            'Draco Meteor': ['Fire Blast', 'Earth Power', 'Gust', 'Ominous Wind'],
                            'Fire Blast': ['Earthquake', 'Fissure', 'Hyper Beam', 'Solar Beam'],
                            'U-turn': ['Fire Punch', 'Dig', 'Toxic', 'Swagger', 'Tailwind', 'Sunny Day', 'Steel Wing']
                        }
                    ),), baseStats=(80, 100, 80, 80, 80, 100), genders=('M', 'F'), images=('330.gif', '330.png', '330 (1).png')
                )
            if 'Salamence':
                root.pokesets['Salamence'] = pokemon_ddl.PokemonSet(
                    name='Salamence', species='Salamence', abilities=('Intimidate',), pkTypes=('Dragon', 'Flying'),
                    sets=(pokemon_ddl.MoveSet(
                        ['Protect'],
                        {'Protect': ['Fire Fang', 'Thunder Fang', 'Crunch', 'Headbutt', 'Hydro Pump', 'Dragon Breath'],
                         'Fire Fang': ['Scary Face', 'Dragon Claw', 'Double-Edge', 'Thunder Fang', 'Dragon Dance'],
                         'Thunder Fang': ['Aerial Ace', 'Fire Fang', 'Zen Headbutt', 'Rain Dance', 'Roar'],
                         'Crunch': ['Brick Break', 'Facade', 'Rest', 'Substitute', 'Earthquake'],
                         'Rest': ['Sleep Talk', 'Snore'],
                         'Headbutt': ['Outrage', 'Rollout', 'Aqua Tail', 'Fury Cutter', 'Shadow Claw', 'Dragon Dance'],
                         'Hydro Pump': ['Dragon Pulse', 'Draco Meteor', 'Heat Wave', 'Swift', 'Air Cutter'],
                         'Dragon Breath': ['Flamethrower', 'Fire Blast'],
                         'Flamethrower': ['Hidden Power [Ice]', 'Sunny Day', 'Hidden Power [Bug]'],
                         'Fire Blast': ['Sunny Day', 'Giga Impact', 'Double Team', 'Mud-Slap'],
                         'Dragon Dance': ['Secret Power', 'Shadow Claw', 'Steel Wing', 'Rock Slide']
                         }
                    ),), baseStats=(95, 135, 80, 110, 80, 100), genders=('M', 'F'), images=('373.gif', '373.png', '373 (1).png')
                )
            if 'Latias':
                root.pokesets['Latias'] = pokemon_ddl.PokemonSet(
                    name='Latias', species='Latias', abilities=('Levitate',), pkTypes=('Dragon', 'Psychic'),
                    sets=(pokemon_ddl.MoveSet(
                        ['Protect'],
                         {
                             'Protect': ['Mist Ball', 'Helping Hand', 'Trick'],
                             'Mist Ball': ['Dragon Pulse', 'Water Pulse', 'Calm Mind', 'Thunder'],
                             'Dragon Pulse': ['Thunderbolt', 'Thunder', 'Solar Beam', 'Hidden Power [Fire]'],
                             'Thunder': ['Rain Dance', 'Attract'],
                             'Water Pulse': ['Shadow Ball', 'Shock Wave', 'Energy Ball', 'Charge Beam', 'Ice Beam'],
                             'Calm Mind': ['Grass Knot', 'Icy Wind', 'Swift'],
                             'Helping Hand': ['Mist Ball', 'Healing Wish', 'Thunder Wave', 'Roost', 'Safeguard', 'Light Screen', 'Reflect'],
                             'Healing Wish': ['Mist Ball', 'Charm'],
                             'Thunder Wave': ['Mist Ball', 'Psychic', 'Wish'],
                             'Roost': ['Draco Meteor', 'Hyper Beam', 'Dragon Pulse']
                         }
                    ),), baseStats=(80, 80, 90, 110, 130, 110), genders=('F',), images=('380.gif', '380.png', '380 (1).png'),
                    item_key='lati'
                )
            if 'Latios':
                root.pokesets['Latios'] = pokemon_ddl.PokemonSet(
                    name='Latios', species='Latios', abilities=('Levitate',), pkTypes=('Dragon', 'Psychic'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                # --- MAIN BRANCHING POINT ---
                                'Protect': ['Calm Mind', 'Luster Purge', 'Draco Meteor', 'Light Screen',
                                            'Dragon Dance', 'Trick'],

                                # --- 1. Calm Mind Setup Sweeper Path ---
                                'Calm Mind': ['Luster Purge', 'Dragon Pulse', 'Recover', 'Surf', 'Thunderbolt',
                                              'Shadow Ball'],
                                'Recover': ['Calm Mind', 'Luster Purge', 'Dragon Pulse', 'Light Screen', 'Reflect'],

                                # --- 2. All-Out Attacker Paths (Special) ---
                                'Luster Purge': ['Dragon Pulse', 'Ice Beam', 'Thunderbolt', 'Surf', 'Shadow Ball',
                                                 'Energy Ball', 'Recover'],
                                'Draco Meteor': ['Surf', 'Thunder', 'Hidden Power [Fire]', 'Shadow Ball', 'Trick',
                                                 'Psychic'],  # Psychic is rare here
                                'Dragon Pulse': ['Luster Purge', 'Surf', 'Thunderbolt', 'Grass Knot', 'Ice Beam',
                                                 'Recover'],

                                # Coverage moves branching and looping
                                'Surf': ['Thunderbolt', 'Ice Beam', 'Hidden Power [Fire]', 'Grass Knot'],
                                'Thunderbolt': ['Ice Beam', 'Surf', 'Hidden Power [Fire]', 'Grass Knot',
                                                'Charge Beam'],
                                'Ice Beam': ['Thunderbolt', 'Shadow Ball', 'Energy Ball'],
                                'Shadow Ball': ['Hidden Power [Fire]', 'Luster Purge', 'Psychic'],
                                'Energy Ball': ['Hidden Power [Fire]', 'Shadow Ball'],
                                'Grass Knot': ['Ice Beam', 'Hidden Power [Fire]'],
                                'Charge Beam': ['Luster Purge', 'Dragon Pulse'],  # Alternative boosting move

                                # --- 3. Support & Disruption Paths ---
                                'Light Screen': ['Reflect', 'Recover', 'Dragon Pulse', 'Luster Purge'],
                                'Reflect': ['Light Screen', 'Recover', 'Memento', 'Dragon Claw'],
                                # Memento is a final option
                                'Memento': [],  # Terminal move, forces backtracking
                                'Trick': ['Draco Meteor', 'Surf', 'Thunderbolt', 'Ice Beam'],
                                # For Choice item sets

                                # --- 4. Physical Attacker Gimmick Path ---
                                'Dragon Dance': ['Dragon Claw', 'Earthquake', 'Shadow Claw', 'Zen Headbutt',
                                                 'Recover', 'Roost'],
                                'Dragon Claw': ['Earthquake', 'Zen Headbutt', 'Waterfall'],
                                'Earthquake': ['Dragon Claw', 'Shadow Claw', 'Steel Wing'],

                                # --- 5. Niche Weather Paths ---
                                'Rain Dance': ['Thunder', 'Surf', 'Dragon Pulse'],
                                'Sunny Day': ['Solar Beam', 'Psychic'],
                                'Thunder': ['Surf', 'Rain Dance', 'Dragon Pulse'],
                                'Solar Beam': ['Sunny Day', 'Psychic'],
                            }
                        ),
                    ),
                    baseStats=(80, 90, 80, 130, 110, 110),
                    genders=('M',), images=('381.gif', '381.png', '381 (1).png'), item_key = 'lati'
                )
            if 'Rayquaza':
                root.pokesets['Rayquaza'] = pokemon_ddl.PokemonSet(
                    name='Rayquaza', species='Rayquaza', abilities=('Air Lock',), pkTypes=('Dragon', 'Flying'),
                    sets=(
                        # MoveSet 1: "The Unpredictable Mix" - Starts with Protect, but the paths are messy.
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                # --- Starting nodes are now weaker, more situational, or non-damaging ---
                                'Protect': ['Aerial Ace', 'Scary Face', 'Bulk Up', 'Ancient Power', 'Dragon Claw',
                                            'Draco Meteor'],

                                # --- Setup paths that force mixed attacking ---
                                'Bulk Up': ['Dragon Claw', 'Earthquake', 'Rock Slide', 'Fire Blast', 'Surf'],
                                # Physical setup -> Special moves
                                'Scary Face': ['Dragon Dance', 'Icy Wind', 'Rock Tomb', 'Draco Meteor'],
                                # Speed control leads to setup or more control
                                'Dragon Dance': ['Fly', 'Waterfall', 'Crunch', 'Overheat'],
                                # The best setup move leads to weaker or self-nerfing attacks

                                # --- Attacking paths with awkward branches ---
                                'Dragon Claw': ['Fly', 'Dive', 'Earthquake', 'Swords Dance', 'Ice Beam'],
                                # Good physical move -> 2-turn moves or special coverage
                                'Draco Meteor': ['Waterfall', 'Rock Slide', 'Extreme Speed', 'Thunder'],
                                # Powerful special move -> Physical moves
                                'Aerial Ace': ['Dragon Dance', 'Swords Dance', 'Rock Slide', 'Tailwind'],

                                # --- Deeper, more specialized moves ---
                                'Swords Dance': ['Extreme Speed', 'Shadow Claw', 'Brick Break', 'Fly'],
                                # A rare but potent physical set
                                'Tailwind': ['Icy Wind', 'Air Slash', 'Dragon Pulse', 'Protect'],
                                # A dedicated support set branch
                                'Extreme Speed': ['Draco Meteor', 'Overheat', 'Dragon Claw', 'Protect'],
                                # The best move is a connector, not a finisher
                                'Ancient Power': ['Earth Power', 'Shadow Claw', 'Signal Beam', 'Cosmic Power'],

                                # Weaker filler moves
                                'Fly': ['Rest', 'Dive'],
                                'Dive': ['Waterfall', 'Rest'],
                                'Rest': ['Sleep Talk']
                            }
                        ),

                        # MoveSet 2: "The Reckless Gambler" - No Protect, high risk, awkward combinations.
                        pokemon_ddl.MoveSet(
                            # Starting moves are powerful but have significant drawbacks or are just plain weird.
                            ['Outrage', 'Overheat', 'Fly', 'Extreme Speed'],
                            {
                                'Outrage': ['Surf', 'Thunder', 'Giga Impact', 'Scary Face'],
                                # Lock-in move leads to special attacks
                                'Overheat': ['Rock Slide', 'Earthquake', 'Extreme Speed', 'Dragon Claw'],
                                # Self-nerfing move leads to physical attacks
                                'Fly': ['Dragon Dance', 'Bulk Up', 'Dive', 'Rest'],  # Risky 2-turn move leads to setup
                                'Extreme Speed': ['Draco Meteor', 'Blizzard', 'Outrage', 'Swords Dance'],
                                # Good priority leads to nukes or lock-in

                                # These paths are short and aggressive, offering little synergy
                                'Draco Meteor': ['Extreme Speed', 'Hyper Beam', 'Giga Impact'],
                                'Earthquake': ['Stone Edge', 'Outrage'],
                                'Blizzard': ['Thunder', 'Focus Blast'],
                                'Dragon Dance': ['Fly', 'Outrage', 'Waterfall']
                            }
                        )
                    ),
                    baseStats=(105, 150, 90, 150, 90, 95),
                    genders=('',), images=('384.gif', '384.png', '384 (1).png')
                )
            if 'Dialga':
                root.pokesets['Dialga'] = pokemon_ddl.PokemonSet(
                    name='Dialga', species='Dialga', abilities=('Pressure',), pkTypes=('Steel', 'Dragon'),
                    sets=(
                        # MoveSet 1: The "Strategic Disrupter" set with Protect.
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                # Starting nodes are now focused on strategy and utility over raw power.
                                'Protect': ['Trick Room', 'Gravity', 'Flash Cannon', 'Substitute', 'Scary Face', 'Roar of Time'],

                                # The Trick Room path now encourages spread moves or defensive plays.
                                'Trick Room': ['Swift', 'Flash Cannon', 'Dragon Pulse', 'Aura Sphere', 'Iron Defense', 'Roar of Time'],

                                # The Gravity path enables low-accuracy, high-power moves.
                                'Gravity': ['Thunder', 'Blizzard', 'Fire Blast', 'Stone Edge', 'Focus Blast'],
                                'Thunder': ['Blizzard', 'Gravity', 'Dragon Pulse'],
                                'Blizzard': ['Thunder', 'Gravity', 'Aura Sphere'],
                                'Fire Blast': ['Thunder', 'Gravity', 'Flash Cannon'],

                                # Substitute provides a defensive pivot into attacks.
                                'Substitute': ['Flash Cannon', 'Flamethrower', 'Thunderbolt', 'Ice Beam',
                                               'Dragon Pulse'],
                                'Flash Cannon': ['Dragon Pulse', 'Aura Sphere', 'Earth Power', 'Power Gem'],

                                # General utility and weaker options.
                                'Dragon Pulse': ['Flash Cannon', 'Aura Sphere', 'Thunderbolt', 'Ice Beam'],
                                'Scary Face': ['Rock Tomb', 'Icy Wind', 'Dragon Breath', 'Roar of Time'],
                                'Swift': ['Dragon Pulse', 'Aura Sphere', 'Shock Wave', 'Roar of Time'],
                                # Leads to other guaranteed-hit or spread moves
                            }
                        ),

                        # MoveSet 2: The "Flawed Powerhouse" set without Protect.
                        pokemon_ddl.MoveSet(
                            # Starting moves are high-commitment or force a mixed role.
                            ['Bulk Up', 'Roar of Time', 'Draco Meteor', 'Roar of Time'],
                            {
                                # High-risk signature move leads to other powerful but non-synergistic moves.
                                'Roar of Time': ['Giga Impact', 'Fire Blast', 'Earthquake'],

                                # Physical setup is intentionally paired with special moves or less ideal physical ones.
                                'Bulk Up': ['Dragon Claw', 'Iron Head', 'Shadow Claw', 'Overheat', 'Thunderbolt', 'Roar of Time'],
                                'Dragon Claw': ['Slash', 'Brick Break', 'Rock Slide', 'Overheat', 'Roar of Time'],
                                'Iron Head': ['Stone Edge', 'Aerial Ace', 'Shadow Claw'],

                                # Special nuke forces stat drops and leads to physical or utility options.
                                'Draco Meteor': ['Earthquake', 'Outrage', 'Metal Burst', 'Swagger'],
                                'Overheat': ['Dragon Claw', 'Earthquake', 'Aura Sphere', 'Roar of Time'],

                                # Outrage is a risky late-graph option.
                                'Outrage': ['Earthquake', 'Stone Edge', 'Roar of Time']
                            }
                        )
                    ),
                    baseStats=(100, 120, 120, 150, 100, 90),
                    genders=('',), images=('483.gif', '483.png', '483 (1).png'), item_key='dialga'
                )
            if 'Palkia':
                root.pokesets['Palkia'] = pokemon_ddl.PokemonSet(
                    name='Palkia', species='Palkia', abilities=('Pressure',), pkTypes=('Water', 'Dragon'),
                    sets=(
                        # MoveSet 1: "The Disruptive Stall" set. High variance and strategic gimmicks.
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                # Starting nodes are now high-commitment strategies or weaker STAB.
                                'Protect': ['Spacial Rend', 'Substitute', 'Rest', 'Whirlpool', 'Heal Block'],

                                # Signature move is present, but leads to less optimal coverage.
                                'Spacial Rend': ['Water Pulse', 'Swift', 'Ancient Power', 'Aura Sphere', 'Earth Power'],

                                # High-risk, high-reward recovery path.
                                'Rest': ['Snore', 'Sleep Talk'],
                                'Sleep Talk': ['Spacial Rend', 'Surf', 'Flamethrower'],

                                # Sub-Punch path remains.
                                'Substitute': ['Focus Punch', 'Spacial Rend', 'Brine'],
                                'Focus Punch': ['Spacial Rend', 'Aqua Tail'],

                                # Trapping and disruption paths.
                                'Whirlpool': ['Toxic', 'Spacial Rend', 'Surf'],
                                'Heal Block': ['Spacial Rend', 'Surf', 'Toxic', 'Swagger'],

                                # Weaker moves have paths to stronger ones, making them more common.
                                'Water Pulse': ['Ice Beam', 'Thunderbolt', 'Spacial Rend'],
                                'Brine': ['Thunder', 'Blizzard', 'Spacial Rend'],
                            }
                        ),

                        # MoveSet 2: "The Awkward Attacker" set. No Protect, forces mixed roles.
                        pokemon_ddl.MoveSet(
                            # Starts are physical setup, or a choice of STABs.
                            ['Bulk Up', 'Spacial Rend', 'Aqua Tail'],
                            {
                                # Physical setup leads to a messy mix of attacks.
                                'Bulk Up': ['Aqua Tail', 'Dragon Claw', 'Avalanche', 'Stone Edge', 'Fire Blast',
                                            'Fling'],
                                'Aqua Tail': ['Outrage', 'Earthquake', 'Stone Edge', 'Spacial Rend'],
                                'Avalanche': ['Dragon Claw', 'Earthquake', 'Aqua Tail'],

                                # Special STAB leads to physical moves or high-risk special moves.
                                'Spacial Rend': ['Outrage', 'Earthquake', 'Hydro Pump', 'Thunder', 'Hail'],
                                'Hydro Pump': ['Draco Meteor', 'Blizzard', 'Focus Blast'],

                                # Risky lock-in move.
                                'Outrage': ['Aqua Tail', 'Earthquake', 'Stone Edge'],

                                # Weather disruption.
                                'Hail': ['Blizzard', 'Spacial Rend', 'Protect']  # Rare chance to get Protect here.
                            }
                        )
                    ),
                    baseStats=(90, 120, 100, 150, 120, 100),
                    genders=('',), images=('484.gif', '484.png', '484 (1).png'), item_key='palkia'
                )
            if 'Giratina':
                root.pokesets['Giratina'] = pokemon_ddl.PokemonSet(
                    name='Giratina', species='Giratina', abilities=('Pressure',), pkTypes=('Ghost', 'Dragon'),
                    sets=(
                        # MoveSet 1: The "Bulky Attacker" set. Has Protect but is forced into a mixed role.
                        pokemon_ddl.MoveSet(
                            ['Shadow Force'],
                            {
                                # Starting nodes offer a mix of setup, utility, and reliable STAB.
                                'Protect': ['Calm Mind', 'Will-O-Wisp', 'Shadow Claw', 'Dragon Pulse', 'Shadow Sneak', 'Dragon Claw','Will-O-Wisp'],

                                # Calm Mind is paired with physical options to create an awkward mixed set.
                                'Calm Mind': ['Dragon Pulse', 'Shadow Ball', 'Earthquake', 'Aura Sphere', 'Rest'],

                                # Will-O-Wisp is a key utility move with offensive follow-ups.
                                'Will-O-Wisp': ['Shadow Ball', 'Dragon Pulse',  'Ominous Wind'],

                                # Physical STAB leads to the risky signature move or special coverage.
                                'Shadow Claw': ['Shadow Force', 'Dragon Claw', 'Earthquake', 'Stone Edge',
                                                'Aura Sphere'],
                                'Dragon Claw': ['Shadow Claw', 'Earthquake', 'Aqua Tail', 'Iron Head'],

                                # The signature move is powerful but slow.
                                'Shadow Force': ['Protect'],

                                # Reliable special STAB and priority.
                                'Dragon Pulse': ['Shadow Ball', 'Aura Sphere', 'Thunderbolt', 'Energy Ball'],
                                'Shadow Sneak': ['Will-O-Wisp', 'Shadow Claw', 'Dragon Claw', 'Toxic'],
                            }
                        ),

                        # MoveSet 2: The "Disruptive Stall" set. No Protect, focuses on status and disruption.
                        pokemon_ddl.MoveSet(
                            # Starts with core stall/disruption moves.
                            ['Will-O-Wisp', 'Rest', 'Toxic', 'Substitute', 'Shadow Force'],
                            {
                                'Will-O-Wisp': ['Spite', 'Heal Block', 'Dragon Breath'],

                                # Classic RestTalk strategy.
                                'Rest': ['Sleep Talk', 'Snore'],
                                'Sleep Talk': ['Dragon Pulse', 'Shadow Ball', 'Earthquake'],

                                # Toxic stall paths.
                                'Toxic': ['Protect', 'Substitute', 'Spite', 'Pain Split'],
                                # A rare chance to get Protect
                                'Pain Split': ['Will-O-Wisp', 'Substitute', 'Destiny Bond'],

                                # Substitute provides a defensive pivot.
                                'Substitute': ['Will-O-Wisp', 'Toxic', 'Calm Mind', 'Dragon Pulse'],

                                # Disruptive moves.
                                'Spite': ['Toxic', 'Will-O-Wisp', 'Protect'],
                                'Destiny Bond': [],  # Terminal move
                            }
                        )
                    ),
                    baseStats=(150, 100, 120, 100, 120, 90),
                    genders=('',), images=('487.gif', '487-a.png', '487-a (1).png')
                )
            if 'Arceus-Dragon':
                root.pokesets['Arceus-Dragon'] = pokemon_ddl.PokemonSet(
                    name='Arceus-Dragon', species='Arceus', abilities=('Multitype',), pkTypes=('Dragon',),
                    sets=(
                        # MoveSet 1: "The Chaotic Bulwark". Guaranteed Protect + Judgement, then maximum variance.
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Judgement'],

                                # Judgement is the central hub for a chaotic web of possibilities.
                                'Judgement': [
                                    'Calm Mind', 'Swords Dance', 'Recover', 'Cosmic Power', 'Will-O-Wisp',
                                    'Thunder Wave', 'Extreme Speed', 'Earth Power', 'Ice Beam', 'Thunderbolt',
                                    'Flamethrower', 'Shadow Claw', 'Gravity', 'Substitute'
                                ],

                                # Every node below is heavily interconnected to create unpredictable sets.
                                'Calm Mind': ['Ice Beam', 'Thunderbolt', 'Earthquake', 'Shadow Claw', 'Recover',
                                              'Swords Dance', 'Will-O-Wisp'],
                                'Swords Dance': ['Extreme Speed', 'Dragon Claw', 'Shadow Claw', 'Earthquake', 'Surf',
                                                 'Ice Beam', 'Calm Mind'],
                                'Recover': ['Calm Mind', 'Will-O-Wisp', 'Ice Beam', 'Flamethrower', 'Substitute',
                                            'Swords Dance', 'Judgement'],
                                'Cosmic Power': ['Recover', 'Will-O-Wisp', 'Toxic', 'Flamethrower', 'Judgement'],
                                'Will-O-Wisp': ['Recover', 'Calm Mind', 'Extreme Speed', 'Dragon Claw'],
                                'Extreme Speed': ['Swords Dance', 'Shadow Claw', 'Draco Meteor', 'Overheat', 'Judgement',
                                                  'Recover'],
                                'Earth Power': ['Ice Beam', 'Thunderbolt', 'Calm Mind', 'Swords Dance', 'Dragon Claw'],
                                'Ice Beam': ['Thunderbolt', 'Earth Power', 'Judgement', 'Calm Mind', 'Swords Dance'],
                                'Thunderbolt': ['Ice Beam', 'Surf', 'Judgement', 'Calm Mind', 'Swords Dance'],
                                'Dragon Claw': ['Earthquake', 'Shadow Claw', 'Swords Dance', 'Calm Mind', 'Ice Beam'],
                                'Substitute': ['Calm Mind', 'Swords Dance', 'Recover', 'Will-O-Wisp', 'Judgement'],
                                'Gravity': ['Thunder', 'Blizzard', 'Focus Blast', 'Earthquake', 'Judgement'],
                            }
                        ),

                        # MoveSet 2: "The Chaotic Gambler". No Protect, starts with Judgement into chaos.
                        pokemon_ddl.MoveSet(
                            ['Judgement'],
                            {
                                'Judgement': [
                                    'Extreme Speed', 'Draco Meteor', 'Outrage', 'Calm Mind', 'Swords Dance',
                                    'Gravity', 'Trick Room', 'Fire Blast', 'Thunder', 'Ice Beam', 'Earthquake',
                                    'Shadow Claw', 'Will-O-Wisp', 'Recover'
                                ],

                                'Draco Meteor': ['Extreme Speed', 'Overheat', 'Earthquake', 'Fire Blast', 'Steel Wing'],
                                'Outrage': ['Extreme Speed', 'Aqua Tail', 'Iron Head', 'Ice Beam', 'Giga Drain'],
                                'Calm Mind': ['Ice Beam', 'Thunder', 'Focus Blast', 'Shadow Claw', 'Recover',
                                              'Swords Dance'],
                                'Swords Dance': ['Extreme Speed', 'Shadow Claw', 'Dragon Claw', 'Giga Drain',
                                                 'Calm Mind'],
                                'Gravity': ['Thunder', 'Blizzard', 'Focus Blast', 'Draco Meteor', 'Judgement'],
                                'Trick Room': ['Judgement', 'Draco Meteor', 'Fire Blast', 'Thunder', 'Focus Blast'],
                                'Extreme Speed': ['Judgement', 'Swords Dance', 'Draco Meteor', 'Will-O-Wisp', 'Recover'],
                                'Fire Blast': ['Draco Meteor', 'Thunder', 'Ice Beam', 'Earthquake'],
                                'Earthquake': ['Stone Edge', 'Outrage', 'Dragon Claw', 'Flamethrower'],
                                'Recover': ['Judgement', 'Calm Mind', 'Swords Dance', 'Will-O-Wisp', 'Toxic']
                            }
                        ),

                        # MoveSet 3: "The Perish Trapper". A specific, high-risk alternate strategy.
                        pokemon_ddl.MoveSet(
                            ['Perish Song'],
                            {
                                'Mean Look': ['Protect', 'Recover', 'Judgement'],
                                'Perish Song': ['Mean Look']
                            }
                        )
                    ),
                    baseStats=(120, 120, 120, 120, 120, 120),
                    genders=('',), images=('493.gif', 'arceus-dragon.png', 'arceus-dragon (1).png'), item_key='arcDrag',
                    stat_key='arcStat'
                )

        # Ice type pokemon
        if 'Ice Type Pokemon':
            if 'Dewgong':
                root.pokesets['Dewgong'] = pokemon_ddl.PokemonSet(
                    name='Dewgong', species='Dewgong', abilities=('Thick Fat', 'Hydration'), pkTypes=('Water', 'Ice'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Perish Song', 'Protect'],
                            {
                                'Perish Song': ['Whirlpool'],
                                'Whirlpool': ['Rest'],
                                'Rest': ['Protect'],
                                'Protect': ['Fake Out', 'Perish Song'],
                                'Fake Out': ['Perish Song']
                            }
                        ), (
                        pokemon_ddl.MoveSet(
                            ['Perish Song', 'Rest'],
                            {
                                'Perish Song': ['Whirlpool'],
                                'Whirlpool': ['Protect'],
                                'Protect': ['Rest'],
                                'Rest': ['Sleep Talk', 'Sheer Cold', 'Horn Drill']
                            }
                        )
                    )
                    ),
                    baseStats=(90, 70, 80, 70, 95, 70),
                    genders=('M', 'F'),
                    images=('087.gif', '087.png', '087 (1).png')
                )
            if 'Cloyster':
                root.pokesets['Cloyster'] = pokemon_ddl.PokemonSet(
                    name='Cloyster', species='Cloyster', abilities=('Shell Armor', 'Skill Link'), pkTypes=('Water', 'Ice'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Spikes', 'Toxic Spikes', 'Ice Shard', 'Rock Blast', 'Explosion']
                            }
                        ),
                    ), baseStats=(50, 95, 180, 85, 45, 70), genders=('M', 'F'),images=('091.gif', '091.png', '091 (1).png')
                )
            if 'Jynx':
                root.pokesets['Jynx'] = pokemon_ddl.PokemonSet(
                    name='Jynx', species='Jynx', abilities=('Oblivious', 'Forewarn'), pkTypes=('Ice', 'Psychic'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Lovely Kiss', 'Taunt', 'Fake Out', 'Wish'],
                                'Lovely Kiss': ['Nasty Plot', 'Ice Beam', 'Psychic', 'Focus Blast', 'Dream Eater'],
                                'Taunt': ['Focus Blast', 'Light Screen', 'Lovely Kiss'],
                                'Fake Out': ['Lovely Kiss', 'Blizzard', 'Hail'],
                                'Psychic': ['Ice Beam', 'Skill Swap'],
                                'Dream Eater': ['Lovely Kiss'],
                                'Wish': ['Dream Eater', 'Perish Song'],
                                'Perish Song': ['Mean Look']
                            }
                        ),
                    ), baseStats=(65, 50, 35, 115, 95, 95), genders=('F',), images=('124.gif', '124.png', '124 (1).png')
                )
            if 'Lapras':
                root.pokesets['Lapras'] = pokemon_ddl.PokemonSet(
                    name='Lapras', species='Lapras', abilities=('Water Absorb', 'Shell Armor'), pkTypes=('Water', 'Ice'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Perish Song', 'Curse', 'Dragon Dance', 'Sing', 'Sheer Cold'],
                                'Curse': ['Hydro Pump', 'Avalanche'],
                                'Dragon Dance': ['Hydro Pump', 'Return'],
                                'Hydro Pump': ['Ice Shard', 'Return', 'Zen Headbutt', 'Outrage'],
                                'Return': ['Waterfall', 'Ice Shard', 'Zen Headbutt', 'Outrage'],
                                'Avalanche': ['Waterfall', 'Ice Shard', 'Return', 'Zen Headbutt', 'Outrage'],
                                'Perish Song': ['Rest'],
                                'Rest': ['Sleep Talk'],
                                'Sheer Cold': ['Hail', 'Safeguard', 'Roar', 'Aqua Tail', 'Thunderbolt', 'Confuse Ray', 'Body Slam'],
                                'Hail': ['Blizzard'],
                                'Sing': ['Dream Eater', 'Signal Beam'],
                                'Signal Beam': ['Dream Eater', 'Ice Beam', 'Giga Impact']
                            }
                        ),
                    ), baseStats=(130, 85, 80, 85, 95, 60), genders=('M', 'F'), images=('131.gif', '131.png', '131 (1).png')
                )
            if 'Articuno':
                root.pokesets['Articuno'] = pokemon_ddl.PokemonSet(
                    name='Articuno', species='Articuno', abilities=('Pressure',), pkTypes=('Ice', 'Flying'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Mind Reader', 'Sheer Cold', 'Roost']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Mind Reader', 'U-turn'],
                                'U-turn': ['Toxic', 'Ice Beam', 'Roar', 'Mind Reader'],
                                'Mind Reader': ['Sheer Cold', 'Roost'],
                                'Sheer Cold': ['Mind Reader']
                            }
                        )
                    ), baseStats=(90, 85, 100, 95, 125, 85), genders=('',), images=('144.gif', '144.png', '144 (1).png')
                )
            if 'Delibird':
                root.pokesets['Delibird'] = pokemon_ddl.PokemonSet(
                    name='Delibird', species='Delibird', abilities=('Vital Spirit', 'Hustle'), pkTypes=('Ice', 'Flying'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Rapid Spin', 'Present'],
                                'Rapid Spin': ['Sky Attack', 'Substitute'],
                                'Substitute': ['Focus Punch'],
                                'Present': ['Rapid Spin', 'Pluck', 'Mud-Slap', 'Icy Wind']
                            }
                        ),
                    ), baseStats=(45, 55, 45, 65, 45, 75), genders=('M', 'F'), images=('225.gif', '225.png', '225 (1).png')
                )
            if 'Glalie':
                root.pokesets['Glalie'] = pokemon_ddl.PokemonSet(
                    name='Glalie', species='Glalie', abilities=('Inner Focus', 'Ice Body'), pkTypes=('Ice',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Spikes', 'Gyro Ball', 'Ice Beam', 'Explosion', 'Taunt', 'Hail'],
                                'Spikes': ['Explosion', 'Earthquake', 'Crunch', 'Shadow Ball', 'Dark Pulse', 'Ice Beam', 'Taunt'],
                                'Taunt': ['Spikes', 'Icy Wind'],
                                'Gyro Ball': ['Ice Shard', 'Avalanche', 'Payback'],
                                'Ice Beam': ['Hidden Power [Fire]', 'Shadow Ball', 'Hyper Beam', 'Icy Wind', 'Signal Beam'],
                                'Hail': ['Weather Ball'],
                                'Explosion': ['Earthquake', 'Crunch', 'Spikes', 'Ice Fang', 'Sheer Cold', 'Taunt']
                            }
                        ),
                    ), baseStats=(80, 80, 80, 80, 80, 80), genders=('M', 'F'), images=('362.gif', '362.png', '362 (1).png')
                )
            if 'Walrein':
                root.pokesets['Walrein'] = pokemon_ddl.PokemonSet(
                    name='Walrein', species='Walrein', abilities=('Thick Fat', 'Ice Body'), pkTypes=('Ice', 'Water'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Protect', 'Protect', 'Protect', 'Rest'],
                            {
                                'Protect': ['Substitute', 'Super Fang', 'Hail', 'Curse'],
                                'Rest': ['Sleep Talk', 'Fissure', 'Sheer Cold'],
                                'Hail': ['Blizzard', 'Blizzard', 'Aqua Ring', 'Toxic'],
                                'Substitute': ['Toxic'],
                                'Toxic': ['Surf', 'Super Fang', 'Aqua Ring', 'Aurora Beam'],
                                'Super Fang': ['Body Slam', 'Blizzard'],
                                'Blizzard': ['Hail'],
                                'Curse': ['Earthquake', 'Body Slam', 'Sleep Talk', 'Crunch', 'Block', 'Double-Edge', 'Encore', 'Rock Slide'],
                                'Sleep Talk': ['Rest']
                            }
                        ),
                    ), baseStats=(110, 80, 90, 95, 90, 65), genders=('M', 'F'), images=('365.gif', '365.png', '365 (1).png')
                )
            if 'Regice':
                root.pokesets['Regice'] = pokemon_ddl.PokemonSet(
                    name='Regice', species='Regice', abilities=('Clear Body',), pkTypes=('Ice',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Rest', 'Lock-On'],
                            {
                                'Protect': ['Ancient Power', 'Icy Wind', 'Thunder Wave', 'Toxic', 'Seismic Toss', 'Hyper Beam'],
                                'Rest': ['Charge Beam', 'Amnesia', 'Sleep Talk'],
                                'Lock-On': ['Zap Cannon'],
                                'Zap Cannon': ['Blizzard', 'Explosion', 'Focus Blast']
                            }
                        ),
                    ), baseStats=(80, 50, 100, 100, 200, 50), genders=('',), images=('378.gif', '378.png', '378 (1).png')
                )
            if 'Abomasnow':
                root.pokesets['Abomasnow'] = pokemon_ddl.PokemonSet(
                    name='Abomasnow', species='Abomasnow', abilities=('Snow Warning',), pkTypes=('Grass', 'Ice'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Blizzard'],
                                'Blizzard': ['Wood Hammer', 'Ice Shard', 'Earthquake', 'Focus Blast'],
                                'Ice Shard': ['Wood Hammer', 'Leech Seed', 'Giga Drain', 'Ingrain'],
                                'Wood Hammer': ['Rock Slide', 'Rock Tomb', 'Fling', 'Outrage', 'Skull Bash'],
                                'Earthquake' : ['Rock Slide', 'Rock Tomb', 'Fling', 'Outrage', 'Skull Bash'],
                                'Focus Blast': ['Grass Knot', 'Energy Ball', 'Shadow Ball', 'Hyper Beam', 'Hidden Power [Fire]', 'Hidden Power [Rock]', 'Hidden Power [Ground]'],
                                'Grass Knot': ['Shadow Ball', 'Hyper Beam', 'Hidden Power [Fire]', 'Hidden Power [Rock]', 'Hidden Power [Ground]'],
                                'Energy Ball': ['Shadow Ball', 'Hyper Beam', 'Hidden Power [Fire]', 'Hidden Power [Rock]', 'Hidden Power [Ground]']
                            }
                        ),
                    ), baseStats=(90, 92, 75, 92, 85, 60), genders=('M', 'F'), images=('460.gif', '460-m.png', '460-m (1).png')
                )
            if 'Weavile':
                root.pokesets['Weavile'] = pokemon_ddl.PokemonSet(
                    name='Weavile', species='Weavile', abilities=('Pressure',), pkTypes=('Dark', 'Ice'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Night Slash', 'Ice Punch'],
                                'Night Slash': ['Ice Punch', 'Fake Out'],
                                'Ice Punch': ['Night Slash', 'Fake Out'],
                                'Fake Out': ['Counter', 'X-Scissor', 'Night Slash', 'Ice Punch', 'Metal Claw', 'Attract', 'Low Kick', 'Pursuit', 'Brick Break', 'Crush Claw', 'Poison Jab', 'Screech']
                            }
                        ),
                    ), baseStats=(70, 120, 65, 45, 85, 125), genders=('M', 'F'), images=('461.gif', '461-m.png', '461-m (1).png')
                )
            if 'Glaceon':
                root.pokesets['Glaceon'] = pokemon_ddl.PokemonSet(
                    name='Glaceon', species='Glaceon', abilities=('Snow Cloak',), pkTypes=('Ice',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Detect'],
                            {
                                'Detect': ['Baton Pass', 'Icy Wind'],
                                'Protect': ['Baton Pass', 'Icy Wind'],
                                'Baton Pass': ['Wish', 'Double Team', 'Curse'],
                                'Wish': ['Hidden Power [Ground]', 'Hidden Power [Grass]', 'Shadow Ball', 'Blizzard', 'Ice Beam', 'Yawn'],
                                'Double Team': ['Hidden Power [Ground]', 'Hidden Power [Grass]', 'Shadow Ball', 'Blizzard', 'Ice Beam', 'Yawn'],
                                'Curse': ['Yawn', 'Hail', 'Sunny Day', 'Water Pulse'],
                                'Icy Wind': ['Signal Beam', 'Shadow Ball', 'Wish']
                            }
                        ),
                    ), baseStats=(65, 60, 110, 130, 95, 65), genders=('M', 'F'), images=('471.gif', '471.png', '471 (1).png')
                )
            if 'Mamoswine':
                root.pokesets['Mamoswine'] = pokemon_ddl.PokemonSet(
                    name='Mamoswine', species='Mamoswine', abilities=('Oblivious', 'Snow Cloak'), pkTypes=('Ice', 'Ground'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Curse', 'Knock Off', 'Substitute', 'Earthquake', 'Dig'],
                                'Curse': ['Ice Shard', 'Avalanche'],
                                'Ice Shard': ['Earthquake', 'Stone Edge', 'Rock Slide', 'Superpower'],
                                'Avalanche': ['Earthquake', 'Stone Edge', 'Peck'],
                                'Knock Off': ['Earthquake', 'Rock Slide', 'Scary Face', 'Roar', 'Substitute', 'Ancient Power', 'Superpower'],
                                'Substitute': ['Ice Shard'],
                                'Earthquake': ['Peck', 'Giga Impact', 'Stealth Rock', 'Swagger']
                            }
                        ),
                    ), baseStats=(110, 130, 80, 70, 60, 80), genders=('M', 'F'), images=('473.gif', '473-m.png', '473-m (1).png')
                )
            if 'Froslass':
                root.pokesets['Froslass'] = pokemon_ddl.PokemonSet(
                    name='Froslass', species='Froslass', abilities=('Snow Cloak',), pkTypes=('Ice', 'Ghost'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Hail', 'Spikes', 'Spikes', 'Ominous Wind'],
                                'Hail': ['Destiny Bond', 'Shadow Ball', 'Attract', 'Hidden Power [Fire]', 'Taunt', 'Icy Wind', 'Spikes', 'Double Team'],
                                'Spikes': ['Destiny Bond', 'Shadow Ball', 'Attract', 'Hidden Power [Fire]', 'Taunt', 'Icy Wind', 'Hail'],
                                'Ominous Wind': ['Destiny Bond', 'Attract', 'Hidden Power [Fire]', 'Taunt', 'Icy Wind', 'Hail']
                            }
                        ),
                    ), baseStats=(70, 80, 70, 80, 70, 110), genders=('F',), images=('478.gif', '478.png', '478 (1).png')
                )
            if 'Arceus-Ice':
                root.pokesets['Arceus-Ice'] = pokemon_ddl.PokemonSet(
                    name='Arceus-Ice', species='Arceus', abilities=('Multitype',), pkTypes=('Ice',),
                    sets=(
                        # MoveSet 1: "The Chaotic Bulwark". Guaranteed Protect + Judgement, then maximum variance.
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Judgement'],

                                # Judgement is the central hub for a chaotic web of possibilities.
                                'Judgement': [
                                    'Calm Mind', 'Swords Dance', 'Recover', 'Cosmic Power', 'Will-O-Wisp',
                                    'Thunder Wave', 'Extreme Speed', 'Earth Power', 'Ice Beam', 'Thunderbolt',
                                    'Flamethrower', 'Shadow Claw', 'Gravity', 'Substitute'
                                ],

                                # Every node below is heavily interconnected to create unpredictable sets.
                                'Calm Mind': ['Ice Beam', 'Thunderbolt', 'Earthquake', 'Shadow Claw', 'Recover',
                                              'Swords Dance', 'Will-O-Wisp'],
                                'Swords Dance': ['Extreme Speed', 'Dragon Claw', 'Shadow Claw', 'Earthquake', 'Surf',
                                                 'Ice Beam', 'Calm Mind'],
                                'Recover': ['Calm Mind', 'Will-O-Wisp', 'Ice Beam', 'Flamethrower', 'Substitute',
                                            'Swords Dance', 'Judgement'],
                                'Cosmic Power': ['Recover', 'Will-O-Wisp', 'Toxic', 'Flamethrower', 'Judgement'],
                                'Will-O-Wisp': ['Recover', 'Calm Mind', 'Extreme Speed', 'Dragon Claw'],
                                'Extreme Speed': ['Swords Dance', 'Shadow Claw', 'Draco Meteor', 'Overheat', 'Judgement',
                                                  'Recover'],
                                'Earth Power': ['Ice Beam', 'Thunderbolt', 'Calm Mind', 'Swords Dance', 'Dragon Claw'],
                                'Ice Beam': ['Thunderbolt', 'Earth Power', 'Judgement', 'Calm Mind', 'Swords Dance'],
                                'Thunderbolt': ['Ice Beam', 'Surf', 'Judgement', 'Calm Mind', 'Swords Dance'],
                                'Dragon Claw': ['Earthquake', 'Shadow Claw', 'Swords Dance', 'Calm Mind', 'Ice Beam'],
                                'Substitute': ['Calm Mind', 'Swords Dance', 'Recover', 'Will-O-Wisp', 'Judgement'],
                                'Gravity': ['Thunder', 'Blizzard', 'Focus Blast', 'Earthquake', 'Judgement'],
                            }
                        ),

                        # MoveSet 2: "The Chaotic Gambler". No Protect, starts with Judgement into chaos.
                        pokemon_ddl.MoveSet(
                            ['Judgement'],
                            {
                                'Judgement': [
                                    'Extreme Speed', 'Draco Meteor', 'Outrage', 'Calm Mind', 'Swords Dance',
                                    'Gravity', 'Trick Room', 'Fire Blast', 'Thunder', 'Ice Beam', 'Earthquake',
                                    'Shadow Claw', 'Will-O-Wisp', 'Recover'
                                ],

                                'Draco Meteor': ['Extreme Speed', 'Overheat', 'Earthquake', 'Fire Blast', 'Steel Wing'],
                                'Outrage': ['Extreme Speed', 'Aqua Tail', 'Iron Head', 'Ice Beam', 'Giga Drain'],
                                'Calm Mind': ['Ice Beam', 'Thunder', 'Focus Blast', 'Shadow Claw', 'Recover',
                                              'Swords Dance'],
                                'Swords Dance': ['Extreme Speed', 'Shadow Claw', 'Dragon Claw', 'Giga Drain',
                                                 'Calm Mind'],
                                'Gravity': ['Thunder', 'Blizzard', 'Focus Blast', 'Draco Meteor', 'Judgement'],
                                'Trick Room': ['Judgement', 'Draco Meteor', 'Fire Blast', 'Thunder', 'Focus Blast'],
                                'Extreme Speed': ['Judgement', 'Swords Dance', 'Draco Meteor', 'Will-O-Wisp', 'Recover'],
                                'Fire Blast': ['Draco Meteor', 'Thunder', 'Ice Beam', 'Earthquake'],
                                'Earthquake': ['Stone Edge', 'Outrage', 'Dragon Claw', 'Flamethrower'],
                                'Recover': ['Judgement', 'Calm Mind', 'Swords Dance', 'Will-O-Wisp', 'Toxic']
                            }
                        ),

                        # MoveSet 3: "The Perish Trapper". A specific, high-risk alternate strategy.
                        pokemon_ddl.MoveSet(
                            ['Perish Song'],
                            {
                                'Mean Look': ['Protect', 'Recover', 'Judgement'],
                                'Perish Song': ['Mean Look']
                            }
                        )
                    ), baseStats=(120, 120, 120, 120, 120, 120), genders=('',), images=('493.gif', 'arceus-ice.png', 'arceus-ice (1).png'),
                    item_key='arcIce', stat_key='arcStat'
                )

        #Fighting type pokemon
        if 'Fighting':
            if 'Primeape':
                root.pokesets['Primeape'] = pokemon_ddl.PokemonSet(
                    name='Primeape', species='Primeape', abilities=('Vital Spirit', 'Anger Point'), pkTypes=('Fighting',),
                    sets=(
                        pokemon_ddl.MoveSet(
                          ['Protect', 'Endure'],
                            {
                                'Protect': ['U-turn', 'Encore', 'Close Combat'],
                                'U-turn': ['Close Combat', 'Punishment', 'Ice Punch', 'Stone Edge', 'Assurance', 'Endure', 'Rock Slide', 'Poison Jab'],
                                'Close Combat': ['Endure', 'Punishment', 'Toxic'],
                                'Endure': ['Endeavor', 'Reversal', 'Close Combat', 'U-turn']
                            }
                        ),
                    ), baseStats=(65, 105, 60, 60, 70, 95), genders=('M', 'F'), images=('057.gif', '057.png', '057 (1).png')
                )
            if 'Poliwrath':
                root.pokesets['Poliwrath'] = pokemon_ddl.PokemonSet(
                    name='Poliwrath', species='Poliwrath', abilities=('Water Absorb', 'Damp'),
                    pkTypes=('Water', 'Fighting'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Hypnosis', 'Vacuum Wave', 'Waterfall', 'Dynamic Punch'],
                                'Hypnosis': ['Double Team', 'Waterfall', 'Earthquake', 'Psychic', 'Substitute'],
                                'Psychic': ['Surf', 'Blizzard', 'Focus Blast', 'Hydro Pump', 'Mud Bomb'],
                                'Substitute': ['Focus Punch', 'Encore'],
                                'Waterfall': ['Brick Break', 'Toxic', 'Encore', 'Poison Jab', 'Hypnosis'],
                                'Dynamic Punch': ['Hypnosis', 'Substitute', 'Body Slam', 'Fling']
                            }
                        ),
                    ), baseStats=(90, 85, 95, 70, 90, 70), genders=('M', 'F'), images=('062.gif', '062.png', '062 (1).png')
                )
            if 'Machamp':
                root.pokesets['Machamp'] = pokemon_ddl.PokemonSet(
                    name='Machamp', species='Machamp', abilities=('Guts', 'No Guard'), pkTypes=('Fighting',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Facade', 'Bullet Punch', 'Dynamic Punch', 'Stone Edge', 'Scary Face'],
                                'Dynamic Punch': ['Earthquake', 'Payback', 'Ice Punch', 'Stone Edge', 'Bullet Punch', 'Facade', 'Mega Punch', 'Mega Kick', 'Smelling Salts', 'Wake-Up Slap'],
                                'Smelling Salts': ['Body Slam', 'Thunder Punch']
                            }
                        ),
                    ), baseStats=(90, 130, 80, 65, 85, 55), genders=('M', 'F'), images=('068.gif', '068.png', '068 (1).png')
                )
            if 'Hitmonlee':
                root.pokesets['Hitmonlee'] = pokemon_ddl.PokemonSet(
                    name='Hitmonlee', species='Hitmonlee', abilities=('Limber', 'Reckless'), pkTypes=('Fighting',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Endure'],
                            {
                                'Protect': ['Close Combat'],
                                'Close Combat': ['Stone Edge', 'Rock Slide'],
                                'Stone Edge': ['Earthquake', 'Blaze Kick', 'Bounce'],
                                'Rock Slide': ['Earthquake', 'Blaze Kick', 'Bullet Punch'],
                                'Earthquake': ['Mach Punch', 'Sucker Punch', 'Feint'],
                                'Blaze Kick': ['Mach Punch', 'Sucker Punch', 'Fling'],
                                'Endure': ['Reversal'],
                                'Reversal': ['Feint', 'Fling', 'Fake Out', 'Rolling Kick', 'Rock Slide', 'Rain Dance', 'Mud-Slap']
                            }
                        ),
                    ), baseStats=(50, 120, 53, 35, 110, 87), genders=('M',), images=('106.gif', '106.png', '106 (1).png')
                )
            if 'Hitmonchan':
                root.pokesets['Hitmonchan'] = pokemon_ddl.PokemonSet(
                    name='Hitmonchan', species='Hitmonchan', abilities=('Keen Eye', 'Iron Fist'), pkTypes=('Fighting',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Rapid Spin', 'Mach Punch', 'Fake Out', 'Sky Uppercut'],
                                'Rapid Spin': ['Drain Punch', 'Ice Punch', 'Bulk Up', 'Thunder Punch', 'Fire Punch', 'Bullet Punch', 'Fling', 'Mega Punch', 'Metronome'],
                                'Mach Punch': ['Drain Punch', 'Ice Punch', 'Bulk Up', 'Thunder Punch', 'Fire Punch', 'Bullet Punch', 'Focus Punch', 'Helping Hand']
                            }
                        ),
                    ), baseStats=(50, 105, 79, 35, 110, 76), genders=('M',), images=('107.gif', '107.png', '107 (1).png')
                )
            if 'Heracross':
                root.pokesets['Heracross'] = pokemon_ddl.PokemonSet(
                    name='Heracross', species='Heracross', abilities=('Swarm', 'Guts'), pkTypes=('Bug', 'Fighting'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Endure'],
                            {
                                'Protect': ['Megahorn', 'Pursuit'],
                                'Megahorn': ['Close Combat'],
                                'Close Combat': ['Stone Edge', 'Sleep Talk', 'Night Slash'],
                                'Pursuit': ['Megahorn', 'Swords Dance'],
                                'Swords Dance': ['Bug Bite', 'Headbutt', 'Horn Attack'],
                                'Endure': ['Reversal'],
                                'Reversal': ['Flail'],
                                'Flail': ['Megahorn', 'Close Combat', 'Aerial Ace', 'Bug Bite', 'Captivate', 'Dig']
                            }
                        ),
                    ), baseStats=(80, 125, 75, 40, 95, 85), genders=('M', 'F'), images=('214.gif', '214-m.png', '214-m (1).png')
                )
            if 'Hitmontop':
                root.pokesets['Hitmontop'] = pokemon_ddl.PokemonSet(
                    name='Hitmontop', species='Hitmontop', abilities=('Intimidate', 'Technician'),
                    pkTypes=('Fighting',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Detect', 'Toxic'],
                            {
                                'Detect': ['Fake Out', 'Sucker Punch', 'Feint', 'Agility', 'Close Combat', 'Gyro Ball', 'Thief'],
                                'Toxic': ['Fake Out', 'Sucker Punch', 'Feint', 'Bulk Up', 'Triple Kick', 'Quick Attack']
                            }
                        ),
                    ), baseStats=(50, 95, 95, 35, 110, 70), genders=('M',), images=('237.gif', '237.png', '237 (1).png')
                )
            if 'Blaziken':
                root.pokesets['Blaziken'] = pokemon_ddl.PokemonSet(
                    name='Blaziken', species='Blaziken', abilities=('Blaze',), pkTypes=('Fire', 'Fighting'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Endure'],
                            {
                                'Protect': ['Sunny Day', 'Superpower', 'Swords Dance', 'Agility'],
                                'Agility': ['Fire Blast', 'Baton Pass'],
                                'Sunny Day': ['Solar Beam', 'Blast Burn', 'Focus Blast'],
                                'Superpower': ['Fire Blast', 'Flare Blitz', 'Blast Burn'],
                                'Fire Blast': ['Hidden Power [Grass]', 'Hidden Power [Electric]', 'Vacuum Wave', 'Stone Edge', 'Hidden Power [Ice]'],
                                'Flare Blitz': ['Hidden Power [Grass]', 'Hidden Power [Electric]', 'Vacuum Wave', 'Stone Edge'],
                                'Blast Burn': ['Hidden Power [Grass]', 'Hidden Power [Electric]', 'Vacuum Wave', 'Stone Edge'],
                                'Swords Dance': ['Low Kick', 'Quick Attack', 'Brave Bird', 'Baton Pass'],
                                'Endure': ['Reversal'],
                                'Reversal': ['Blaze Kick'],
                                'Blaze Kick': ['Aerial Ace', 'Shadow Claw', 'Thunder Punch', 'Superpower', 'Night Slash']
                            }
                        ),
                    ), baseStats=(80, 120, 70, 110, 70, 80), genders=('M', 'F'), images=('257.gif', '257-m.png', '257-m (1).png')
                )
            if 'Breloom':
                root.pokesets['Breloom'] = pokemon_ddl.PokemonSet(
                    name='Breloom', species='Breloom', abilities=('Effect Spore', 'Poison Heal'),
                    pkTypes=('Grass', 'Fighting'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Drain Punch', 'Spore', 'Seed Bomb', 'Swords Dance', 'Facade'],
                                'Drain Punch': ['Giga Drain', 'Leech Seed', 'Synthesis', 'Spore', 'Facade'],
                                'Seed Bomb': ['Sky Uppercut', 'Rock Slide', 'Counter', 'Thunder Punch', 'Facade'],
                                'Spore': ['Facade', 'Sky Uppercut', 'Thunder Punch', 'Stone Edge', 'Focus Punch', 'Superpower', 'Force Palm', 'Facade'],
                                'Swords Dance': ['Force Palm', 'Facade', 'Mach Punch', 'Substitute', 'Seed Bomb', 'Iron Tail']
                            }
                        ),
                    ), baseStats=(60, 130, 80, 60, 60, 70), genders=('M', 'F'), images=('286.gif', '286.png', '286 (1).png')
                )
            if 'Hariyama':
                root.pokesets['Hariyama'] = pokemon_ddl.PokemonSet(
                    name='Hariyama', species='Hariyama', abilities=('Thick Fat', 'Guts'), pkTypes=('Fighting',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Detect', 'Detect', 'Detect', 'Whirlwind'],
                            {
                                'Detect': ['Belly Drum', 'Fake Out', 'Substitute', 'Cross Chop', 'Facade'],
                                'Belly Drum': ['Rock Slide'],
                                'Rock Slide': ['Cross Chop'],
                                'Whirlwind': ['Rest'],
                                'Rest': ['Sleep Talk'],
                                'Sleep Talk': ['Force Palm', 'Cross Chop'],
                                'Substitute': ['Focus Punch'],
                                'Focus Punch': ['Payback', 'Facade'],
                                'Payback': ['Ice Punch', 'Stone Edge', 'Facade'],
                                'Cross Chop': ['Payback', 'Bullet Punch', 'Poison Jab', 'Stone Edge', 'Earthquake', 'Facade']
                            }
                        ),
                    ), baseStats=(144, 120, 60, 40, 60, 50), genders=('M', 'F'), images=('297.gif', '297.png', '297 (1).png')
                )
            if 'Medicham':
                root.pokesets['Medicham'] = pokemon_ddl.PokemonSet(
                    name='Medicham', species='Medicham', abilities=('Pure Power',), pkTypes=('Fighting', 'Psychic'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Detect'],
                            {
                                'Detect': ['High Jump Kick', 'Fake Out', 'Drain Punch'],
                                'High Jump Kick': ['Ice Punch', 'Psycho Cut', 'Zen Headbutt'],
                                'Ice Punch': ['Zen Headbutt', 'Fake Out', 'Bullet Punch'],
                                'Zen Headbutt': ['Thunder Punch', 'Fake Out', 'Bullet Punch'],
                                'Psycho Cut': ['Trick', 'Reflect'],
                                'Drain Punch': ['Recover', 'Psycho Cut']
                            }
                        ),
                    ), baseStats=(60, 60, 75, 60, 75, 80), genders=('M', 'F'), images=('308.gif', '308-m.png', '308-m (1).png')
                )
            if 'Infernape':
                root.pokesets['Infernape'] = pokemon_ddl.PokemonSet(
                    name='Infernape', species='Infernape', abilities=('Blaze',), pkTypes=('Fire', 'Fighting'),
                    sets=(
                        pokemon_ddl.MoveSet(
                        ['Protect', 'Protect', 'Nasty Plot'],
                        {
                            'Protect': ['U-turn', 'Fire Blast', 'Overheat', 'Close Combat', 'Hidden Power [Ice]', 'Mach Punch', 'Slack Off', 'Flare Blitz', 'Taunt', 'Blaze Kick', 'Blast Burn', 'Stone Edge', 'Gunk Shot', 'Shadow Claw', 'Thunder Punch', 'Earthquake'],
                            'Nasty Plot': ['Grass Knot', 'Hidden Power [Ice]'],
                            'Grass Knot': ['Vacuum Wave', 'Close Combat'],
                            'Hidden Power [Ice]': ['Vacuum Wave', 'Close Combat'],
                            'Vacuum Wave': ['Protect'],
                            'Close Combat': ['Protect']
                        }
                    ),
                    ), baseStats=(76, 104, 71, 104, 71, 108), genders=('M', 'F'), images=('392.gif', '392.png', '392 (1).png')
                )
            if 'Lucario':
                root.pokesets['Lucario'] = pokemon_ddl.PokemonSet(
                    name='Lucario', species='Lucario', abilities=('Steadfast', 'Inner Focus'),
                    pkTypes=('Fighting', 'Steel'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Aura Sphere'],
                            {
                                'Aura Sphere': ['Protect'],
                                'Protect': ['Focus Blast', 'Aura Sphere', 'Bone Rush', 'Calm Mind', 'Close Combat', 'Crunch', 'Dark Pulse', 'Dig', 'Dragon Pulse', 'Double Team', 'Earthquake', 'Extreme Speed', 'Flash Cannon', 'Focus Blast', 'Ice Punch', 'Iron Tail', 'Poison Jab', 'Psychic', 'Shadow Claw', 'Shadow Ball', 'Sky Uppercut', 'Stone Edge', 'Water Pulse', 'Zen Headbutt']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Follow Me'],
                            {
                                'Protect': ['Swords Dance', 'Agility'],
                                'Swords Dance': ['Extreme Speed', 'Close Combat', 'Bullet Punch', 'Crunch', 'Ice Punch', 'Copycat'],
                                'Agility': ['Close Combat', 'Bullet Punch', 'Crunch', 'Ice Punch'],
                                'Follow Me': ['Helping Hand', 'Magnet Rise', 'Me First'],
                                'Helping Hand': ['Extreme Speed'],
                                'Magnet Rise': ['Extreme Speed'],
                                'Me First': ['Force Palm'],
                                'Force Palm': ['Protect'],
                                'Extreme Speed': ['Protect']
                            }
                        )
                    ), baseStats=(70, 110, 70, 115, 70, 90), genders=('M', 'F'), images=('448.gif', '448.png', '448 (1).png')
                )
            if 'Toxicroak':
                root.pokesets['Toxicroak'] = pokemon_ddl.PokemonSet(
                    name='Toxicroak', species='Toxicroak', abilities=('Anticipation', 'Dry Skin'),
                    pkTypes=('Poison', 'Fighting'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Swords Dance', 'Nasty Plot', 'Knock Off'],
                                'Knock Off': ['Gunk Shot', 'Cross Chop', 'Stone Edge', 'Gunk Shot', 'Rain Dance', 'Gunk Shot'],
                                'Swords Dance': ['Low Kick', 'Cross Chop', 'Sucker Punch'],
                                'Low Kick': ['Sucker Punch'],
                                'Sucker Punch': ['Ice Punch', 'Taunt'],
                                'Cross Chop': ['Sucker Punch'],
                                'Nasty Plot': ['Vacuum Wave', 'Sludge Bomb'],
                                'Vacuum Wave': ['Sludge Bomb', 'Dark Pulse'],
                                'Sludge Bomb': ['Dark Pulse', 'Focus Blast']
                            }
                        ),
                    ), baseStats=(83, 106, 65, 86, 65, 85), genders=('M', 'F'), images=('454.gif', '454-m.png', '454-m (1).png')
                )
            if 'Gallade':
                root.pokesets['Gallade'] = pokemon_ddl.PokemonSet(
                    name='Gallade', species='Gallade', abilities=('Steadfast',), pkTypes=('Psychic', 'Fighting'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Thunder Wave', 'Confuse Ray', 'Will-O-Wisp'],
                                'Thunder Wave': ['Taunt', 'Close Combat'],
                                'Taunt': ['Ice Punch', 'Destiny Bond'],
                                'Close Combat': ['Destiny Bond'],
                                'Confuse Ray': ['Taunt', 'Close Combat'],
                                'Will-O-Wisp': ['Taunt', 'Close Combat']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Psycho Cut', 'Night Slash', 'X-Scissor', 'Leaf Blade', 'Aerial Ace', 'Close Combat']
                            }
                        )
                    ), baseStats=(68, 125, 65, 65, 115, 80), genders=('M',), images=('475.gif', '475.png', '475 (1).png')
                )
            if 'Arceus-Fighting':
                root.pokesets['Arceus-Fighting'] = pokemon_ddl.PokemonSet(
                    name='Arceus-Fighting', species='Arceus', abilities=('Multitype',), pkTypes=('Fighting',),
                    sets=(
                        # MoveSet 1: "The Chaotic Bulwark". Guaranteed Protect + Judgement, then maximum variance.
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Judgement'],

                                # Judgement is the central hub for a chaotic web of possibilities.
                                'Judgement': [
                                    'Calm Mind', 'Swords Dance', 'Recover', 'Cosmic Power', 'Will-O-Wisp',
                                    'Thunder Wave', 'Extreme Speed', 'Earth Power', 'Ice Beam', 'Thunderbolt',
                                    'Flamethrower', 'Shadow Claw', 'Gravity', 'Substitute'
                                ],

                                # Every node below is heavily interconnected to create unpredictable sets.
                                'Calm Mind': ['Ice Beam', 'Thunderbolt', 'Earthquake', 'Shadow Claw', 'Recover',
                                              'Swords Dance', 'Will-O-Wisp'],
                                'Swords Dance': ['Extreme Speed', 'Dragon Claw', 'Shadow Claw', 'Earthquake', 'Surf',
                                                 'Ice Beam', 'Calm Mind'],
                                'Recover': ['Calm Mind', 'Will-O-Wisp', 'Ice Beam', 'Flamethrower', 'Substitute',
                                            'Swords Dance', 'Judgement'],
                                'Cosmic Power': ['Recover', 'Will-O-Wisp', 'Toxic', 'Flamethrower', 'Judgement'],
                                'Will-O-Wisp': ['Recover', 'Calm Mind', 'Extreme Speed', 'Dragon Claw'],
                                'Extreme Speed': ['Swords Dance', 'Shadow Claw', 'Draco Meteor', 'Overheat', 'Judgement',
                                                  'Recover'],
                                'Earth Power': ['Ice Beam', 'Thunderbolt', 'Calm Mind', 'Swords Dance', 'Dragon Claw'],
                                'Ice Beam': ['Thunderbolt', 'Earth Power', 'Judgement', 'Calm Mind', 'Swords Dance'],
                                'Thunderbolt': ['Ice Beam', 'Surf', 'Judgement', 'Calm Mind', 'Swords Dance'],
                                'Dragon Claw': ['Earthquake', 'Shadow Claw', 'Swords Dance', 'Calm Mind', 'Ice Beam'],
                                'Substitute': ['Calm Mind', 'Swords Dance', 'Recover', 'Will-O-Wisp', 'Judgement'],
                                'Gravity': ['Thunder', 'Blizzard', 'Focus Blast', 'Earthquake', 'Judgement'],
                            }
                        ),

                        # MoveSet 2: "The Chaotic Gambler". No Protect, starts with Judgement into chaos.
                        pokemon_ddl.MoveSet(
                            ['Judgement'],
                            {
                                'Judgement': [
                                    'Extreme Speed', 'Draco Meteor', 'Outrage', 'Calm Mind', 'Swords Dance',
                                    'Gravity', 'Trick Room', 'Fire Blast', 'Thunder', 'Ice Beam', 'Earthquake',
                                    'Shadow Claw', 'Will-O-Wisp', 'Recover'
                                ],

                                'Draco Meteor': ['Extreme Speed', 'Overheat', 'Earthquake', 'Fire Blast', 'Steel Wing'],
                                'Outrage': ['Extreme Speed', 'Aqua Tail', 'Iron Head', 'Ice Beam', 'Giga Drain'],
                                'Calm Mind': ['Ice Beam', 'Thunder', 'Focus Blast', 'Shadow Claw', 'Recover',
                                              'Swords Dance'],
                                'Swords Dance': ['Extreme Speed', 'Shadow Claw', 'Dragon Claw', 'Giga Drain',
                                                 'Calm Mind'],
                                'Gravity': ['Thunder', 'Blizzard', 'Focus Blast', 'Draco Meteor', 'Judgement'],
                                'Trick Room': ['Judgement', 'Draco Meteor', 'Fire Blast', 'Thunder', 'Focus Blast'],
                                'Extreme Speed': ['Judgement', 'Swords Dance', 'Draco Meteor', 'Will-O-Wisp', 'Recover'],
                                'Fire Blast': ['Draco Meteor', 'Thunder', 'Ice Beam', 'Earthquake'],
                                'Earthquake': ['Stone Edge', 'Outrage', 'Dragon Claw', 'Flamethrower'],
                                'Recover': ['Judgement', 'Calm Mind', 'Swords Dance', 'Will-O-Wisp', 'Toxic']
                            }
                        ),

                        # MoveSet 3: "The Perish Trapper". A specific, high-risk alternate strategy.
                        pokemon_ddl.MoveSet(
                            ['Perish Song'],
                            {
                                'Mean Look': ['Protect', 'Recover', 'Judgement'],
                                'Perish Song': ['Mean Look']
                            }
                        )
                    ), baseStats=(120, 120, 120, 120, 120, 120), genders=('',), images=('493.gif', 'arceus-fighting.png', 'arceus-fighting (1).png'),
                    item_key='arcFight', stat_key='arcStat'
                )

        # Dark type pokemon
        if 'Dark':
            if 'Umbreon':
                root.pokesets['Umbreon'] = pokemon_ddl.PokemonSet(
                    name='Umbreon', species='Umbreon', abilities=('Synchronize',), pkTypes=('Dark',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Moonlight'],
                            {
                                'Protect': ['Curse', 'Confuse Ray', 'Fake Tears', 'Last Resort', 'Mean Look', 'Wish'],
                                'Curse': ['Baton Pass'],
                                'Baton Pass': ['Payback', 'Wish'],
                                'Payback': ['Last Resort'],
                                'Last Resort': ['Dark Pulse'],
                                'Wish': ['Baton Pass'],
                                'Fake Tears': ['Dark Pulse'],
                                'Moonlight': ['Curse', 'Confuse Ray', 'Fake Tears', 'Last Resort', 'Mean Look', 'Nightmare', 'Swagger'],
                                'Nightmare': ['Dream Eater'],
                                'Mean Look': ['Toxic'],
                                'Swagger': ['Psych Up'],
                                'Psych Up': ['Feint Attack', 'Payback']
                            }
                        ),
                    ), baseStats=(95, 65, 110, 60, 130, 65), genders=('M', 'F'), images=('197.gif', '197.png', '197 (1).png')
                )
            if 'Houndoom':
                root.pokesets['Houndoom'] = pokemon_ddl.PokemonSet(
                    name='Houndoom', species='Houndoom', abilities=('Early Bird', 'Flash Fire'),
                    pkTypes=('Dark', 'Fire'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Nasty Plot', 'Sucker Punch', 'Punishment'],
                                'Nasty Plot': ['Dark Pulse'],
                                'Dark Pulse': ['Overheat', 'Fire Blast', 'Flamethrower', 'Hidden Power [Grass]'],
                                'Sucker Punch': ['Overheat', 'Pursuit', 'Beat Up', 'Toxic'],
                                'Punishment': ['Fire Blast', 'Flamethrower', 'Sunny Day', 'Sludge Bomb', 'Will-O-Wisp'],
                                'Sunny Day': ['Solar Beam']
                            }
                        ),
                    ), baseStats=(75, 90, 50, 110, 80, 95), genders=('M', 'F'), images=('229.gif', '229-m.png', '229-m (1).png')
                )
            if 'Tyranitar':
                root.pokesets['Tyranitar'] = pokemon_ddl.PokemonSet(
                    name='Tyranitar', species='Tyranitar', abilities=('Sand Stream',), pkTypes=('Rock', 'Dark'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Crunch', 'Fling', 'Curse', 'Ice Beam', 'Pursuit', 'Dragon Dance', 'Stealth Rock'],
                                'Curse': ['Payback', 'Avalanche'],
                                'Payback': ['Avalanche', 'Rock Slide', 'Stone Edge'],
                                'Avalanche': ['Payback', 'Rock Slide', 'Stone Edge'],
                                'Pursuit': ['Rock Slide', 'Stone Edge', 'Superpower', 'Low Kick', 'Crunch'],
                                'Crunch': ['Ice Fang', 'Fire Fang', 'Thunder Fang', 'Aerial Ace'],
                                'Dragon Dance': ['Superpower', 'Dragon Claw', 'Shadow Claw', 'Aqua Tail', 'Stone Edge', 'Crunch', 'Earthquake', 'Shock Wave', 'Dynamic Punch'],
                                'Ice Beam': ['Flamethrower', 'Focus Blast', 'Blizzard', 'Outrage', 'Roar', 'Thunderbolt', 'Surf'],
                                'Fling': ['Thrash']
                            }
                        ),
                    ), baseStats=(100, 134, 110, 95, 100, 61), genders=('M', 'F'), images=('248.gif', '248.png', '248 (1).png')
                )
            if 'Mightyena':
                root.pokesets['Mightyena'] = pokemon_ddl.PokemonSet(
                    name='Mightyena', species='Mightyena', abilities=('Intimidate', 'Quick Feet'),
                    pkTypes=('Dark',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Crunch', 'Sucker Punch', 'Taunt'],
                                'Crunch': ['Poison Fang', 'Thunder Fang', 'Ice Fang', 'Fire Fang', 'Super Fang'],
                                'Sucker Punch': ['Facade', 'Taunt'],
                                'Taunt': ['Uproar', 'Swagger', 'Substitute', 'Crunch', 'Sucker Punch', 'Embargo']
                            }
                        ),
                    ), baseStats=(70, 90, 70, 60, 60, 70), genders=('M', 'F'), images=('262.gif', '262.png', '262 (1).png')
                )
            if 'Shiftry':
                root.pokesets['Shiftry'] = pokemon_ddl.PokemonSet(
                    name='Shiftry', species='Shiftry', abilities=('Chlorophyll', 'Early Bird'),
                    pkTypes=('Grass', 'Dark'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Nasty Plot', 'Sunny Day', 'Fake Out', 'Swords Dance'],
                                'Sunny Day': ['Nasty Plot'],
                                'Nasty Plot': ['Leaf Storm', 'Dark Pulse', 'Energy Ball', 'Focus Blast'],
                                'Leaf Storm': ['Leaf Storm', 'Dark Pulse', 'Synthesis', 'Energy Ball', 'Focus Blast'],
                                'Dark Pulse': ['Leaf Storm', 'Dark Pulse', 'Synthesis', 'Energy Ball', 'Focus Blast'],
                                'Energy Ball': ['Leaf Storm', 'Dark Pulse', 'Synthesis', 'Energy Ball', 'Focus Blast'],
                                'Focus Blast': ['Leaf Storm', 'Dark Pulse', 'Synthesis', 'Energy Ball', 'Focus Blast'],
                                'Fake Out': ['Feint Attack', 'Explosion', 'Sucker Punch', 'X-Scissor'],
                                'Swords Dance': ['Seed Bomb', 'Sucker Punch']
                            }
                        ),
                    ), baseStats=(90, 100, 60, 90, 60, 80), genders=('M', 'F'), images=('275.gif', '275-m.png', '275-m (1).png')
                )
            if 'Sableye':
                root.pokesets['Sableye'] = pokemon_ddl.PokemonSet(
                    name='Sableye', species='Sableye', abilities=('Keen Eye', 'Stall'), pkTypes=('Dark', 'Ghost'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Recover', 'Protect', 'Gravity', 'Pain Split'],
                            {
                                'Recover': ['Will-O-Wisp', 'Toxic'],
                                'Protect': ['Will-O-Wisp', 'Toxic'],
                                'Will-O-Wisp': ['Seismic Toss', 'Night Shade'],
                                'Toxic': ['Seismic Toss', 'Night Shade'],
                                'Seismic Toss': ['Taunt', 'Knock Off'],
                                'Night Shade': ['Taunt', 'Knock Off'],
                                'Gravity': ['Protect', 'Recover', 'Helping Hand', 'Icy Wind'],
                                'Pain Split': ['Will-O-Wisp', 'Toxic', 'Recover']
                            }
                        ),
                    ), baseStats=(50, 75, 75, 65, 65, 50), genders=('M', 'F'), images=('302.gif', '302.png', '302 (1).png')
                )
            if 'Sharpedo':
                root.pokesets['Sharpedo'] = pokemon_ddl.PokemonSet(
                    name='Sharpedo', species='Sharpedo', abilities=('Rough Skin',), pkTypes=('Water', 'Dark'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                        {
                            'Protect': ['Hydro Pump', 'Crunch', 'Night Slash'],
                            'Hydro Pump': ['Dark Pulse', 'Ice Beam', 'Aqua Jet', 'Hidden Power [Grass]', 'Ancient Power'],
                            'Crunch': ['Waterfall', 'Taunt', 'Aqua Jet', 'Substitute'],
                            'Taunt': ['Earthquake', 'Ice Fang'],
                            'Substitute': ['Zen Headbutt'],
                            'Night Slash': ['Focus Energy'],
                            'Focus Energy': ['Waterfall', 'Earthquake', 'Ice Fang', 'Zen Headbutt']
                            }
                        ),
                    ), baseStats=(70, 120, 40, 95, 40, 95), genders=('M', 'F'), images=('319.gif', '319.png', '319 (1).png')
                )
            if 'Cacturne':
                root.pokesets['Cacturne'] = pokemon_ddl.PokemonSet(
                    name='Cacturne', species='Cacturne', abilities=('Sand Veil',), pkTypes=('Grass', 'Dark'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Spikes', 'Swords Dance'],
                                'Spikes': ['Energy Ball', 'Encore', 'Needle Arm', 'Sandstorm', 'Teeter Dance'],
                                'Encore': ['Sucker Punch'],
                                'Sucker Punch': ['Needle Arm', 'Seed Bomb'],
                                'Energy Ball': ['Dark Pulse', 'Leech Seed'],
                                'Dark Pulse': ['Synthesis', 'Substitute'],
                                'Swords Dance': ['Substitute', 'Needle Arm', 'Sucker Punch'],
                                'Substitute': ['Focus Punch', 'Low Kick'],
                                'Sandstorm': ['Double Team', 'Mud-Slap', 'Pin Missile']
                            }
                        ),
                    ), baseStats=(70, 115, 60, 115, 60, 55), genders=('M', 'F'), images=('332.gif', '332-m.png', '332-m (1).png')
                )
            if 'Crawdaunt':
                root.pokesets['Crawdaunt'] = pokemon_ddl.PokemonSet(
                    name='Crawdaunt', species='Crawdaunt', abilities=('Hyper Cutter', 'Shell Armor'),
                    pkTypes=('Water', 'Dark'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Dragon Dance', 'Swords Dance', 'Crabhammer'],
                                'Dragon Dance': ['Crunch', 'Crabhammer', 'Superpower', 'X-Scissor', 'Return', 'Frustration', 'Aerial Ace', 'Brick Break', 'Waterfall', 'Crabhammer'],
                                'Swords Dance': ['Crunch', 'Crabhammer', 'Superpower', 'X-Scissor', 'Return', 'Frustration', 'Aerial Ace', 'Brick Break', 'Waterfall', 'Crabhammer'],
                                'Crabhammer': ['Crunch', 'Guillotine', 'Superpower', 'X-Scissor', 'Return', 'Frustration', 'Aerial Ace', 'Brick Break', 'Hail']
                            }
                        ),
                    ), baseStats=(63, 120, 85, 90, 55, 55), genders=('M', 'F'), images=('342.gif', '342.png', '342 (1).png')
                )
            if 'Absol':
                root.pokesets['Absol'] = pokemon_ddl.PokemonSet(
                    name='Absol', species='Absol', abilities=('Pressure', 'Super Luck'), pkTypes=('Dark',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Detect'],
                            {
                                'Protect': ['Swords Dance'],
                                'Swords Dance': ['Psycho Cut', 'Night Slash'],
                                'Psycho Cut': ['Superpower', 'Sucker Punch', 'Pursuit', 'Taunt', 'Night Slash'],
                                'Night Slash': ['Superpower', 'Sucker Punch', 'Pursuit', 'Taunt', 'Psycho Cut'],
                                'Detect': ['Swagger', 'Megahorn', 'Perish Song', 'Quick Attack'],
                                'Perish Song': ['Mean Look'],
                                'Swagger': ['Punishment']
                            }
                        ),
                    ), baseStats=(65, 130, 60, 75, 60, 75), genders=('M', 'F'), images=('359.gif', '359.png', '359 (1).png'),
                    ability_weights=(0.2, 0.8)
                )
            if 'Honchkrow':
                root.pokesets['Honchkrow'] = pokemon_ddl.PokemonSet(
                    name='Honchkrow', species='Honchkrow', abilities=('Insomnia', 'Super Luck'),
                    pkTypes=('Dark', 'Flying'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Roost', 'Brave Bird', 'Heat Wave', 'Drill Peck', 'Haze', 'Mirror Move', 'Air Cutter'],
                                'Brave Bird': ['Sucker Punch', 'Night Slash', 'Dark Pulse'],
                                'Heat Wave': ['Air Cutter', 'Calm Mind'],
                                'Roost': ['Air Cutter']
                            }
                        ),
                    ), baseStats=(100, 125, 52, 105, 52, 71), genders=('M', 'F'), images=('430.gif', '430.png', '430 (1).png'), ability_weights=(0.2, 0.8)
                )
            if 'Skuntank':
                root.pokesets['Skuntank'] = pokemon_ddl.PokemonSet(
                    name='Skuntank', species='Skuntank', abilities=('Aftermath',),
                    pkTypes=('Poison', 'Dark'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Explosion'],
                                'Explosion': ['Crunch', 'Taunt', 'Pursuit'],
                                'Taunt': ['Crunch', 'Poison Gas', 'Return']
                            }
                        ),
                    ), baseStats=(103, 93, 67, 71, 61, 84), genders=('M', 'F'), images=('435.gif', '435.png', '435 (1).png')
                )
            if 'Spiritomb':
                root.pokesets['Spiritomb'] = pokemon_ddl.PokemonSet(
                    name='Spiritomb', species='Spiritomb', abilities=('Pressure',), pkTypes=('Ghost', 'Dark'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Rest'],
                            {
                                'Rest': ['Sleep Talk'],
                                'Sleep Talk': ['Calm Mind', 'Will-O-Wisp'],
                                'Calm Mind': ['Dark Pulse'],
                                'Will-O-Wisp': ['Dark Pulse', 'Shadow Ball'],
                                'Protect': ['Shadow Sneak'],
                                'Shadow Sneak': ['Hidden Power [Fighting]', 'Trick', 'Sucker Punch', 'Will-O-Wisp']
                            }
                        ),
                    ), baseStats=(50, 92, 108, 92, 108, 35), genders=('',), images=('442.gif', '442.png', '442 (1).png')
                )
            if 'Drapion':
                root.pokesets['Drapion'] = pokemon_ddl.PokemonSet(
                    name='Drapion', species='Drapion', abilities=('Battle Armor', 'Sniper'),
                    pkTypes=('Poison', 'Dark'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Acupressure'],
                            {
                                'Protect': ['Toxic Spikes', 'Night Slash', 'Swords Dance'],
                                'Toxic Spikes': ['Whirlwind'],
                                'Whirlwind': ['Knock Off', 'Rest', 'Taunt', 'Crunch'],
                                'Night Slash': ['Cross Poison'],
                                'Cross Poison': ['Slash', 'Aqua Tail', 'Earthquake'],
                                'Swords Dance': ['Night Slash', 'Cross Poison', 'Pursuit', 'Earthquake', 'Aqua Tail', 'Ice Fang'],
                                'Acupressure': ['Rest', 'Sleep Talk', 'Crunch']
                            }
                        ),
                    ), baseStats=(70, 90, 110, 60, 75, 95), genders=('M', 'F'), ability_weights=(0.2, 0.8), images=('452.gif', '452.png', '452 (1).png')
                )
            if 'Darkrai':
                root.pokesets['Darkrai'] = pokemon_ddl.PokemonSet(
                    name='Darkrai', species='Darkrai', abilities=('Bad Dreams',), pkTypes=('Dark',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Dark Void'],
                            {
                                'Dark Void': ['Dream Eater'],
                                'Dream Eater': ['Nightmare'],
                                'Nightmare': ['Ominous Wind', 'Knock Off', 'Last Resort', 'Rain Dance', 'Sunny Day', 'Taunt', 'Hidden Power [Dragon]', 'Embargo', 'Disable', 'Night Shade']
                            }
                        ),
                    ), baseStats=(70, 90, 90, 135, 90, 125), genders=('',), images=('491.gif', '491.png', '491 (1).png')
                )
            if 'Arceus-Dark':
                root.pokesets['Arceus-Dark'] = pokemon_ddl.PokemonSet(
                    name='Arceus-Dark', species='Arceus', abilities=('Multitype',), pkTypes=('Dark',),
                    sets=(
                        # MoveSet 1: "The Chaotic Bulwark". Guaranteed Protect + Judgement, then maximum variance.
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Judgement'],

                                # Judgement is the central hub for a chaotic web of possibilities.
                                'Judgement': [
                                    'Calm Mind', 'Swords Dance', 'Recover', 'Cosmic Power', 'Will-O-Wisp',
                                    'Thunder Wave', 'Extreme Speed', 'Earth Power', 'Ice Beam', 'Thunderbolt',
                                    'Flamethrower', 'Shadow Claw', 'Gravity', 'Substitute'
                                ],

                                # Every node below is heavily interconnected to create unpredictable sets.
                                'Calm Mind': ['Ice Beam', 'Thunderbolt', 'Earthquake', 'Shadow Claw', 'Recover',
                                              'Swords Dance', 'Will-O-Wisp'],
                                'Swords Dance': ['Extreme Speed', 'Dragon Claw', 'Shadow Claw', 'Earthquake', 'Surf',
                                                 'Ice Beam', 'Calm Mind'],
                                'Recover': ['Calm Mind', 'Will-O-Wisp', 'Ice Beam', 'Flamethrower', 'Substitute',
                                            'Swords Dance', 'Judgement'],
                                'Cosmic Power': ['Recover', 'Will-O-Wisp', 'Toxic', 'Flamethrower', 'Judgement'],
                                'Will-O-Wisp': ['Recover', 'Calm Mind', 'Extreme Speed', 'Dragon Claw'],
                                'Extreme Speed': ['Swords Dance', 'Shadow Claw', 'Draco Meteor', 'Overheat', 'Judgement',
                                                  'Recover'],
                                'Earth Power': ['Ice Beam', 'Thunderbolt', 'Calm Mind', 'Swords Dance', 'Dragon Claw'],
                                'Ice Beam': ['Thunderbolt', 'Earth Power', 'Judgement', 'Calm Mind', 'Swords Dance'],
                                'Thunderbolt': ['Ice Beam', 'Surf', 'Judgement', 'Calm Mind', 'Swords Dance'],
                                'Dragon Claw': ['Earthquake', 'Shadow Claw', 'Swords Dance', 'Calm Mind', 'Ice Beam'],
                                'Substitute': ['Calm Mind', 'Swords Dance', 'Recover', 'Will-O-Wisp', 'Judgement'],
                                'Gravity': ['Thunder', 'Blizzard', 'Focus Blast', 'Earthquake', 'Judgement'],
                            }
                        ),

                        # MoveSet 2: "The Chaotic Gambler". No Protect, starts with Judgement into chaos.
                        pokemon_ddl.MoveSet(
                            ['Judgement'],
                            {
                                'Judgement': [
                                    'Extreme Speed', 'Draco Meteor', 'Outrage', 'Calm Mind', 'Swords Dance',
                                    'Gravity', 'Trick Room', 'Fire Blast', 'Thunder', 'Ice Beam', 'Earthquake',
                                    'Shadow Claw', 'Will-O-Wisp', 'Recover'
                                ],

                                'Draco Meteor': ['Extreme Speed', 'Overheat', 'Earthquake', 'Fire Blast', 'Steel Wing'],
                                'Outrage': ['Extreme Speed', 'Aqua Tail', 'Iron Head', 'Ice Beam', 'Giga Drain'],
                                'Calm Mind': ['Ice Beam', 'Thunder', 'Focus Blast', 'Shadow Claw', 'Recover',
                                              'Swords Dance'],
                                'Swords Dance': ['Extreme Speed', 'Shadow Claw', 'Dragon Claw', 'Giga Drain',
                                                 'Calm Mind'],
                                'Gravity': ['Thunder', 'Blizzard', 'Focus Blast', 'Draco Meteor', 'Judgement'],
                                'Trick Room': ['Judgement', 'Draco Meteor', 'Fire Blast', 'Thunder', 'Focus Blast'],
                                'Extreme Speed': ['Judgement', 'Swords Dance', 'Draco Meteor', 'Will-O-Wisp', 'Recover'],
                                'Fire Blast': ['Draco Meteor', 'Thunder', 'Ice Beam', 'Earthquake'],
                                'Earthquake': ['Stone Edge', 'Outrage', 'Dragon Claw', 'Flamethrower'],
                                'Recover': ['Judgement', 'Calm Mind', 'Swords Dance', 'Will-O-Wisp', 'Toxic']
                            }
                        ),

                        # MoveSet 3: "The Perish Trapper". A specific, high-risk alternate strategy.
                        pokemon_ddl.MoveSet(
                            ['Perish Song'],
                            {
                                'Mean Look': ['Protect', 'Recover', 'Judgement'],
                                'Perish Song': ['Mean Look']
                            }
                        )
                    ), baseStats=(120, 120, 120, 120, 120, 120), genders=('',), images=('493.gif', 'arceus-dark.png', 'arceus-dark (1).png'),
                    item_key='arcDark', stat_key='arcStat'
                )

        # Fire type pokemon
        if 'Fire':
            if 'Charizard':
                root.pokesets['Charizard'] = pokemon_ddl.PokemonSet(
                    name='Charizard', species='Charizard', abilities=('Blaze',), pkTypes=('Fire', 'Flying'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Roost', 'Substitute'],
                            {
                                'Protect': ['Air Slash', 'Focus Blast'],
                                'Air Slash': ['Fire Blast', 'Blast Burn', 'Hidden Power [Grass]'],
                                'Roost': ['Ancient Power', 'Air Slash', 'Flamethrower'],
                                'Substitute': ['Air Slash', 'Swords Dance', 'Sunny Day'],
                                'Swords Dance': ['Earthquake', 'Flare Blitz'],
                                'Flare Blitz': ['Thunder Punch'],
                                'Sunny Day': ['Solar Beam', 'Flamethrower']
                            }
                        ),
                    ), baseStats=(78, 84, 78, 109, 85, 100), genders=('M', 'F'), images=('006.gif', '006.png', '006 (1).png')
                )
            if 'Ninetales':
                root.pokesets['Ninetales'] = pokemon_ddl.PokemonSet(
                    name='Ninetales', species='Ninetales', abilities=('Flash Fire',), pkTypes=('Fire',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Energy Ball', 'Pain Split', 'Confuse Ray', 'Sunny Day'],
                                'Pain Split': ['Fire Blast', 'Overheat'],
                                'Fire Blast': ['Will-O-Wisp'],
                                'Overheat': ['Will-O-Wisp'],
                                'Energy Ball': ['Fire Blast', 'Overheat', 'Hypnosis', 'Hidden Power [Rock]', 'Nasty Plot'],
                                'Hidden Power [Rock]': ['Extrasensory'],
                                'Nasty Plot': ['Hidden Power [Rock]', 'Fire Blast', 'Flamethrower'],
                                'Sunny Day': ['Solar Beam', 'Energy Ball'],
                                'Solar Beam': ['Fire Blast', 'Overheat', 'Hidden Power [Rock]'],
                                'Confuse Ray': ['Pain Split']
                            }
                        ),
                    ), baseStats=(73, 76, 75, 81, 100, 100), genders=('M', 'F'), images=('038.gif', '038.png', '038 (1).png')
                )
            if 'Arcanine':
                root.pokesets['Arcanine'] = pokemon_ddl.PokemonSet(
                    name='Arcanine', species='Arcanine', abilities=('Intimidate', 'Flash Fire'), pkTypes=('Fire',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Morning Sun'],
                            {
                                'Protect': ['Extreme Speed'],
                                'Morning Sun': ['Sunny Day'],
                                'Sunny Day': ['Flare Blitz', 'Solar Beam'],
                                'Flare Blitz': ['Extreme Speed', 'Thunder Fang', 'Hidden Power [Grass]'],
                                'Solar Beam': ['Fire Blast', 'Flamethrower', 'Dragon Pulse'],
                                'Extreme Speed': ['Flare Blitz', 'Toxic', 'Will-O-Wisp'],
                                'Toxic': ['Flare Blitz', 'Rest'],
                                'Will-O-Wisp': ['Roar', 'Flare Blitz']
                            }
                        ),
                    ), baseStats=(90, 110, 80, 100, 80, 95), genders=('M', 'F'), ability_weights=(0.8, 0.2), images=('059.gif', '059.png', '059 (1).png')
                )
            if 'Rapidash':
                root.pokesets['Rapidash'] = pokemon_ddl.PokemonSet(
                    name='Rapidash', species='Rapidash', abilities=('Flash Fire',), pkTypes=('Fire',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Substitute', 'Protect'],
                            {
                                'Protect': ['Megahorn', 'Bounce'],
                                'Megahorn': ['Horn Drill', 'Hypnosis', 'Flare Blitz', 'Iron Tail', 'Double-Edge'],
                                'Substitute': ['Baton Pass'],
                                'Baton Pass': ['Agility'],
                                'Agility': ['Flare Blitz'],
                                'Bounce': ['Double Kick', 'Megahorn', 'Stomp', 'Quick Attack']
                            }
                        ),
                    ), baseStats=(65, 100, 70, 80, 80, 105), genders=('M', 'F'), images=('078.gif', '078.png', '078 (1).png')
                )
            if 'Flareon':
                root.pokesets['Flareon'] = pokemon_ddl.PokemonSet(
                    name='Flareon', species='Flareon', abilities=('Flash Fire',), pkTypes=('Fire',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Wish', 'Superpower', 'Last Resort'],
                                'Wish': ['Toxic'],
                                'Toxic': ['Flamethrower', 'Lava Plume'],
                                'Superpower': ['Return'],
                                'Return': ['Fire Blast', 'Hidden Power [Grass]'],
                                'Last Resort': ['Curse', 'Fire Fang', 'Bite'],
                                'Curse': ['Quick Attack']
                            }
                        ),
                    ), baseStats=(65, 130, 60, 95, 110, 65), genders=('M', 'F'), images=('136.gif', '136.png', '136 (1).png')
                )
            if 'Moltres':
                root.pokesets['Moltres'] = pokemon_ddl.PokemonSet(
                    name='Moltres', species='Moltres', abilities=('Pressure',), pkTypes=('Fire', 'Flying'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Roost', 'Sunny Day'],
                            {
                                'Roost': ['Ancient Power', 'Fire Blast', 'Flamethrower', 'Air Slash'],
                                'Protect': ['Sky Attack', 'Steel Wing', 'U-turn', 'Fire Blast'],
                                'Fire Blast': ['Hidden Power [Grass]', 'Hidden Power [Ice]'],
                                'Sunny Day': ['Morning Sun', 'Flamethrower', 'Solar Beam']
                            }
                        ),
                    ), baseStats=(90, 100, 90, 125, 85, 90), genders=('',), images=('146.gif', '146.png', '146 (1).png')
                )
            if 'Typhlosion':
                root.pokesets['Typhlosion'] = pokemon_ddl.PokemonSet(
                    name='Typhlosion', species='Typhlosion', abilities=('Blaze',), pkTypes=('Fire',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Eruption', 'Shadow Claw'],
                                'Eruption': ['Focus Blast'],
                                'Focus Blast': ['Flamethrower', 'Fire Blast', 'Hidden Power [Grass]', 'Hidden Power [Rock]'],
                                'Shadow Claw': ['Blast Burn', 'Earthquake', 'Aerial Ace', 'Overheat', 'Solar Beam', 'Focus Blast']
                            }
                        ),
                    ), baseStats=(78, 84, 78, 109, 85, 100), genders=('M', 'F'), images=('157.gif', '157.png', '157 (1).png')
                )
            if 'Magcargo':
                root.pokesets['Magcargo'] = pokemon_ddl.PokemonSet(
                    name='Magcargo', species='Magcargo', abilities=('Magma Armor', 'Flame Body'),
                    pkTypes=('Fire', 'Rock'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Stealth Rock'],
                                'Stealth Rock': ['Lava Plume', 'Recover', 'Memento'],
                                'Recover': ['Toxic'],
                                'Memento': ['Will-O-Wisp', 'Gyro Ball', 'Explosion']
                            }
                        ),
                    ), baseStats=(50, 50, 120, 80, 80, 30), genders=('M', 'F'), images=('219.gif', '219.png', '219 (1).png'),
                    ability_weights=(0.2, 0.8)
                )
            if 'Entei':
                root.pokesets['Entei'] = pokemon_ddl.PokemonSet(
                    name='Entei', species='Entei', abilities=('Pressure',), pkTypes=('Fire',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Extreme Speed', 'Eruption', 'Reflect'],
                                'Extreme Speed': ['Stone Edge', 'Flare Blitz', 'Crush Claw'],
                                'Eruption': ['Calm Mind', 'Hidden Power [Grass]', 'Extrasensory', 'Shadow Ball'],
                                'Reflect': ['Rain Dance', 'Sandstorm'],
                                'Rain Dance': ['Toxic', 'Will-O-Wisp'],
                                'Sandstorm': ['Toxic', 'Will-O-Wisp', 'Flamethrower', 'Lava Plume']
                            }
                        ),
                    ), baseStats=(115, 115, 85, 90, 75, 100), genders=('',), images=('244.gif', '244.png', '244 (1).png')
                )
            if 'Ho-oh':
                root.pokesets['Ho-oh'] = pokemon_ddl.PokemonSet(
                    name='Ho-oh', species='Ho-oh', abilities=('Pressure',), pkTypes=('Fire', 'Flying'),
                    sets=(
                        pokemon_ddl.MoveSet(['Sacred Fire'],
                        {
                            'Sacred Fire': ['Whirlwind', 'Safeguard', 'Recover', 'Natural Gift', 'Punishment', 'Sky Attack', 'Weather Ball', 'Earthquake', 'Frustration',
                                            'Rain Dance', 'Sandstorm', 'Secret Power', 'Steel Wing', 'Giga Impact', 'Thunder Wave', 'Pluck', 'Brave Bird', 'Fly', 'Rock Smash',
                                            'Zen Headbutt', 'Gust', 'Swift', 'Ancient Power', 'Future Sight', 'Calm Mind', 'Roar', 'Hyper Beam', 'Light Screen', 'Giga Drain', 'Thunderbolt', 'Thunder',
                                            'Psychic', 'Shadow Ball', 'Double Team', 'Reflect', 'Charge Beam', 'Endure', 'Flash', 'Dream Eater', 'Defog', 'Ominous Wind',
                                            'Snore', 'Earth Power', 'Heat Wave', 'Iron Head', 'Signal Beam', 'Twister', 'Hidden Power [Dragon]', 'Hidden Power [Fighting]', 'Tailwind',
                                            'Sky Attack', 'Sky Attack', 'Sky Attack', 'Protect', 'Recover', 'Recover']
                        }),

                    ), baseStats=(106, 130, 90, 110, 154, 90), genders=('',), images=('250.gif', '250.png', '250 (1).png')
                )
            if 'Camerupt':
                root.pokesets['Camerupt'] = pokemon_ddl.PokemonSet(
                    name='Camerupt', species='Camerupt', abilities=('Magma Armor', 'Solid Rock'),
                    pkTypes=('Fire', 'Ground'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Stealth Rock', 'Eruption'],
                                'Stealth Rock': ['Lava Plume', 'Explosion', 'Earthquake'],
                                'Eruption': ['Earthquake', 'Earth Power', 'Stockpile', 'Rock Polish'],
                                'Earthquake': ['Flash Cannon', 'Rollout', 'Yawn', 'Stone Edge', 'Rock Slide'],
                                'Stockpile': ['Swallow', 'Spit Up'],
                                'Earth Power': ['Flash Cannon', 'Rollout', 'Yawn', 'Stone Edge', 'Rock Slide'],
                                'Rock Polish': ['Earthquake', 'Earth Power']
                            }
                        ),
                    ), baseStats=(70, 100, 70, 105, 75, 40), genders=('M', 'F'), images=('323.gif', '323-m.png', '323-m (1).png'),
                    ability_weights=(0.2, 0.8)
                )
            if 'Torkoal':
                root.pokesets['Torkoal'] = pokemon_ddl.PokemonSet(
                    name='Torkoal', species='Torkoal', abilities=('White Smoke',), pkTypes=('Fire',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Curse', 'Stealth Rock'],
                                'Stealth Rock': ['Lava Plume', 'Flamethrower', 'Yawn'],
                                'Lava Plume': ['Rapid Spin', 'Explosion'],
                                'Flamethrower': ['Rapid Spin', 'Toxic', 'Explosion'],
                                'Yawn': ['Rapid Spin', 'Explosion'],
                                'Curse': ['Gyro Ball', 'Body Slam']
                            }
                        ),
                    ), baseStats=(70, 85, 140, 85, 70, 20), genders=('M', 'F'), images=('324.gif', '324.png', '324 (1).png')
                )
            if 'Magmortar':
                root.pokesets['Magmortar'] = pokemon_ddl.PokemonSet(
                    name='Magmortar', species='Magmortar', abilities=('Flame Body',), pkTypes=('Fire',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Fire Blast', 'Follow Me'],
                                'Fire Blast': ['Thunderbolt'],
                                'Thunderbolt': ['Hidden Power [Grass]'],
                                'Hidden Power [Grass]': ['Flamethrower', 'Focus Blast', 'Overheat'],
                                'Follow Me': ['Heat Wave', 'Smog', 'Rock Tomb']
                            }
                        ),
                    ), baseStats=(75, 95, 67, 125, 95, 83), genders=('M', 'F'), images=('467.gif', '467.png', '467 (1).png')
                )
            if 'Heatran':
                root.pokesets['Heatran'] = pokemon_ddl.PokemonSet(
                    name='Heatran', species='Heatran', abilities=('Flash Fire',), pkTypes=('Fire', 'Steel'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Magma Storm', 'Eruption'],
                                'Magma Storm': ['Toxic', 'Stealth Rock', 'Will-O-Wisp', 'Substitute'],
                                'Toxic': ['Explosion', 'Dragon Pulse', 'Hidden Power [Grass]', 'Taunt', 'Earth Power'],
                                'Will-O-Wisp': ['Explosion', 'Dragon Pulse', 'Hidden Power [Grass]', 'Taunt', 'Earth Power'],
                                'Stealth Rock': ['Explosion', 'Dragon Pulse', 'Hidden Power [Grass]', 'Taunt', 'Earth Power', 'Roar'],
                                'Substitute': ['Toxic', 'Torment'],
                                'Earth Power': ['Hidden Power [Ice]', 'Hidden Power [Electric]', 'Stealth Rock', 'Explosion', 'Flamethrower', 'Fire Blast'],
                                'Torment': ['Roar', 'Lava Plume', 'Bug Bite'],
                                'Eruption': ['Dragon Pulse', 'Dark Pulse', 'Earth Power', 'Flash Cannon', 'Uproar']
                             }
                        ),
                    ), baseStats=(91, 90, 106, 130, 106, 77), genders=('M', 'F'), images=('485.gif', '485.png', '485 (1).png')
                )
            if 'Arceus-Fire':
                root.pokesets['Arceus-Fire'] = pokemon_ddl.PokemonSet(
                    name='Arceus-Fire', species='Arceus', abilities=('Multitype',), pkTypes=('Fire',),
                    sets=(
                        # MoveSet 1: "The Chaotic Bulwark". Guaranteed Protect + Judgement, then maximum variance.
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Judgement'],

                                # Judgement is the central hub for a chaotic web of possibilities.
                                'Judgement': [
                                    'Calm Mind', 'Swords Dance', 'Recover', 'Cosmic Power', 'Will-O-Wisp',
                                    'Thunder Wave', 'Extreme Speed', 'Earth Power', 'Ice Beam', 'Thunderbolt',
                                    'Flamethrower', 'Shadow Claw', 'Gravity', 'Substitute'
                                ],

                                # Every node below is heavily interconnected to create unpredictable sets.
                                'Calm Mind': ['Ice Beam', 'Thunderbolt', 'Earthquake', 'Shadow Claw', 'Recover',
                                              'Swords Dance', 'Will-O-Wisp'],
                                'Swords Dance': ['Extreme Speed', 'Dragon Claw', 'Shadow Claw', 'Earthquake', 'Surf',
                                                 'Ice Beam', 'Calm Mind'],
                                'Recover': ['Calm Mind', 'Will-O-Wisp', 'Ice Beam', 'Flamethrower', 'Substitute',
                                            'Swords Dance', 'Judgement'],
                                'Cosmic Power': ['Recover', 'Will-O-Wisp', 'Toxic', 'Flamethrower', 'Judgement'],
                                'Will-O-Wisp': ['Recover', 'Calm Mind', 'Extreme Speed', 'Dragon Claw'],
                                'Extreme Speed': ['Swords Dance', 'Shadow Claw', 'Draco Meteor', 'Overheat', 'Judgement',
                                                  'Recover'],
                                'Earth Power': ['Ice Beam', 'Thunderbolt', 'Calm Mind', 'Swords Dance', 'Dragon Claw'],
                                'Ice Beam': ['Thunderbolt', 'Earth Power', 'Judgement', 'Calm Mind', 'Swords Dance'],
                                'Thunderbolt': ['Ice Beam', 'Surf', 'Judgement', 'Calm Mind', 'Swords Dance'],
                                'Dragon Claw': ['Earthquake', 'Shadow Claw', 'Swords Dance', 'Calm Mind', 'Ice Beam'],
                                'Substitute': ['Calm Mind', 'Swords Dance', 'Recover', 'Will-O-Wisp', 'Judgement'],
                                'Gravity': ['Thunder', 'Blizzard', 'Focus Blast', 'Earthquake', 'Judgement'],
                            }
                        ),

                        # MoveSet 2: "The Chaotic Gambler". No Protect, starts with Judgement into chaos.
                        pokemon_ddl.MoveSet(
                            ['Judgement'],
                            {
                                'Judgement': [
                                    'Extreme Speed', 'Draco Meteor', 'Outrage', 'Calm Mind', 'Swords Dance',
                                    'Gravity', 'Trick Room', 'Fire Blast', 'Thunder', 'Ice Beam', 'Earthquake',
                                    'Shadow Claw', 'Will-O-Wisp', 'Recover'
                                ],

                                'Draco Meteor': ['Extreme Speed', 'Overheat', 'Earthquake', 'Fire Blast', 'Steel Wing'],
                                'Outrage': ['Extreme Speed', 'Aqua Tail', 'Iron Head', 'Ice Beam', 'Giga Drain'],
                                'Calm Mind': ['Ice Beam', 'Thunder', 'Focus Blast', 'Shadow Claw', 'Recover',
                                              'Swords Dance'],
                                'Swords Dance': ['Extreme Speed', 'Shadow Claw', 'Dragon Claw', 'Giga Drain',
                                                 'Calm Mind'],
                                'Gravity': ['Thunder', 'Blizzard', 'Focus Blast', 'Draco Meteor', 'Judgement'],
                                'Trick Room': ['Judgement', 'Draco Meteor', 'Fire Blast', 'Thunder', 'Focus Blast'],
                                'Extreme Speed': ['Judgement', 'Swords Dance', 'Draco Meteor', 'Will-O-Wisp', 'Recover'],
                                'Fire Blast': ['Draco Meteor', 'Thunder', 'Ice Beam', 'Earthquake'],
                                'Earthquake': ['Stone Edge', 'Outrage', 'Dragon Claw', 'Flamethrower'],
                                'Recover': ['Judgement', 'Calm Mind', 'Swords Dance', 'Will-O-Wisp', 'Toxic']
                            }
                        ),

                        # MoveSet 3: "The Perish Trapper". A specific, high-risk alternate strategy.
                        pokemon_ddl.MoveSet(
                            ['Perish Song'],
                            {
                                'Mean Look': ['Protect', 'Recover', 'Judgement'],
                                'Perish Song': ['Mean Look']
                            }
                        )
                    ), baseStats=(120, 120, 120, 120, 120, 120), genders=('',), images=('493.gif', 'arceus-fire.png', 'arceus-fire (1).png'),
                    item_key='arcFire', stat_key='arcStat'
                )

        # Ghost type pokemon
        if 'Ghost':
            if 'Gengar':
                root.pokesets['Gengar'] = pokemon_ddl.PokemonSet(
                    name='Gengar', species='Gengar', abilities=('Levitate',), pkTypes=('Ghost', 'Poison'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Protect', 'Substitute'],
                            {
                                'Protect': ['Encore', 'Shadow Ball'],
                                'Encore': ['Disable'],
                                'Disable': ['Shadow Ball', 'Sludge Bomb'],
                                'Shadow Ball': ['Focus Blast', 'Thunderbolt', 'Confuse Ray', 'Destiny Bond'],
                                'Focus Blast': ['Taunt', 'Will-O-Wisp', 'Explosion'],
                                'Substitute': ['Pain Split', 'Trick'],
                                'Pain Split': ['Shadow Ball', 'Hypnosis'],
                                'Thunderbolt': ['Taunt', 'Hidden Power [Fire]', 'Explosion'],
                                'Confuse Ray': ['Icy Wind', 'Knock Off', 'Metronome'],
                                'Hypnosis': ['Dream Eater']
                            }
                        ),
                    ), baseStats=(60, 65, 60, 130, 75, 110), genders=('M', 'F'), images=('094.gif', '094.png', '094 (1).png')
                )
            if 'Shedinja':
                root.pokesets['Shedinja'] = pokemon_ddl.PokemonSet(
                    name='Shedinja', species='Shedinja', abilities=('Wonder Guard',), pkTypes=('Bug', 'Ghost'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Swords Dance'],
                            {
                                'Protect': ['Swords Dance'],
                                'Swords Dance': ['Shadow Sneak', 'Sucker Punch'],
                                'Shadow Sneak': ['X-Scissor'],
                                'Sucker Punch': ['X-Scissor', 'Shadow Sneak'],
                                'X-Scissor': ['Aerial Ace', 'Will-O-Wisp', 'Dig', 'Metal Claw', 'Mimic']
                            }
                        ),
                    ), baseStats=(1, 90, 45, 30, 30, 40), genders=('',), images=('292.gif', '292.png', '292 (1).png'),
                    stat_key='shedStat'
                )
            if 'Banette':
                root.pokesets['Banette'] = pokemon_ddl.PokemonSet(
                    name='Banette', species='Banette', abilities=('Insomnia', 'Frisk'), pkTypes=('Ghost',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Trick Room'],
                                'Trick Room': ['Shadow Claw', 'Destiny Bond'],
                                'Shadow Claw': ['Hidden Power [Fighting]', 'Sucker Punch', 'Shadow Sneak', 'Thunder Wave', 'Destiny Bond'],
                                'Destiny Bond': ['Taunt', 'Trick']
                            }
                        ),
                    ), baseStats=(64, 115, 65, 83, 63, 65), genders=('M', 'F'), images=('354.gif', '354.png', '354 (1).png')
                )
            if 'Drifblim':
                root.pokesets['Drifblim'] = pokemon_ddl.PokemonSet(
                    name='Drifblim', species='Drifblim', abilities=('Aftermath', 'Unburden'),
                    pkTypes=('Ghost', 'Flying'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Trick', 'Hypnosis', 'Calm Mind', 'Rain Dance', 'Stockpile'],
                                'Trick': ['Shadow Ball'],
                                'Shadow Ball': ['Thunderbolt', 'Hidden Power [Fighting]', 'Explosion'],
                                'Rain Dance': ['Thunder', 'Weather Ball'],
                                'Thunder': ['Explosion', 'Shadow Ball'],
                                'Weather Ball': ['Explosion', 'Shadow Ball'],
                                'Calm Mind': ['Shadow Ball'],
                                'Hypnosis': ['Shadow Ball'],
                                'Stockpile': ['Baton Pass'],
                                'Baton Pass': ['Shadow Ball', 'Swallow']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Substitute'],
                            {
                                'Substitute': ['Calm Mind', 'Stockpile'],
                                'Calm Mind': ['Baton Pass'],
                                'Stockpile': ['Baton Pass'],
                                'Baton Pass': ['Shadow Ball', 'Hypnosis', 'Recycle', 'Explosion']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                        ['Rest'],
                            {
                                'Rest': ['Calm Mind'],
                                'Calm Mind': ['Shadow Ball'],
                                'Shadow Ball': ['Baton Pass', 'Thunderbolt', 'Hidden Power [Fighting]']
                            }
                    )
                    ), baseStats=(150, 80, 44, 90, 54, 80), genders=('M', 'F'), images=('426.gif', '426.png', '426 (1).png')
                )
            if 'Mismagius':
                root.pokesets['Mismagius'] = pokemon_ddl.PokemonSet(
                    name='Mismagius', species='Mismagius', abilities=('Levitate',), pkTypes=('Ghost',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Pain Split'],
                            {
                                'Protect': ['Power Gem', 'Nasty Plot', 'Taunt'],
                                'Pain Split': ['Shadow Ball'],
                                'Shadow Ball': ['Will-O-Wisp', 'Thunder Wave', 'Destiny Bond'],
                                'Power Gem': ['Shadow Ball'],
                                'Nasty Plot': ['Thunderbolt', 'Hidden Power [Ground]', 'Hidden Power [Fighting]'],
                                'Thunderbolt': ['Shadow Ball'],
                                'Hidden Power [Ground]': ['Shadow Ball'],
                                'Hidden Power [Fighting]': ['Shadow Ball'],
                                'Taunt': ['Shadow Ball']
                            }
                        ),
                    ), baseStats=(60, 60, 60, 105, 105, 105), genders=('M', 'F'), images=('429.gif', '429.png', '429 (1).png')
                )
            if 'Dusknoir':
                root.pokesets['Dusknoir'] = pokemon_ddl.PokemonSet(
                    name='Dusknoir', species='Dusknoir', abilities=('Pressure',), pkTypes=('Ghost',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Substitute', 'Pain Split'],
                            {
                                'Protect': ['Shadow Punch'],
                                'Shadow Punch': ['Imprison'],
                                'Imprison': ['Fling', 'Earthquake', 'Fire Punch', 'Ice Punch'],
                                'Pain Split': ['Confuse Ray', 'Curse', 'Shadow Sneak'],
                                'Substitute': ['Trick Room'],
                                'Trick Room': ['Fling'],
                                'Fling': ['Trick Room', 'Attract', 'Brick Break', 'Rock Slide'],
                                'Earthquake': ['Trick Room', 'Attract', 'Brick Break', 'Rock Slide']
                            }
                        ),
                    ), baseStats=(45, 100, 135, 65, 135, 45), genders=('M', 'F'), images=('477.gif', '477.png', '477 (1).png')
                )
            if 'Rotom':
                root.pokesets['Rotom'] = pokemon_ddl.PokemonSet(
                    name='Rotom', species='Rotom', abilities=('Levitate',), pkTypes=('Electric', 'Ghost'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Substitute'],
                            {
                                'Protect': ['Uproar', 'Pain Split', 'Reflect', 'Light Screen', 'Charge Beam', 'Discharge', 'Trick'],
                                'Substitute': ['Pain Split', 'Trick'],
                                'Pain Split': ['Discharge', 'Shadow Ball', 'Confuse Ray', 'Thunder Wave', 'Uproar', 'Reflect', 'Light Screen', 'Trick']
                            }
                        ),
                    ), baseStats=(50, 50, 77, 95, 77, 91), genders=('',), images=('479.gif', 'Rotom.png', 'Rotom (1).png')
                )
            if 'Rotom-Fan':
                root.pokesets['Rotom-Fan'] = pokemon_ddl.PokemonSet(
                    name='Rotom-Fan', species='Rotom', abilities=('Levitate',), pkTypes=('Electric', 'Flying'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Air Slash'],
                                'Air Slash': ['Shadow Ball', 'Thunderbolt', 'Trick', 'Discharge'],
                                'Thunderbolt': ['Hidden Power [Ice]'],
                                'Hidden Power [Ice]': ['Trick', 'Will-O-Wisp']
                            }
                        ),
                    ), baseStats=(50, 65, 107, 105, 107, 86), genders=('',), images=('479.gif', 'rotom-fan.png', 'rotom-fan (1).png')
                )
            if 'Rotom-Frost':
                root.pokesets['Rotom-Frost'] = pokemon_ddl.PokemonSet(
                    name='Rotom-Frost', species='Rotom', abilities=('Levitate',), pkTypes=('Electric', 'Ice'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Blizzard'],
                                'Blizzard': ['Shadow Ball', 'Thunderbolt', 'Trick', 'Discharge', 'Discharge'],
                                'Thunderbolt': ['Shadow Ball', 'Will-O-Wisp', 'Pain Split']
                            }
                        ),
                    ), baseStats=(50, 65, 107, 105, 107, 86), genders=('',), images=('479.gif', 'rotom-frost.png', 'rotom-frost (1).png')
                )
            if 'Rotom-Heat':
                root.pokesets['Rotom-Heat'] = pokemon_ddl.PokemonSet(
                    name='Rotom-Heat', species='Rotom', abilities=('Levitate',), pkTypes=('Electric', 'Fire'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Overheat'],
                                'Overheat': ['Shadow Ball', 'Thunderbolt', 'Trick', 'Discharge', 'Discharge'],
                                'Thunderbolt': ['Shadow Ball', 'Thunder Wave', 'Pain Split']
                            }
                        ),
                    ), baseStats=(50, 65, 107, 105, 107, 86), genders=('',), images=('479.gif', 'rotom-heat.png', 'rotom-heat (1).png')
                )
            if 'Rotom-Mow':
                root.pokesets['Rotom-Mow'] = pokemon_ddl.PokemonSet(
                    name='Rotom-Mow', species='Rotom', abilities=('Levitate',), pkTypes=('Electric', 'Grass'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Leaf Storm'],
                                'Leaf Storm': ['Shadow Ball', 'Thunderbolt', 'Trick', 'Discharge', 'Discharge'],
                                'Thunderbolt': ['Shadow Ball', 'Thunder Wave', 'Pain Split']
                            }
                        ),
                    ), baseStats=(50, 65, 107, 105, 107, 86), genders=('',), images=('479.gif', 'rotom-mow.png', 'rotom-mow (1).png')
                )
            if 'Rotom-Wash':
                root.pokesets['Rotom-Wash'] = pokemon_ddl.PokemonSet(
                    name='Rotom-Wash', species='Rotom', abilities=('Levitate',), pkTypes=('Electric', 'Water'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Pain Split'],
                            {
                                'Protect': ['Hydro Pump'],
                                'Hydro Pump': ['Shadow Ball', 'Thunderbolt', 'Trick', 'Discharge',
                                               'Discharge'],
                                'Thunderbolt': ['Shadow Ball', 'Will-O-Wisp', 'Pain Split'],
                                'Pain Split': ['Hydro Pump']
                            }
                        ),
                    ), baseStats=(50, 65, 107, 105, 107, 86), genders=('',), images=('479.gif', 'rotom-wash.png', 'rotom-wash (1).png')
                )
            if 'Arceus-Ghost':
                root.pokesets['Arceus-Ghost'] = pokemon_ddl.PokemonSet(
                    name='Arceus-Ghost', species='Arceus', abilities=('Multitype',), pkTypes=('Ghost',),
                    sets=(
                        # MoveSet 1: "The Chaotic Bulwark". Guaranteed Protect + Judgement, then maximum variance.
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Judgement'],

                                # Judgement is the central hub for a chaotic web of possibilities.
                                'Judgement': [
                                    'Calm Mind', 'Swords Dance', 'Recover', 'Cosmic Power', 'Will-O-Wisp',
                                    'Thunder Wave', 'Extreme Speed', 'Earth Power', 'Ice Beam', 'Thunderbolt',
                                    'Flamethrower', 'Shadow Claw', 'Gravity', 'Substitute'
                                ],

                                # Every node below is heavily interconnected to create unpredictable sets.
                                'Calm Mind': ['Ice Beam', 'Thunderbolt', 'Earthquake', 'Shadow Claw', 'Recover',
                                              'Swords Dance', 'Will-O-Wisp'],
                                'Swords Dance': ['Extreme Speed', 'Dragon Claw', 'Shadow Claw', 'Earthquake', 'Surf',
                                                 'Ice Beam', 'Calm Mind'],
                                'Recover': ['Calm Mind', 'Will-O-Wisp', 'Ice Beam', 'Flamethrower', 'Substitute',
                                            'Swords Dance', 'Judgement'],
                                'Cosmic Power': ['Recover', 'Will-O-Wisp', 'Toxic', 'Flamethrower', 'Judgement'],
                                'Will-O-Wisp': ['Recover', 'Calm Mind', 'Extreme Speed', 'Dragon Claw'],
                                'Extreme Speed': ['Swords Dance', 'Shadow Claw', 'Draco Meteor', 'Overheat',
                                                  'Judgement',
                                                  'Recover'],
                                'Earth Power': ['Ice Beam', 'Thunderbolt', 'Calm Mind', 'Swords Dance', 'Dragon Claw'],
                                'Ice Beam': ['Thunderbolt', 'Earth Power', 'Judgement', 'Calm Mind', 'Swords Dance'],
                                'Thunderbolt': ['Ice Beam', 'Surf', 'Judgement', 'Calm Mind', 'Swords Dance'],
                                'Dragon Claw': ['Earthquake', 'Shadow Claw', 'Swords Dance', 'Calm Mind', 'Ice Beam'],
                                'Substitute': ['Calm Mind', 'Swords Dance', 'Recover', 'Will-O-Wisp', 'Judgement'],
                                'Gravity': ['Thunder', 'Blizzard', 'Focus Blast', 'Earthquake', 'Judgement'],
                            }
                        ),

                        # MoveSet 2: "The Chaotic Gambler". No Protect, starts with Judgement into chaos.
                        pokemon_ddl.MoveSet(
                            ['Judgement'],
                            {
                                'Judgement': [
                                    'Extreme Speed', 'Draco Meteor', 'Outrage', 'Calm Mind', 'Swords Dance',
                                    'Gravity', 'Trick Room', 'Fire Blast', 'Thunder', 'Ice Beam', 'Earthquake',
                                    'Shadow Claw', 'Will-O-Wisp', 'Recover'
                                ],

                                'Draco Meteor': ['Extreme Speed', 'Overheat', 'Earthquake', 'Fire Blast', 'Steel Wing'],
                                'Outrage': ['Extreme Speed', 'Aqua Tail', 'Iron Head', 'Ice Beam', 'Giga Drain'],
                                'Calm Mind': ['Ice Beam', 'Thunder', 'Focus Blast', 'Shadow Claw', 'Recover',
                                              'Swords Dance'],
                                'Swords Dance': ['Extreme Speed', 'Shadow Claw', 'Dragon Claw', 'Giga Drain',
                                                 'Calm Mind'],
                                'Gravity': ['Thunder', 'Blizzard', 'Focus Blast', 'Draco Meteor', 'Judgement'],
                                'Trick Room': ['Judgement', 'Draco Meteor', 'Fire Blast', 'Thunder', 'Focus Blast'],
                                'Extreme Speed': ['Judgement', 'Swords Dance', 'Draco Meteor', 'Will-O-Wisp',
                                                  'Recover'],
                                'Fire Blast': ['Draco Meteor', 'Thunder', 'Ice Beam', 'Earthquake'],
                                'Earthquake': ['Stone Edge', 'Outrage', 'Dragon Claw', 'Flamethrower'],
                                'Recover': ['Judgement', 'Calm Mind', 'Swords Dance', 'Will-O-Wisp', 'Toxic']
                            }
                        ),

                        # MoveSet 3: "The Perish Trapper". A specific, high-risk alternate strategy.
                        pokemon_ddl.MoveSet(
                            ['Perish Song'],
                            {
                                'Mean Look': ['Protect', 'Recover', 'Judgement'],
                                'Perish Song': ['Mean Look']
                            }
                        )
                    ), baseStats=(120, 120, 120, 120, 120, 120), genders=('',), images=('493.gif', 'arceus-ghost.png', 'arceus-ghost (1).png'),
                    item_key='arcGhost', stat_key='arcStat'
                )

        # Steel type pokemon
        if 'Steel':
            if 'Forretress':
                root.pokesets['Forretress'] = pokemon_ddl.PokemonSet(
                    name='Forretress', species='Forretress', abilities=('Sturdy',), pkTypes=('Bug', 'Steel'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Stealth Rock', 'Spikes', 'Toxic Spikes'],
                            {
                                'Stealth Rock': ['Spikes', 'Toxic Spikes', 'Protect', 'Zap Cannon'],
                                'Spikes': ['Toxic Spikes', 'Stealth Rock', 'Protect', 'Explosion'],
                                'Toxic Spikes': ['Spikes', 'Stealth Rock', 'Protect', 'Hidden Power [Fire]'],
                                'Protect': ['Zap Cannon', 'Gyro Ball', 'Explosion', 'Bug Bite', 'Rapid Spin']
                            }
                        ),
                    ), baseStats=(75, 90, 140, 60, 60, 40), genders=('M', 'F'), images=('205.gif', '205.png', '205 (1).png')
                )
            if 'Steelix':
                root.pokesets['Steelix'] = pokemon_ddl.PokemonSet(
                    name='Steelix', species='Steelix', abilities=('Rock Head', 'Sturdy'), pkTypes=('Steel', 'Ground'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Protect', 'Curse'],
                            {
                                'Protect': ['Stealth Rock', 'Torment'],
                                'Stealth Rock': ['Roar'],
                                'Roar': ['Gyro Ball', 'Stone Edge', 'Explosion'],
                                'Torment': ['Substitute', 'Explosion'],
                                'Substitute': ['Toxic', 'Earthquake', 'Gyro Ball', 'Explosion'],
                                'Curse': ['Gyro Ball', 'Rest', 'Sleep Talk']
                            }
                        ),
                    ), baseStats=(75, 85, 200, 55, 65, 30), genders=('M', 'F'), images=('208.gif', '208-m.png', '208-m (1).png')
                )
            if 'Scizor':
                root.pokesets['Scizor'] = pokemon_ddl.PokemonSet(
                    name='Scizor', species='Scizor', abilities=('Swarm', 'Technician'), pkTypes=('Bug', 'Steel'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Swords Dance', 'U-turn'],
                                'Swords Dance': ['Bullet Punch', 'Bug Bite', 'Superpower', 'Pursuit', 'Baton Pass'],
                                'Superpower': ['Bullet Punch', 'Bug Bite', 'Pursuit', 'Night Slash', 'Knock Off', 'Morning Sun'],
                                'U-turn': ['Bullet Punch', 'Pursuit', 'Night Slash', 'Knock Off', 'Iron Head', 'Superpower', 'Roost']
                            }
                        ),
                    ), baseStats=(70, 130, 100, 55, 80, 65), genders=('M', 'F'), images=('212.gif', '212-m.png', '212-m (1).png')
                )
            if 'Skarmory':
                root.pokesets['Skarmory'] = pokemon_ddl.PokemonSet(
                    name='Skarmory', species='Skarmory', abilities=('Keen Eye', 'Sturdy'), pkTypes=('Steel', 'Flying'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Roost'],
                            {
                                'Protect': ['Stealth Rock', 'Spikes', 'Roost'],
                                'Roost': ['Stealth Rock', 'Spikes'],
                                'Spikes': ['Whirlwind', 'Steel Wing', 'Icy Wind'],
                                'Stealth Rock': ['Whirlwind', 'Brave Bird', 'Icy Wind'],
                                'Whirlwind': ['Counter', 'Taunt', 'Drill Peck', 'Steel Wing']
                            }
                        ),
                    ), baseStats=(65, 80, 140, 40, 70, 70), genders=('M', 'F'), images=('227.gif', '227.png', '227 (1).png')
                )
            if 'Mawile':
                root.pokesets['Mawile'] = pokemon_ddl.PokemonSet(
                    name='Mawile', species='Mawile', abilities=('Hyper Cutter', 'Intimidate'), pkTypes=('Steel',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Protect', 'Protect', 'Seismic Toss'],
                            {
                                'Protect': ['Baton Pass', 'Swords Dance'],
                                'Baton Pass': ['Swords Dance', 'Substitute', 'Iron Head'],
                                'Seismic Toss': ['Brick Break', 'Sucker Punch'],
                                'Brick Break': ['Toxic'],
                                'Sucker Punch': ['Toxic'],
                                'Toxic': ['Protect']
                            }
                        ),
                    ), baseStats=(50, 85, 85, 55, 55, 50), genders=('M', 'F'), ability_weights=(0.2, 0.8), images=('303.gif', '303.png', '303 (1).png')
                )
            if 'Aggron':
                root.pokesets['Aggron'] = pokemon_ddl.PokemonSet(
                    name='Aggron', species='Aggron', abilities=('Sturdy', 'Rock Head'), pkTypes=('Steel', 'Rock'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Head Smash'],
                            {
                                'Protect': ['Head Smash','Double-Edge', 'Iron Head', 'Substitute', 'Iron Tail', 'Dragon Claw', 'Rock Slide', 'Dynamic Punch', 'Fire Punch', 'Sandstorm', 'Shock Wave', 'Dragon Rush', 'Avalanche', 'Metal Burst'],
                                'Substitute': ['Focus Punch'],
                                'Head Smash': ['Protect']
                            }
                        ),
                    ), baseStats=(70, 110, 180, 60, 60, 50), genders=('M', 'F'), images=('306.gif', '306.png', '306 (1).png')
                )
            if 'Metagross':
                root.pokesets['Metagross'] = pokemon_ddl.PokemonSet(
                    name='Metagross', species='Metagross', abilities=('Clear Body',), pkTypes=('Steel', 'Psychic'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Flash Cannon', 'Trick', 'Stealth Rock', 'Agility', 'Meteor Mash', 'Light Screen'],
                                'Flash Cannon': ['Psychic'],
                                'Psychic': ['Hyper Beam', 'Grass Knot', 'Swift'],
                                'Trick': ['Earthquake', 'Explosion', 'Stealth Rock'],
                                'Earthquake': ['Meteor Mash', 'Bullet Punch'],
                                'Meteor Mash': ['Ice Punch', 'Earthquake', 'Explosion', 'Pursuit'],
                                'Pursuit': ['Thunder Punch', 'Ice Punch', 'Explosion', 'Trick'],
                                'Agility': ['Earthquake', 'Zen Headbutt'],
                                'Zen Headbutt': ['Meteor Mash', 'Hammer Arm', 'Bullet Punch'],
                                'Stealth Rock': ['Meteor Mash', 'Zen Headbutt', 'Rollout', 'Bullet Punch'],
                                'Light Screen': ['Brick Break', 'Gyro Ball', 'Rain Dance', 'Sandstorm', 'Sunny Day'],
                                'Brick Break': ['Swagger', 'Toxic', 'Scary Face', 'Icy Wind', 'Explosion'],
                                'Rain Dance': ['Swagger', 'Toxic', 'Scary Face', 'Icy Wind', 'Explosion'],
                                'Sandstorm': ['Swagger', 'Toxic', 'Scary Face', 'Icy Wind', 'Explosion'],
                                'Sunny Day': ['Swagger', 'Toxic', 'Scary Face', 'Icy Wind', 'Explosion']
                            }
                        ),
                    ), baseStats=(80, 135, 130, 95, 90, 70), genders=('',), images=('376.gif', '376.png', '376 (1).png')
                )
            if 'Registeel':
                root.pokesets['Registeel'] = pokemon_ddl.PokemonSet(
                    name='Registeel', species='Registeel', abilities=('Clear Body',), pkTypes=('Steel',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Explosion', 'Curse', 'Protect', 'Stealth Rock'],
                            {
                                'Explosion': ['Stealth Rock', 'Thunder Wave', 'Ice Punch', 'Lock-On'],
                                'Stealth Rock': ['Thunder Wave', 'Toxic', 'Gravity'],
                                'Thunder Wave': ['Seismic Toss'],
                                'Toxic': ['Seismic Toss'],
                                'Seismic Toss': ['Shadow Claw', 'Iron Head', 'Superpower'],
                                'Curse': ['Iron Head', 'Counter'],
                                'Counter': ['Explosion', 'Ice Punch', 'Earthquake', 'Seismic Toss', 'Flash Cannon', 'Focus Punch', 'Gravity'],
                                'Iron Head': ['Rest'],
                                'Rest': ['Sleep Talk'],
                                'Lock-On': ['Zap Cannon', 'Focus Blast'],
                                'Gravity': ['Zap Cannon', 'Focus Blast'],
                                'Protect': ['Explosion', 'Counter', 'Gravity']
                            }
                        ),
                    ), baseStats=(80, 75, 150, 75, 150, 50), genders=('',), images=('379.gif', '379.png', '379 (1).png')
                )
            if 'Jirachi':
                root.pokesets['Jirachi'] = pokemon_ddl.PokemonSet(
                    name='Jirachi', species='Jirachi', abilities=('Serene Grace',), pkTypes=('Steel', 'Psychic'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Iron Head', 'Draco Meteor', 'Calm Mind'],
                                'Iron Head': ['Fire Punch', 'Body Slam', 'Psychic', 'Wish', 'U-turn', 'Stealth Rock'],
                                'Draco Meteor': ['Hidden Power [Ground]', 'Hidden Power [Fire]', 'Iron Head', 'Thunderbolt',
                                                 'Grass Knot', 'Psychic', 'Icy Wind', 'Flash Cannon'],
                                'Calm Mind': ['Wish'],
                                'Wish': ['Psychic', 'Confusion', 'Flash Cannon', 'Water Pulse']
                            }
                        ),
                    ), baseStats=(100, 100, 100, 100, 100, 100), genders=('',), images=('385.gif', '385.png', '385 (1).png')
                )
            if 'Empoleon':
                root.pokesets['Empoleon'] = pokemon_ddl.PokemonSet(
                    name='Empoleon', species='Empoleon', abilities=('Torrent',), pkTypes=('Water', 'Steel'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Stealth Rock', 'Knock Off', 'Agility', 'Feather Dance'],
                                'Agility': ['Waterfall', 'Hydro Cannon'],
                                'Waterfall': ['Metal Claw', 'Pluck', 'Shadow Claw', 'Steel Wing'],
                                'Hydro Cannon': ['Ice Beam', 'Grass Knot', 'Signal Beam'],
                                'Feather Dance': ['Hydro Cannon', 'Hyper Beam', 'Flash Cannon'],
                                'Stealth Rock': ['Roar', 'Knock Off', 'Surf'],
                                'Knock Off': ['Aqua Jet', 'Drill Peck']
                            }
                        ),
                    ), baseStats=(84, 86, 88, 111, 101, 60), genders=('M', 'F'), images=('395.gif', '395.png', '395 (1).png')
                )
            if 'Bastiodon':
                root.pokesets['Bastiodon'] = pokemon_ddl.PokemonSet(
                    name='Bastiodon', species='Bastiodon', abilities=('Sturdy',), pkTypes=('Rock', 'Steel'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Rest'],
                            {
                                'Rest': ['Sleep Talk'],
                                'Sleep Talk': ['Roar'],
                                'Roar': ['Stealth Rock'],
                                'Protect': ['Roar', 'Toxic', 'Flamethrower'],
                                'Stealth Rock': ['Metal Burst'],
                                'Toxic': ['Iron Head', 'Rock Slide'],
                                'Flamethrower': ['Thunderbolt', 'Ice Beam', 'Magnet Rise', 'Metal Burst', 'Outrage']
                            }
                        ),
                    ), baseStats=(60, 52, 168, 47, 138, 30), genders=('M', 'F'), images=('411.gif', '411.png', '411 (1).png')
                )
            if 'Wormadam-Trash':
                root.pokesets['Wormadam-Trash'] = pokemon_ddl.PokemonSet(
                    name='Wormadam-Trash', species='Wormadam', abilities=('Anticipation',), pkTypes=('Bug', 'Steel'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Stealth Rock', 'Gyro Ball', 'Toxic'],
                                'Stealth Rock': ['Psych Up', 'Toxic'],
                                'Psych Up': ['Gyro Ball'],
                                'Toxic': ['Gyro Ball', 'Mirror Shot']
                            }
                        ),
                    ), baseStats=(60, 79, 105, 59, 85, 36), genders=('F',), images=('413.gif', '413-s.png', '413-s (1).png')
                )
            if 'Bronzong':
                root.pokesets['Bronzong'] = pokemon_ddl.PokemonSet(
                    name='Bronzong', species='Bronzong', abilities=('Levitate', 'Heatproof'),
                    pkTypes=('Steel', 'Psychic'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Trick Room', 'Gravity'],
                            {
                                'Trick Room': ['Gyro Ball', 'Gravity', 'Calm Mind', 'Light Screen'],
                                'Gyro Ball': ['Curse', 'Rain Dance', 'Stealth Rock', 'Explosion', 'Earthquake', 'Payback'],
                                'Gravity': ['Hypnosis'],
                                'Calm Mind': ['Flash Cannon', 'Extrasensory'],
                                'Hypnosis': ['Dream Eater', 'Gyro Ball', 'Trick Room'],
                                'Light Screen': ['Rain Dance', 'Gyro Ball']
                            }
                        ),
                    ), baseStats=(67, 89, 116, 79, 116, 33), genders=('',), images=('437.gif', '437.png', '437 (1).png')
                )
            if 'Magnezone':
                root.pokesets['Magnezone'] = pokemon_ddl.PokemonSet(
                    name='Magnezone', species='Magnezone', abilities=('Magnet Pull', 'Sturdy'),
                    pkTypes=('Electric', 'Steel'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Hidden Power [Fire]'],
                                'Hidden Power [Fire]': ['Thunder', 'Thunderbolt'],
                                'Thunder': ['Thunderbolt', 'Mirror Coat', 'Light Screen', 'Reflect'],
                                'Thunderbolt': ['Thunder', 'Flash Cannon', 'Explosion', 'Magnet Rise', 'Zap Cannon']
                            }
                        ),
                    ), baseStats=(70, 70, 115, 130, 90, 60), genders=('',), images=('462.gif', '462.png', '462 (1).png'),
                    ability_weights=(0.8, 0.2)
                )
            if 'Probopass':
                root.pokesets['Probopass'] = pokemon_ddl.PokemonSet(
                    name='Probopass', species='Probopass', abilities=('Sturdy', 'Magnet Pull'),
                    pkTypes=('Rock', 'Steel'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Earth Power', 'Gravity'],
                                'Gravity': ['Zap Cannon', 'Rock Tomb', 'Dynamic Punch', 'Zap Cannon', 'Dynamic Punch'],
                                'Earth Power': ['Power Gem', 'Thunderbolt', 'Hidden Power [Grass]', 'Magnet Rise', 'Thunder', 'Stealth Rock']
                            }
                        ),
                    ), baseStats=(60, 55, 145, 75, 150, 40), genders=('M', 'F'), ability_weights=(0.2, 0.8),
                    images = ('476.gif', '476.png', '476 (1).png')
                )
            if 'Arceus-Steel':
                root.pokesets['Arceus-Steel'] = pokemon_ddl.PokemonSet(
                    name='Arceus-Steel', species='Arceus', abilities=('Multitype',), pkTypes=('Steel',),
                    sets=(
                        # MoveSet 1: "The Chaotic Bulwark". Guaranteed Protect + Judgement, then maximum variance.
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Judgement'],

                                # Judgement is the central hub for a chaotic web of possibilities.
                                'Judgement': [
                                    'Calm Mind', 'Swords Dance', 'Recover', 'Cosmic Power', 'Will-O-Wisp',
                                    'Thunder Wave', 'Extreme Speed', 'Earth Power', 'Ice Beam', 'Thunderbolt',
                                    'Flamethrower', 'Shadow Claw', 'Gravity', 'Substitute'
                                ],

                                # Every node below is heavily interconnected to create unpredictable sets.
                                'Calm Mind': ['Ice Beam', 'Thunderbolt', 'Earthquake', 'Shadow Claw', 'Recover',
                                              'Swords Dance', 'Will-O-Wisp'],
                                'Swords Dance': ['Extreme Speed', 'Dragon Claw', 'Shadow Claw', 'Earthquake', 'Surf',
                                                 'Ice Beam', 'Calm Mind'],
                                'Recover': ['Calm Mind', 'Will-O-Wisp', 'Ice Beam', 'Flamethrower', 'Substitute',
                                            'Swords Dance', 'Judgement'],
                                'Cosmic Power': ['Recover', 'Will-O-Wisp', 'Toxic', 'Flamethrower', 'Judgement'],
                                'Will-O-Wisp': ['Recover', 'Calm Mind', 'Extreme Speed', 'Dragon Claw'],
                                'Extreme Speed': ['Swords Dance', 'Shadow Claw', 'Draco Meteor', 'Overheat',
                                                  'Judgement',
                                                  'Recover'],
                                'Earth Power': ['Ice Beam', 'Thunderbolt', 'Calm Mind', 'Swords Dance', 'Dragon Claw'],
                                'Ice Beam': ['Thunderbolt', 'Earth Power', 'Judgement', 'Calm Mind', 'Swords Dance'],
                                'Thunderbolt': ['Ice Beam', 'Surf', 'Judgement', 'Calm Mind', 'Swords Dance'],
                                'Dragon Claw': ['Earthquake', 'Shadow Claw', 'Swords Dance', 'Calm Mind', 'Ice Beam'],
                                'Substitute': ['Calm Mind', 'Swords Dance', 'Recover', 'Will-O-Wisp', 'Judgement'],
                                'Gravity': ['Thunder', 'Blizzard', 'Focus Blast', 'Earthquake', 'Judgement'],
                            }
                        ),

                        # MoveSet 2: "The Chaotic Gambler". No Protect, starts with Judgement into chaos.
                        pokemon_ddl.MoveSet(
                            ['Judgement'],
                            {
                                'Judgement': [
                                    'Extreme Speed', 'Draco Meteor', 'Outrage', 'Calm Mind', 'Swords Dance',
                                    'Gravity', 'Trick Room', 'Fire Blast', 'Thunder', 'Ice Beam', 'Earthquake',
                                    'Shadow Claw', 'Will-O-Wisp', 'Recover'
                                ],

                                'Draco Meteor': ['Extreme Speed', 'Overheat', 'Earthquake', 'Fire Blast', 'Steel Wing'],
                                'Outrage': ['Extreme Speed', 'Aqua Tail', 'Iron Head', 'Ice Beam', 'Giga Drain'],
                                'Calm Mind': ['Ice Beam', 'Thunder', 'Focus Blast', 'Shadow Claw', 'Recover',
                                              'Swords Dance'],
                                'Swords Dance': ['Extreme Speed', 'Shadow Claw', 'Dragon Claw', 'Giga Drain',
                                                 'Calm Mind'],
                                'Gravity': ['Thunder', 'Blizzard', 'Focus Blast', 'Draco Meteor', 'Judgement'],
                                'Trick Room': ['Judgement', 'Draco Meteor', 'Fire Blast', 'Thunder', 'Focus Blast'],
                                'Extreme Speed': ['Judgement', 'Swords Dance', 'Draco Meteor', 'Will-O-Wisp',
                                                  'Recover'],
                                'Fire Blast': ['Draco Meteor', 'Thunder', 'Ice Beam', 'Earthquake'],
                                'Earthquake': ['Stone Edge', 'Outrage', 'Dragon Claw', 'Flamethrower'],
                                'Recover': ['Judgement', 'Calm Mind', 'Swords Dance', 'Will-O-Wisp', 'Toxic']
                            }
                        ),

                        # MoveSet 3: "The Perish Trapper". A specific, high-risk alternate strategy.
                        pokemon_ddl.MoveSet(
                            ['Perish Song'],
                            {
                                'Mean Look': ['Protect', 'Recover', 'Judgement'],
                                'Perish Song': ['Mean Look']
                            }
                        )
                    ), baseStats=(120, 120, 120, 120, 120, 120), genders=('',), images=('493.gif', 'arceus-steel.png', 'arceus-steel (1).png'),
                    item_key='arcSteel', stat_key='arcStat'
                )

        # Electric type pokemon
        if 'Electric':
            if 'Pikachu':
                root.pokesets['Pikachu'] = pokemon_ddl.PokemonSet(
                    name='Pikachu', species='Pikachu', abilities=('Static',), pkTypes=('Electric',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Surf'],
                                'Surf': ['Volt Tackle'],
                                'Volt Tackle': ['Fake Out', 'Endeavor', 'Quick Attack', 'Iron Tail']
                            }
                        ),
                    ), baseStats=(35, 55, 30, 50, 40, 90), genders=('M', 'F'), images=('025.gif', '025-m.png', '025-m (1).png'),
                    item_key='pika'
                )
            if 'Raichu':
                root.pokesets['Raichu'] = pokemon_ddl.PokemonSet(
                    name='Raichu', species='Raichu', abilities=('Static',), pkTypes=('Electric',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Fake Out', 'Nasty Plot'],
                                'Fake Out': ['Endeavor', 'Encore', 'Volt Tackle'],
                                'Endeavor': ['Quick Attack'],
                                'Encore': ['Volt Tackle', 'Grass Knot'],
                                'Volt Tackle': ['Focus Blast'],
                                'Nasty Plot': ['Focus Blast', 'Discharge', 'Volt Tackle', 'Grass Knot', 'Swift']
                            }
                        ),
                    ), baseStats=(60, 90, 55, 90, 80, 100), genders=('M', 'F'), images=('026.gif', '026-m.png', '026-m (1).png')
                )
            if 'Electrode':
                root.pokesets['Electrode'] = pokemon_ddl.PokemonSet(
                    name='Electrode', species='Electrode', abilities=('Soundproof', 'Static'), pkTypes=('Electric',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Light Screen', 'Reflect', 'Taunt', 'Thunder', 'Explosion'],
                                'Thunder': ['Rain Dance']
                            }
                        ),
                    ), baseStats=(60, 50, 70, 80, 80, 140), genders=('',), images=('101.gif', '101.png', '101 (1).png')
                )
            if 'Jolteon':
                root.pokesets['Jolteon'] = pokemon_ddl.PokemonSet(
                    name='Jolteon', species='Jolteon', abilities=('Volt Absorb',), pkTypes=('Electric',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Thunderbolt'],
                            {
                                'Protect': ['Helping Hand', 'Rain Dance', 'Thunderbolt'],
                                'Helping Hand': ['Thunderbolt'],
                                'Rain Dance': ['Thunder'],
                                'Thunderbolt': ['Hidden Power [Ice]', 'Signal Beam', 'Shadow Ball', 'Thunder Wave', 'Light Screen', 'Reflect', 'Swift'],
                                'Thunder': ['Hidden Power [Ice]', 'Signal Beam', 'Shadow Ball', 'Thunder Wave', 'Light Screen', 'Reflect', 'Hyper Beam']
                            }
                        ),
                    ), baseStats=(65, 65, 60, 110, 95, 130), genders=('M', 'F'), images=('135.gif', '135.png', '135 (1).png')
                )
            if 'Zapdos':
                root.pokesets['Zapdos'] = pokemon_ddl.PokemonSet(
                    name='Zapdos', species='Zapdos', abilities=('Pressure',), pkTypes=('Electric', 'Flying'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Substitute', 'Discharge'],
                                'Substitute': ['Hidden Power [Flying]', 'Toxic', 'Roar', 'Heat Wave', 'Steel Wing'],
                                'Discharge': ['Hidden Power [Flying]', 'Drill Peck', 'Agility', 'Sky Attack'],
                                'Agility': ['Baton Pass'],
                                'Hidden Power [Flying]': ['Heat Wave', 'Ancient Power', 'Double Team'],
                                'Drill Peck': ['Extrasensory', 'Light Screen', 'Ominous Wind'],
                                'Sky Attack': ['Tailwind', 'Sunny Day', 'Twister', 'Steel Wing']
                            }
                        ),
                    ), baseStats=(90, 90, 85, 125, 90, 100), genders=('',), images=('145.gif', '145.png', '145 (1).png')
                )
            if 'Lanturn':
                root.pokesets['Lanturn'] = pokemon_ddl.PokemonSet(
                    name='Lanturn', species='Lanturn', abilities=('Volt Absorb',),
                    pkTypes=('Water', 'Electric'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Substitute', 'Rest'],
                            {
                                'Protect': ['Agility', 'Surf'],
                                'Surf': ['Discharge'],
                                'Discharge': ['Surf', 'Bounce', 'Charge Beam', 'Spark', 'Stockpile', 'Water Pulse'],
                                'Agility': ['Surf'],
                                'Rest': ['Sleep Talk'],
                                'Sleep Talk': ['Surf'],
                                'Substitute': ['Heal Bell', 'Surf'],
                                'Heal Bell': ['Charge Beam']
                            }
                        ),
                    ), baseStats=(125, 58, 58, 76, 76, 67), genders=('M', 'F'), images=('171.gif', '171.png', '171 (1).png')
                )
            if 'Ampharos':
                root.pokesets['Ampharos'] = pokemon_ddl.PokemonSet(
                    name='Ampharos', species='Ampharos', abilities=('Static',), pkTypes=('Electric',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Reflect', 'Light Screen', 'Focus Blast', 'Power Gem'],
                                'Reflect': ['Heal Bell'],
                                'Light Screen': ['Heal Bell'],
                                'Heal Bell': ['Discharge', 'Thunderbolt', 'Thunder', 'Hidden Power [Ice]', 'Hidden Power [Grass]'],
                                'Focus Blast': ['Discharge', 'Thunderbolt', 'Hidden Power [Ice]', 'Hidden Power [Grass]', 'Substitute', 'Signal Beam'],
                                'Substitute': ['Focus Punch'],
                                'Power Gem': ['Hidden Power [Water]', 'Safeguard', 'Rain Dance', 'Thunder']
                            }
                        ),
                    ), baseStats=(90, 75, 75, 115, 90, 55), genders=('M', 'F'), images=('181.gif', '181.png', '181 (1).png')
                )
            if 'Raikou':
                root.pokesets['Raikou'] = pokemon_ddl.PokemonSet(
                    name='Raikou', species='Raikou', abilities=('Pressure',), pkTypes=('Electric',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Aura Sphere', 'Extreme Speed'],
                                'Extreme Speed': ['Body Slam', 'Crunch', 'Dig', 'Double-Edge', 'Flash', 'Giga Impact',
                                                  'Iron Head', 'Iron Tail', 'Light Screen', 'Magnet Rise', 'Mimic',
                                                  'Rock Smash', 'Secret Power', 'Spark', 'Spark', 'Spark', 'Thunder Fang',
                                                  'Thunder Fang', 'Weather Ball', 'Aura Sphere'],
                                'Aura Sphere': ['Rain Dance', 'Reflect', 'Charge Beam', 'Discharge', 'Extrasensory',
                                                'Extreme Speed', 'Hidden Power [Ice]', 'Hyper Beam', 'Shadow Ball', 'Shock Wave',
                                                'Signal Beam', 'Sleep Talk', 'Swift', 'Thunderbolt', 'Thunder', 'Thundershock',
                                                'Thunder Wave', 'Weather Ball', 'Zap Cannon'],
                                'Rain Dance': ['Thunder']
                            }
                        ),
                    ), baseStats=(90, 85, 75, 115, 100, 115), genders=('',), images=('243.gif', '243.png', '243 (1).png')
                )
            if 'Manectric':
                root.pokesets['Manectric'] = pokemon_ddl.PokemonSet(
                    name='Manectric', species='Manectric', abilities=('Static', 'Lightning Rod'), pkTypes=('Electric',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Thunderbolt', 'Thunder Fang', 'Charge Beam'],
                                'Thunderbolt': ['Flamethrower', 'Overheat'],
                                'Thunder Fang': ['Crunch', 'Fire Fang', 'Ice Fang', 'Roar'],
                                'Flamethrower': ['Hidden Power [Ice]', 'Hidden Power [Grass]', 'Substitute'],
                                'Overheat': ['Hidden Power [Grass]', 'Switcheroo', 'Charge Beam'],
                                'Charge Beam': ['Substitute', 'Toxic', 'Swift', 'Uproar']
                            }
                        ),
                    ), baseStats=(70, 75, 60, 105, 60, 105), genders=('M', 'F'), images=('310.gif', '310.png', '310 (1).png')
                )
            if 'Plusle':
                root.pokesets['Plusle'] = pokemon_ddl.PokemonSet(
                    name='Plusle', species='Plusle', abilities=('Plus',), pkTypes=('Electric',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {'Protect': ['Encore', 'Fake Out', 'Baton Pass'],
                             'Baton Pass': ['Nasty Plot', 'Charge Beam']}
                        ),
                    ), baseStats=(60, 50, 40, 85, 75, 95), genders=('M', 'F'), images=('311.gif', '311.png', '311 (1).png')
                )
            if 'Minun':
                root.pokesets['Minun'] = pokemon_ddl.PokemonSet(
                    name='Minun', species='Minun', abilities=('Minus',), pkTypes=('Electric',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Nasty Plot', 'Helping Hand'],
                                'Nasty Plot':['Thunderbolt', 'Hidden Power [Ice]'],
                                'Helping Hand': ['Baton Pass'],
                                'Baton Pass': ['Double Team', 'Nasty Plot']
                            }
                        ),
                    ), baseStats=(60, 40, 50, 75, 85, 95), genders=('M', 'F'), images=('312.gif', '312.png', '312 (1).png')
                )
            if 'Luxray':
                root.pokesets['Luxray'] = pokemon_ddl.PokemonSet(
                    name='Luxray', species='Luxray', abilities=('Rivalry', 'Intimidate'), pkTypes=('Electric',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Rest', 'Protect', 'Protect', 'Protect'],
                            {
                                'Protect': ['Spark', 'Thunder Fang', 'Thunderbolt'],
                                'Spark': ['Crunch', 'Night Slash'],
                                'Thunder Fang': ['Crunch', 'Night Slash', 'Ice Fang'],
                                'Crunch': ['Superpower', 'Swagger', 'Ice Fang', 'Fire Fang'],
                                'Night Slash': ['Superpower', 'Quick Attack', 'Iron Tail', 'Ice Fang'],
                                'Thunderbolt': ['Hidden Power [Grass]', 'Hidden Power [Water]', 'Ice Fang', 'Toxic'],
                                'Hidden Power [Grass]': ['Superpower', 'Crunch'],
                                'Hidden Power [Water]': ['Superpower', 'Crunch'],
                                'Toxic': ['Roar'],
                                'Rest': ['Sleep Talk', 'Discharge', 'Roar']
                            }
                        ),
                    ), baseStats=(80, 120, 79, 95, 79, 70), genders=('M', 'F'), images=('405.gif', '405-m.png', '405-m (1).png')
                )
            if 'Pachirisu':
                root.pokesets['Pachirisu'] = pokemon_ddl.PokemonSet(
                    name='Pachirisu', species='Pachirisu', abilities=('Run Away', 'Pick Up'), pkTypes=('Electric',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Toxic', 'U-turn', 'Discharge', 'Thunder Wave'],
                                'Toxic': ['Super Fang'],
                                'U-turn': ['Super Fang'],
                                'Discharge': ['Flatter'],
                                'Thunder Wave': ['Flatter'],
                                'Super Fang': ['Helping Hand', 'Last Resort'],
                                'Flatter': ['Mud-Slap']
                            }
                        ),
                    ), baseStats=(60, 45, 70, 45, 90, 95), genders=('M', 'F'), images=('417.gif', '417-m.png', '417-m (1).png')
                )
            if 'Electivire':
                root.pokesets['Electivire'] = pokemon_ddl.PokemonSet(
                    name='Electivire', species='Electivire', abilities=('Motor Drive',), pkTypes=('Electric',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Thunder Punch'],
                                'Thunder Punch': ['Ice Punch', 'Hidden Power [Ice]'],
                                'Ice Punch': ['Cross Chop', 'Earthquake', 'Flamethrower', 'Rock Slide'],
                                'Hidden Power [Ice]': ['Cross Chop', 'Earthquake', 'Flamethrower', 'Rock Slide']
                            }
                        ),
                    ), baseStats=(75, 123, 67, 95, 85, 95), genders=('M', 'F'), images=('466.gif', '466.png', '466 (1).png')
                )
            if 'Arceus-Electric':
                root.pokesets['Arceus-Electric'] = pokemon_ddl.PokemonSet(
                    name='Arceus-Electric', species='Arceus', abilities=('Multitype',), pkTypes=('Electric',),
                    sets=(
                        # MoveSet 1: "The Chaotic Bulwark". Guaranteed Protect + Judgement, then maximum variance.
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Judgement'],

                                # Judgement is the central hub for a chaotic web of possibilities.
                                'Judgement': [
                                    'Calm Mind', 'Swords Dance', 'Recover', 'Cosmic Power', 'Will-O-Wisp',
                                    'Thunder Wave', 'Extreme Speed', 'Earth Power', 'Ice Beam', 'Thunderbolt',
                                    'Flamethrower', 'Shadow Claw', 'Gravity', 'Substitute'
                                ],

                                # Every node below is heavily interconnected to create unpredictable sets.
                                'Calm Mind': ['Ice Beam', 'Thunderbolt', 'Earthquake', 'Shadow Claw', 'Recover',
                                              'Swords Dance', 'Will-O-Wisp'],
                                'Swords Dance': ['Extreme Speed', 'Dragon Claw', 'Shadow Claw', 'Earthquake', 'Surf',
                                                 'Ice Beam', 'Calm Mind'],
                                'Recover': ['Calm Mind', 'Will-O-Wisp', 'Ice Beam', 'Flamethrower', 'Substitute',
                                            'Swords Dance', 'Judgement'],
                                'Cosmic Power': ['Recover', 'Will-O-Wisp', 'Toxic', 'Flamethrower', 'Judgement'],
                                'Will-O-Wisp': ['Recover', 'Calm Mind', 'Extreme Speed', 'Dragon Claw'],
                                'Extreme Speed': ['Swords Dance', 'Shadow Claw', 'Draco Meteor', 'Overheat',
                                                  'Judgement',
                                                  'Recover'],
                                'Earth Power': ['Ice Beam', 'Thunderbolt', 'Calm Mind', 'Swords Dance', 'Dragon Claw'],
                                'Ice Beam': ['Thunderbolt', 'Earth Power', 'Judgement', 'Calm Mind', 'Swords Dance'],
                                'Thunderbolt': ['Ice Beam', 'Surf', 'Judgement', 'Calm Mind', 'Swords Dance'],
                                'Dragon Claw': ['Earthquake', 'Shadow Claw', 'Swords Dance', 'Calm Mind', 'Ice Beam'],
                                'Substitute': ['Calm Mind', 'Swords Dance', 'Recover', 'Will-O-Wisp', 'Judgement'],
                                'Gravity': ['Thunder', 'Blizzard', 'Focus Blast', 'Earthquake', 'Judgement'],
                            }
                        ),

                        # MoveSet 2: "The Chaotic Gambler". No Protect, starts with Judgement into chaos.
                        pokemon_ddl.MoveSet(
                            ['Judgement'],
                            {
                                'Judgement': [
                                    'Extreme Speed', 'Draco Meteor', 'Outrage', 'Calm Mind', 'Swords Dance',
                                    'Gravity', 'Trick Room', 'Fire Blast', 'Thunder', 'Ice Beam', 'Earthquake',
                                    'Shadow Claw', 'Will-O-Wisp', 'Recover'
                                ],

                                'Draco Meteor': ['Extreme Speed', 'Overheat', 'Earthquake', 'Fire Blast', 'Steel Wing'],
                                'Outrage': ['Extreme Speed', 'Aqua Tail', 'Iron Head', 'Ice Beam', 'Giga Drain'],
                                'Calm Mind': ['Ice Beam', 'Thunder', 'Focus Blast', 'Shadow Claw', 'Recover',
                                              'Swords Dance'],
                                'Swords Dance': ['Extreme Speed', 'Shadow Claw', 'Dragon Claw', 'Giga Drain',
                                                 'Calm Mind'],
                                'Gravity': ['Thunder', 'Blizzard', 'Focus Blast', 'Draco Meteor', 'Judgement'],
                                'Trick Room': ['Judgement', 'Draco Meteor', 'Fire Blast', 'Thunder', 'Focus Blast'],
                                'Extreme Speed': ['Judgement', 'Swords Dance', 'Draco Meteor', 'Will-O-Wisp',
                                                  'Recover'],
                                'Fire Blast': ['Draco Meteor', 'Thunder', 'Ice Beam', 'Earthquake'],
                                'Earthquake': ['Stone Edge', 'Outrage', 'Dragon Claw', 'Flamethrower'],
                                'Recover': ['Judgement', 'Calm Mind', 'Swords Dance', 'Will-O-Wisp', 'Toxic']
                            }
                        ),

                        # MoveSet 3: "The Perish Trapper". A specific, high-risk alternate strategy.
                        pokemon_ddl.MoveSet(
                            ['Perish Song'],
                            {
                                'Mean Look': ['Protect', 'Recover', 'Judgement'],
                                'Perish Song': ['Mean Look']
                            }
                        )
                    ), baseStats=(120, 120, 120, 120, 120, 120), genders=('',), images=('493.gif', 'arceus-electric.png', 'arceus-electric (1).png'),
                    item_key='arcElec', stat_key='arcStat'
                )

        # Rock type pokemon
        if 'Rock':
            if 'Golem':
                root.pokesets['Golem'] = pokemon_ddl.PokemonSet(
                    name='Golem', species='Golem', abilities=('Rock Head', 'Sturdy'), pkTypes=('Rock', 'Ground'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Substitute'],
                            {
                                'Protect': ['Gyro Ball', 'Stealth Rock'],
                                'Gyro Ball': ['Fling'],
                                'Fling': ['Hammer Arm'],
                                'Stealth Rock': ['Earthquake'],
                                'Earthquake': ['Stone Edge', 'Rock Blast', 'Explosion', 'Sucker Punch', 'Rock Slide'],
                                'Substitute': ['Earthquake', 'Double-Edge'],
                                'Double-Edge': ['Earthquake', 'Block', 'Dynamic Punch']
                            }
                        ),
                    ), baseStats=(80, 110, 130, 55, 65, 45), genders=('M', 'F'), images=('076.gif', '076.png', '076 (1).png')
                )
            if 'Omastar':
                root.pokesets['Omastar'] = pokemon_ddl.PokemonSet(
                    name='Omastar', species='Omastar', abilities=('Swift Swim', 'Shell Armor'),
                    pkTypes=('Rock', 'Water'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Stealth Rock', 'Spikes', 'Rain Dance', 'Hydro Pump', 'Hidden Power [Rock]'],
                                'Stealth Rock': ['Spikes', 'Ice Beam', 'Earth Power', 'Surf', 'Hydro Pump'],
                                'Spikes': ['Surf', 'Hydro Pump', 'Stealth Rock'],
                                'Surf': ['Hidden Power [Grass]', 'Earth Power', 'Ice Beam', 'Hidden Power [Rock]'],
                                'Hydro Pump': ['Hidden Power [Grass]', 'Earth Power', 'Ice Beam', 'Hidden Power [Rock]'],
                                'Rain Dance': ['Surf', 'Hydro Pump']
                            }
                        ),
                          ), baseStats=(70, 60, 125, 115, 70, 55), genders=('M', 'F'), images=('139.gif', '139.png', '139 (1).png'),
                    ability_weights=(0.8, 0.2)
                )
            if 'Kabutops':
                root.pokesets['Kabutops'] = pokemon_ddl.PokemonSet(
                    name='Kabutops', species='Kabutops', abilities=('Swift Swim', 'Battle Armor'),
                    pkTypes=('Rock', 'Water'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Rain Dance', 'Stealth Rock', 'Rapid Spin', 'Knock Off'],
                                'Rain Dance': ['Waterfall', 'Aqua Tail'],
                                'Waterfall': ['Stone Edge', 'Rock Slide'],
                                'Aqua Tail': ['Stone Edge', 'Rock Slide'],
                                'Stone Edge': ['Aqua Jet', 'Return', 'Swords Dance', 'Night Slash'],
                                'Rock Slide': ['Aqua Jet', 'Swords Dance', 'Rapid Spin', 'Confuse Ray'],
                                'Stealth Rock': ['Stone Edge', 'Rapid Spin', 'Superpower'],
                                'Rapid Spin': ['Waterfall', 'Aqua Tail', 'Aqua Jet'],
                                'Knock Off': ['Swords Dance'],
                                'Swords Dance': ['Waterfall', 'Stone Edge', 'Rock Slide', 'Aqua Tail']
                            }
                        ),
                    ), baseStats=(60, 115, 105, 65, 70, 80), genders=('M', 'F'), images=('141.gif', '141.png', '141 (1).png'),
                    ability_weights=(0.7, 0.3)
                )
            if 'Aerodactyl':
                root.pokesets['Aerodactyl'] = pokemon_ddl.PokemonSet(
                    name='Aerodactyl', species='Aerodactyl', abilities=('Rock Head', 'Pressure'),
                    pkTypes=('Rock', 'Flying'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Substitute'],
                            {
                                'Substitute': ['Roost'],
                                'Roost': ['Taunt', 'Stealth Rock', 'Dragon Claw', 'Torment'],
                                'Protect': ['Taunt', 'Torment', 'Earthquake', 'Stone Edge', 'Rock Slide'],
                                'Earthquake': ['Aerial Ace', 'Crunch', 'Defog', 'Dragon Claw', 'Fire Fang'],
                                'Stone Edge': ['Dragon Claw', 'Sky Attack', 'Ice Fang', 'Earthquake'],
                                'Rock Slide': ['Dragon Claw', 'Steel Wing', 'Sandstorm'],
                                'Dragon Claw': ['Earthquake', 'Rock Smash', 'Stone Edge', 'Rock Tomb', 'Sandstorm',
                                                'Rock Slide', 'Swagger'],
                                'Taunt': ['Earthquake', 'Rock Slide', 'Dragon Claw'],
                                'Torment': ['Earthquake', 'Stone Edge', 'Dragon Claw', 'Steel Wing'],
                                'Stealth Rock': ['Steel Wing', 'Aerial Ace', 'Dragon Claw', 'Ice Fang', 'Bite', 'Crunch']
                            }
                        ),
                          ), baseStats=(80, 105, 65, 60, 75, 130), genders=('M', 'F'), images=('142.gif', '142.png', '142 (1).png')
                )
            if 'Sudowoodo':
                root.pokesets['Sudowoodo'] = pokemon_ddl.PokemonSet(
                    name='Sudowoodo', species='Sudowoodo', abilities=('Sturdy', 'Rock Head'), pkTypes=('Rock',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Wood Hammer', 'Mimic', 'Rock Polish', 'Seismic Toss'],
                                'Wood Hammer': ['Double-Edge'],
                                'Double-Edge': ['Counter', 'Explosion', 'Stealth Rock', 'Dynamic Punch', 'Earthquake'],
                                'Mimic': ['Ice Punch'],
                                'Ice Punch': ['Wood Hammer', 'Double-Edge'],
                                'Rock Polish': ['Wood Hammer'],
                                'Seismic Toss': ['Toxic', 'Sand Tomb', 'Explosion']
                            }
                        ),
                    ), baseStats=(70, 100, 115, 30, 65, 30), genders=('M', 'F'), images=('185.gif', '185-m.png', '185-m (1).png'),
                    ability_weights=(0.2, 0.8)
                )
            if 'Shuckle':
                root.pokesets['Shuckle'] = pokemon_ddl.PokemonSet(
                    name='Shuckle', species='Shuckle', abilities=('Sturdy', 'Gluttony'), pkTypes=('Bug', 'Rock'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Knock Off', 'Rest', 'Power Trick', 'Power Trick'],
                            {
                                'Protect': ['Toxic'],
                                'Knock Off': ['Toxic'],
                                'Rest': ['Toxic', 'Protect'],
                                'Toxic': ['Encore', 'String Shot', 'Helping Hand'],
                                'Encore': ['Rest'],
                                'Power Trick': ['Gyro Ball'],
                                'Gyro Ball': ['Stone Edge', 'Rock Slide', 'Bug Bite'],
                                'Stone Edge': ['Protect'],
                                'Rock Slide': ['Protect'],
                                'Bug Bite': ['Protect']
                            }
                        ),
                    ), baseStats=(20, 10, 230, 10, 230, 5), genders=('M', 'F'), images=('213.gif', '213.png', '213 (1).png')
                )
            if 'Corsola':
                root.pokesets['Corsola'] = pokemon_ddl.PokemonSet(
                    name='Corsola', species='Corsola', abilities=('Hustle', 'Natural Cure'), pkTypes=('Water', 'Rock'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Amnesia', 'Barrier', 'Confuse Ray', 'Mirror Coat'],
                                'Amnesia': ['Toxic', 'Body Slam'],
                                'Barrier': ['Toxic', 'Body Slam'],
                                'Confuse Ray': ['Body Slam', 'Icy Wind'],
                                'Toxic': ['Recover', 'Ingrain', 'Aqua Ring', 'Recover', 'Recover'],
                                'Body Slam': ['Recover', 'Ingrain', 'Aqua Ring', 'Recover', 'Recover'],
                                'Mirror Coat': ['Recover', 'Ingrain', 'Aqua Ring', 'Recover', 'Recover']
                            }
                        ),
                    ), baseStats=(55, 55, 85, 65, 85, 35), genders=('M', 'F'), images=('222.gif', '222.png', '222 (1).png'),
                    ability_weights=(0.1, 0.9)
                )
            if 'Lunatone':
                root.pokesets['Lunatone'] = pokemon_ddl.PokemonSet(
                    name='Lunatone', species='Lunatone', abilities=('Levitate',), pkTypes=('Rock', 'Psychic'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Baton Pass'],
                            {
                                'Protect': ['Trick Room'],
                                'Baton Pass': ['Psychic'],
                                'Psychic': ['Calm Mind', 'Substitute', 'Rock Polish'],
                                'Trick Room': ['Earth Power', 'Gyro Ball', 'Helping Hand', 'Heal Block', 'Gravity', 'Gravity', 'Gravity'],
                                'Earth Power': ['Shadow Ball', 'Grass Knot', 'Psychic', 'Explosion'],
                                'Gyro Ball': ['Shadow Ball', 'Grass Knot', 'Psychic', 'Explosion'],
                                'Gravity': ['Hypnosis']
                            }
                        ),
                          ), baseStats=(70, 55, 65, 95, 85, 70), genders=('',), images=('337.gif', '337.png', '337 (1).png')
                )
            if 'Solrock':
                root.pokesets['Solrock'] = pokemon_ddl.PokemonSet(
                    name='Solrock', species='Solrock', abilities=('Levitate',), pkTypes=('Rock', 'Psychic'),
                    sets=(
                       pokemon_ddl.MoveSet(
                       ['Protect'],
                           {
                               'Protect': ['Trick Room', 'Sunny Day', 'Rock Slide'],
                               'Trick Room': ['Will-O-Wisp'],
                               'Will-O-Wisp': ['Explosion', 'Embargo', 'Helping Hand', 'Pain Split'],
                               'Sunny Day': ['Solar Beam', 'Zen Headbutt'],
                               'Rock Slide': ['Zen Headbutt', 'Explosion', 'Iron Head', 'Body Slam']
                           }
                    ),
                    ), baseStats=(70, 95, 85, 55, 65, 70), genders=('',), images=('338.gif', '338.png', '338 (1).png')
                )
            if 'Cradily':
                root.pokesets['Cradily'] = pokemon_ddl.PokemonSet(
                    name='Cradily', species='Cradily', abilities=('Suction Cups',), pkTypes=('Rock', 'Grass'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Stealth Rock', 'Seed Bomb', 'Giga Drain'],
                                'Stealth Rock': ['Toxic'],
                                'Seed Bomb': ['Toxic', 'Rock Slide'],
                                'Toxic': ['Recover'],
                                'Rock Slide': ['Recover'],
                                'Giga Drain': ['Ancient Power'],
                                'Ancient Power': ['Earth Power', 'Recover', 'Sludge Bomb', 'Wring Out']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Rest'],
                            {
                                'Rest': ['Sleep Talk', 'Seed Bomb'],
                                'Sleep Talk': ['Curse', 'Rock Slide'],
                                'Curse': ['Rock Slide'],
                                'Seed Bomb': ['Curse']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Recover'],
                            {
                                'Recover': ['Stockpile'],
                                'Swords Dance': ['Rock Slide'],
                                'Stockpile': ['Toxic'],
                                'Toxic': ['Rock Slide', 'Earthquake'],
                                'Rock Slide': ['Seed Bomb', 'Body Slam', 'Stockpile']
                            }
                        )
                    ), baseStats=(86, 81, 97, 81, 107, 43), genders=('M', 'F'), images=('346.gif', '346.png', '346 (1).png')
                )
            if 'Armaldo':
                root.pokesets['Armaldo'] = pokemon_ddl.PokemonSet(
                    name='Armaldo', species='Armaldo', abilities=('Battle Armor',), pkTypes=('Rock', 'Bug'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Swords Dance', 'Rock Polish', 'Rock Blast'],
                                'Rock Polish': ['Stone Edge', 'X-Scissor'],
                                'Swords Dance': ['Stone Edge', 'X-Scissor'],
                                'Stone Edge': ['X-Scissor', 'Aqua Tail', 'Earthquake', 'Superpower'],
                                'X-Scissor': ['Stone Edge', 'Rock Slide', 'Aqua Tail', 'Earthquake', 'Superpower'],
                                'Rock Blast': ['Stealth Rock', 'Rapid Spin', 'Knock Off', 'Toxic']
                            }
                        ),
                    ), baseStats=(75, 125, 100, 70, 80, 45), genders=('M', 'F'), images=('348.gif', '348.png', '348 (1).png')
                )
            if 'Relicanth':
                root.pokesets['Relicanth'] = pokemon_ddl.PokemonSet(
                    name='Relicanth', species='Relicanth', abilities=('Swift Swim', 'Rock Head'),
                    pkTypes=('Water', 'Rock'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Head Smash', 'Rock Polish', 'Rain Dance'],
                                'Head Smash': ['Double-Edge'],
                                'Double-Edge': ['Waterfall', 'Aqua Tail'],
                                'Rock Polish': ['Waterfall', 'Aqua Tail'],
                                'Waterfall': ['Head Smash'],
                                'Aqua Tail': ['Head Smash'],
                                'Rain Dance': ['Waterfall', 'Aqua Tail', 'Stone Edge', 'Earthquake'],
                                'Stone Edge': ['Skull Bash'],
                                'Earthquake': ['Skull Bash', 'Head Smash']
                            }
                        ),
                    ), baseStats=(100, 90, 130, 45, 65, 55), genders=('M', 'F'), images=('369.gif', '369-m.png', '369-m (1).png')
                )
            if 'Regirock':
                root.pokesets['Regirock'] = pokemon_ddl.PokemonSet(
                    name='Regirock', species='Regirock', abilities=('Clear Body',), pkTypes=('Rock',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Stealth Rock', 'Rest', 'Protect'],
                            {
                                'Stealth Rock': ['Stone Edge'],
                                'Stone Edge': ['Explosion'],
                                'Explosion': ['Thunder Wave', 'Earthquake', 'Toxic'],
                                'Rest': ['Rock Slide'],
                                'Rock Slide': ['Curse'],
                                'Curse': ['Earthquake', 'Sleep Talk'],
                                'Protect': ['Rock Polish', 'Ice Punch'],
                                'Rock Polish': ['Ice Punch'],
                                'Ice Punch': ['Earthquake'],
                                'Earthquake': ['Stone Edge', 'Rock Slide']
                            }
                        ),
                    ), baseStats=(80, 100, 200, 50, 100, 50), genders=('',), images=('377.gif', '377.png', '377 (1).png')
                )
            if 'Rampardos':
                root.pokesets['Rampardos'] = pokemon_ddl.PokemonSet(
                    name='Rampardos', species='Rampardos', abilities=('Mold Breaker',), pkTypes=('Rock',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Stone Edge', 'Rock Slide', 'Head Smash', 'Rock Polish', 'Avalanche'],
                                'Stone Edge': ['Earthquake', 'Fire Punch', 'Zen Headbutt', 'Fling', 'Outrage'],
                                'Head Smash': ['Earthquake', 'Fire Punch', 'Zen Headbutt', 'Ice Beam', 'Iron Head'],
                                'Rock Slide': ['Earthquake', 'Fire Punch', 'Zen Headbutt', 'Substitute', 'Hammer Arm', 'Pursuit'],
                                'Rock Polish': ['Rock Slide'],
                                'Avalanche': ['Payback'],
                                'Payback': ['Stone Edge', 'Rock Slide', 'Head Smash', 'Earthquake', 'Iron Head', 'Fire Punch',
                                            'Outrage', 'Superpower', 'Zen Headbutt', 'Zen Headbutt', 'Whirlpool']
                            }
                        ),
                    ), baseStats=(97, 165, 60, 65, 50, 58), genders=('M', 'F'), images=('409.gif', '409.png', '409 (1).png')
                )
            if 'Rhyperior':
                root.pokesets['Rhyperior'] = pokemon_ddl.PokemonSet(
                    name='Rhyperior', species='Rhyperior', abilities=('Lightning Rod', 'Solid Rock'),
                    pkTypes=('Rock', 'Ground'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Rock Wrecker', 'Rock Slide', 'Rock Polish'],
                                'Rock Slide': ['Swords Dance'],
                                'Swords Dance': ['Earthquake'],
                                'Rock Wrecker': ['Megahorn'],
                                'Megahorn': ['Earthquake', 'Ice Punch', 'Aqua Tail', 'Brick Break', 'Crunch', 'Dragon Rush'],
                                'Rock Polish': ['Outrage', 'Shadow Claw', 'Earthquake', 'Rock Slide', 'Stone Edge', 'Thunder Punch', 'Fire Punch', 'Rock Wrecker', 'Megahorn',
                                                'Ice Punch', 'Ice Fang', 'Iron Head', 'Iron Tail', 'Magnitude', 'Horn Drill', 'Dragon Rush',
                                                'Poison Jab', 'Rollout']
                            }
                        ),
                    ), baseStats=(115, 140, 130, 55, 55, 40), genders=('M', 'F'), images=('464.gif', '464-m.png', '464-m (1).png')
                )
            if 'Arceus-Rock':
                root.pokesets['Arceus-Rock'] = pokemon_ddl.PokemonSet(
                    name='Arceus-Rock', species='Arceus', abilities=('Multitype',), pkTypes=('Rock',),
                    sets=(
                        # MoveSet 1: "The Chaotic Bulwark". Guaranteed Protect + Judgement, then maximum variance.
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Judgement'],

                                # Judgement is the central hub for a chaotic web of possibilities.
                                'Judgement': [
                                    'Calm Mind', 'Swords Dance', 'Recover', 'Cosmic Power', 'Will-O-Wisp',
                                    'Thunder Wave', 'Extreme Speed', 'Earth Power', 'Ice Beam', 'Thunderbolt',
                                    'Flamethrower', 'Shadow Claw', 'Gravity', 'Substitute'
                                ],

                                # Every node below is heavily interconnected to create unpredictable sets.
                                'Calm Mind': ['Ice Beam', 'Thunderbolt', 'Earthquake', 'Shadow Claw', 'Recover',
                                              'Swords Dance', 'Will-O-Wisp'],
                                'Swords Dance': ['Extreme Speed', 'Dragon Claw', 'Shadow Claw', 'Earthquake', 'Surf',
                                                 'Ice Beam', 'Calm Mind'],
                                'Recover': ['Calm Mind', 'Will-O-Wisp', 'Ice Beam', 'Flamethrower', 'Substitute',
                                            'Swords Dance', 'Judgement'],
                                'Cosmic Power': ['Recover', 'Will-O-Wisp', 'Toxic', 'Flamethrower', 'Judgement'],
                                'Will-O-Wisp': ['Recover', 'Calm Mind', 'Extreme Speed', 'Dragon Claw'],
                                'Extreme Speed': ['Swords Dance', 'Shadow Claw', 'Draco Meteor', 'Overheat',
                                                  'Judgement',
                                                  'Recover'],
                                'Earth Power': ['Ice Beam', 'Thunderbolt', 'Calm Mind', 'Swords Dance', 'Dragon Claw'],
                                'Ice Beam': ['Thunderbolt', 'Earth Power', 'Judgement', 'Calm Mind', 'Swords Dance'],
                                'Thunderbolt': ['Ice Beam', 'Surf', 'Judgement', 'Calm Mind', 'Swords Dance'],
                                'Dragon Claw': ['Earthquake', 'Shadow Claw', 'Swords Dance', 'Calm Mind', 'Ice Beam'],
                                'Substitute': ['Calm Mind', 'Swords Dance', 'Recover', 'Will-O-Wisp', 'Judgement'],
                                'Gravity': ['Thunder', 'Blizzard', 'Focus Blast', 'Earthquake', 'Judgement'],
                            }
                        ),

                        # MoveSet 2: "The Chaotic Gambler". No Protect, starts with Judgement into chaos.
                        pokemon_ddl.MoveSet(
                            ['Judgement'],
                            {
                                'Judgement': [
                                    'Extreme Speed', 'Draco Meteor', 'Outrage', 'Calm Mind', 'Swords Dance',
                                    'Gravity', 'Trick Room', 'Fire Blast', 'Thunder', 'Ice Beam', 'Earthquake',
                                    'Shadow Claw', 'Will-O-Wisp', 'Recover'
                                ],

                                'Draco Meteor': ['Extreme Speed', 'Overheat', 'Earthquake', 'Fire Blast', 'Steel Wing'],
                                'Outrage': ['Extreme Speed', 'Aqua Tail', 'Iron Head', 'Ice Beam', 'Giga Drain'],
                                'Calm Mind': ['Ice Beam', 'Thunder', 'Focus Blast', 'Shadow Claw', 'Recover',
                                              'Swords Dance'],
                                'Swords Dance': ['Extreme Speed', 'Shadow Claw', 'Dragon Claw', 'Giga Drain',
                                                 'Calm Mind'],
                                'Gravity': ['Thunder', 'Blizzard', 'Focus Blast', 'Draco Meteor', 'Judgement'],
                                'Trick Room': ['Judgement', 'Draco Meteor', 'Fire Blast', 'Thunder', 'Focus Blast'],
                                'Extreme Speed': ['Judgement', 'Swords Dance', 'Draco Meteor', 'Will-O-Wisp',
                                                  'Recover'],
                                'Fire Blast': ['Draco Meteor', 'Thunder', 'Ice Beam', 'Earthquake'],
                                'Earthquake': ['Stone Edge', 'Outrage', 'Dragon Claw', 'Flamethrower'],
                                'Recover': ['Judgement', 'Calm Mind', 'Swords Dance', 'Will-O-Wisp', 'Toxic']
                            }
                        ),

                        # MoveSet 3: "The Perish Trapper". A specific, high-risk alternate strategy.
                        pokemon_ddl.MoveSet(
                            ['Perish Song'],
                            {
                                'Mean Look': ['Protect', 'Recover', 'Judgement'],
                                'Perish Song': ['Mean Look']
                            }
                        )
                    ), baseStats=(120, 120, 120, 120, 120, 120), genders=('',), images=('493.gif', 'arceus-rock.png', 'arceus-rock (1).png'),
                    item_key='arcRock', stat_key='arcStat'
                )

        # Poison type pokemon
        if 'Poison':
            if 'Venusaur':
                root.pokesets['Venusaur'] = pokemon_ddl.PokemonSet(
                    name='Venusaur', species='Venusaur', abilities=('Overgrow',), pkTypes=('Grass', 'Poison'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Leaf Storm', 'Swords Dance', 'Sunny Day', 'Frenzy Plant', 'Leech Seed'],
                                'Leaf Storm': ['Sludge Bomb'],
                                'Sludge Bomb': ['Sleep Powder', 'Hidden Power [Ice]', 'Roar', 'Synthesis'],
                                'Swords Dance': ['Power Whip'],
                                'Power Whip': ['Earthquake', 'Sleep Powder', 'Return'],
                                'Sunny Day': ['Solar Beam', 'Synthesis'],
                                'Frenzy Plant': ['Earthquake', 'Knock Off', 'Outrage', 'Sludge Bomb', 'Sleep Powder'],
                                'Leech Seed': ['Giga Drain', 'Ingrain']
                            }
                        ),
                    ), baseStats=(80, 82, 83, 100, 100, 80), genders=('M', 'F'), images=('003.gif', '003-m.png', '003-m (1).png')
                )
            if 'Beedrill':
                root.pokesets['Beedrill'] = pokemon_ddl.PokemonSet(
                    name='Beedrill', species='Beedrill', abilities=('Swarm',), pkTypes=('Bug', 'Poison'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['U-turn', 'Baton Pass', 'Swords Dance', 'Endeavor'],
                                'U-turn': ['Pursuit', 'Toxic Spikes'],
                                'Baton Pass': ['X-Scissor'],
                                'X-Scissor': ['Agility', 'Swords Dance', 'Substitute'],
                                'Swords Dance': ['X-Scissor', 'Poison Jab', 'Brick Break'],
                                'Endeavor': ['Toxic Spikes'],
                                'Toxic Spikes': ['U-turn']
                            }
                        ),
                    ), baseStats=(65, 80, 40, 45, 80, 75), genders=('M', 'F'), images=('015.gif', '015.png', '015 (1).png')
                )
            if 'Arbok':
                root.pokesets['Arbok'] = pokemon_ddl.PokemonSet(
                    name='Arbok', species='Arbok', abilities=('Intimidate', 'Shed Skin'), pkTypes=('Poison',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Glare', 'Switcheroo'],
                                'Glare': ['Gunk Shot', 'Poison Jab', 'Poison Tail'],
                                'Gunk Shot': ['Seed Bomb', 'Crunch', 'Earthquake', 'Aqua Tail', 'Iron Tail', 'Payback'],
                                'Poison Jab': ['Seed Bomb', 'Crunch', 'Earthquake', 'Fire Fang'],
                                'Switcheroo': ['Gunk Shot', 'Poison Jab', 'Poison Fang'],
                                'Poison Fang': ['Seed Bomb', 'Crunch', 'Earthquake', 'Aqua Tail', 'Iron Tail', 'Leer'],
                                'Poison Tail': ['Seed Bomb', 'Crunch', 'Earthquake', 'Fire Fang', 'Rain Dance', 'Ice Fang']
                            }
                        ),
                    ), baseStats=(60, 85, 69, 65, 79, 80), genders=('M', 'F'), images=('024.gif', '024.png', '024 (1).png')
                )
            if 'Nidoqueen':
                root.pokesets['Nidoqueen'] = pokemon_ddl.PokemonSet(
                    name='Nidoqueen', species='Nidoqueen', abilities=('Poison Point', 'Rivalry'),
                    pkTypes=('Poison', 'Ground'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Earth Power', 'Stealth Rock', 'Toxic Spikes', 'Aqua Tail', 'Poison Fang'],
                                'Earth Power': ['Ice Beam'],
                                'Ice Beam': ['Stealth Rock', 'Toxic Spikes'],
                                'Stealth Rock': ['Roar'],
                                'Toxic Spikes': ['Roar'],
                                'Aqua Tail': ['Counter', 'Poison Fang', 'Aerial Ace', 'Helping Hand', 'Toxic Spikes'],
                                'Roar': ['Earthquake', 'Earth Power', 'Toxic Spikes', 'Stealth Rock', 'Earthquake', 'Earth Power'],
                                'Poison Fang': ['Earthquake', 'Outrage', 'Mega Kick', 'Icy Wind', 'Sandstorm', 'Surf', 'Stealth Rock']
                            }
                        ),
                    ), baseStats=(90, 82, 87, 75, 85, 76), genders=('F',), images=('031.gif', '031.png', '031 (1).png')
                )
            if 'Nidoking':
                root.pokesets['Nidoking'] = pokemon_ddl.PokemonSet(
                    name='Nidoking', species='Nidoking', abilities=('Poison Point', 'Rivalry'),
                    pkTypes=('Poison', 'Ground'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Stealth Rock', 'Megahorn'],
                                'Stealth Rock': ['Taunt'],
                                'Taunt': ['Earth Power', 'Ice Beam', 'Toxic Spikes'],
                                'Megahorn': ['Earthquake', 'Outrage', 'Sucker Punch', 'Head Smash', 'Helping Hand']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Thunderbolt', 'Thunder', 'Earthquake', 'Earth Power'],
                                'Thunderbolt': ['Blizzard', 'Ice Beam'],
                                'Thunder': ['Blizzard', 'Ice Beam'],
                                'Blizzard': ['Superpower', 'Shadow Ball', 'Taunt'],
                                'Earthquake': ['Megahorn', 'Ice Beam', 'Blizzard'],
                                'Earth Power': ['Ice Beam', 'Blizzard', 'Dragon Pulse', 'Toxic Spikes']
                            }
                        )
                    ), baseStats=(81, 92, 77, 85, 75, 85), genders=('M',), images=('034.gif', '034.png', '034 (1).png')
                )
            if 'Vileplume':
                root.pokesets['Vileplume'] = pokemon_ddl.PokemonSet(
                    name='Vileplume', species='Vileplume', abilities=('Chlorophyll',), pkTypes=('Grass', 'Poison'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Sunny Day', 'Sleep Powder', 'Aromatherapy', 'Giga Drain'],
                                'Sunny Day': ['Solar Beam'],
                                'Solar Beam': ['Sludge Bomb'],
                                'Sleep Powder': ['Energy Ball', 'Sludge Bomb'],
                                'Energy Ball': ['Moonlight'],
                                'Sludge Bomb': ['Moonlight'],
                                'Aromatherapy': ['Leech Seed', 'Sleep Powder'],
                                'Leech Seed': ['Energy Ball', 'Sludge Bomb'],
                                'Giga Drain': ['Drain Punch'],
                                'Drain Punch': ['Leech Seed', 'Ingrain', 'Toxic', 'Teeter Dance']
                            }
                        ),
                    ), baseStats=(75, 80, 85, 100, 90, 50), genders=('M', 'F'), images=('045.gif', '045-m.png', '045-m (1).png')
                )
            if 'Venomoth':
                root.pokesets['Venomoth'] = pokemon_ddl.PokemonSet(
                    name='Venomoth', species='Venomoth', abilities=('Shield Dust', 'Tinted Lens'),
                    pkTypes=('Bug', 'Poison'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Bug Buzz', 'Toxic Spikes', 'Stun Spore'],
                                'Bug Buzz': ['Psychic'],
                                'Psychic': ['Roost', 'Sleep Powder', 'U-turn'],
                                'Toxic Spikes': ['Bug Buzz'],
                                'Stun Spore': ['Sleep Powder', 'Bug Buzz', 'Twister']
                            }
                        ),
                    ), baseStats=(70, 65, 60, 90, 75, 90), genders=('M', 'F'), images=('049.gif', '049.png', '049 (1).png'),
                    ability_weights=(0.2, 0.8)
                )
            if 'Victreebel':
                root.pokesets['Victreebel'] = pokemon_ddl.PokemonSet(
                    name='Victreebel', species='Victreebel', abilities=('Chlorophyll',), pkTypes=('Grass', 'Poison'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Sunny Day', 'Leaf Storm', 'Swords Dance'],
                                'Sunny Day': ['Solar Beam'],
                                'Solar Beam': ['Weather Ball'],
                                'Weather Ball': ['Sludge Bomb', 'Hidden Power [Rock]', 'Sleep Powder'],
                                'Leaf Storm': ['Sludge Bomb', 'Weather Ball'],
                                'Sludge Bomb': ['Morning Sun', 'Sucker Punch'],
                                'Swords Dance': ['Leaf Blade'],
                                'Leaf Blade': ['Sucker Punch', 'Return'],
                                'Sucker Punch': ['Sleep Powder', 'Return', 'Secret Power'],
                                'Return': ['Leaf Blade', 'Razor Leaf']
                            }
                        ),
                    ), baseStats=(80, 105, 65, 100, 60, 70), genders=('M', 'F'), images=('071.gif', '071.png', '071 (1).png')
                )
            if 'Tentacruel':
                root.pokesets['Tentacruel'] = pokemon_ddl.PokemonSet(
                    name='Tentacruel', species='Tentacruel', abilities=('Clear Body', 'Liquid Ooze'),
                    pkTypes=('Water', 'Poison'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Toxic Spikes'],
                                'Toxic Spikes': ['Rapid Spin', 'Icy Wind', 'Ice Beam'],
                                'Icy Wind': ['Hydro Pump', 'Surf', 'Hidden Power [Fire]'],
                                'Ice Beam': ['Hydro Pump', 'Surf', 'Hidden Power [Fire]'],
                                'Rapid Spin': ['Knock Off', 'Sludge Bomb', 'Surf']
                            }
                        ),
                    ), baseStats=(80, 70, 65, 80, 120, 100), genders=('M', 'F'), images=('073.gif', '073.png', '073 (1).png')
                )
            if 'Muk':
                root.pokesets['Muk'] = pokemon_ddl.PokemonSet(
                    name='Muk', species='Muk', abilities=('Sticky Hold',), pkTypes=('Poison',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Curse', 'Poison Jab', 'Gunk Shot'],
                                'Curse': ['Poison Jab'],
                                'Poison Jab': ['Shadow Sneak', 'Explosion', 'Thunder Punch', 'Ice Punch'],
                                'Gunk Shot': ['Focus Punch', 'Brick Break'],
                                'Focus Punch': ['Ice Punch', 'Explosion'],
                                'Brick Break': ['Ice Punch', 'Shadow Sneak', 'Payback']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Rest', 'Pain Split'],
                            {
                                'Rest': ['Curse'],
                                'Curse': ['Payback', 'Shadow Sneak', 'Gunk Shot'],
                                'Pain Split': ['Brick Break', 'Poison Jab', 'Gunk Shot'],
                                'Poison Jab': ['Explosion', 'Rock Slide'],
                                'Gunk Shot': ['Shadow Punch']
                            }
                        )
                    ), baseStats=(105, 105, 75, 65, 100, 50), genders=('M', 'F'), images=('089.gif', '089.png', '089 (1).png')
                )
            if 'Weezing':
                root.pokesets['Weezing'] = pokemon_ddl.PokemonSet(
                    name='Weezing', species='Weezing', abilities=('Levitate',), pkTypes=('Poison',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Double Hit', 'Will-O-Wisp', 'Sludge Bomb'],
                                'Double Hit': ['Payback', 'Will-O-Wisp', 'Assurance'],
                                'Will-O-Wisp': ['Explosion', 'Haze', 'Thunderbolt', 'Flamethrower', 'Sludge Bomb', 'Psywave'],
                                'Payback': ['Will-O-Wisp', 'Explosion', 'Rollout'],
                                'Assurance': ['Will-O-Wisp', 'Taunt', 'Toxic', 'Pain Split'],
                                'Sludge Bomb': ['Psywave', 'Shadow Ball', 'Haze', 'Will-O-Wisp', 'Thunderbolt']
                            }
                        ),
                    ), baseStats=(65, 90, 120, 85, 70, 60), genders=('M', 'F'), images=('110.gif', '110.png', '110 (1).png')
                )
            if 'Ariados':
                root.pokesets['Ariados'] = pokemon_ddl.PokemonSet(
                    name='Ariados', species='Ariados', abilities=('Swarm', 'Insomnia'), pkTypes=('Bug', 'Poison'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Spider Web', 'Toxic Spikes'],
                                'Spider Web': ['Baton Pass'],
                                'Baton Pass': ['Agility', 'Bug Bite', 'Toxic Spikes'],
                                'Toxic Spikes': ['Sucker Punch', 'Shadow Sneak', 'Night Shade'],
                                'Sucker Punch': ['Poison Jab', 'Bug Bite'],
                                'Shadow Sneak': ['Poison Jab', 'Bug Bite'],
                                'Night Shade': ['Swagger']
                            }
                        ),
                    ), baseStats=(70, 90, 70, 60, 60, 40), genders=('M', 'F'), images=('168.gif', '168.png', '168 (1).png')
                )
            if 'Crobat':
                root.pokesets['Crobat'] = pokemon_ddl.PokemonSet(
                    name='Crobat', species='Crobat', abilities=('Inner Focus',), pkTypes=('Poison', 'Flying'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Taunt', 'Cross Poison', 'Hypnosis'],
                                'Taunt': ['Brave Bird', 'Roost', 'Hypnosis'],
                                'Brave Bird': ['Roost', 'U-turn'],
                                'Roost': ['Super Fang', 'Toxic', 'Brave Bird'],
                                'Cross Poison': ['X-Scissor'],
                                'X-Scissor': ['Brave Bird', 'Steel Wing', 'Brave Bird'],
                                'Hypnosis': ['Heat Wave', 'Sludge Bomb', 'Air Slash', 'Dark Pulse']
                            }
                        ),
                    ), baseStats=(85, 90, 80, 70, 80, 130), genders=('M', 'F'), images=('169.gif', '169.png', '169 (1).png')
                )
            if 'Dustox':
                root.pokesets['Dustox'] = pokemon_ddl.PokemonSet(
                    name='Dustox', species='Dustox', abilities=('Shield Dust',), pkTypes=('Bug', 'Poison'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Ominous Wind', 'Light Screen', 'Silver Wind'],
                                'Ominous Wind': ['Whirlwind', 'Sludge Bomb', 'Bug Buzz', 'Roost', 'Bug Buzz', 'Hyper Beam'],
                                'Light Screen': ['Whirlwind', 'Sludge Bomb', 'Thief', 'Bug Buzz', 'Air Cutter'],
                                'Silver Wind': ['Ominous Wind']
                            }
                        ),
                    ), baseStats=(60, 50, 70, 50, 90, 65), genders=('M', 'F'), images=('269.gif', '269-m.png', '269-m (1).png')
                )
            if 'Swalot':
                root.pokesets['Swalot'] = pokemon_ddl.PokemonSet(
                    name='Swalot', species='Swalot', abilities=('Liquid Ooze', 'Sticky Hold'), pkTypes=('Poison',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Gastro Acid', 'Yawn', 'Stockpile'],
                                'Gastro Acid': ['Encore'],
                                'Yawn': ['Encore'],
                                'Encore': ['Pain Split', 'Ice Beam', 'Sludge Bomb'],
                                'Stockpile': ['Wring Out', 'Earthquake', 'Spit Up'],
                                'Wring Out': ['Rest'],
                                'Earthquake': ['Seed Bomb', 'Rest'],
                                'Spit Up': ['Swallow', 'Gastro Acid']
                            }
                        ),
                    ), baseStats=(100, 73, 83, 73, 83, 55), genders=('M', 'F'), images=('317.gif', '317-m.png', '317-m (1).png')
                )
            if 'Seviper':
                root.pokesets['Seviper'] = pokemon_ddl.PokemonSet(
                    name='Seviper', species='Seviper', abilities=('Shed Skin',), pkTypes=('Poison',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Poison Jab', 'Poison Fang', 'Dark Pulse'],
                                'Dark Pulse': ['Flamethrower', 'Sludge Bomb'],
                                'Poison Jab': ['Sucker Punch', 'Earthquake', 'Aqua Tail', 'X-Scissor'],
                                'Poison Fang': ['Crunch', 'Aqua Tail'],
                                'Crunch': ['Switcheroo', 'Earthquake'],
                                'Aqua Tail': ['Assurance', 'Iron Tail']
                            }
                        ),
                    ), baseStats=(73, 100, 60, 100, 60, 65), genders=('M', 'F'), images=('336.gif', '336.png', '336 (1).png')
                )
            if 'Roserade':
                root.pokesets['Roserade'] = pokemon_ddl.PokemonSet(
                    name='Roserade', species='Roserade', abilities=('Natural Cure', 'Poison Point'),
                    pkTypes=('Grass', 'Poison'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Leaf Storm', 'Spikes', 'Toxic Spikes'],
                                'Spikes': ['Grass Knot', 'Energy Ball', 'Sludge Bomb'],
                                'Grass Knot': ['Hidden Power [Fire]', 'Hidden Power [Ice]', 'Stun Spore', 'Toxic Spikes', 'Sleep Talk'],
                                'Energy Ball': ['Hidden Power [Fire]', 'Hidden Power [Ice]', 'Stun Spore', 'Toxic Spikes', 'Sleep Talk'],
                                'Sludge Bomb': ['Hidden Power [Fire]', 'Hidden Power [Ice]', 'Stun Spore', 'Toxic Spikes', 'Sleep Talk'],
                                'Toxic Spikes': ['Sleep Powder'],
                                'Sleep Powder': ['Leaf Storm', 'Hidden Power [Ground]', 'Hidden Power [Ice]', 'Hidden Power [Fire]'],
                                'Leaf Storm': ['Sleep Powder', 'Hidden Power [Fire]', 'Hidden Power [Ice]', 'Sludge Bomb', 'Toxic Spikes']
                            }
                        ),
                    ), baseStats=(60, 70, 55, 125, 105, 90), genders=('M', 'F'), images=('407.gif', '407-m.png', '407-m (1).png')
                )
            if 'Arceus-Poison':
                root.pokesets['Arceus-Poison'] = pokemon_ddl.PokemonSet(
                    name='Arceus-Poison', species='Arceus', abilities=('Multitype',), pkTypes=('Poison',),
                    sets=(
                        # MoveSet 1: "The Chaotic Bulwark". Guaranteed Protect + Judgement, then maximum variance.
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Judgement'],

                                # Judgement is the central hub for a chaotic web of possibilities.
                                'Judgement': [
                                    'Calm Mind', 'Swords Dance', 'Recover', 'Cosmic Power', 'Will-O-Wisp',
                                    'Thunder Wave', 'Extreme Speed', 'Earth Power', 'Ice Beam', 'Thunderbolt',
                                    'Flamethrower', 'Shadow Claw', 'Gravity', 'Substitute'
                                ],

                                # Every node below is heavily interconnected to create unpredictable sets.
                                'Calm Mind': ['Ice Beam', 'Thunderbolt', 'Earthquake', 'Shadow Claw', 'Recover',
                                              'Swords Dance', 'Will-O-Wisp'],
                                'Swords Dance': ['Extreme Speed', 'Dragon Claw', 'Shadow Claw', 'Earthquake', 'Surf',
                                                 'Ice Beam', 'Calm Mind'],
                                'Recover': ['Calm Mind', 'Will-O-Wisp', 'Ice Beam', 'Flamethrower', 'Substitute',
                                            'Swords Dance', 'Judgement'],
                                'Cosmic Power': ['Recover', 'Will-O-Wisp', 'Toxic', 'Flamethrower', 'Judgement'],
                                'Will-O-Wisp': ['Recover', 'Calm Mind', 'Extreme Speed', 'Dragon Claw'],
                                'Extreme Speed': ['Swords Dance', 'Shadow Claw', 'Draco Meteor', 'Overheat',
                                                  'Judgement',
                                                  'Recover'],
                                'Earth Power': ['Ice Beam', 'Thunderbolt', 'Calm Mind', 'Swords Dance', 'Dragon Claw'],
                                'Ice Beam': ['Thunderbolt', 'Earth Power', 'Judgement', 'Calm Mind', 'Swords Dance'],
                                'Thunderbolt': ['Ice Beam', 'Surf', 'Judgement', 'Calm Mind', 'Swords Dance'],
                                'Dragon Claw': ['Earthquake', 'Shadow Claw', 'Swords Dance', 'Calm Mind', 'Ice Beam'],
                                'Substitute': ['Calm Mind', 'Swords Dance', 'Recover', 'Will-O-Wisp', 'Judgement'],
                                'Gravity': ['Thunder', 'Blizzard', 'Focus Blast', 'Earthquake', 'Judgement'],
                            }
                        ),

                        # MoveSet 2: "The Chaotic Gambler". No Protect, starts with Judgement into chaos.
                        pokemon_ddl.MoveSet(
                            ['Judgement'],
                            {
                                'Judgement': [
                                    'Extreme Speed', 'Draco Meteor', 'Outrage', 'Calm Mind', 'Swords Dance',
                                    'Gravity', 'Trick Room', 'Fire Blast', 'Thunder', 'Ice Beam', 'Earthquake',
                                    'Shadow Claw', 'Will-O-Wisp', 'Recover'
                                ],

                                'Draco Meteor': ['Extreme Speed', 'Overheat', 'Earthquake', 'Fire Blast', 'Steel Wing'],
                                'Outrage': ['Extreme Speed', 'Aqua Tail', 'Iron Head', 'Ice Beam', 'Giga Drain'],
                                'Calm Mind': ['Ice Beam', 'Thunder', 'Focus Blast', 'Shadow Claw', 'Recover',
                                              'Swords Dance'],
                                'Swords Dance': ['Extreme Speed', 'Shadow Claw', 'Dragon Claw', 'Giga Drain',
                                                 'Calm Mind'],
                                'Gravity': ['Thunder', 'Blizzard', 'Focus Blast', 'Draco Meteor', 'Judgement'],
                                'Trick Room': ['Judgement', 'Draco Meteor', 'Fire Blast', 'Thunder', 'Focus Blast'],
                                'Extreme Speed': ['Judgement', 'Swords Dance', 'Draco Meteor', 'Will-O-Wisp',
                                                  'Recover'],
                                'Fire Blast': ['Draco Meteor', 'Thunder', 'Ice Beam', 'Earthquake'],
                                'Earthquake': ['Stone Edge', 'Outrage', 'Dragon Claw', 'Flamethrower'],
                                'Recover': ['Judgement', 'Calm Mind', 'Swords Dance', 'Will-O-Wisp', 'Toxic']
                            }
                        ),

                        # MoveSet 3: "The Perish Trapper". A specific, high-risk alternate strategy.
                        pokemon_ddl.MoveSet(
                            ['Perish Song'],
                            {
                                'Mean Look': ['Protect', 'Recover', 'Judgement'],
                                'Perish Song': ['Mean Look']
                            }
                        )
                    ), baseStats=(120, 120, 120, 120, 120, 120), genders=('',), images=('493.gif', 'arceus-poison.png', 'arceus-poison (1).png'),
                    item_key='arcPoison', stat_key='arcStat'
                )

        # Ground type pokemon
        if 'Ground':
            if 'Sandslash':
                root.pokesets['Sandslash'] = pokemon_ddl.PokemonSet(
                    name='Sandslash', species='Sandslash', abilities=('Sand Veil',), pkTypes=('Ground',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Dig', 'Rapid Spin', 'Swords Dance'],
                                'Rapid Spin': ['Stealth Rock', 'Toxic'],
                                'Stealth Rock': ['Shadow Claw', 'Stone Edge', 'Earthquake', 'Aerial Ace'],
                                'Toxic': ['Shadow Claw', 'Stone Edge', 'Earthquake', 'Aerial Ace'],
                                'Dig': ['Metal Claw', 'Poison Jab', 'Aerial Ace', 'Shadow Claw', 'X-Scissor'],
                                'Swords Dance': ['Earthquake'],
                                'Earthquake': ['Night Slash', 'Stone Edge']
                            }
                        ),
                    ), baseStats=(75, 100, 110, 45, 55, 65), genders=('M', 'F'), images=('028.gif', '028.png', '028 (1).png')
                )
            if 'Dugtrio':
                root.pokesets['Dugtrio'] = pokemon_ddl.PokemonSet(
                    name='Dugtrio', species='Dugtrio', abilities=('Sand Veil', 'Arena Trap'), pkTypes=('Ground',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Earthquake', 'Rock Slide', 'Beat Up', 'Fissure'],
                                'Earthquake': ['Sucker Punch', 'Night Slash', 'Rock Slide'],
                                'Rock Slide': ['Sucker Punch', 'Night Slash', 'Earthquake'],
                                'Sucker Punch': ['Substitute', 'Pursuit', 'Aerial Ace'],
                                'Night Slash': ['Substitute', 'Pursuit'],
                                'Beat Up': ['Sandstorm', 'Sunny Day'],
                                'Sandstorm': ['Earthquake'],
                                'Sunny Day': ['Earthquake'],
                                'Fissure': ['Substitute'],
                                'Substitute': ['Sand Attack']
                            }
                        ),
                    ), baseStats=(35, 80, 50, 50, 70, 120), genders=('M', 'F'), images=('051.gif', '051.png', '051 (1).png'),
                    ability_weights=(0.2, 0.8)
                )
            if 'Marowak':
                root.pokesets['Marowak'] = pokemon_ddl.PokemonSet(
                    name='Marowak', species='Marowak', abilities=('Rock Head', 'Lightning Rod'), pkTypes=('Ground',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Swords Dance', 'Double-Edge', 'Fling'],
                                'Swords Dance': ['Earthquake', 'Bonemerang', 'Bone Rush', 'Bone Club'],
                                'Earthquake': ['Stone Edge', 'Thunder Punch', 'Double-Edge'],
                                'Bonemerang': ['Stone Edge', 'Thunder Punch', 'Double-Edge'],
                                'Bone Rush': ['Stone Edge', 'Thunder Punch', 'Double-Edge'],
                                'Bone Club': ['Stone Edge', 'Thunder Punch', 'Double-Edge'],
                                'Double-Edge': ['Fire Punch', 'Thunder Punch', 'Earthquake'],
                                'Fling': ['Iron Head', 'Outrage', 'Skull Bash', 'Stealth Rock']
                            }
                        ),
                    ), baseStats=(60, 80, 110, 50, 80, 45), genders=('M', 'F'), images=('105.gif', '105.png', '105 (1).png'),
                    item_key='maro'
                )
            if 'Quagsire':
                root.pokesets['Quagsire'] = pokemon_ddl.PokemonSet(
                    name='Quagsire', species='Quagsire', abilities=('Damp', 'Water Absorb'),
                    pkTypes=('Water', 'Ground'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Recover'],
                            {
                                'Protect': ['Earthquake', 'Yawn'],
                                'Recover': ['Encore', 'Yawn', 'Toxic'],
                                'Yawn': ['Earthquake', 'Aqua Tail', 'Stone Edge'],
                                'Earthquake': ['Counter', 'Brick Break', 'Dynamic Punch'],
                                'Counter': ['Stone Edge', 'Aqua Tail', 'Haze', 'Icy Wind', 'Waterfall'],
                                'Brick Break': ['Stone Edge', 'Aqua Tail', 'Haze', 'Icy Wind', 'Waterfall'],
                                'Dynamic Punch': ['Stone Edge', 'Aqua Tail', 'Haze', 'Icy Wind', 'Waterfall']

                            }
                        ),
                    ), baseStats=(95, 85, 85, 65, 65, 35), genders=('M', 'F'), images=('195.gif', '195-m.png', '195-m (1).png'),
                    ability_weights=(0.2, 0.8)
                )
            if 'Donphan':
                root.pokesets['Donphan'] = pokemon_ddl.PokemonSet(
                    name='Donphan', species='Donphan', abilities=('Sturdy',), pkTypes=('Ground',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Earthquake'],
                                'Earthquake': ['Rock Slide', 'Assurance', 'Superpower', 'Gyro Ball'],
                                'Rock Slide': ['Seed Bomb', 'Poison Jab', 'Fissure', 'Counter', 'Sandstorm'],
                                'Assurance': ['Rapid Spin', 'Stealth Rock', 'Ice Shard', 'Head Smash'],
                                'Gyro Ball': ['Thunder Fang', 'Fire Fang', 'Ice Shard'],
                                'Superpower': ['Gunk Shot', 'Giga Impact', 'Head Smash', 'Ice Shard', 'Last Resort']
                            }
                        ),
                    ), baseStats=(90, 120, 120, 60, 60, 50), genders=('M', 'F'), images=('232.gif', '232-m.png', '232-m (1).png')
                )
            if 'Swampert':
                root.pokesets['Swampert'] = pokemon_ddl.PokemonSet(
                    name='Swampert', species='Swampert', abilities=('Torrent',), pkTypes=('Water', 'Ground'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Stealth Rock'],
                                'Stealth Rock': ['Ice Beam', 'Roar', 'Hydro Pump', 'Earthquake'],
                                'Ice Beam': ['Earthquake'],
                                'Roar': ['Earthquake'],
                                'Hydro Pump': ['Ice Beam', 'Earth Power'],
                                'Earthquake': ['Waterfall', 'Ice Punch']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Earthquake'],
                                'Earthquake': ['Waterfall', 'Ice Beam'],
                                'Waterfall': ['Stone Edge', 'Superpower', 'Ice Punch'],
                                'Ice Beam': ['Hydro Pump', 'Focus Punch']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Hydro Pump'],
                                'Hydro Pump': ['Earth Power'],
                                'Earth Power': ['Ice Beam', 'Hidden Power [Grass]', 'Hidden Power [Electric]', 'Sleep Talk']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Rest'],
                            {
                                'Rest': ['Curse'],
                                'Curse': ['Earthquake', 'Waterfall', 'Aqua Tail', 'Counter', 'Mirror Coat'],
                                'Earthquake': ['Ice Punch', 'Waterfall', 'Sleep Talk'],
                                'Waterfall': ['Ice Punch', 'Sleep Talk'],
                                'Aqua Tail': ['Ice Punch', 'Sleep Talk', 'Outrage']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Ancient Power', 'Yawn', 'Earthquake'],
                                'Ancient Power': ['Hydro Pump', 'Hydro Cannon', 'Surf', 'Muddy Water'],
                                'Hydro Pump': ['Ice Beam', 'Focus Blast', 'Earth Power'],
                                'Hydro Cannon': ['Ice Beam', 'Focus Blast', 'Earth Power'],
                                'Surf': ['Ice Beam', 'Focus Blast', 'Earth Power'],
                                'Muddy Water': ['Ice Beam', 'Focus Blast', 'Earth Power'],
                                'Yawn': ['Bite', 'Outrage', 'Earthquake', 'Aqua Tail', 'Hammer Arm', 'Iron Tail'],
                                'Earthquake': ['Curse', 'Avalanche']
                            }
                        )
                    ), baseStats=(100, 110, 90, 85, 90, 60), genders=('M', 'F'), images=('260.gif', '260.png', '260 (1).png')
                )
            if 'Whiscash':
                root.pokesets['Whiscash'] = pokemon_ddl.PokemonSet(
                    name='Whiscash', species='Whiscash', abilities=('Oblivious', 'Anticipation'),
                    pkTypes=('Water', 'Ground'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Dragon Dance', 'Icy Wind'],
                                'Dragon Dance': ['Waterfall', 'Aqua Tail', 'Zen Headbutt', 'Spark'],
                                'Waterfall': ['Earthquake', 'Stone Edge', 'Bounce'],
                                'Aqua Tail': ['Earthquake', 'Stone Edge', 'Bounce'],
                                'Zen Headbutt': ['Earthquake', 'Stone Edge', 'Bounce'],
                                'Icy Wind': ['Attract', 'Double Team', 'Rock Slide'],
                                'Attract': ['Fissure', 'Stone Edge', 'Surf', 'Thrash', 'Rock Slide'],
                                'Double Team': ['Fissure', 'Stone Edge', 'Surf', 'Thrash', 'Rock Slide'],
                                'Rock Slide': ['Earthquake', 'Fissure', 'Earth Power', 'Blizzard']
                            }
                        ),
                    ), baseStats=(110, 78, 73, 76, 71, 60), genders=('M', 'F'), images=('340.gif', '340.png', '340 (1).png')
                )
            if 'Claydol':
                root.pokesets['Claydol'] = pokemon_ddl.PokemonSet(
                    name='Claydol', species='Claydol', abilities=('Levitate',), pkTypes=('Ground', 'Psychic'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Protect', 'Protect', 'Rest', 'Protect'],
                            {
                                'Protect': ['Trick', 'Trick Room', 'Charge Beam', 'Rapid Spin', 'Stealth Rock', 'Reflect', 'Light Screen', 'Stealth Rock', 'Ancient Power'],
                                'Trick': ['Stealth Rock', 'Rapid Spin', 'Trick Room'],
                                'Stealth Rock': ['Earth Power', 'Explosion', 'Trick Room'],
                                'Rapid Spin': ['Earth Power', 'Explosion'],
                                'Trick Room': ['Grass Knot', 'Zen Headbutt', 'Earthquake', 'Light Screen', 'Reflect', 'Psychic', 'Explosion', 'Earth Power', 'Stone Edge'],
                                'Charge Beam': ['Earth Power', 'Ice Beam', 'Shadow Ball', 'Ancient Power', 'Psychic', 'Trick Room'],
                                'Rest': ['Cosmic Power', 'Sleep Talk', 'Toxic'],
                                'Ancient Power': ['Solar Beam', 'Rain Dance'],
                                'Solar Beam': ['Sunny Day'],
                                'Rain Dance': ['Psychic']
                            }
                        ),
                    ), baseStats=(60, 70, 105, 70, 120, 75), genders=('',), images=('344.gif', '344.png', '344 (1).png')
                )
            if 'Groudon':
                root.pokesets['Groudon'] = pokemon_ddl.PokemonSet(
                    name='Groudon', species='Groudon', abilities=('Drought',), pkTypes=('Ground',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Solar Beam', 'Eruption', 'Defense Curl', 'Counter', 'Stealth Rock', 'Protect'],
                            {
                                'Solar Beam': ['Uproar', 'Thunderbolt', 'Swift', 'Seismic Toss', 'Overheat', 'Lava Plume', 'Hyper Beam',
                                               'Hidden Power [Ice]', 'Focus Blast', 'Flamethrower', 'Fire Blast',
                                               'Earth Power', 'Dragon Pulse', 'Ancient Power', 'Block', 'Counter', 'Double Team', 'Protect',
                                               'Mimic', 'Roar'],
                                'Eruption': ['Earthquake', 'Earth Power', 'Dragon Pulse', 'Dragon Claw', 'Stone Edge', 'Rock Polish',
                                             'Rock Slide', 'Rock Climb', 'Rest', 'Protect', 'Iron Head', 'Iron Tail', 'Mega Punch',
                                             'Mega Kick', 'Mud Shot', 'Giga Impact', 'Hyper Beam', 'Hammer Arm'],
                                'Defense Curl': ['Rollout'],
                                'Rollout': ['Earth Power', 'Earthquake', 'Fire Punch', 'Dragon Claw', 'Double-Edge'],
                                'Counter': ['Fling', 'Dynamic Punch', 'Dragon Pulse', 'Dragon Claw', 'Earthquake', 'Protect', 'Fury Cutter',
                                            'Hammer Arm', 'Hidden Power [Dark]', 'Solar Beam', 'Fire Punch'],
                                'Stealth Rock': ['Roar', 'Mud Shot', 'Shadow Claw', 'Shock Wave'],
                                'Protect': ['Bulk Up', 'Rock Polish', 'Swords Dance'],
                                'Bulk Up': ['Shadow Claw', 'Earthquake', 'Rock Tomb', 'Fire Punch', 'Brick Break', 'Dragon Claw', 'Slash'],
                                'Rock Polish': ['Shadow Claw', 'Earthquake', 'Rock Tomb', 'Fire Punch', 'Brick Break', 'Dragon Claw', 'Slash'],
                                'Swords Dance': ['Shadow Claw', 'Earthquake', 'Rock Tomb', 'Fire Punch', 'Brick Break', 'Dragon Claw', 'Slash']
                            }
                        ),
                    ), baseStats=(100, 150, 140, 100, 90, 90), genders=('',), images=('383.gif', '383.png', '383 (1).png')
                )
            if 'Torterra':
                root.pokesets['Torterra'] = pokemon_ddl.PokemonSet(
                    name='Torterra', species='Torterra', abilities=('Overgrow',), pkTypes=('Grass', 'Ground'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Rock Polish', 'Reflect', 'Wood Hammer', 'Rock Polish', 'Curse'],
                                'Rock Polish': ['Earthquake', 'Stone Edge', 'Earthquake', 'Rock Slide'],
                                'Earthquake': ['Wood Hammer', 'Seed Bomb', 'Crunch', 'Superpower', 'Razor Leaf', 'Stone Edge'],
                                'Stone Edge': ['Wood Hammer', 'Seed Bomb', 'Crunch', 'Superpower', 'Razor Leaf', 'Earthquake'],
                                'Rock Slide': ['Earthquake', 'Wood Hammer', 'Seed Bomb'],
                                'Reflect': ['Light Screen', 'Stealth Rock', 'Earthquake', 'Synthesis'],
                                'Light Screen': ['Earthquake', 'Wood Hammer', 'Outrage'],
                                'Stealth Rock': ['Roar', 'Stone Edge', 'Iron Tail', 'Giga Impact'],
                                'Wood Hammer': ['Rock Polish', 'Earthquake', 'Rock Slide', 'Rest'],
                                'Curse': ['Hammer Arm', 'Avalanche', 'Earthquake', 'Stone Edge']
                            }
                        ),
                    ), baseStats=(95, 109, 105, 75, 85, 56), genders=('M', 'F'), images=('389.gif', '389.png', '389 (1).png')
                )
            if 'Wormadam-Sandy':
                root.pokesets['Wormadam-Sandy'] = pokemon_ddl.PokemonSet(
                    name='Wormadam-Sandy', species='Wormadam', abilities=('Anticipation',), pkTypes=('Bug', 'Ground'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Rest'],
                            {
                                'Protect': ['Fissure', 'Earthquake'],
                                'Fissure': ['Bug Bite', 'Rain Dance'],
                                'Bug Bite': ['Toxic'],
                                'Rain Dance': ['Toxic'],
                                'Earthquake': ['Bug Bite', 'Rain Dance'],
                                'Rest': ['Sleep Talk'],
                                'Sleep Talk': ['Earthquake', 'Toxic']
                            }
                        ),
                    ), baseStats=(60, 79, 105, 59, 85, 36), genders=('F',), images=('413.gif', '413-c.png', '413-c (1).png')
                )
            if 'Gastrodon':
                root.pokesets['Gastrodon'] = pokemon_ddl.PokemonSet(
                    name='Gastrodon', species='Gastrodon', abilities=('Sticky Hold', 'Storm Drain'),
                    pkTypes=('Water', 'Ground'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Curse'],
                            {
                                'Curse': ['Recover', 'Waterfall', 'Earthquake']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Recover'],
                            {
                                'Recover': ['Icy Wind', 'Muddy Water', 'Fissure', 'Mirror Coat', 'Mud Bomb', 'Yawn', 'Protect', 'Protect', 'Toxic', 'Hidden Power [Electric]', 'Protect']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Recover'],
                            {
                                'Recover': ['Icy Wind', 'Muddy Water', 'Fissure', 'Mirror Coat', 'Mud Bomb', 'Yawn', 'Protect', 'Protect', 'Toxic', 'Hidden Power [Electric]', 'Protect']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Recover', 'Protect'],
                            {
                                'Recover': ['Amnesia', 'Muddy Water', 'Blizzard', 'Brine', 'Earth Power', 'Icy Wind', 'Ice Beam', 'Surf', 'Mud Bomb'],
                                'Protect': ['Amnesia', 'Muddy Water', 'Blizzard', 'Brine', 'Earth Power', 'Icy Wind', 'Ice Beam', 'Surf'],
                                'Muddy Water': ['Blizzard', 'Ice Beam', 'Icy Wind', 'Sludge Bomb', 'Hidden Power [Electric]', 'Earth Power'],
                                'Brine': ['Blizzard', 'Ice Beam', 'Icy Wind', 'Sludge Bomb', 'Hidden Power [Electric]', 'Earth Power'],
                                'Surf': ['Blizzard', 'Ice Beam', 'Icy Wind', 'Sludge Bomb', 'Hidden Power [Electric]', 'Earth Power'],
                                'Blizzard': ['Surf', 'Muddy Water', 'Brine', 'Water Pulse', 'Sludge Bomb', 'Hidden Power [Fire]', 'Earth Power'],
                                'Ice Beam': ['Surf', 'Muddy Water', 'Brine', 'Water Pulse', 'Sludge Bomb', 'Hidden Power [Fire]', 'Earth Power'],
                                'Icy Wind': ['Surf', 'Muddy Water', 'Brine', 'Water Pulse', 'Sludge Bomb', 'Hidden Power [Fire]', 'Earth Power']
                            }
                        )
                    ), baseStats=(111, 83, 68, 92, 82, 39), genders=('M', 'F'), images=('423.gif', '423-w.png', '423-w (1).png')
                )
            if 'Gastrodon-East':
                root.pokesets['Gastrodon-East'] = pokemon_ddl.PokemonSet(
                    name='Gastrodon-East', species='Gastrodon', abilities=('Sticky Hold', 'Storm Drain'),
                    pkTypes=('Water', 'Ground'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Curse'],
                            {
                                'Curse': ['Recover', 'Waterfall', 'Earthquake']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Recover'],
                            {
                                'Recover': ['Icy Wind', 'Muddy Water', 'Fissure', 'Mirror Coat', 'Mud Bomb', 'Yawn',
                                            'Protect', 'Protect', 'Toxic', 'Hidden Power [Electric]', 'Protect']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Recover'],
                            {
                                'Recover': ['Icy Wind', 'Muddy Water', 'Fissure', 'Mirror Coat', 'Mud Bomb', 'Yawn',
                                            'Protect', 'Protect', 'Toxic', 'Hidden Power [Electric]', 'Protect']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Recover', 'Protect'],
                            {
                                'Recover': ['Amnesia', 'Muddy Water', 'Blizzard', 'Brine', 'Earth Power', 'Icy Wind',
                                            'Ice Beam', 'Surf', 'Mud Bomb'],
                                'Protect': ['Amnesia', 'Muddy Water', 'Blizzard', 'Brine', 'Earth Power', 'Icy Wind',
                                            'Ice Beam', 'Surf'],
                                'Muddy Water': ['Blizzard', 'Ice Beam', 'Icy Wind', 'Sludge Bomb',
                                                'Hidden Power [Electric]', 'Earth Power'],
                                'Brine': ['Blizzard', 'Ice Beam', 'Icy Wind', 'Sludge Bomb', 'Hidden Power [Electric]',
                                          'Earth Power'],
                                'Surf': ['Blizzard', 'Ice Beam', 'Icy Wind', 'Sludge Bomb', 'Hidden Power [Electric]',
                                         'Earth Power'],
                                'Blizzard': ['Surf', 'Muddy Water', 'Brine', 'Water Pulse', 'Sludge Bomb',
                                             'Hidden Power [Fire]', 'Earth Power'],
                                'Ice Beam': ['Surf', 'Muddy Water', 'Brine', 'Water Pulse', 'Sludge Bomb',
                                             'Hidden Power [Fire]', 'Earth Power'],
                                'Icy Wind': ['Surf', 'Muddy Water', 'Brine', 'Water Pulse', 'Sludge Bomb',
                                             'Hidden Power [Fire]', 'Earth Power']
                            }
                        )
                    ), baseStats=(111, 83, 68, 92, 82, 39), genders=('M', 'F'), images=('423.gif', '423-e.png', '423-e (1).png')
                )
            if 'Garchomp':
                root.pokesets['Garchomp'] = pokemon_ddl.PokemonSet(
                    name='Garchomp', species='Garchomp', abilities=('Sand Veil',), pkTypes=('Dragon', 'Ground'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Stealth Rock', 'Dragon Rush', 'Sandstorm'],
                                'Dragon Rush': ['Thrash', 'Outrage', 'Take Down', 'Strength', 'Stone Edge', 'Slash', 'Shadow Claw', 'Secret Power',
                                                'Sand Tomb', 'Sand Attack', 'Rock Smash', 'Rock Slide', 'Roar', 'Rock Climb', 'Rest',
                                                'Poison Jab', 'Metal Claw', 'Iron Tail', 'Iron Head', 'Hyper Beam', 'Headbutt',
                                                'Giga Impact', 'Fury Cutter', 'Fling', 'Flamethrower', 'Fire Fang', 'Fire Blast', 'Facade', 'Endure',
                                                'Earthquake', 'Earth Power', 'Dragon Claw', 'Dragon Breath', 'Draco Meteor',
                                                'Double Team', 'Brick Break', 'Aqua Tail', 'Aerial Ace', 'Surf', 'Dig', 'Crunch'],
                                'Stealth Rock': ['Outrage', 'Dragon Rush', 'Dragon Claw', 'Dragon Pulse', 'Aqua Tail', 'Roar', 'Fire Blast',
                                                 'Iron Head', 'Aerial Ace', 'Poison Jab', 'Roar', 'Roar', 'Rock Smash', 'Shadow Claw', 'Dig',
                                                 'Crunch'],
                                'Sandstorm': ['Double Team', 'Sand Tomb'],
                                'Double Team': ['Outrage', 'Dragon Claw', 'Dragon Rush'],
                                'Sand Tomb': ['Thrash', 'Outrage', 'Take Down', 'Strength', 'Stone Edge', 'Slash', 'Shadow Claw', 'Secret Power',
                                                'Sand Tomb', 'Sand Attack', 'Rock Smash', 'Rock Slide', 'Roar', 'Rock Climb', 'Rest',
                                                'Poison Jab', 'Metal Claw', 'Iron Tail', 'Iron Head', 'Hyper Beam', 'Headbutt',
                                                'Giga Impact', 'Fury Cutter', 'Fling', 'Flamethrower', 'Fire Fang', 'Fire Blast', 'Facade', 'Endure',
                                                'Earthquake', 'Earth Power', 'Dragon Claw', 'Dragon Breath', 'Draco Meteor',
                                                'Double Team', 'Brick Break', 'Aqua Tail', 'Aerial Ace', 'Surf', 'Dig', 'Crunch']
                            }
                        ),
                    ), baseStats=(108, 130, 95, 80, 85, 102), genders=('M', 'F'), images=('445.gif', '445-m.png', '445-m (1).png')
                )
            if 'Hippowdon':
                root.pokesets['Hippowdon'] = pokemon_ddl.PokemonSet(
                    name='Hippowdon', species='Hippowdon', abilities=('Sand Stream',), pkTypes=('Ground',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Slack Off'],
                            {
                                'Protect': ['Stealth Rock', 'Earthquake', 'Slack Off'],
                                'Stealth Rock': ['Roar', 'Ice Fang', 'Fire Fang'],
                                'Earthquake': ['Rock Slide', 'Swagger'],
                                'Slack Off': ['Stealth Rock', 'Earthquake', 'Swagger'],
                                'Roar': ['Earthquake', 'Thunder Fang', 'Rock Tomb'],
                                'Ice Fang': ['Crunch', 'Earthquake', 'Stone Edge'],
                                'Fire Fang': ['Earthquake', 'Superpower']
                            }
                        ),
                    ), baseStats=(108, 112, 118, 68, 72, 47), genders=('M', 'F'), images=('450.gif', '450-m.png', '450-m (1).png')
                )
            if 'Gliscor':
                root.pokesets['Gliscor'] = pokemon_ddl.PokemonSet(
                    name='Gliscor', species='Gliscor', abilities=('Hyper Cutter', 'Sand Veil'),
                    pkTypes=('Ground', 'Flying'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Swords Dance'],
                                'Swords Dance': ['Baton Pass', 'Earthquake'],
                                'Baton Pass': ['Aerial Ace', 'Earthquake'],
                                'Earthquake': ['X-Scissor', 'Ice Fang', 'Aerial Ace', 'Thunder Fang', 'Sky Attack']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Taunt'],
                                'Taunt': ['Roost', 'Earthquake'],
                                'Roost': ['Ice Fang', 'Knock Off', 'Wing Attack', 'Earthquake'],
                                'Earthquake': ['Ice Fang', 'Knock Off', 'Wing Attack']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Substitute', 'Taunt'],
                            {
                                'Substitute': ['Roost'],
                                'Taunt': ['Roost'],
                                'Roost': ['Toxic'],
                                'Toxic': ['Earthquake']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Aqua Tail', 'Brick Break', 'Cross Poison', 'Aerial Ace', 'Counter', 'Dig', 'Earthquake',
                                            'Facade', 'Feint Attack', 'Fire Fang', 'Fling', 'Guillotine', 'Ice Fang', 'Iron Tail',
                                            'Knock Off', 'Metal Claw', 'Night Slash', 'Power Trick', 'Quick Attack', 'Roost', 'Sand Attack',
                                            'Sky Attack', 'Slash', 'Steel Wing', 'Stealth Rock', 'Stone Edge', 'Swagger', 'Swords Dance', 'Taunt',
                                            'Thunder Fang', 'Torment', 'Toxic', 'U-turn', 'Wing Attack', 'X-Scissor']
                            }
                        )
                    ), baseStats=(75, 95, 125, 45, 75, 95), genders=('M', 'F'), images=('472.gif', '472.png', '472 (1).png')
                )
            if 'Arceus-Ground':
                root.pokesets['Arceus-Ground'] = pokemon_ddl.PokemonSet(
                    name='Arceus-Ground', species='Arceus', abilities=('Multitype',), pkTypes=('Ground',),
                    sets=(
                        # MoveSet 1: "The Chaotic Bulwark". Guaranteed Protect + Judgement, then maximum variance.
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Judgement'],

                                # Judgement is the central hub for a chaotic web of possibilities.
                                'Judgement': [
                                    'Calm Mind', 'Swords Dance', 'Recover', 'Cosmic Power', 'Will-O-Wisp',
                                    'Thunder Wave', 'Extreme Speed', 'Earth Power', 'Ice Beam', 'Thunderbolt',
                                    'Flamethrower', 'Shadow Claw', 'Gravity', 'Substitute'
                                ],

                                # Every node below is heavily interconnected to create unpredictable sets.
                                'Calm Mind': ['Ice Beam', 'Thunderbolt', 'Earthquake', 'Shadow Claw', 'Recover',
                                              'Swords Dance', 'Will-O-Wisp'],
                                'Swords Dance': ['Extreme Speed', 'Dragon Claw', 'Shadow Claw', 'Earthquake', 'Surf',
                                                 'Ice Beam', 'Calm Mind'],
                                'Recover': ['Calm Mind', 'Will-O-Wisp', 'Ice Beam', 'Flamethrower', 'Substitute',
                                            'Swords Dance', 'Judgement'],
                                'Cosmic Power': ['Recover', 'Will-O-Wisp', 'Toxic', 'Flamethrower', 'Judgement'],
                                'Will-O-Wisp': ['Recover', 'Calm Mind', 'Extreme Speed', 'Dragon Claw'],
                                'Extreme Speed': ['Swords Dance', 'Shadow Claw', 'Draco Meteor', 'Overheat',
                                                  'Judgement',
                                                  'Recover'],
                                'Earth Power': ['Ice Beam', 'Thunderbolt', 'Calm Mind', 'Swords Dance', 'Dragon Claw'],
                                'Ice Beam': ['Thunderbolt', 'Earth Power', 'Judgement', 'Calm Mind', 'Swords Dance'],
                                'Thunderbolt': ['Ice Beam', 'Surf', 'Judgement', 'Calm Mind', 'Swords Dance'],
                                'Dragon Claw': ['Earthquake', 'Shadow Claw', 'Swords Dance', 'Calm Mind', 'Ice Beam'],
                                'Substitute': ['Calm Mind', 'Swords Dance', 'Recover', 'Will-O-Wisp', 'Judgement'],
                                'Gravity': ['Thunder', 'Blizzard', 'Focus Blast', 'Earthquake', 'Judgement'],
                            }
                        ),

                        # MoveSet 2: "The Chaotic Gambler". No Protect, starts with Judgement into chaos.
                        pokemon_ddl.MoveSet(
                            ['Judgement'],
                            {
                                'Judgement': [
                                    'Extreme Speed', 'Draco Meteor', 'Outrage', 'Calm Mind', 'Swords Dance',
                                    'Gravity', 'Trick Room', 'Fire Blast', 'Thunder', 'Ice Beam', 'Earthquake',
                                    'Shadow Claw', 'Will-O-Wisp', 'Recover'
                                ],

                                'Draco Meteor': ['Extreme Speed', 'Overheat', 'Earthquake', 'Fire Blast', 'Steel Wing'],
                                'Outrage': ['Extreme Speed', 'Aqua Tail', 'Iron Head', 'Ice Beam', 'Giga Drain'],
                                'Calm Mind': ['Ice Beam', 'Thunder', 'Focus Blast', 'Shadow Claw', 'Recover',
                                              'Swords Dance'],
                                'Swords Dance': ['Extreme Speed', 'Shadow Claw', 'Dragon Claw', 'Giga Drain',
                                                 'Calm Mind'],
                                'Gravity': ['Thunder', 'Blizzard', 'Focus Blast', 'Draco Meteor', 'Judgement'],
                                'Trick Room': ['Judgement', 'Draco Meteor', 'Fire Blast', 'Thunder', 'Focus Blast'],
                                'Extreme Speed': ['Judgement', 'Swords Dance', 'Draco Meteor', 'Will-O-Wisp',
                                                  'Recover'],
                                'Fire Blast': ['Draco Meteor', 'Thunder', 'Ice Beam', 'Earthquake'],
                                'Earthquake': ['Stone Edge', 'Outrage', 'Dragon Claw', 'Flamethrower'],
                                'Recover': ['Judgement', 'Calm Mind', 'Swords Dance', 'Will-O-Wisp', 'Toxic']
                            }
                        ),

                        # MoveSet 3: "The Perish Trapper". A specific, high-risk alternate strategy.
                        pokemon_ddl.MoveSet(
                            ['Perish Song'],
                            {
                                'Mean Look': ['Protect', 'Recover', 'Judgement'],
                                'Perish Song': ['Mean Look']
                            }
                        )
                    ), baseStats=(120, 120, 120, 120, 120, 120), genders=('',), images=('493.gif', 'arceus-ground.png', 'arceus-ground (1).png'),
                    item_key='arcGround', stat_key='arcStat'
                )

        # Bug type pokemon
        if 'Bug':
            if 'Butterfree':
                root.pokesets['Butterfree'] = pokemon_ddl.PokemonSet(
                    name='Butterfree', species='Butterfree', abilities=('Compound Eyes',), pkTypes=('Bug', 'Flying'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Sleep Powder'],
                                'Sleep Powder': ['U-turn', 'Stun Spore'],
                                'U-turn': ['Bug Buzz', 'Swagger', 'Tailwind', 'Giga Drain'],
                                'Stun Spore': ['U-turn', 'Bug Buzz', 'Giga Drain']
                            }
                        ),
                    ), baseStats=(60, 45, 50, 80, 80, 70), genders=('M', 'F'), images=('012.gif', '012-m.png', '012-m (1).png')
                )
            if 'Parasect':
                root.pokesets['Parasect'] = pokemon_ddl.PokemonSet(
                    name='Parasect', species='Parasect', abilities=('Effect Spore', 'Dry Skin'),
                    pkTypes=('Bug', 'Grass'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Spore'],
                                'Spore': ['Synthesis', 'Stun Spore', 'X-Scissor', 'Brick Break'],
                                'Synthesis': ['Seed Bomb', 'X-Scissor'],
                                'Stun Spore': ['Seed Bomb', 'X-Scissor'],
                                'X-Scissor': ['Seed Bomb'],
                                'Brick Break': ['X-Scissor', 'Pursuit', 'Synthesis', 'Seed Bomb', 'Cross Poison', 'Knock Off', 'Light Screen']
                            }
                        ),
                    ), baseStats=(60, 95, 80, 60, 80, 30), genders=('M', 'F'), images=('047.gif', '047.png', '047 (1).png')
                )
            if 'Pinsir':
                root.pokesets['Pinsir'] = pokemon_ddl.PokemonSet(
                    name='Pinsir', species='Pinsir', abilities=('Hyper Cutter', 'Mold Breaker'), pkTypes=('Bug',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Swords Dance', 'Stealth Rock', 'X-Scissor', 'Guillotine'],
                                'Swords Dance': ['Close Combat', 'Earthquake'],
                                'Close Combat': ['X-Scissor', 'Stone Edge'],
                                'Earthquake': ['X-Scissor', 'Stone Edge'],
                                'Stealth Rock': ['Stone Edge', 'Quick Attack'],
                                'Stone Edge': ['X-Scissor', 'Close Combat', 'Earthquake'],
                                'Quick Attack': ['X-Scissor', 'Close Combat', 'Earthquake'],
                                'X-Scissor': ['Giga Impact', 'Close Combat', 'Stone Edge', 'Earthquake'],
                                'Guillotine': ['Substitute'],
                                'Substitute': ['Close Combat', 'Seismic Toss']
                            }
                        ),
                    ), baseStats=(65, 125, 100, 55, 70, 85), genders=('M', 'F'), images=('127.gif', '127.png', '127 (1).png')
                )
            if 'Ledian':
                root.pokesets['Ledian'] = pokemon_ddl.PokemonSet(
                    name='Ledian', species='Ledian', abilities=('Swarm', 'Early Bird'), pkTypes=('Bug', 'Flying'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Agility', 'Swords Dance', 'Silver Wind', 'Agility'],
                                'Agility': ['Swords Dance', 'Baton Pass'],
                                'Swords Dance': ['Agility', 'Baton Pass'],
                                'Baton Pass': ['Agility', 'Swords Dance', 'Roost', 'Encore', 'Silver Wind'],
                                'Silver Wind': ['Agility', 'Ominous Wind'],
                                'Ominous Wind': ['Hyper Beam', 'Focus Blast', 'Encore', 'Toxic']
                            }
                        ),
                    ), baseStats=(55, 35, 50, 55, 110, 85), genders=('M', 'F'), images=('166.gif', '166-m.png', '166-m (1).png'),
                    ability_weights=(0.2, 0.8)
                )
            if 'Beautifly':
                root.pokesets['Beautifly'] = pokemon_ddl.PokemonSet(
                    name='Beautifly', species='Beautifly', abilities=('Swarm',), pkTypes=('Bug', 'Flying'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Bug Buzz'],
                                'Bug Buzz': ['Hidden Power [Ground]', 'Shadow Ball', 'Psychic'],
                                'Hidden Power [Ground]': ['Stun Spore', 'U-turn', 'Air Cutter'],
                                'Shadow Ball': ['Stun Spore', 'U-turn', 'Air Cutter', 'Whirlwind']
                            }
                        ),
                    ), baseStats=(60, 70, 50, 90, 50, 65), genders=('M', 'F'), images=('267.gif', '267-m.png', '267-m (1).png')
                )
            if 'Masquerain':
                root.pokesets['Masquerain'] = pokemon_ddl.PokemonSet(
                    name='Masquerain', species='Masquerain', abilities=('Intimidate',), pkTypes=('Bug', 'Flying'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Agility', 'Air Slash', 'Bug Buzz'],
                                'Agility': ['Baton Pass'],
                                'Baton Pass': ['Hydro Pump', 'Blizzard', 'Air Slash', 'Bug Buzz'],
                                'Air Slash': ['Hydro Pump', 'Roost', 'Energy Ball', 'Agility'],
                                'Bug Buzz': ['Hydro Pump', 'Blizzard', 'Agility']
                            }
                        ),
                    ), baseStats=(70, 60, 62, 80, 82, 60), genders=('M', 'F'), images=('284.gif', '284.png', '284 (1).png')
                )
            if 'Ninjask':
                root.pokesets['Ninjask'] = pokemon_ddl.PokemonSet(
                    name='Ninjask', species='Ninjask', abilities=('Speed Boost',), pkTypes=('Bug', 'Flying'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Dig'],
                            {
                                'Protect': ['Swords Dance', 'Substitute'],
                                'Swords Dance': ['Baton Pass'],
                                'Substitute': ['Baton Pass'],
                                'Baton Pass': ['Substitute', 'Swords Dance', 'X-Scissor'],
                                'Dig': ['Night Slash', 'X-Scissor', 'Swords Dance', 'Metal Claw', 'Sunny Day']
                            }
                        ),
                    ), baseStats=(61, 90, 45, 50, 50, 160), genders=('M', 'F'), images=('291.gif', '291.png', '291 (1).png')
                )
            if 'Volbeat':
                root.pokesets['Volbeat'] = pokemon_ddl.PokemonSet(
                    name='Volbeat', species='Volbeat', abilities=('Swarm',), pkTypes=('Bug',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Substitute'],
                            {
                                'Protect': ['Tail Glow', 'Tail Glow', 'Trick'],
                                'Substitute': ['Tail Glow'],
                                'Tail Glow': ['Baton Pass', 'Encore', 'Baton Pass'],
                                'Baton Pass': ['Bug Buzz'],
                                'Encore': ['Bug Buzz'],
                                'Trick': ['Bug Buzz', 'U-turn'],
                                'Bug Buzz': ['Tail Glow'],
                                'U-turn': ['Zen Headbutt', 'Brick Break', 'Thunder Wave', 'Mega Kick']
                            }
                        ),
                    ), baseStats=(65, 73, 55, 47, 75, 85), genders=('M',), images=('313.gif', '313.png', '313 (1).png')
                )
            if 'Illumise':
                root.pokesets['Illumise'] = pokemon_ddl.PokemonSet(
                    name='Illumise', species='Illumise', abilities=('Oblivious', 'Tinted Lens'), pkTypes=('Bug',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Bug Buzz', 'Baton Pass', 'Helping Hand'],
                                'Bug Buzz': ['Thunderbolt'],
                                'Thunderbolt': ['Hidden Power [Ice]', 'Hidden Power [Ground]', 'Encore', 'U-turn'],
                                'Baton Pass': ['Substitute'],
                                'Substitute': ['Flatter', 'Dynamic Punch', 'Thunder Wave', 'Water Pulse'],
                                'Helping Hand': ['Light Screen', 'Metronome', 'Seismic Toss'],
                                'Light Screen': ['Thunder Wave', 'Bug Buzz', 'Shadow Ball'],
                                'Metronome': ['Bug Buzz'],
                                'Seismic Toss': ['Thunder Wave', 'Flatter']
                            }
                        ),
                    ), baseStats=(65, 47, 55, 73, 75, 85), genders=('F',), images=('314.gif', '314.png', '314 (1).png'),
                    ability_weights=(0.2, 0.8)
                )
            if 'Kricketune':
                root.pokesets['Kricketune'] = pokemon_ddl.PokemonSet(
                    name='Kricketune', species='Kricketune', abilities=('Swarm',), pkTypes=('Bug',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Swords Dance', 'Perish Song'],
                                'Swords Dance': ['X-Scissor'],
                                'X-Scissor': ['Brick Break', 'Slash', 'Night Slash', 'Giga Impact', 'Aerial Ace'],
                                'Perish Song': ['Sing', 'Swords Dance'],
                                'Sing': ['Double Team']
                            }
                        ),
                    ), baseStats=(77, 85, 51, 55, 51, 65), genders=('M', 'F'), images=('402.gif', '402-m.png', '402-m (1).png')
                )
            if 'Wormadam':
                root.pokesets['Wormadam'] = pokemon_ddl.PokemonSet(
                    name='Wormadam', species='Wormadam', abilities=('Anticipation',), pkTypes=('Bug', 'Grass'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Leaf Storm', 'Sunny Day'],
                                'Sunny Day': ['Solar Beam'],
                                'Solar Beam': ['Growth', 'Hidden Power [Fire]'],
                                'Leaf Storm': ['Signal Beam'],
                                'Signal Beam': ['Psychic', 'Hidden Power [Rock]', 'Hidden Power [Ice]']
                            }
                        ),
                    ), baseStats=(60, 59, 85, 79, 105, 36), genders=('F',), images=('413.gif', '413.png', '413 (1).png')
                )
            if 'Mothim':
                root.pokesets['Mothim'] = pokemon_ddl.PokemonSet(
                    name='Mothim', species='Mothim', abilities=('Swarm',), pkTypes=('Bug', 'Flying'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Bug Buzz', 'Skill Swap'],
                                'Bug Buzz': ['Air Slash', 'Hidden Power [Ground]', 'U-turn', 'Shadow Ball'],
                                'Skill Swap': ['Tailwind', 'Safeguard'],
                                'Tailwind': ['Bug Buzz', 'U-turn', 'Air Slash'],
                                'Safeguard': ['Bug Buzz', 'U-turn', 'Air Slash']
                            }
                        ),
                    ), baseStats=(70, 94, 50, 94, 50, 66), genders=('M',), images=('414.gif', '414.png', '414 (1).png')
                )
            if 'Vespiquen':
                root.pokesets['Vespiquen'] = pokemon_ddl.PokemonSet(
                    name='Vespiquen', species='Vespiquen', abilities=('Pressure',), pkTypes=('Bug', 'Flying'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Substitute', 'Protect'],
                            {
                                'Substitute': ['Toxic'],
                                'Toxic': ['Roost', 'Heal Order'],
                                'Roost': ['Attack Order'],
                                'Heal Order': ['Attack Order'],
                                'Protect': ['Toxic', 'Defend Order', 'Attack Order'],
                                'Defend Order': ['Toxic', 'Attack Order'],
                                'Attack Order': ['Air Cutter', 'Power Gem', 'Pursuit'],
                                'Air Cutter': ['Slash'],
                                'Power Gem': ['Ominous Wind', 'Destiny Bond'],
                                'Pursuit': ['Slash', 'Aerial Ace']
                            }
                        ),
                    ), baseStats=(70, 80, 102, 80, 102, 40), genders=('F',), images=('416.gif', '416.png', '416 (1).png')
                )
            if 'Yanmega':
                root.pokesets['Yanmega'] = pokemon_ddl.PokemonSet(
                    name='Yanmega', species='Yanmega', abilities=('Speed Boost', 'Tinted Lens'),
                    pkTypes=('Bug', 'Flying'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Hypnosis', 'Bug Buzz'],
                                'Hypnosis': ['Dream Eater', 'Air Cutter', 'Bug Buzz'],
                                'Bug Buzz': ['Psychic', 'Air Slash', 'Ancient Power'],
                                'Dream Eater': ['Air Slash', 'Bug Buzz', 'U-turn', 'Silver Wind'],
                                'Psychic': ['Air Slash', 'Hidden Power [Fire]', 'Hidden Power [Ground]', 'Hidden Power [Electric]', 'Hidden Power [Ice]', 'Shadow Ball'],
                                'Air Slash': ['Psychic', 'Shadow Ball', 'Hidden Power [Fire]', 'Hidden Power [Ground]', 'Hidden Power [Electric]', 'Hidden Power [Ice]', 'Hidden Power [Water]'],
                                'Ancient Power': ['Air Slash', 'Shadow Ball', 'Psychic', 'Giga Drain', 'Hypnosis']
                            }
                        ),
                    ), baseStats=(86, 76, 86, 116, 56, 95), genders=('M', 'F'), images=('469.gif', '469.png', '469 (1).png')
                )
            if 'Arceus-Bug':
                root.pokesets['Arceus-Bug'] = pokemon_ddl.PokemonSet(
                    name='Arceus-Bug', species='Arceus', abilities=('Multitype',), pkTypes=('Bug',),
                    sets=(
                        # MoveSet 1: "The Chaotic Bulwark". Guaranteed Protect + Judgement, then maximum variance.
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Judgement'],

                                # Judgement is the central hub for a chaotic web of possibilities.
                                'Judgement': [
                                    'Calm Mind', 'Swords Dance', 'Recover', 'Cosmic Power', 'Will-O-Wisp',
                                    'Thunder Wave', 'Extreme Speed', 'Earth Power', 'Ice Beam', 'Thunderbolt',
                                    'Flamethrower', 'Shadow Claw', 'Gravity', 'Substitute'
                                ],

                                # Every node below is heavily interconnected to create unpredictable sets.
                                'Calm Mind': ['Ice Beam', 'Thunderbolt', 'Earthquake', 'Shadow Claw', 'Recover',
                                              'Swords Dance', 'Will-O-Wisp'],
                                'Swords Dance': ['Extreme Speed', 'Dragon Claw', 'Shadow Claw', 'Earthquake', 'Surf',
                                                 'Ice Beam', 'Calm Mind'],
                                'Recover': ['Calm Mind', 'Will-O-Wisp', 'Ice Beam', 'Flamethrower', 'Substitute',
                                            'Swords Dance', 'Judgement'],
                                'Cosmic Power': ['Recover', 'Will-O-Wisp', 'Toxic', 'Flamethrower', 'Judgement'],
                                'Will-O-Wisp': ['Recover', 'Calm Mind', 'Extreme Speed', 'Dragon Claw'],
                                'Extreme Speed': ['Swords Dance', 'Shadow Claw', 'Draco Meteor', 'Overheat',
                                                  'Judgement',
                                                  'Recover'],
                                'Earth Power': ['Ice Beam', 'Thunderbolt', 'Calm Mind', 'Swords Dance', 'Dragon Claw'],
                                'Ice Beam': ['Thunderbolt', 'Earth Power', 'Judgement', 'Calm Mind', 'Swords Dance'],
                                'Thunderbolt': ['Ice Beam', 'Surf', 'Judgement', 'Calm Mind', 'Swords Dance'],
                                'Dragon Claw': ['Earthquake', 'Shadow Claw', 'Swords Dance', 'Calm Mind', 'Ice Beam'],
                                'Substitute': ['Calm Mind', 'Swords Dance', 'Recover', 'Will-O-Wisp', 'Judgement'],
                                'Gravity': ['Thunder', 'Blizzard', 'Focus Blast', 'Earthquake', 'Judgement'],
                            }
                        ),

                        # MoveSet 2: "The Chaotic Gambler". No Protect, starts with Judgement into chaos.
                        pokemon_ddl.MoveSet(
                            ['Judgement'],
                            {
                                'Judgement': [
                                    'Extreme Speed', 'Draco Meteor', 'Outrage', 'Calm Mind', 'Swords Dance',
                                    'Gravity', 'Trick Room', 'Fire Blast', 'Thunder', 'Ice Beam', 'Earthquake',
                                    'Shadow Claw', 'Will-O-Wisp', 'Recover'
                                ],

                                'Draco Meteor': ['Extreme Speed', 'Overheat', 'Earthquake', 'Fire Blast', 'Steel Wing'],
                                'Outrage': ['Extreme Speed', 'Aqua Tail', 'Iron Head', 'Ice Beam', 'Giga Drain'],
                                'Calm Mind': ['Ice Beam', 'Thunder', 'Focus Blast', 'Shadow Claw', 'Recover',
                                              'Swords Dance'],
                                'Swords Dance': ['Extreme Speed', 'Shadow Claw', 'Dragon Claw', 'Giga Drain',
                                                 'Calm Mind'],
                                'Gravity': ['Thunder', 'Blizzard', 'Focus Blast', 'Draco Meteor', 'Judgement'],
                                'Trick Room': ['Judgement', 'Draco Meteor', 'Fire Blast', 'Thunder', 'Focus Blast'],
                                'Extreme Speed': ['Judgement', 'Swords Dance', 'Draco Meteor', 'Will-O-Wisp',
                                                  'Recover'],
                                'Fire Blast': ['Draco Meteor', 'Thunder', 'Ice Beam', 'Earthquake'],
                                'Earthquake': ['Stone Edge', 'Outrage', 'Dragon Claw', 'Flamethrower'],
                                'Recover': ['Judgement', 'Calm Mind', 'Swords Dance', 'Will-O-Wisp', 'Toxic']
                            }
                        ),

                        # MoveSet 3: "The Perish Trapper". A specific, high-risk alternate strategy.
                        pokemon_ddl.MoveSet(
                            ['Perish Song'],
                            {
                                'Mean Look': ['Protect', 'Recover', 'Judgement'],
                                'Perish Song': ['Mean Look']
                            }
                        )
                    ), baseStats=(120, 120, 120, 120, 120, 120), genders=('',), images=('493.gif', 'arceus-bug.png', 'arceus-bug (1).png'),
                    item_key='arcBug', stat_key='arcStat'
                )

        # Grass type pokemon
        if 'Grass':
            if 'Exeggutor':
                root.pokesets['Exeggutor'] = pokemon_ddl.PokemonSet(
                    name='Exeggutor', species='Exeggutor', abilities=('Chlorophyll',), pkTypes=('Grass', 'Psychic'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Sunny Day', 'Trick Room', 'Leaf Storm'],
                                'Sunny Day': ['Solar Beam', 'Sleep Powder', 'Synthesis'],
                                'Synthesis': ['Solar Beam'],
                                'Solar Beam':['Sleep Powder', 'Psychic', 'Sludge Bomb'],
                                'Sleep Powder': ['Solar Beam', 'Dream Eater'],
                                'Leaf Storm': ['Reflect', 'Light Screen', 'Psychic'],
                                'Reflect': ['Light Screen', 'Explosion', 'Low Kick'],
                                'Light Screen': ['Reflect', 'Explosion', 'Psychic'],
                                'Trick Room': ['Sleep Powder', 'Leaf Storm', 'Egg Bomb'],
                                'Psychic': ['Low Kick', 'Explosion'],
                                'Egg Bomb': ['Wood Hammer']
                            }
                        ),
                    ), baseStats=(95, 95, 85, 125, 65, 55), genders=('M', 'F'), images=('103.gif', '103.png', '103 (1).png')
                )
            if 'Meganium':
                root.pokesets['Meganium'] = pokemon_ddl.PokemonSet(
                    name='Meganium', species='Meganium', abilities=('Overgrow',), pkTypes=('Grass',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Aromatherapy', 'Sunny Day'],
                                'Aromatherapy': ['Leech Seed', 'Toxic', 'Synthesis'],
                                'Leech Seed': ['Energy Ball', 'Seed Bomb'],
                                'Toxic': ['Energy Ball', 'Seed Bomb'],
                                'Synthesis': ['Energy Ball', 'Seed Bomb'],
                                'Sunny Day': ['Solar Beam'],
                                'Solar Beam': ['Synthesis', 'Frenzy Plant', 'Ancient Power']

                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Light Screen', 'Reflect'],
                                'Reflect': ['Light Screen', 'Energy Ball', 'Seed Bomb', 'Body Slam'],
                                'Light Screen': ['Reflect', 'Energy Ball', 'Seed Bomb', 'Earthquake'],
                                'Energy Ball': ['Aromatherapy', 'Synthesis'],
                                'Seed Bomb': ['Aromatherapy', 'Synthesis'],
                                'Body Slam': ['Aromatherapy', 'Outrage'],
                                'Earthquake': ['Aromatherapy', 'Giga Drain', 'Synthesis']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Swords Dance'],
                                'Swords Dance': ['Seed Bomb', 'Earthquake', 'Return', 'Iron Tail']
                            }
                        )
                    ), baseStats=(80, 82, 100, 83, 100, 80), genders=('M', 'F'), images=('154.gif', '154-m.png', '154-m (1).png')
                )
            if 'Bellossom':
                root.pokesets['Bellossom'] = pokemon_ddl.PokemonSet(
                    name='Bellossom', species='Bellossom', abilities=('Chlorophyll',), pkTypes=('Grass',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Sunny Day'],
                                'Sunny Day': ['Moonlight', 'Sleep Powder', 'Hidden Power [Rock]', 'Hidden Power [Fire]', 'Leaf Blade'],
                                'Moonlight': ['Solar Beam', 'Leaf Storm'],
                                'Sleep Powder': ['Solar Beam', 'Leaf Storm'],
                                'Hidden Power [Rock]': ['Solar Beam', 'Leaf Storm'],
                                'Hidden Power [Fire]': ['Solar Beam', 'Leaf Storm'],
                                'Leaf Blade': ['Synthesis'],
                                'Synthesis': ['Sleep Powder', 'Leech Seed', 'Stun Spore', 'Gastro Acid']
                            }
                        ),
                    ), baseStats=(75, 80, 85, 90, 100, 50), genders=('M', 'F'), images=('182.gif', '182.png', '182 (1).png')
                )
            if 'Jumpluff':
                root.pokesets['Jumpluff'] = pokemon_ddl.PokemonSet(
                    name='Jumpluff', species='Jumpluff', abilities=('Chlorophyll', 'Leaf Guard'),
                    pkTypes=('Grass', 'Flying'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Sleep Powder'],
                                'Sleep Powder': ['Memento', 'U-turn', 'Substitute', 'Sunny Day'],
                                'Memento': ['Encore', 'Reflect'],
                                'U-turn': ['Sunny Day', 'Memento', 'Encore'],
                                'Substitute': ['Leech Seed'],
                                'Sunny Day': ['U-turn', 'Encore', 'Memento', 'Solar Beam']
                            }
                        ),
                    ), baseStats=(75, 55, 70, 55, 85, 110), genders=('M', 'F'), images=('189.gif', '189.png', '189 (1).png'),
                    ability_weights=(0.8, 0.2)
                )
            if 'Sunflora':
                root.pokesets['Sunflora'] = pokemon_ddl.PokemonSet(
                    name='Sunflora', species='Sunflora', abilities=('Chlorophyll', 'Solar Power'), pkTypes=('Grass',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Sunny Day', 'Sunny Day', 'Hidden Power [Ice]'],
                                'Sunny Day': ['Hidden Power [Fire]', 'Earth Power'],
                                'Hidden Power [Fire]': ['Solar Beam', 'Leaf Storm'],
                                'Earth Power': ['Solar Beam', 'Leaf Storm'],
                                'Hidden Power [Ice]': ['Leaf Storm'],
                                'Leaf Storm': ['Earth Power', 'Synthesis']
                            }
                        ),
                    ), baseStats=(75, 75, 55, 105, 85, 30), genders=('M', 'F'), images=('192.gif', '192.png', '192 (1).png'),
                    ability_weights=(0.2, 0.8)
                )
            if 'Celebi':
                root.pokesets['Celebi'] = pokemon_ddl.PokemonSet(
                    name='Celebi', species='Celebi', abilities=('Natural Cure',), pkTypes=('Psychic', 'Grass'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Nasty Plot'],
                                'Nasty Plot': ['Earth Power', 'Shadow Ball'],
                                'Earth Power': ['Leaf Storm', 'Grass Knot', 'Psychic', 'Confusion', 'Silver Wind'],
                                'Shadow Ball': ['Leaf Storm', 'Grass Knot', 'Psychic', 'Charge Beam', 'Skill Swap'],
                                'Leaf Storm': ['Hidden Power [Ice]', 'Hidden Power [Fire]', 'Recover', 'Signal Beam'],
                                'Grass Knot': ['Hidden Power [Ice]', 'Hidden Power [Fire]', 'Recover', 'Shock Wave'],
                                'Psychic': ['Hidden Power [Ice]', 'Hidden Power [Fire]', 'Recover', 'Water Pulse'],
                                'Confusion': ['Hidden Power [Ice]', 'Hidden Power [Fire]', 'Recover', 'Grass Knot', 'Energy Ball'],
                                'Charge Beam': ['Hidden Power [Ice]', 'Hidden Power [Fire]', 'Recover', 'Leaf Storm', 'Energy Ball', 'Psychic'],
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Recover', 'Thunder Wave', 'Stealth Rock'],
                                'Recover': ['Stealth Rock', 'Thunder Wave', 'Grass Knot', 'Leaf Storm'],
                                'Thunder Wave': ['Grass Knot', 'Leaf Storm', 'Water Pulse'],
                                'Stealth Rock': ['Energy Ball', 'Grass Knot', 'Leaf Storm'],
                                'Grass Knot': ['Earth Power', 'Hidden Power [Fire]', 'Hidden Power [Ice]', 'Psychic', 'U-turn', 'Signal Beam', 'Confusion'],
                                'Leaf Storm': ['U-turn', 'Sucker Punch', 'Zen Headbutt'],
                                'Energy Ball': ['Shock Wave', 'Confusion', 'Psychic', 'Toxic', 'Trick']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Baton Pass', 'Leech Seed', 'Calm Mind'],
                                'Baton Pass': ['Double Team', 'Calm Mind', 'Leech Seed', 'Swords Dance'],
                                'Leech Seed': ['Recover', 'Psychic', 'Reflect', 'Heal Bell', 'Energy Ball', 'Grass Knot', 'Baton Pass', 'Double Team'],
                                'Calm Mind': ['Giga Drain', 'Psychic', 'Hidden Power [Fire]', 'Baton Pass'],
                                'Swords Dance': ['Seed Bomb', 'Secret Power', 'Sucker Punch', 'Zen Headbutt']
                            }
                        )
                    ), baseStats=(100, 100, 100, 100, 100, 100), genders=('',), images=('251.gif', '251.png', '251 (1).png')
                )
            if 'Sceptile':
                root.pokesets['Sceptile'] = pokemon_ddl.PokemonSet(
                    name='Sceptile', species='Sceptile', abilities=('Overgrow',), pkTypes=('Grass',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Protect', 'Protect', 'Substitute'],
                            {
                                'Protect': ['Leaf Storm', 'Energy Ball', 'Swords Dance'],
                                'Substitute': ['Leech Seed'],
                                'Leech Seed': ['Hidden Power [Ice]', 'Leaf Storm', 'Energy Ball'],
                                'Leaf Storm': ['Dragon Pulse', 'Hidden Power [Ice]', 'Focus Blast', 'Quick Attack'],
                                'Energy Ball': ['Dragon Pulse', 'Hidden Power [Ice]', 'Focus Blast'],
                                'Focus Blast': ['Hidden Power [Psychic]'],
                                'Swords Dance': ['Leaf Blade', 'X-Scissor', 'Earthquake', 'Rock Slide', 'Double-Edge', 'Low Kick', 'Aerial Ace'],
                                'Quick Attack': ['Rock Slide', 'Endeavor', 'Hidden Power [Ice]']
                            }
                        ),
                    ), baseStats=(70, 85, 65, 105, 85, 120), genders=('M', 'F'), images=('254.gif', '254.png', '254 (1).png')
                )
            if 'Ludicolo':
                root.pokesets['Ludicolo'] = pokemon_ddl.PokemonSet(
                    name='Ludicolo', species='Ludicolo', abilities=('Swift Swim', 'Rain Dish'),
                    pkTypes=('Water', 'Grass'),
                    sets=(
                        pokemon_ddl.MoveSet(['Protect'],
                        {
                            'Protect': ['Surf', 'Hydro Pump', 'Rain Dance', 'Swords Dance', 'Fake Out'],
                            'Surf': ['Energy Ball', 'Rain Dance'],
                            'Energy Ball': ['Ice Beam', 'Hidden Power [Psychic]', 'Focus Punch'],
                            'Hydro Pump': ['Energy Ball', 'Rain Dance'],
                            'Rain Dance': ['Surf', 'Hydro Pump', 'Water Pulse', 'Energy Ball', 'Giga Drain'],
                            'Water Pulse': ['Ice Beam', 'Energy Ball'],
                            'Swords Dance': ['Waterfall'],
                            'Waterfall': ['Rain Dance', 'Seed Bomb', 'Ice Punch', 'Zen Headbutt'],
                            'Fake Out': ['Rain Dance', 'Surf', 'Brick Break', 'Focus Blast', 'Icy Wind'],
                            'Brick Break': ['Swords Dance', 'Fire Punch', 'Thunder Punch', 'Bullet Seed'],
                            'Focus Blast': ['Water Pulse', 'Surf', 'Hydro Pump', 'Energy Ball', 'Giga Drain'],
                            'Icy Wind': ['Seismic Toss', 'Hydro Pump', 'Blizzard'],
                            'Giga Drain': ['Surf', 'Bubble Beam', 'Uproar', 'Hydro Pump']
                        }),
                    ), baseStats=(80, 70, 70, 90, 100, 70), genders=('M', 'F'), images=('272.gif', '272-m.png', '272-m (1).png')
                )
            if 'Tropius':
                root.pokesets['Tropius'] = pokemon_ddl.PokemonSet(
                    name='Tropius', species='Tropius', abilities=('Chlorophyll', 'Solar Power'),
                    pkTypes=('Grass', 'Flying'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Leaf Storm', 'Swords Dance', 'Toxic'],
                                'Toxic': ['Energy Ball', 'Roost'],
                                'Energy Ball': ['Air Slash', 'Whirlwind'],
                                'Roost': ['Air Slash', 'Whirlwind', 'Energy Ball'],
                                'Swords Dance': ['Leaf Blade', 'Earthquake'],
                                'Leaf Blade': ['Earthquake', 'Aerial Ace', 'Roost', 'Body Slam', 'Outrage'],
                                'Earthquake': ['Leaf Blade', 'Aerial Ace', 'Roost', 'Return', 'Headbutt', 'Steel Wing'],
                                'Leaf Storm': ['Sunny Day'],
                                'Sunny Day': ['Air Slash', 'Hidden Power [Fire]', 'Solar Beam']
                            }
                        ),
                    ), baseStats=(99, 68, 83, 72, 87, 51), genders=('M', 'F'), images=('357.gif', '357.png', '357 (1).png')
                )
            if 'Cherrim':
                root.pokesets['Cherrim'] = pokemon_ddl.PokemonSet(
                    name='Cherrim', species='Cherrim', abilities=('Flower Gift',), pkTypes=('Grass',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Sunny Day'],
                                'Sunny Day': ['Aromatherapy', 'Grass Whistle', 'Solar Beam', 'Razor Leaf'],
                                'Aromatherapy': ['Hidden Power [Fire]', 'Hidden Power [Ground]', 'Hidden Power [Psychic]', 'Energy Ball',
                                                 'Hidden Power [Dark]', 'Helping Hand'],
                                'Grass Whistle': ['Hidden Power [Ice]', 'Hidden Power [Fire]', 'Hidden Power [Ghost]', 'Grass Knot',
                                                  'Leech Seed', 'Helping Hand'],
                                'Solar Beam': ['Hidden Power [Fire]', 'Hyper Beam', 'Helping Hand'],
                                'Razor Leaf': ['Giga Impact', 'Helping Hand', 'Rollout']
                            }
                        ),
                    ), baseStats=(70, 60, 70, 87, 78, 85), genders=('M', 'F'), images=('421.gif', '421-closed.png', '421-closed (1).png')
                )
            if 'Carnivine':
                root.pokesets['Carnivine'] = pokemon_ddl.PokemonSet(
                    name='Carnivine', species='Carnivine', abilities=('Levitate',), pkTypes=('Grass',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Swords Dance', 'Swords Dance', 'Stockpile', 'Knock Off'],
                                'Swords Dance': ['Power Whip'],
                                'Power Whip': ['Return', 'Substitute', 'Crunch'],
                                'Stockpile': ['Spit Up'],
                                'Spit Up': ['Gastro Acid', 'Swallow', 'Crunch'],
                                'Knock Off': ['Power Whip', 'Crunch', 'Bind', 'Flash']
                            }
                        ),
                    ), baseStats=(74, 100, 72, 90, 72, 46), genders=('M', 'F'), images=('455.gif', '455.png', '455 (1).png')
                )
            if 'Tangrowth':
                root.pokesets['Tangrowth'] = pokemon_ddl.PokemonSet(
                    name='Tangrowth', species='Tangrowth', abilities=('Chlorophyll', 'Leaf Guard'), pkTypes=('Grass',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Power Whip', 'Leaf Storm', 'Swords Dance'],
                                'Power Whip': ['Synthesis', 'Hidden Power [Ice]', 'Sleep Powder', 'Earthquake'],
                                'Synthesis': ['Earthquake', 'Sleep Powder', 'Stun Spore'],
                                'Hidden Power [Ice]': ['Earthquake', 'Sleep Powder', 'Stun Spore'],
                                'Sleep Powder': ['Earthquake', 'Ancient Power', 'Knock Off', 'Stun Spore'],
                                'Stun Spore': ['Earthquake', 'Rock Slide', 'Knock Off'],
                                'Earthquake': ['Hidden Power [Fire]', 'Rock Slide'],
                                'Rock Slide': ['Sleep Powder', 'Knock Off', 'Brick Break', 'Aerial Ace'],
                                'Hidden Power [Fire]': ['Rock Slide', 'Sleep Powder', 'Ancient Power', 'Focus Blast'],
                                'Swords Dance': ['Poison Jab', 'Earthquake', 'Power Whip', 'Rock Slide']
                            }
                        ),
                    ), baseStats=(100, 100, 125, 110, 50, 50), genders=('M', 'F'), images=('465.gif', '465-m.png', '465-m (1).png')
                )
            if 'Leafeon':
                root.pokesets['Leafeon'] = pokemon_ddl.PokemonSet(
                    name='Leafeon', species='Leafeon', abilities=('Leaf Guard',), pkTypes=('Grass',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Detect'],
                            {
                                'Detect': ['Swords Dance', 'Wish', 'Curse'],
                                'Protect': ['Swords Dance', 'Swords Dance', 'Wish'],
                                'Swords Dance': ['Leaf Blade', 'Baton Pass'],
                                'Leaf Blade': ['Double-Edge', 'Synthesis', 'Quick Attack', 'Rock Smash', 'Iron Tail'],
                                'Baton Pass': ['Roar', 'Synthesis', 'Leaf Blade'],
                                'Wish': ['Yawn', 'Roar', 'Heal Bell'],
                                'Yawn': ['Leaf Blade', 'Baton Pass', 'Last Resort'],
                                'Roar': ['Knock Off', 'Leaf Blade'],
                                'Heal Bell': ['Leaf Blade', 'X-Scissor'],
                                'Curse': ['Baton Pass', 'Bite', 'Leaf Blade', 'Synthesis', 'Grass Whistle']
                            }
                        ),
                    ), baseStats=(65, 110, 130, 60, 65, 95), genders=('M', 'F'), images=('470.gif', '470.png', '470 (1).png')
                )
            if 'Shaymin':
                root.pokesets['Shaymin'] = pokemon_ddl.PokemonSet(
                    name='Shaymin', species='Shaymin', abilities=('Natural Cure',), pkTypes=('Grass',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Rest', 'Protect'],
                            {
                                'Protect': ['Seed Flare'],
                                'Rest': ['Sleep Talk'],
                                'Sleep Talk': ['Hidden Power [Ice]', 'Hidden Power [Fire]'],
                                'Hidden Power [Ice]': ['Seed Flare'],
                                'Hidden Power [Fire]': ['Seed Flare'],
                                'Seed Flare': ['Air Cutter', 'Air Slash', 'Aromatherapy', 'Bullet Seed', 'Double Team', 'Earth Power',
                                               'Facade', 'Flash', 'Giga Drain', 'Grass Whistle', 'Growth', 'Healing Wish',
                                               'Hidden Power [Rock]', 'Hidden Power [Steel]', 'Mud-Slap', 'Ominous Wind', 'Psychic',
                                               'Quick Attack', 'Return', 'Rest', 'Safeguard', 'Substitute', 'Tailwind', 'Toxic',
                                               'Zen Headbutt']
                            }
                        ),
                    ), baseStats=(100, 100, 100, 100, 100, 100), genders=('',), images=('492.gif', '492-l.png', '492-l (1).png')
                )
            if 'Arceus-Grass':
                root.pokesets['Arceus-Grass'] = pokemon_ddl.PokemonSet(
                    name='Arceus-Grass', species='Arceus', abilities=('Multitype',), pkTypes=('Grass',),
                    sets=(
                        # MoveSet 1: "The Chaotic Bulwark". Guaranteed Protect + Judgement, then maximum variance.
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Judgement'],

                                # Judgement is the central hub for a chaotic web of possibilities.
                                'Judgement': [
                                    'Calm Mind', 'Swords Dance', 'Recover', 'Cosmic Power', 'Will-O-Wisp',
                                    'Thunder Wave', 'Extreme Speed', 'Earth Power', 'Ice Beam', 'Thunderbolt',
                                    'Flamethrower', 'Shadow Claw', 'Gravity', 'Substitute'
                                ],

                                # Every node below is heavily interconnected to create unpredictable sets.
                                'Calm Mind': ['Ice Beam', 'Thunderbolt', 'Earthquake', 'Shadow Claw', 'Recover',
                                              'Swords Dance', 'Will-O-Wisp'],
                                'Swords Dance': ['Extreme Speed', 'Dragon Claw', 'Shadow Claw', 'Earthquake', 'Surf',
                                                 'Ice Beam', 'Calm Mind'],
                                'Recover': ['Calm Mind', 'Will-O-Wisp', 'Ice Beam', 'Flamethrower', 'Substitute',
                                            'Swords Dance', 'Judgement'],
                                'Cosmic Power': ['Recover', 'Will-O-Wisp', 'Toxic', 'Flamethrower', 'Judgement'],
                                'Will-O-Wisp': ['Recover', 'Calm Mind', 'Extreme Speed', 'Dragon Claw'],
                                'Extreme Speed': ['Swords Dance', 'Shadow Claw', 'Draco Meteor', 'Overheat',
                                                  'Judgement',
                                                  'Recover'],
                                'Earth Power': ['Ice Beam', 'Thunderbolt', 'Calm Mind', 'Swords Dance', 'Dragon Claw'],
                                'Ice Beam': ['Thunderbolt', 'Earth Power', 'Judgement', 'Calm Mind', 'Swords Dance'],
                                'Thunderbolt': ['Ice Beam', 'Surf', 'Judgement', 'Calm Mind', 'Swords Dance'],
                                'Dragon Claw': ['Earthquake', 'Shadow Claw', 'Swords Dance', 'Calm Mind', 'Ice Beam'],
                                'Substitute': ['Calm Mind', 'Swords Dance', 'Recover', 'Will-O-Wisp', 'Judgement'],
                                'Gravity': ['Thunder', 'Blizzard', 'Focus Blast', 'Earthquake', 'Judgement'],
                            }
                        ),

                        # MoveSet 2: "The Chaotic Gambler". No Protect, starts with Judgement into chaos.
                        pokemon_ddl.MoveSet(
                            ['Judgement'],
                            {
                                'Judgement': [
                                    'Extreme Speed', 'Draco Meteor', 'Outrage', 'Calm Mind', 'Swords Dance',
                                    'Gravity', 'Trick Room', 'Fire Blast', 'Thunder', 'Ice Beam', 'Earthquake',
                                    'Shadow Claw', 'Will-O-Wisp', 'Recover'
                                ],

                                'Draco Meteor': ['Extreme Speed', 'Overheat', 'Earthquake', 'Fire Blast', 'Steel Wing'],
                                'Outrage': ['Extreme Speed', 'Aqua Tail', 'Iron Head', 'Ice Beam', 'Giga Drain'],
                                'Calm Mind': ['Ice Beam', 'Thunder', 'Focus Blast', 'Shadow Claw', 'Recover',
                                              'Swords Dance'],
                                'Swords Dance': ['Extreme Speed', 'Shadow Claw', 'Dragon Claw', 'Giga Drain',
                                                 'Calm Mind'],
                                'Gravity': ['Thunder', 'Blizzard', 'Focus Blast', 'Draco Meteor', 'Judgement'],
                                'Trick Room': ['Judgement', 'Draco Meteor', 'Fire Blast', 'Thunder', 'Focus Blast'],
                                'Extreme Speed': ['Judgement', 'Swords Dance', 'Draco Meteor', 'Will-O-Wisp',
                                                  'Recover'],
                                'Fire Blast': ['Draco Meteor', 'Thunder', 'Ice Beam', 'Earthquake'],
                                'Earthquake': ['Stone Edge', 'Outrage', 'Dragon Claw', 'Flamethrower'],
                                'Recover': ['Judgement', 'Calm Mind', 'Swords Dance', 'Will-O-Wisp', 'Toxic']
                            }
                        ),

                        # MoveSet 3: "The Perish Trapper". A specific, high-risk alternate strategy.
                        pokemon_ddl.MoveSet(
                            ['Perish Song'],
                            {
                                'Mean Look': ['Protect', 'Recover', 'Judgement'],
                                'Perish Song': ['Mean Look']
                            }
                        )
                    ), baseStats=(120, 120, 120, 120, 120, 120), genders=('',), images=('493.gif', 'arceus-grass.png', 'arceus-grass (1).png'),
                    item_key='arcGrass', stat_key='arcStat'
                )

        # Psychic type pokemon
        if 'Psychic':
            if 'Alakazam':
                root.pokesets['Alakazam'] = pokemon_ddl.PokemonSet(
                    name='Alakazam', species='Alakazam', abilities=('Synchronize', 'Inner Focus'), pkTypes=('Psychic',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Protect', 'Substitute'],
                            {
                                'Substitute': ['Psychic', 'Psybeam', 'Confusion', 'Psychic', 'Encore'],
                                'Psybeam': ['Charge Beam', 'Energy Ball', 'Focus Blast', 'Focus Blast', 'Focus Blast',
                                            'Future Sight', 'Grass Knot', 'Snore', 'Thunder Wave', 'Swagger',
                                            'Hyper Beam', 'Shadow Ball', 'Shadow Ball', 'Shadow Ball', 'Shock Wave',
                                            'Signal Beam', 'Signal Beam', 'Signal Beam'],
                                'Psychic': ['Charge Beam', 'Energy Ball', 'Focus Blast', 'Focus Blast', 'Focus Blast',
                                            'Future Sight', 'Grass Knot', 'Snore', 'Thunder Wave', 'Swagger',
                                            'Hyper Beam', 'Shadow Ball', 'Shadow Ball', 'Shadow Ball', 'Shock Wave',
                                            'Signal Beam', 'Signal Beam', 'Signal Beam'],
                                'Confusion': ['Charge Beam', 'Energy Ball', 'Focus Blast', 'Focus Blast', 'Focus Blast',
                                            'Future Sight', 'Grass Knot', 'Snore', 'Thunder Wave', 'Swagger',
                                            'Hyper Beam', 'Shadow Ball', 'Shadow Ball', 'Shadow Ball', 'Shock Wave',
                                            'Signal Beam', 'Signal Beam', 'Signal Beam'],
                                'Protect': ['Light Screen', 'Reflect', 'Taunt', 'Calm Mind', 'Trick', 'Psychic', 'Psychic', 'Gravity'],
                                'Light Screen': ['Reflect', 'Encore', 'Taunt'],
                                'Reflect': ['Light Screen', 'Encore', 'Taunt'],
                                'Encore': ['Psychic'],
                                'Taunt': ['Psychic'],
                                'Calm Mind': ['Encore', 'Psychic'],
                                'Trick': ['Focus Blast', 'Psychic', 'Counter'],
                                'Focus Blast': ['Signal Beam', 'Grass Knot', 'Psychic'],
                                'Counter': ['Psychic'],
                                'Gravity': ['Focus Blast', 'Disable']
                            }
                        ),
                    ), baseStats=(55, 50, 45, 135, 85, 120), genders=('M', 'F'), images=('065.gif', '065-m.png', '065-m (1).png')
                )
            if 'Slowbro':
                root.pokesets['Slowbro'] = pokemon_ddl.PokemonSet(
                    name='Slowbro', species='Slowbro', abilities=('Oblivious', 'Own Tempo'),
                    pkTypes=('Water', 'Psychic'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Slack Off', 'Protect', 'Rest'],
                            {
                                'Protect': ['Slack Off', 'Trick Room', 'Trick', 'Avalanche'],
                                'Rest': ['Sleep Talk'],
                                'Sleep Talk': ['Calm Mind', 'Psychic'],
                                'Calm Mind': ['Psychic', 'Surf', 'Water Pulse'],
                                'Slack Off': ['Trick Room'],
                                'Trick Room': ['Psychic', 'Grass Knot', 'Slack Off', 'Blizzard', 'Flamethrower', 'Brine',
                                               'Surf', 'Confusion', 'Flamethrower', 'Flash', 'Grass Knot', 'Ice Beam',
                                               'Icy Wind', 'Mud-Slap', 'Shadow Ball', 'Signal Beam', 'Thunder Wave'],
                                'Blizzard': ['Fire Blast', 'Focus Blast'],
                                'Avalanche': ['Zen Headbutt'],
                                'Zen Headbutt': ['Earthquake', 'Drain Punch', 'Dynamic Punch', 'Double-Edge', 'Counter',
                                                 'Brick Break', 'Body Slam', 'Aqua Tail'],
                                'Trick': ['Seismic Toss', 'Icy Wind', 'Psychic']
                            }
                        ),
                    ), baseStats=(95, 75, 110, 100, 80, 30), genders=('M', 'F'), images=('080.gif', '080.png', '080 (1).png')
                )
            if 'Hypno':
                root.pokesets['Hypno'] = pokemon_ddl.PokemonSet(
                    name='Hypno', species='Hypno', abilities=('Insomnia', 'Forewarn'), pkTypes=('Psychic',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Wish', 'Baton Pass'],
                                'Wish': ['Seismic Toss', 'Psychic'],
                                'Seismic Toss': ['Thunder Wave', 'Psychic'],
                                'Psychic': ['Thunder Wave', 'Seismic Toss'],
                                'Baton Pass': ['Nasty Plot', 'Calm Mind'],
                                'Nasty Plot': ['Psychic', 'Substitute'],
                                'Calm Mind': ['Substitute', 'Psychic']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Hypnosis', 'Trick Room', 'Drain Punch', 'Psycho Cut'],
                                'Hypnosis': ['Dream Eater'],
                                'Dream Eater': ['Nightmare', 'Drain Punch'],
                                'Trick Room': ['Fling', 'Hypnosis', 'Shadow Ball'],
                                'Shadow Ball': ['Psychic', 'Signal Beam', 'Focus Blast'],
                                'Drain Punch': ['Fire Punch', 'Thunder Punch', 'Fire Punch', 'Focus Punch', 'Mega Punch'],
                                'Psycho Cut': ['Drain Punch', 'Fire Punch', 'Return', 'Skill Swap', 'Trick Room', 'Fling']
                            }
                        )
                    ), baseStats=(85, 73, 70, 73, 115, 67), genders=('M', 'F'), images=('097.gif', '097-m.png', '097-m (1).png')
                )
            if 'Starmie':
                root.pokesets['Starmie'] = pokemon_ddl.PokemonSet(
                    name='Starmie', species='Starmie', abilities=('Natural Cure',),
                    pkTypes=('Water', 'Psychic'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Rapid Spin', 'Ice Beam', 'Blizzard', 'Power Gem', 'Signal Beam'],
                                'Rapid Spin': ['Recover', 'Surf', 'Hydro Pump'],
                                'Recover': ['Surf', 'Hydro Pump', 'Thunderbolt', 'Psychic'],
                                'Surf': ['Thunder Wave', 'Confuse Ray', 'Thunderbolt', 'Psychic'],
                                'Hydro Pump': ['Signal Beam', 'Thunder Wave', 'Confuse Ray', 'Thunderbolt', 'Psychic'],
                                'Ice Beam': ['Grass Knot', 'Thunder Wave', 'Thunderbolt', 'Psychic'],
                                'Thunder Wave': ['Hydro Pump', 'Surf'],
                                'Thunderbolt': ['Hydro Pump', 'Surf'],
                                'Grass Knot': ['Hydro Pump', 'Surf'],
                                'Psychic': ['Rapid Spin', 'Hydro Pump', 'Surf'],
                                'Blizzard': ['Thunder', 'Hydro Pump', 'Recover'],
                                'Power Gem': ['Signal Beam', 'Ice Beam', 'Psychic', 'Surf', 'Hydro Pump', 'Rapid Spin'],
                                'Signal Beam': ['Power Gem', 'Ice Beam', 'Psychic', 'Surf', 'Hydro Pump']
                            }
                        ),
                    ), baseStats=(60, 75, 85, 100, 85, 115), genders=('',), images=('121.gif', '121.png', '121 (1).png')
                )
            if 'Mr. Mime':
                root.pokesets['Mr. Mime'] = pokemon_ddl.PokemonSet(
                    name='Mr. Mime', species='Mr. Mime', abilities=('Soundproof', 'Filter'), pkTypes=('Psychic',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Baton Pass', 'Trick', 'Copycat', 'Hypnosis', 'Metronome', 'Trick Room', 'Teeter Dance'],
                                'Baton Pass': ['Nasty Plot', 'Calm Mind'],
                                'Nasty Plot': ['Taunt', 'Substitute', 'Encore', 'Psychic', 'Charge Beam'],
                                'Calm Mind': ['Taunt', 'Substitute', 'Encore', 'Psychic', 'Charge Beam'],
                                'Trick': ['Psychic'],
                                'Psychic': ['Thunderbolt', 'Shadow Ball'],
                                'Thunderbolt': ['Focus Blast', 'Baton Pass', 'Shadow Ball'],
                                'Copycat': ['Mimic'],
                                'Mimic': ['Psychic', 'Shadow Ball', 'Light Screen', 'Reflect'],
                                'Hypnosis': ['Psychic', 'Baton Pass', 'Light Screen', 'Reflect'],
                                'Light Screen': ['Signal Beam', 'Copycat', 'Mimic', 'Energy Ball'],
                                'Reflect': ['Light Screen', 'Signal Beam', 'Shadow Ball'],
                                'Metronome': ['Psychic', 'Copycat', 'Mimic', 'Shadow Ball', 'Solar Beam'],
                                'Trick Room': ['Psychic'],
                                'Teeter Dance': ['Psychic', 'Shock Wave']
                            }
                        ),
                    ), baseStats=(40, 45, 65, 100, 120, 90), genders=('M', 'F'), images=('122.gif', '122.png', '122 (1).png')
                )
            if 'Mewtwo':
                root.pokesets['Mewtwo'] = pokemon_ddl.PokemonSet(
                    name='Mewtwo', species='Mewtwo', abilities=('Pressure',), pkTypes=('Psychic',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Calm Mind'],
                            {
                                'Calm Mind': ['Ice Beam'],
                                'Ice Beam': ['Aura Sphere', 'Thunder', 'Thunderbolt'],
                                'Aura Sphere': ['Recover'],
                                'Thunder': ['Recover'],
                                'Thunderbolt': ['Recover']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Aura Sphere', 'Self-Destruct'],
                            {
                                'Aura Sphere': ['Ice Beam', 'Psychic'],
                                'Ice Beam': ['Self-Destruct'],
                                'Self-Destruct': ['Fire Blast', 'Flamethrower', 'Thunder', 'Thunderbolt', 'Grass Knot',
                                                  'Energy Ball', 'Focus Blast', 'Aerial Ace', 'Aqua Tail', 'Avalanche', 'Blizzard',
                                                  'Barrier', 'Body Slam', 'Brick Break', 'Charge Beam', 'Confusion', 'Counter',
                                                  'Disable', 'Double Team', 'Double-Edge', 'Drain Punch', 'Dream Eater', 'Dynamic Punch',
                                                  'Earthquake', 'Embargo', 'Endure', 'Facade', 'Fire Punch', 'Flash', 'Fling',
                                                  'Focus Blast', 'Frustration', 'Future Sight', 'Giga Impact', 'Gravity', 'Hail',
                                                  'Headbutt', 'Hyper Beam', 'Hidden Power [Dark]', 'Ice Punch', 'Icy Wind', 'Iron Tail',
                                                  'Light Screen', 'Low Kick', 'Magic Coat', 'Me First', 'Mega Kick', 'Mega Punch',
                                                  'Mist', 'Mud-Slap', 'Nightmare', 'Poison Jab', 'Protect', 'Psycho Cut', 'Psych Up',
                                                  'Rain Dance', 'Recover', 'Recycle', 'Reflect', 'Rest', 'Return', 'Rock Climb',
                                                  'Rock Slide', 'Rock Smash', 'Rock Tomb', 'Role Play', 'Safeguard', 'Sandstorm',
                                                  'Secret Power', 'Shadow Ball', 'Shock Wave', 'Signal Beam', 'Skill Swap', 'Snatch',
                                                  'Snore', 'Solar Beam', 'Stone Edge', 'Strength', 'Substitute', 'Sunny Day',
                                                  'Swagger', 'Swift', 'Taunt', 'Thunder Punch', 'Thunder Wave', 'Torment', 'Toxic',
                                                  'Trick', 'Trick Room', 'Water Pulse', 'Will-O-Wisp', 'Zen Headbutt']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Taunt'],
                            {
                                'Taunt': ['Reflect', 'Light Screen', 'Self-Destruct'],
                                'Self-Destruct': ['Fire Blast', 'Flamethrower', 'Thunder', 'Thunderbolt', 'Grass Knot',
                                                  'Energy Ball', 'Focus Blast', 'Aerial Ace', 'Aqua Tail', 'Avalanche', 'Blizzard',
                                                  'Barrier', 'Body Slam', 'Brick Break', 'Charge Beam', 'Confusion', 'Counter',
                                                  'Disable', 'Double Team', 'Double-Edge', 'Drain Punch', 'Dream Eater', 'Dynamic Punch',
                                                  'Earthquake', 'Embargo', 'Endure', 'Facade', 'Fire Punch', 'Flash', 'Fling',
                                                  'Focus Blast', 'Frustration', 'Future Sight', 'Giga Impact', 'Gravity', 'Hail',
                                                  'Headbutt', 'Hyper Beam', 'Hidden Power [Dark]', 'Ice Punch', 'Icy Wind', 'Iron Tail',
                                                  'Light Screen', 'Low Kick', 'Magic Coat', 'Me First', 'Mega Kick', 'Mega Punch',
                                                  'Mist', 'Mud-Slap', 'Nightmare', 'Poison Jab', 'Protect', 'Psycho Cut', 'Psych Up',
                                                  'Rain Dance', 'Recover', 'Recycle', 'Reflect', 'Rest', 'Return', 'Rock Climb',
                                                  'Rock Slide', 'Rock Smash', 'Rock Tomb', 'Role Play', 'Safeguard', 'Sandstorm',
                                                  'Secret Power', 'Shadow Ball', 'Shock Wave', 'Signal Beam', 'Skill Swap', 'Snatch',
                                                  'Snore', 'Solar Beam', 'Stone Edge', 'Strength', 'Substitute', 'Sunny Day',
                                                  'Swagger', 'Swift', 'Taunt', 'Thunder Punch', 'Thunder Wave', 'Torment', 'Toxic',
                                                  'Trick', 'Trick Room', 'Water Pulse', 'Will-O-Wisp', 'Zen Headbutt', 'Psychic',
                                                  'Ice Beam', 'Aura Sphere']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Will-O-Wisp', 'Thunder Wave'],
                            {
                                'Taunt': ['Ice Beam', 'Aura Sphere', 'Light Screen'],
                                'Will-O-Wisp': ['Recover'],
                                'Thunder Wave': ['Recover'],
                                'Recover': ['Taunt']
                            }
                        )
                    ), baseStats=(106, 110, 90, 154, 90, 130), genders=('',), images=('150.gif', '150.png', '150 (1).png')
                )
            if 'Mew':
                root.pokesets['Mew'] = pokemon_ddl.PokemonSet(
                    name='Mew', species='Mew', abilities=('Synchronize',), pkTypes=('Psychic',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Rock Polish'],
                            {
                                'Rock Polish': ['Swords Dance', 'Nasty Plot'],
                                'Swords Dance': ['Baton Pass', 'Baton Pass', 'Baton Pass', 'Baton Pass', 'Baton Pass', 'Baton Pass',
                                                 'Baton Pass', 'Baton Pass', 'Baton Pass', 'Baton Pass', 'Baton Pass', 'Baton Pass',
                                                 'Baton Pass', 'Baton Pass', 'Baton Pass', 'Baton Pass', 'Baton Pass', 'Baton Pass',
                                                 'Baton Pass', 'Baton Pass', 'Baton Pass', 'Baton Pass', 'Baton Pass', 'Baton Pass',
                                                 'Baton Pass', 'Baton Pass', 'Baton Pass', 'Baton Pass', 'Baton Pass', 'Baton Pass',
                                                 'Baton Pass', 'Baton Pass', 'Baton Pass', 'Baton Pass', 'Baton Pass', 'Baton Pass',
                                                 'Baton Pass', 'Baton Pass', 'Baton Pass', 'Baton Pass', 'Baton Pass', 'Baton Pass',
                                                 'Baton Pass', 'Baton Pass', 'Baton Pass', 'Baton Pass', 'Baton Pass', 'Baton Pass',
                                                 'Aerial Ace', 'Aqua Tail', 'Avalanche', 'Body Slam', 'Bounce', 'Brick Break',
                                                 'Bug Bite', 'Bullet Seed', 'Cut', 'Dig', 'Fly', 'Dive', 'Double-Edge', 'Dragon Claw',
                                                 'Drain Punch', 'Dynamic Punch', 'Earthquake', 'Explosion', 'Facade', 'Fake Out',
                                                 'Feint Attack', 'Fire Punch', 'Focus Punch', 'Frustration', 'Fury Cutter', 'Gastro Acid',
                                                 'Gunk Shot', 'Gyro Ball', 'Headbutt', 'Ice Punch', 'Iron Head', 'Iron Tail',
                                                 'Knock Off', 'Low Kick', 'Mega Kick', 'Mega Punch', 'Outrage', 'Payback', 'Pluck',
                                                 'Poison Jab', 'Rock Climb', 'Rock Slide', 'Rock Smash', 'Rock Tomb', 'Rollout',
                                                 'Roost', 'Secret Power', 'Seed Bomb', 'Self-Destruct', 'Shadow Claw', 'Sky Attack',
                                                 'Steel Wing', 'Stone Edge', 'Strength', 'Sucker Punch', 'Superpower', 'Thief', 'Thunder Punch',
                                                 'Waterfall', 'X-Scissor', 'Zen Headbutt'],
                                'Nasty Plot': ['Baton Pass', 'Baton Pass', 'Baton Pass', 'Baton Pass', 'Baton Pass', 'Baton Pass',
                                               'Baton Pass', 'Baton Pass', 'Baton Pass', 'Baton Pass', 'Baton Pass', 'Baton Pass',
                                               'Baton Pass', 'Baton Pass', 'Baton Pass', 'Baton Pass', 'Baton Pass', 'Baton Pass',
                                               'Baton Pass', 'Baton Pass', 'Baton Pass', 'Baton Pass', 'Baton Pass', 'Baton Pass',
                                               'Baton Pass', 'Baton Pass', 'Baton Pass', 'Baton Pass', 'Baton Pass', 'Baton Pass',
                                               'Baton Pass', 'Baton Pass', 'Baton Pass', 'Baton Pass', 'Baton Pass', 'Baton Pass',
                                               'Air Cutter', 'Ancient Power', 'Aura Sphere', 'Blizzard', 'Brine', 'Charge Beam',
                                               'Dark Pulse', 'Dragon Pulse', 'Earth Power', 'Dream Eater', 'Energy Ball', 'Fire Blast',
                                               'Flamethrower', 'Flash Cannon', 'Focus Blast', 'Giga Drain', 'Grass Knot', 'Heat Wave',
                                               'Hyper Beam', 'Ice Beam', 'Icy Wind', 'Mud-Slap', 'Ominous Wind', 'Overheat',
                                               'Psychic', 'Shadow Ball', 'Shock Wave', 'Signal Beam', 'Silver Wind', 'Sludge Bomb',
                                               'Solar Beam', 'Surf', 'Swift', 'Thunder', 'Thunderbolt', 'Twister', 'Uproar',
                                               'Vacuum Wave', 'Water Pulse', 'Whirlpool', 'Zap Cannon'],
                                'Baton Pass': ['Taunt', 'Protect']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Stealth Rock'],
                                'Stealth Rock': ['Taunt', 'U-turn'],
                                'Taunt': ['Explosion', 'U-turn'],
                                'U-turn': ['Explosion', 'Taunt']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Trick', 'Hypnosis'],
                                'Trick': ['Transform'],
                                'Hypnosis': ['Transform'],
                                'Transform': ['Light Screen', 'Reflect', 'Explosion', 'Dragon Claw', 'Dragon Pulse']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Soft-Boiled': ['U-turn'],
                                'Protect': ['Soft-Boiled'],
                                'U-turn': ['Thunder Wave', 'Hypnosis', 'Will-O-Wisp', 'Toxic']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Knock Off', 'Blizzard', 'Defog', 'Swords Dance', 'Super Fang', 'Heal Bell'],
                                'Knock Off': ['Taunt'],
                                'Taunt': ['Will-O-Wisp'],
                                'Blizzard': ['Thunder', 'Fire Blast', 'Outrage', 'Focus Blast'],
                                'Defog': ['Will-O-Wisp'],
                                'Will-O-Wisp': ['Roost', 'Super Fang'],
                                'Swords Dance': ['Sucker Punch', 'Zen Headbutt', 'Drain Punch'],
                                'Super Fang': ['Brine'],
                                'Brine': ['Giga Drain', 'Psychic'],
                                'Heal Bell': ['Taunt', 'U-turn', 'Psychic', 'Ice Beam', 'Light Screen', 'Reflect']
                            }
                        )
                    ), baseStats=(100, 100, 100, 100, 100, 100), genders=('',), images=('151.gif', '151.png', '151 (1).png')
                )
            if 'Xatu':
                root.pokesets['Xatu'] = pokemon_ddl.PokemonSet(
                    name='Xatu', species='Xatu', abilities=('Synchronize', 'Early Bird'), pkTypes=('Psychic', 'Flying'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Wish', 'Psychic', 'Reflect'],
                                'Wish': ['U-turn'],
                                'U-turn': ['Psychic', 'Reflect', 'Light Screen'],
                                'Psychic': ['Heat Wave'],
                                'Heat Wave': ['Trick', 'Roost', 'Hidden Power [Ground]', 'Shadow Ball', 'Calm Mind', 'Haze'],
                                'Reflect': ['Light Screen', 'Night Shade']
                            }
                        ),
                    ), baseStats=(65, 75, 70, 95, 70, 95), genders=('M', 'F'), images=('178.gif', '178-m.png', '178-m (1).png')
                )
            if 'Espeon':
                root.pokesets['Espeon'] = pokemon_ddl.PokemonSet(
                    name='Espeon', species='Espeon', abilities=('Synchronize',), pkTypes=('Psychic',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Calm Mind', 'Calm Mind', 'Trick'],
                                'Calm Mind': ['Baton Pass', 'Psychic'],
                                'Baton Pass': ['Substitute', 'Psychic'],
                                'Psychic': ['Hidden Power [Ground]', 'Baton Pass', 'Shadow Ball', 'Signal Beam'],
                                'Trick': ['Psychic']
                            }
                        ),
                    ), baseStats=(65, 65, 60, 130, 95, 110), genders=('M', 'F'), images=('196.gif', '196.png', '196 (1).png')
                )
            if 'Slowking':
                root.pokesets['Slowking'] = pokemon_ddl.PokemonSet(
                    name='Slowking', species='Slowking', abilities=('Oblivious', 'Own Tempo'),
                    pkTypes=('Water', 'Psychic'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Trick Room', 'Nasty Plot', 'Trick Room'],
                                'Trick Room': ['Calm Mind', 'Surf', 'Slack Off'],
                                'Calm Mind': ['Surf', 'Psychic', 'Ice Beam'],
                                'Surf': ['Psychic', 'Ice Beam', 'Slack Off', 'Fire Blast', 'Grass Knot', 'Trick'],
                                'Slack Off': ['Psychic', 'Flamethrower', 'Grass Knot', 'Focus Blast'],
                                'Nasty Plot': ['Surf', 'Future Sight']
                            }
                        ),
                    ), baseStats=(95, 75, 80, 100, 110, 30), genders=('M', 'F'), images=('199.gif', '199.png', '199 (1).png')
                )
            if 'Unown':
                root.pokesets['Unown'] = pokemon_ddl.PokemonSet(
                    name='Unown', species='Unown', abilities=('Levitate',), pkTypes=('Psychic',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Hidden Power [Dragon]', 'Hidden Power [Ice]', 'Hidden Power [Fighting]',
                         'Hidden Power [Dark]', 'Hidden Power [Fire]',
                         'Hidden Power [Ghost]', 'Hidden Power [Steel]', 'Hidden Power [Electric]',
                         'Hidden Power [Rock]', 'Hidden Power [Poison]',
                         'Hidden Power [Ground]', 'Hidden Power [Bug]', 'Hidden Power [Grass]',
                         'Hidden Power [Psychic]', 'Hidden Power [Flying]', 'Hidden Power [Water]'],
                            {}
                        ),
                    ), baseStats=(48, 72, 48, 72, 48, 48), genders=('',), images=('201.gif', '201.png', '201 (1).png')
                )
            if 'Wobbuffet':
                root.pokesets['Wobbuffet'] = pokemon_ddl.PokemonSet(
                    name='Wobbuffet', species='Wobbuffet', abilities=('Shadow Tag',), pkTypes=('Psychic',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Encore'],
                            {
                                'Encore': ['Counter'],
                                'Counter': ['Mirror Coat'],
                                'Mirror Coat': ['Safeguard', 'Destiny Bond', 'Tickle']
                            }
                        ),
                    ), baseStats=(190, 33, 58, 33, 58, 33), genders=('M', 'F'), images=('202.gif', '202-m.png', '202-m (1).png')
                )
            if 'Girafarig':
                root.pokesets['Girafarig'] = pokemon_ddl.PokemonSet(
                    name='Girafarig', species='Girafarig', abilities=('Inner Focus', 'Early Bird'),
                    pkTypes=('Normal', 'Psychic'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Baton Pass', 'Trick', 'Trick Room', 'Psychic', 'Assurance'],
                                'Baton Pass': ['Calm Mind', 'Agility'],
                                'Calm Mind': ['Psychic', 'Shadow Ball', 'Thunderbolt'],
                                'Agility': ['Psychic', 'Shadow Ball', 'Thunderbolt'],
                                'Trick': ['Psychic'],
                                'Psychic': ['Thunderbolt', 'Grass Knot'],
                                'Thunderbolt': ['Sucker Punch', 'Hidden Power [Fighting]', 'Shadow Ball'],
                                'Assurance': ['Zen Headbutt', 'Thunder Wave', 'Sunny Day', 'Zen Headbutt', 'Thunder Wave']
                            }
                        ),
                    ), baseStats=(70, 80, 65, 90, 65, 85), genders=('M', 'F'), images=('203.gif', '203-m.png', '203-m (1).png')
                )
            if 'Lugia':
                root.pokesets['Lugia'] = pokemon_ddl.PokemonSet(
                    name='Lugia', species='Lugia', abilities=('Pressure',), pkTypes=('Psychic', 'Flying'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Aeroblast'],
                            {
                                'Aeroblast': ['Roost', 'Calm Mind', 'Trick', 'Dragon Pulse'],
                                'Roost': ['Whirlwind', 'Ice Beam'],
                                'Whirlwind': ['Ice Beam', 'Toxic'],
                                'Calm Mind': ['Earth Power', 'Weather Ball', 'Thunder'],
                                'Earth Power': ['Roost', 'Ice Beam'],
                                'Weather Ball': ['Roost'],
                                'Thunder': ['Roost', 'Ice Beam', 'Hidden Power [Fighting]'],
                                'Trick': ['Thunder'],
                                'Ice Beam': ['Toxic', 'Light Screen', 'Reflect', 'Reflect'],
                                'Dragon Pulse': ['Calm Mind', 'Ancient Power', 'Blizzard', 'Earth Power', 'Extrasensory',
                                                 'Future Sight', 'Giga Drain', 'Hail', 'Hydro Pump', 'Icy Wind', 'Psycho Boost',
                                                 'Psychic', 'Rain Dance', 'Shadow Ball', 'Signal Beam', 'Sky Attack', 'Skill Swap',
                                                 'Thunder Wave', 'Whirlpool']
                            }
                        ),
                    ), baseStats=(106, 90, 130, 90, 154, 110), genders=('',), images=('249.gif', '249.png', '249 (1).png')
                )
            if 'Gardevoir':
                root.pokesets['Gardevoir'] = pokemon_ddl.PokemonSet(
                    name='Gardevoir', species='Gardevoir', abilities=('Synchronize', 'Trace'), pkTypes=('Psychic',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Psychic'],
                                'Psychic': ['Signal Beam', 'Thunderbolt', 'Hidden Power [Ground]', 'Focus Blast', 'Will-O-Wisp', 'Wish', 'Pain Split', 'Reflect', 'Light Screen', 'Icy Wind'],
                                'Signal Beam': ['Trick', 'Taunt', 'Destiny Bond', 'Encore', 'Calm Mind', 'Will-O-Wisp'],
                                'Thunderbolt': ['Trick', 'Taunt', 'Destiny Bond', 'Encore', 'Calm Mind', 'Will-O-Wisp'],
                                'Hidden Power [Ground]': ['Trick', 'Taunt', 'Destiny Bond', 'Encore', 'Calm Mind', 'Will-O-Wisp'],
                                'Focus Blast': ['Trick', 'Taunt', 'Destiny Bond', 'Encore', 'Calm Mind', 'Will-O-Wisp', 'Shadow Ball'],
                                'Will-O-Wisp': ['Trick', 'Taunt', 'Destiny Bond', 'Encore', 'Calm Mind', 'Will-O-Wisp'],
                                'Wish': ['Heal Bell', 'Will-O-Wisp'],
                                'Pain Split': ['Heal Bell', 'Will-O-Wisp'],
                                'Reflect': ['Light Screen', 'Memento', 'Taunt', 'Will-O-Wisp'],
                                'Light Screen': ['Reflect', 'Memento', 'Taunt', 'Will-O-Wisp'],
                                'Icy Wind': ['Imprison', 'Light Screen', 'Reflect', 'Memento', 'Destiny Bond', 'Shadow Sneak', 'Trick Room']
                            }
                        ),
                    ), baseStats=(68, 65, 65, 125, 115, 80), genders=('M', 'F'), images=('282.gif', '282.png', '282 (1).png')
                )
            if 'Grumpig':
                root.pokesets['Grumpig'] = pokemon_ddl.PokemonSet(
                    name='Grumpig', species='Grumpig', abilities=('Thick Fat', 'Own Tempo'), pkTypes=('Psychic',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Heal Bell', 'Trick Room'],
                                'Heal Bell': ['Thunder Wave', 'Toxic', 'Confuse Ray'],
                                'Thunder Wave': ['Reflect', 'Magic Coat', 'Psychic'],
                                'Toxic': ['Reflect', 'Magic Coat', 'Psychic', 'Counter'],
                                'Trick Room': ['Psychic'],
                                'Psychic': ['Signal Beam', 'Hidden Power [Fighting]', 'Substitute']
                            }
                        ),
                    ), baseStats=(80, 45, 65, 90, 110, 80), genders=('M', 'F'), images=('326.gif', '326.png', '326 (1).png')
                )
            if 'Chimecho':
                root.pokesets['Chimecho'] = pokemon_ddl.PokemonSet(
                    name='Chimecho', species='Chimecho', abilities=('Levitate',), pkTypes=('Psychic',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Psychic'],
                                'Psychic': ['Heal Bell', 'Wish', 'Recover', 'Hidden Power [Ground]', 'Shadow Ball', 'Icy Wind'],
                                'Heal Bell': ['Thunder Wave', 'Yawn'],
                                'Wish': ['Thunder Wave', 'Yawn', 'Heal Bell'],
                                'Recover': ['Thunder Wave', 'Yawn', 'Heal Bell'],
                                'Hidden Power [Ground]': ['Recover'],
                                'Shadow Ball': ['Recover'],
                                'Icy Wind': ['Knock Off', 'Reflect', 'Light Screen', 'Gravity', 'Helping Hand']
                            }
                        ),
                    ), baseStats=(65, 50, 70, 95, 80, 65), genders=('M', 'F'), images=('358.gif', '358.png', '358 (1).png')
                )
            if 'Deoxys':
                root.pokesets['Deoxys'] = pokemon_ddl.PokemonSet(
                    name='Deoxys', species='Deoxys', abilities=('Pressure',), pkTypes=('Psychic',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Shadow Ball', 'Extreme Speed', 'Spikes', 'Stealth Rock', 'Psycho Boost'],
                                'Psycho Boost': ['Charge Beam', 'Knock Off']
                            }
                        ),
                    ), baseStats=(50, 150, 50, 150, 50, 150), genders=('',), images=('386.gif', '386.png', '386 (1).png')
                )
            if 'Deoxys-Attack':
                root.pokesets['Deoxys-Attack'] = pokemon_ddl.PokemonSet(
                    name='Deoxys-Attack', species='Deoxys', abilities=('Pressure',), pkTypes=('Psychic',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Psycho Boost', 'Meteor Mash'],
                                'Psycho Boost': ['Aerial Ace', 'Body Slam', 'Brick Break', 'Charge Beam', 'Cut', 'Double-Edge',
                                                 'Drain Punch', 'Dynamic Punch', 'Energy Ball', 'Extreme Speed', 'Fire Punch',
                                                 'Flash Cannon', 'Focus Blast', 'Focus Punch', 'Giga Impact', 'Grass Knot',
                                                 'Hyper Beam', 'Ice Beam', 'Ice Punch', 'Icy Wind', 'Knock Off', 'Low Kick', 'Meteor Mash',
                                                 'Poison Jab', 'Psychic', 'Pursuit', 'Hidden Power [Dark]', 'Rock Slide', 'Shadow Ball',
                                                 'Signal Beam', 'Solar Beam', 'Superpower', 'Swift', 'Thunder', 'Thunderbolt',
                                                 'Thunder Punch', 'Zen Headbutt', 'Water Pulse', 'Zap Cannon'],
                                'Meteor Mash': ['Aerial Ace', 'Brick Break', 'Drain Punch', 'Extreme Speed', 'Fire Punch',
                                                'Ice Punch', 'Knock Off', 'Psycho Boost', 'Poison Jab', 'Pursuit', 'Rock Slide',
                                                'Superpower', 'Thunder Punch', 'Zen Headbutt', 'Wrap']
                            }
                        ),
                    ), baseStats=(50, 180, 20, 180, 20, 150), genders=('',), images=('386.gif', '386-a.png', '386-a (1).png')
                )
            if 'Deoxys-Defense':
                root.pokesets['Deoxys-Defense'] = pokemon_ddl.PokemonSet(
                    name='Deoxys-Defense', species='Deoxys', abilities=('Pressure',), pkTypes=('Psychic',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Spikes', 'Knock Off', 'Trick Room', 'Stealth Rock', 'Cosmic Power', 'Icy Wind'],
                                'Spikes': ['Recover', 'Taunt'],
                                'Stealth Rock': ['Thunderbolt', 'Recover'],
                                'Recover': ['Toxic', 'Ice Beam', 'Seismic Toss', 'Psycho Boost'],
                                'Taunt': ['Toxic', 'Ice Beam', 'Psycho Boost', 'Seismic Toss', 'Fire Punch', 'Knock Off', 'Thunder Wave'],
                                'Knock Off': ['Taunt', 'Seismic Toss'],
                                'Trick Room': ['Recover', 'Ice Beam', 'Thunderbolt'],
                                'Cosmic Power': ['Seismic Toss'],
                                'Seismic Toss': ['Recover']
                            }
                        ),
                    ), baseStats=(50, 70, 160, 70, 160, 90), genders=('',), images=('386.gif', '386-d.png', '386-d (1).png')
                )
            if 'Deoxys-Speed':
                root.pokesets['Deoxys-Speed'] = pokemon_ddl.PokemonSet(
                    name='Deoxys-Speed', species='Deoxys', abilities=('Pressure',), pkTypes=('Psychic',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Spikes'],
                                'Spikes': ['Taunt', 'Stealth Rock', 'Trick', 'Psycho Boost'],
                                'Taunt': ['Extreme Speed', 'Psycho Boost', 'Thunder Wave'],
                                'Stealth Rock': ['Extreme Speed', 'Psycho Boost', 'Thunder Wave'],
                                'Trick': ['Thunder Wave'],
                                'Thunder Wave': ['Taunt', 'Stealth Rock'],
                                'Psycho Boost': ['Thunderbolt', 'Ice Beam', 'Focus Blast', 'Knock Off', 'Shadow Ball',
                                                 'Superpower', 'Hidden Power [Fire]', 'Signal Beam', 'Spikes']
                            }
                        ),
                    ), baseStats=(50, 95, 90, 95, 90, 180), genders=('',), images=('386.gif', '386-s.png', '386-s (1).png')
                )
            if 'Uxie':
                root.pokesets['Uxie'] = pokemon_ddl.PokemonSet(
                    name='Uxie', species='Uxie', abilities=('Levitate',), pkTypes=('Psychic',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Psychic'],
                                'Psychic': ['Stealth Rock'],
                                'Stealth Rock': ['U-turn', 'Thunderbolt', 'Reflect', 'Light Screen', 'Yawn', 'Thunder Wave',
                                                 'Memento', 'Rain Dance', 'Sunny Day', 'Heal Bell', 'Trick']
                            }
                        ),
                    ), baseStats=(75, 75, 130, 75, 130, 95), genders=('',), images=('480.gif', '480.png', '480 (1).png')
                )
            if 'Mesprit':
                root.pokesets['Mesprit'] = pokemon_ddl.PokemonSet(
                    name='Mesprit', species='Mesprit', abilities=('Levitate',), pkTypes=('Psychic',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Stealth Rock', 'Calm Mind', 'Healing Wish'],
                                'Stealth Rock': ['Psychic'],
                                'Calm Mind': ['Hidden Power [Ground]', 'Ice Beam', 'Substitute', 'Thunderbolt'],
                                'Hidden Power [Ground]': ['Psychic'],
                                'Ice Beam': ['Psychic'],
                                'Substitute': ['Psychic'],
                                'Thunderbolt': ['Psychic'],
                                'Psychic': ['U-turn', 'Grass Knot', 'Healing Wish', 'Ice Beam', 'Thunderbolt', 'Grass Knot', 'Healing Wish'],
                                'Healing Wish': ['Sunny Day', 'Rain Dance'],
                                'Sunny Day': ['Psychic', 'Zen Headbutt', 'Stealth Rock', 'U-turn', 'Grass Knot'],
                                'Rain Dance': ['Psychic', 'Zen Headbutt', 'Stealth Rock', 'U-turn', 'Grass Knot']
                            }
                        ),
                    ), baseStats=(80, 105, 105, 105, 105, 80), genders=('',), images=('481.gif', '481.png', '481 (1).png')
                )
            if 'Azelf':
                root.pokesets['Azelf'] = pokemon_ddl.PokemonSet(
                    name='Azelf', species='Azelf', abilities=('Levitate',), pkTypes=('Psychic',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Stealth Rock', 'Explosion', 'Rain Dance', 'Flamethrower'],
                                'Stealth Rock': ['Explosion'],
                                'Explosion': ['Taunt', 'Thunder Wave', 'U-turn', 'Fire Blast', 'U-turn'],
                                'U-turn': ['Zen Headbutt', 'Sleep Talk', 'Trick', 'Ice Punch'],
                                'Rain Dance': ['Stealth Rock', 'Taunt', 'Explosion', 'U-turn'],
                                'Flamethrower': ['Psychic', 'Shadow Ball', 'Signal Beam', 'Swagger', 'Energy Ball']
                            }
                        ),
                    ), baseStats=(75, 125, 70, 125, 70, 115), genders=('',), images=('482.gif', '482.png', '482 (1).png')
                )
            if 'Cresselia':
                root.pokesets['Cresselia'] = pokemon_ddl.PokemonSet(
                    name='Cresselia', species='Cresselia', abilities=('Levitate',), pkTypes=('Psychic',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Psychic', 'Lunar Dance'],
                            {
                                'Psychic': ['Toxic', 'Ice Beam', 'Icy Wind', 'Trick Room'],
                                'Toxic': ['Helping Hand'],
                                'Ice Beam': ['Helping Hand'],
                                'Helping Hand': ['Trick Room', 'Icy Wind'],
                                'Lunar Dance': ['Ice Beam', 'Thunder Wave'],
                                'Thunder Wave': ['Hidden Power [Fire]', 'Toxic', 'Moonlight'],
                                'Moonlight': ['Sunny Day', 'Icy Wind', 'Helping Hand', 'Psychic'],
                                'Icy Wind': ['Light Screen', 'Reflect'],
                                'Light Screen': ['Helping Hand', 'Moonlight', 'Psychic'],
                                'Reflect': ['Helping Hand', 'Moonlight', 'Psychic'],
                                'Trick Room': ['Safeguard', 'Helping Hand'],
                                'Safeguard': ['Light Screen', 'Reflect']
                            }
                        ),
                    ), baseStats=(120, 70, 120, 75, 130, 85), genders=('F',), images=('488.gif', '488.png', '488 (1).png')
                )
            if 'Arceus-Psychic':
                root.pokesets['Arceus-Psychic'] = pokemon_ddl.PokemonSet(
                    name='Arceus-Psychic', species='Arceus', abilities=('Multitype',), pkTypes=('Psychic',),
                    sets=(
                        # MoveSet 1: "The Chaotic Bulwark". Guaranteed Protect + Judgement, then maximum variance.
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Judgement'],

                                # Judgement is the central hub for a chaotic web of possibilities.
                                'Judgement': [
                                    'Calm Mind', 'Swords Dance', 'Recover', 'Cosmic Power', 'Will-O-Wisp',
                                    'Thunder Wave', 'Extreme Speed', 'Earth Power', 'Ice Beam', 'Thunderbolt',
                                    'Flamethrower', 'Shadow Claw', 'Gravity', 'Substitute'
                                ],

                                # Every node below is heavily interconnected to create unpredictable sets.
                                'Calm Mind': ['Ice Beam', 'Thunderbolt', 'Earthquake', 'Shadow Claw', 'Recover',
                                              'Swords Dance', 'Will-O-Wisp'],
                                'Swords Dance': ['Extreme Speed', 'Dragon Claw', 'Shadow Claw', 'Earthquake', 'Surf',
                                                 'Ice Beam', 'Calm Mind'],
                                'Recover': ['Calm Mind', 'Will-O-Wisp', 'Ice Beam', 'Flamethrower', 'Substitute',
                                            'Swords Dance', 'Judgement'],
                                'Cosmic Power': ['Recover', 'Will-O-Wisp', 'Toxic', 'Flamethrower', 'Judgement'],
                                'Will-O-Wisp': ['Recover', 'Calm Mind', 'Extreme Speed', 'Dragon Claw'],
                                'Extreme Speed': ['Swords Dance', 'Shadow Claw', 'Draco Meteor', 'Overheat',
                                                  'Judgement',
                                                  'Recover'],
                                'Earth Power': ['Ice Beam', 'Thunderbolt', 'Calm Mind', 'Swords Dance', 'Dragon Claw'],
                                'Ice Beam': ['Thunderbolt', 'Earth Power', 'Judgement', 'Calm Mind', 'Swords Dance'],
                                'Thunderbolt': ['Ice Beam', 'Surf', 'Judgement', 'Calm Mind', 'Swords Dance'],
                                'Dragon Claw': ['Earthquake', 'Shadow Claw', 'Swords Dance', 'Calm Mind', 'Ice Beam'],
                                'Substitute': ['Calm Mind', 'Swords Dance', 'Recover', 'Will-O-Wisp', 'Judgement'],
                                'Gravity': ['Thunder', 'Blizzard', 'Focus Blast', 'Earthquake', 'Judgement'],
                            }
                        ),

                        # MoveSet 2: "The Chaotic Gambler". No Protect, starts with Judgement into chaos.
                        pokemon_ddl.MoveSet(
                            ['Judgement'],
                            {
                                'Judgement': [
                                    'Extreme Speed', 'Draco Meteor', 'Outrage', 'Calm Mind', 'Swords Dance',
                                    'Gravity', 'Trick Room', 'Fire Blast', 'Thunder', 'Ice Beam', 'Earthquake',
                                    'Shadow Claw', 'Will-O-Wisp', 'Recover'
                                ],

                                'Draco Meteor': ['Extreme Speed', 'Overheat', 'Earthquake', 'Fire Blast', 'Steel Wing'],
                                'Outrage': ['Extreme Speed', 'Aqua Tail', 'Iron Head', 'Ice Beam', 'Giga Drain'],
                                'Calm Mind': ['Ice Beam', 'Thunder', 'Focus Blast', 'Shadow Claw', 'Recover',
                                              'Swords Dance'],
                                'Swords Dance': ['Extreme Speed', 'Shadow Claw', 'Dragon Claw', 'Giga Drain',
                                                 'Calm Mind'],
                                'Gravity': ['Thunder', 'Blizzard', 'Focus Blast', 'Draco Meteor', 'Judgement'],
                                'Trick Room': ['Judgement', 'Draco Meteor', 'Fire Blast', 'Thunder', 'Focus Blast'],
                                'Extreme Speed': ['Judgement', 'Swords Dance', 'Draco Meteor', 'Will-O-Wisp',
                                                  'Recover'],
                                'Fire Blast': ['Draco Meteor', 'Thunder', 'Ice Beam', 'Earthquake'],
                                'Earthquake': ['Stone Edge', 'Outrage', 'Dragon Claw', 'Flamethrower'],
                                'Recover': ['Judgement', 'Calm Mind', 'Swords Dance', 'Will-O-Wisp', 'Toxic']
                            }
                        ),

                        # MoveSet 3: "The Perish Trapper". A specific, high-risk alternate strategy.
                        pokemon_ddl.MoveSet(
                            ['Perish Song'],
                            {
                                'Mean Look': ['Protect', 'Recover', 'Judgement'],
                                'Perish Song': ['Mean Look']
                            }
                        )
                    ), baseStats=(120, 120, 120, 120, 120, 120), genders=('',), images=('493.gif', 'arceus-psychic.png', 'arceus-psychic (1).png'),
                    item_key='arcPsychic', stat_key='arcStat'
                )

        # Flying type pokemon
        if 'Flying':
            if 'Pidgeot':
                root.pokesets['Pidgeot'] = pokemon_ddl.PokemonSet(
                    name='Pidgeot', species='Pidgeot', abilities=('Keen Eye', 'Tangled Feet'),
                    pkTypes=('Normal', 'Flying'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Brave Bird', 'Heat Wave', 'Sky Attack'],
                                'Brave Bird': ['Return', 'Steel Wing'],
                                'Return': ['U-turn', 'Pursuit', 'Quick Attack'],
                                'Heat Wave': ['Air Slash', 'Air Cutter'],
                                'Air Slash': ['Ominous Wind', 'Feather Dance'],
                                'Air Cutter': ['Air Slash', 'Ominous Wind', 'Mirror Move'],
                                'Sky Attack': ['Return']
                            }
                        ),
                    ), baseStats=(83, 80, 75, 70, 70, 91), genders=('M', 'F'), images=('018.gif', '018.png', '018 (1).png')
                )
            if 'Fearow':
                root.pokesets['Fearow'] = pokemon_ddl.PokemonSet(
                    name='Fearow', species='Fearow', abilities=('Keen Eye',), pkTypes=('Normal', 'Flying'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Drill Peck', 'Sky Attack'],
                                'Drill Peck': ['Return'],
                                'Return': ['U-turn', 'Quick Attack', 'Pursuit', 'Feint Attack', 'Mirror Move'],
                                'Sky Attack': ['Return', 'Steel Wing', 'Thief', 'Whirlwind', 'Return']
                            }
                        ),
                    ), baseStats=(65, 90, 65, 61, 61, 100), genders=('M', 'F'), images=('022.gif', '022.png', '022 (1).png')
                )
            if "Farfetch'd":
                root.pokesets["Farfetch'd"] = pokemon_ddl.PokemonSet(
                    name="Farfetch'd", species="Farfetch'd", abilities=('Keen Eye', 'Inner Focus'),
                    pkTypes=('Normal', 'Flying'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Endure', 'Protect'],
                            {
                                'Endure': ['Flail'],
                                'Protect': ['Slash'],
                                'Slash': ['Night Slash'],
                                'Night Slash': ['Air Cutter', 'Steel Wing', 'Knock Off'],
                                'Flail': ['Swords Dance'],
                                'Swords Dance': ['Double-Edge', 'Aerial Ace', 'Quick Attack', 'Substitute']
                            }
                        ),
                    ), baseStats=(52, 65, 55, 58, 62, 60), genders=('M', 'F'), images=('083.gif', '083.png', '083 (1).png'),
                    item_key='farf'
                )
            if 'Dodrio':
                root.pokesets['Dodrio'] = pokemon_ddl.PokemonSet(
                    name='Dodrio', species='Dodrio', abilities=('Early Bird',), pkTypes=('Normal', 'Flying'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Brave Bird', 'Acupressure'],
                                'Brave Bird': ['Roost', 'Return'],
                                'Roost': ['Return', 'Quick Attack', 'Taunt', 'Toxic', 'Payback'],
                                'Return': ['Pursuit', 'Payback', 'Quick Attack', 'Toxic'],
                                'Acupressure': ['Baton Pass', 'Substitute'],
                                'Baton Pass': ['Roost', 'Brave Bird'],
                                'Substitute': ['Roost', 'Steel Wing']
                            }
                        ),
                    ), baseStats=(60, 110, 70, 60, 60, 100), genders=('M', 'F'), images=('085.gif', '085-m.png', '085-m (1).png')
                )
            if 'Gyarados':
                root.pokesets['Gyarados'] = pokemon_ddl.PokemonSet(
                    name='Gyarados', species='Gyarados', abilities=('Intimidate',), pkTypes=('Water', 'Flying'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Rest', 'Protect', 'Protect'],
                            {
                                'Protect': ['Dragon Dance', 'Payback', 'Dragon Dance', 'Payback', 'Hydro Pump'],
                                'Dragon Dance': ['Waterfall', 'Aqua Tail'],
                                'Waterfall': ['Ice Fang', 'Outrage', 'Bounce', 'Earthquake', 'Stone Edge', 'Thunder Wave',
                                              'Taunt'],
                                'Aqua Tail': ['Ice Fang', 'Outrage', 'Bounce', 'Earthquake', 'Stone Edge', 'Thunder Wave',
                                              'Taunt'],
                                'Rest': ['Sleep Talk'],
                                'Sleep Talk': ['Roar'],
                                'Roar': ['Waterfall', 'Aqua Tail'],
                                'Payback': ['Stone Edge', 'Earthquake', 'Ice Fang', 'Avalanche'],
                                'Stone Edge': ['Waterfall', 'Aqua Tail'],
                                'Earthquake': ['Waterfall', 'Aqua Tail'],
                                'Ice Fang': ['Waterfall', 'Aqua Tail'],
                                'Avalanche': ['Waterfall', 'Aqua Tail'],
                                'Hydro Pump': ['Blizzard', 'Fire Blast', 'Dragon Pulse', 'Dark Pulse', 'Hyper Beam', 'Thunder']
                            }
                        ),
                    ), baseStats=(95, 125, 79, 60, 100, 81), genders=('M', 'F'), images=('130.gif', '130-m.png', '130-m (1).png')
                )
            if 'Noctowl':
                root.pokesets['Noctowl'] = pokemon_ddl.PokemonSet(
                    name='Noctowl', species='Noctowl', abilities=('Insomnia', 'Keen Eye'), pkTypes=('Normal', 'Flying'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Whirlwind', 'Hypnosis'],
                                'Whirlwind': ['Roost', 'Psycho Shift', 'Roost'],
                                'Roost': ['Night Shade', 'Night Shade', 'Toxic', 'Reflect'],
                                'Psycho Shift': ['Night Shade', 'Toxic'],
                                'Hypnosis': ['Dream Eater'],
                                'Dream Eater': ['Night Shade', 'Nightmare', 'Shadow Ball', 'Tailwind']
                            }
                        ),
                    ), baseStats=(100, 50, 50, 76, 96, 70), genders=('M', 'F'), images=('164.gif', '164.png', '164 (1).png')
                )
            if 'Mantine':
                root.pokesets['Mantine'] = pokemon_ddl.PokemonSet(
                    name='Mantine', species='Mantine', abilities=('Swift Swim', 'Water Absorb'),
                    pkTypes=('Water', 'Flying'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Rest'],
                            {
                                'Protect': ['Hydro Pump', 'Surf', 'Icy Wind'],
                                'Hydro Pump': ['Ice Beam', 'Rain Dance'],
                                'Ice Beam': ['Hidden Power [Flying]', 'Signal Beam', 'Toxic', 'Rain Dance'],
                                'Rain Dance': ['Ice Beam', 'Hidden Power [Flying]', 'Signal Beam', 'Toxic'],
                                'Surf': ['Rain Dance', 'Ice Beam'],
                                'Rest': ['Sleep Talk'],
                                'Sleep Talk': ['Hidden Power [Flying]', 'Signal Beam', 'Toxic'],
                                'Hidden Power [Flying]': ['Surf', 'Hydro Pump'],
                                'Signal Beam': ['Surf', 'Hydro Pump'],
                                'Toxic': ['Surf', 'Hydro Pump'],
                                'Icy Wind': ['Helping Hand'],
                                'Helping Hand': ['Surf', 'Hydro Pump', 'Hidden Power [Flying]', 'Mirror Coat']
                            }
                        ),
                    ), baseStats=(65, 40, 70, 80, 140, 70), genders=('M', 'F'), images=('226.gif', '226.png', '226 (1).png')
                )
            if 'Swellow':
                root.pokesets['Swellow'] = pokemon_ddl.PokemonSet(
                    name='Swellow', species='Swellow', abilities=('Guts',), pkTypes=('Normal', 'Flying'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Facade'],
                                'Facade': ['Brave Bird'],
                                'Brave Bird': ['Quick Attack', 'U-turn', 'Pursuit', 'Steel Wing']
                            }
                        ),
                    ), baseStats=(60, 85, 60, 50, 50, 125), genders=('M', 'F'), images=('277.gif', '277.png', '277 (1).png')
                )
            if 'Pelipper':
                root.pokesets['Pelipper'] = pokemon_ddl.PokemonSet(
                    name='Pelipper', species='Pelipper', abilities=('Keen Eye',), pkTypes=('Water', 'Flying'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Surf', 'Hydro Pump', 'Gunk Shot'],
                                'Surf': ['Air Slash', 'Hidden Power [Grass]'],
                                'Air Slash': ['Hidden Power [Grass]', 'Roost'],
                                'Hydro Pump': ['Air Slash'],
                                'Gunk Shot': ['Steel Wing', 'Wing Attack', 'Rain Dance', 'Seed Bomb'],
                                'Hidden Power [Grass]': ['Toxic', 'Roost']
                            }
                        ),
                    ), baseStats=(60, 50, 100, 85, 70, 65), genders=('M', 'F'), images=('279.gif', '279.png', '279 (1).png')
                )
            if 'Altaria':
                root.pokesets['Altaria'] = pokemon_ddl.PokemonSet(
                    name='Altaria', species='Altaria', abilities=('Natural Cure',), pkTypes=('Dragon', 'Flying'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Protect', 'Rest', 'Protect'],
                            {
                                'Protect': ['Dragon Dance', 'Dragon Dance', 'Dragon Claw', 'Outrage', 'Draco Meteor'],
                                'Dragon Dance': ['Dragon Claw', 'Dragon Rush', 'Outrage'],
                                'Dragon Claw': ['Roost', 'Roost', 'Heal Bell', 'Safeguard'],
                                'Roost': ['Perish Song', 'Roar', 'Haze'],
                                'Dragon Rush': ['Earthquake', 'Heal Bell', 'Safeguard'],
                                'Outrage': ['Earthquake', 'Roost', 'Fire Blast'],
                                'Rest': ['Sleep Talk'],
                                'Sleep Talk': ['Dragon Dance'],
                                'Draco Meteor': ['Fire Blast', 'Flamethrower', 'Heat Wave', 'Iron Tail', 'Pluck'],
                                'Fire Blast': ['Solar Beam', 'Dragon Pulse', 'Rest'],
                                'Flamethrower': ['Solar Beam', 'Dragon Pulse', 'Rest'],
                                'Heat Wave': ['Solar Beam', 'Dragon Pulse', 'Rest'],
                                'Iron Tail': ['Earthquake', 'Outrage'],
                                'Pluck': ['Earthquake', 'Iron Tail', 'Outrage', 'Dragon Claw']
                            }
                        ),
                    ), baseStats=(75, 70, 90, 70, 105, 80), genders=('M', 'F'), images=('334.gif', '334.png', '334 (1).png')
                )
            if 'Staraptor':
                root.pokesets['Staraptor'] = pokemon_ddl.PokemonSet(
                    name='Staraptor', species='Staraptor', abilities=('Intimidate',), pkTypes=('Normal', 'Flying'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Protect', 'Protect', 'Substitute', 'Endure'],
                            {
                                'Protect': ['Brave Bird', 'Aerial Ace'],
                                'Brave Bird': ['Return', 'Double-Edge', 'Giga Impact'],
                                'Return': ['Close Combat', 'Close Combat', 'U-turn'],
                                'Double-Edge': ['Close Combat', 'Close Combat', 'Pursuit', 'Roost'],
                                'Giga Impact': ['Close Combat', 'Close Combat', 'Quick Attack'],
                                'Substitute': ['Roost'],
                                'Roost': ['Brave Bird'],
                                'Aerial Ace': ['Return', 'Double-Edge', 'Giga Impact'],
                                'Endure': ['Endeavor'],
                                'Endeavor': ['Quick Attack'],
                                'Quick Attack': ['Aerial Ace', 'Close Combat', 'Sky Attack', 'Steel Wing', 'U-turn']
                            }
                        ),
                    ), baseStats=(85, 120, 70, 50, 50, 100), genders=('M', 'F'), images=('398.gif', '398-m.png', '398-m (1).png')
                )
            if 'Chatot':
                root.pokesets['Chatot'] = pokemon_ddl.PokemonSet(
                    name='Chatot', species='Chatot', abilities=('Keen Eye', 'Tangled Feet'),
                    pkTypes=('Normal', 'Flying'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Nasty Plot', 'Hyper Voice'],
                                'Nasty Plot': ['Hyper Voice'],
                                'Hyper Voice': ['Heat Wave', 'Encore', 'Hidden Power [Grass]', 'Heat Wave']
                            }
                        ),
                    ), baseStats=(76, 65, 45, 92, 42, 91), genders=('M', 'F'), images=('441.gif', '441.png', '441 (1).png')
                )
            if 'Togekiss':
                root.pokesets['Togekiss'] = pokemon_ddl.PokemonSet(
                    name='Togekiss', species='Togekiss', abilities=('Serene Grace',),
                    pkTypes=('Normal', 'Flying'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Air Slash'],
                                'Air Slash': ['Nasty Plot', 'Roost', 'Soft-Boiled', 'Aura Sphere', 'Ominous Wind', 'Body Slam',
                                              'Tri Attack'],
                                'Nasty Plot': ['Aura Sphere', 'Extrasensory'],
                                'Aura Sphere': ['Extreme Speed', 'Fire Blast', 'Flamethrower', 'Ominous Wind', 'Heat Wave'],
                                'Roost': ['Thunder Wave', 'Substitute', 'Heal Bell', 'Aura Sphere'],
                                'Soft-Boiled': ['Thunder Wave', 'Substitute', 'Heal Bell', 'Aura Sphere'],
                                'Ominous Wind': ['Ancient Power', 'Body Slam', 'Shadow Ball', 'Signal Beam', 'Silver Wind'],
                                'Body Slam': ['Roost', 'Soft-Boiled'],
                                'Tri Attack': ['Ominous Wind', 'Ancient Power', 'Silver Wind', 'Water Pulse']
                            }
                        ),
                    ), baseStats=(85, 50, 95, 120, 115, 80), genders=('M', 'F'), images=('468.gif', '468.png', '468 (1).png')
                )
            if 'Arceus-Flying':
                root.pokesets['Arceus-Flying'] = pokemon_ddl.PokemonSet(
                    name='Arceus-Flying', species='Arceus', abilities=('Multitype',), pkTypes=('Flying',),
                    sets=(
                        # MoveSet 1: "The Chaotic Bulwark". Guaranteed Protect + Judgement, then maximum variance.
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Judgement'],

                                # Judgement is the central hub for a chaotic web of possibilities.
                                'Judgement': [
                                    'Calm Mind', 'Swords Dance', 'Recover', 'Cosmic Power', 'Will-O-Wisp',
                                    'Thunder Wave', 'Extreme Speed', 'Earth Power', 'Ice Beam', 'Thunderbolt',
                                    'Flamethrower', 'Shadow Claw', 'Gravity', 'Substitute'
                                ],

                                # Every node below is heavily interconnected to create unpredictable sets.
                                'Calm Mind': ['Ice Beam', 'Thunderbolt', 'Earthquake', 'Shadow Claw', 'Recover',
                                              'Swords Dance', 'Will-O-Wisp'],
                                'Swords Dance': ['Extreme Speed', 'Dragon Claw', 'Shadow Claw', 'Earthquake', 'Surf',
                                                 'Ice Beam', 'Calm Mind'],
                                'Recover': ['Calm Mind', 'Will-O-Wisp', 'Ice Beam', 'Flamethrower', 'Substitute',
                                            'Swords Dance', 'Judgement'],
                                'Cosmic Power': ['Recover', 'Will-O-Wisp', 'Toxic', 'Flamethrower', 'Judgement'],
                                'Will-O-Wisp': ['Recover', 'Calm Mind', 'Extreme Speed', 'Dragon Claw'],
                                'Extreme Speed': ['Swords Dance', 'Shadow Claw', 'Draco Meteor', 'Overheat',
                                                  'Judgement',
                                                  'Recover'],
                                'Earth Power': ['Ice Beam', 'Thunderbolt', 'Calm Mind', 'Swords Dance', 'Dragon Claw'],
                                'Ice Beam': ['Thunderbolt', 'Earth Power', 'Judgement', 'Calm Mind', 'Swords Dance'],
                                'Thunderbolt': ['Ice Beam', 'Surf', 'Judgement', 'Calm Mind', 'Swords Dance'],
                                'Dragon Claw': ['Earthquake', 'Shadow Claw', 'Swords Dance', 'Calm Mind', 'Ice Beam'],
                                'Substitute': ['Calm Mind', 'Swords Dance', 'Recover', 'Will-O-Wisp', 'Judgement'],
                                'Gravity': ['Thunder', 'Blizzard', 'Focus Blast', 'Earthquake', 'Judgement'],
                            }
                        ),

                        # MoveSet 2: "The Chaotic Gambler". No Protect, starts with Judgement into chaos.
                        pokemon_ddl.MoveSet(
                            ['Judgement'],
                            {
                                'Judgement': [
                                    'Extreme Speed', 'Draco Meteor', 'Outrage', 'Calm Mind', 'Swords Dance',
                                    'Gravity', 'Trick Room', 'Fire Blast', 'Thunder', 'Ice Beam', 'Earthquake',
                                    'Shadow Claw', 'Will-O-Wisp', 'Recover'
                                ],

                                'Draco Meteor': ['Extreme Speed', 'Overheat', 'Earthquake', 'Fire Blast', 'Steel Wing'],
                                'Outrage': ['Extreme Speed', 'Aqua Tail', 'Iron Head', 'Ice Beam', 'Giga Drain'],
                                'Calm Mind': ['Ice Beam', 'Thunder', 'Focus Blast', 'Shadow Claw', 'Recover',
                                              'Swords Dance'],
                                'Swords Dance': ['Extreme Speed', 'Shadow Claw', 'Dragon Claw', 'Giga Drain',
                                                 'Calm Mind'],
                                'Gravity': ['Thunder', 'Blizzard', 'Focus Blast', 'Draco Meteor', 'Judgement'],
                                'Trick Room': ['Judgement', 'Draco Meteor', 'Fire Blast', 'Thunder', 'Focus Blast'],
                                'Extreme Speed': ['Judgement', 'Swords Dance', 'Draco Meteor', 'Will-O-Wisp',
                                                  'Recover'],
                                'Fire Blast': ['Draco Meteor', 'Thunder', 'Ice Beam', 'Earthquake'],
                                'Earthquake': ['Stone Edge', 'Outrage', 'Dragon Claw', 'Flamethrower'],
                                'Recover': ['Judgement', 'Calm Mind', 'Swords Dance', 'Will-O-Wisp', 'Toxic']
                            }
                        ),

                        # MoveSet 3: "The Perish Trapper". A specific, high-risk alternate strategy.
                        pokemon_ddl.MoveSet(
                            ['Perish Song'],
                            {
                                'Mean Look': ['Protect', 'Recover', 'Judgement'],
                                'Perish Song': ['Mean Look']
                            }
                        )
                    ), baseStats=(120, 120, 120, 120, 120, 120), genders=('',), images=('493.gif', 'arceus-flying.png', 'arceus-flying (1).png'),
                    item_key='arcFly', stat_key='arcStat'
                )

        # Normal type pokemon
        if 'Normal':
            if 'Raticate':
                root.pokesets['Raticate'] = pokemon_ddl.PokemonSet(
                    name='Raticate', species='Raticate', abilities=('Guts',), pkTypes=('Normal',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Facade', 'Super Fang'],
                                'Facade': ['Sucker Punch', 'Crunch'],
                                'Sucker Punch': ['U-turn', 'Reversal', 'Swords Dance'],
                                'Crunch': ['U-turn', 'Reversal', 'Swords Dance'],
                                'Super Fang': ['Thunder Wave'],
                                'Thunder Wave': ['U-turn', 'Facade', 'Zen Headbutt', 'Taunt', 'Swagger']
                            }
                        ),
                    ), baseStats=(55, 81, 60, 50, 70, 97), genders=('M', 'F'), images=('020.gif', '020-m.png', '020-m (1).png')
                )
            if 'Clefable':
                root.pokesets['Clefable'] = pokemon_ddl.PokemonSet(
                    name='Clefable', species='Clefable', abilities=('Cute Charm', 'Magic Guard'), pkTypes=('Normal',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Ice Beam', 'Encore'],
                                'Ice Beam': ['Seismic Toss'],
                                'Encore': ['Seismic Toss'],
                                'Seismic Toss': ['Soft-Boiled', 'Wish', 'Thunder Wave'],
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Wish'],
                                'Wish': ['Seismic Toss'],
                                'Seismic Toss': ['Toxic', 'Heal Bell']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Calm Mind'],
                                'Calm Mind': ['Thunderbolt', 'Flamethrower'],
                                'Thunderbolt': ['Ice Beam', 'Soft-Boiled', 'Hyper Beam'],
                                'Flamethrower': ['Ice Beam', 'Soft-Boiled', 'Psychic']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Double-Edge'],
                                'Double-Edge': ['Fire Blast', 'Meteor Mash'],
                                'Fire Blast': ['Grass Knot', 'Meteor Mash'],
                                'Meteor Mash': ['Soft-Boiled', 'Dynamic Punch', 'Thunder Wave']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Reflect', 'Light Screen'],
                                'Reflect': ['Light Screen', 'Seismic Toss'],
                                'Light Screen': ['Reflect', 'Seismic Toss'],
                                'Seismic Toss': ['Wish', 'Soft-Boiled', 'Encore']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Endeavor'],
                                'Endeavor': ['Encore'],
                                'Encore': ['Toxic', 'Thunder Wave']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Knock Off'],
                                'Knock Off': ['Seismic Toss', 'Soft-Boiled'],
                                'Seismic Toss': ['Thunder Wave', 'Stealth Rock'],
                                'Soft-Boiled': ['Thunder Wave', 'Stealth Rock']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Seismic Toss'],
                                'Seismic Toss': ['Encore', 'Stealth Rock'],
                                'Encore': ['Thunder Wave', 'Heal Bell', 'Soft-Boiled'],
                                'Stealth Rock': ['Thunder Wave', 'Heal Bell', 'Soft-Boiled']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Blizzard', 'Fire Blast', 'Focus Blast', 'Thunder']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Zen Headbutt', 'Thunder Punch', 'Strength', 'Rollout', 'Rock Smash',
                                            'Meteor Mash', 'Knock Off', 'Double-Edge', 'Ice Punch', 'Fire Punch',
                                            'Dynamic Punch'],
                                'Rollout': ['Defense Curl']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Icy Wind'],
                                'Icy Wind': ['Knock Off'],
                                'Knock Off': ['Trick', 'Thunder Wave', 'Toxic', 'Water Pulse']
                            }
                        )
                    ), baseStats=(95, 70, 73, 85, 90, 60), genders=('M', 'F'), images=('036.gif', '036.png', '036 (1).png')
                )
            if 'Wigglytuff':
                root.pokesets['Wigglytuff'] = pokemon_ddl.PokemonSet(
                    name='Wigglytuff', species='Wigglytuff', abilities=('Cute Charm', 'Competitive'),
                    pkTypes=('Normal',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Wish', 'Icy Wind', 'Thunder Wave'],
                                'Wish': ['Seismic Toss', 'Icy Wind'],
                                'Seismic Toss': ['Heal Bell', 'Thunder Wave', 'Icy Wind', 'Stealth Rock', 'Helping Hand'],
                                'Icy Wind': ['Toxic', 'Stealth Rock', 'Thunder Wave', 'Seismic Toss', 'Helping Hand'],
                                'Thunder Wave': ['Wish', 'Reflect', 'Light Screen', 'Seismic Toss', 'Helping Hand']
                            }
                        ),
                    ), baseStats=(140, 70, 45, 75, 50, 45), genders=('M', 'F'), images=('040.gif', '040.png', '040 (1).png')
                )
            if 'Persian':
                root.pokesets['Persian'] = pokemon_ddl.PokemonSet(
                    name='Persian', species='Persian', abilities=('Limber', 'Technician'), pkTypes=('Normal',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Hypnosis', 'Fake Out', 'Switcheroo', 'Rain Dance', 'Sunny Day', 'Hypnosis'],
                                'Hypnosis': ['Nasty Plot'],
                                'Nasty Plot': ['Swift', 'Water Pulse', 'Swift'],
                                'Fake Out': ['Bite', 'Return', 'Taunt'],
                                'Bite': ['Hypnosis', 'U-turn', 'Hypnosis'],
                                'Return': ['Hypnosis', 'U-turn', 'Hypnosis'],
                                'Taunt': ['Swift', 'Return', 'Hypnosis', 'U-turn'],
                                'Switcheroo': ['Return', 'Night Slash'],
                                'Rain Dance': ['Return'],
                                'Sunny Day': ['Return']
                            }
                        ),
                    ), baseStats=(65, 70, 60, 65, 65, 115), genders=('M', 'F'), images=('053.gif', '053.png', '053 (1).png')
                )
            if 'Kangaskhan':
                root.pokesets['Kangaskhan'] = pokemon_ddl.PokemonSet(
                    name='Kangaskhan', species='Kangaskhan', abilities=('Early Bird', 'Scrappy'), pkTypes=('Normal',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Return', 'Double-Edge', 'Dizzy Punch', 'Fake Out'],
                                'Return': ['Hammer Arm', 'Low Kick'],
                                'Double-Edge': ['Hammer Arm', 'Low Kick'],
                                'Dizzy Punch': ['Hammer Arm', 'Low Kick'],
                                'Hammer Arm': ['Sucker Punch', 'Crunch', 'Shadow Claw', 'Earthquake', 'Outrage', 'Fake Out'],
                                'Low Kick': ['Sucker Punch', 'Crunch', 'Shadow Claw', 'Avalanche', 'Fire Punch', 'Outrage', 'Earthquake', 'Fake Out'],
                                'Fake Out': ['Fire Punch', 'Ice Punch', 'Return', 'Double-Edge', 'Dizzy Punch']
                            }
                        ),
                    ), baseStats=(105, 95, 80, 40, 80, 90), genders=('F',), images=('115.gif', '115.png', '115 (1).png'),
                    ability_weights=(0.2, 0.8)
                )
            if 'Ditto':
                root.pokesets['Ditto'] = pokemon_ddl.PokemonSet(
                    name='Ditto', species='Ditto', abilities=('Limber',), pkTypes=('Normal',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Transform'],
                            {}
                        ),
                    ), baseStats=(48, 48, 48, 48, 48, 48), genders=('',), images=('132.gif', '132.png', '132 (1).png')
                )
            if 'Tauros':
                root.pokesets['Tauros'] = pokemon_ddl.PokemonSet(
                    name='Tauros', species='Tauros', abilities=('Intimidate', 'Anger Point'), pkTypes=('Normal',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Double-Edge', 'Thrash', 'Return'],
                                'Thrash': ['Outrage'],
                                'Outrage': ['Zen Headbutt', 'Rock Slide', 'Iron Head'],
                                'Double-Edge': ['Stone Edge', 'Earthquake', 'Zen Headbutt', 'Iron Head'],
                                'Zen Headbutt': ['Payback', 'Pursuit'],
                                'Iron Head': ['Earthquake']
                            }
                        ),
                    ), baseStats=(75, 100, 95, 40, 70, 110), genders=('M',), images=('128.gif', '128.png', '128 (1).png'),
                    ability_weights=(0.8, 0.2)
                )
            if 'Snorlax':
                root.pokesets['Snorlax'] = pokemon_ddl.PokemonSet(
                    name='Snorlax', species='Snorlax', abilities=('Immunity', 'Thick Fat'), pkTypes=('Normal',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Rest'],
                            {
                                'Protect': ['Body Slam', 'Return', 'Rock Climb', 'Double-Edge'],
                                'Body Slam': ['Brick Break', 'Crunch', 'Dynamic Punch', 'Earthquake', 'Fire Punch', 'Fling',
                                              'Giga Impact', 'Gunk Shot', 'Ice Punch', 'Iron Head', 'Outrage', 'Rock Slide',
                                              'Seed Bomb', 'Self-Destruct', 'Superpower', 'Thunder Punch', 'Zen Headbutt'],
                                'Return': ['Brick Break', 'Crunch', 'Dynamic Punch', 'Earthquake', 'Fire Punch', 'Fling',
                                              'Giga Impact', 'Gunk Shot', 'Ice Punch', 'Iron Head', 'Outrage', 'Rock Slide',
                                              'Seed Bomb', 'Self-Destruct', 'Superpower', 'Thunder Punch', 'Aqua Tail'],
                                'Rock Climb': ['Brick Break', 'Crunch', 'Dynamic Punch', 'Earthquake', 'Fire Punch', 'Fling',
                                              'Giga Impact', 'Gunk Shot', 'Ice Punch', 'Iron Head', 'Outrage', 'Rock Slide',
                                              'Seed Bomb', 'Self-Destruct', 'Superpower', 'Thunder Punch', 'Zen Headbutt'],
                                'Double-Edge': ['Brick Break', 'Crunch', 'Dynamic Punch', 'Earthquake', 'Fire Punch', 'Fling',
                                              'Giga Impact', 'Gunk Shot', 'Ice Punch', 'Iron Head', 'Outrage', 'Rock Slide',
                                              'Seed Bomb', 'Self-Destruct', 'Superpower', 'Thunder Punch', 'Zen Headbutt'],
                                'Rest': ['Sleep Talk', 'Body Slam'],
                                'Sleep Talk': ['Curse', 'Body Slam'],
                                'Curse': ['Brick Break', 'Crunch', 'Dynamic Punch', 'Earthquake', 'Fire Punch',
                                              'Giga Impact', 'Gunk Shot', 'Ice Punch', 'Iron Head', 'Outrage', 'Rock Slide',
                                              'Seed Bomb', 'Self-Destruct', 'Superpower', 'Thunder Punch', 'Zen Headbutt'],
                            }
                        ),
                    ), baseStats=(160, 110, 65, 65, 110, 30), genders=('M', 'F'), images=('143.gif', '143.png', '143 (1).png')
                )
            if 'Furret':
                root.pokesets['Furret'] = pokemon_ddl.PokemonSet(
                    name='Furret', species='Furret', abilities=('Keen Eye',), pkTypes=('Normal',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Last Resort'],
                            {
                                'Last Resort': ['Protect']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Trick', 'Trick', 'Assist', 'Iron Tail'],
                                'Trick': ['Brick Break', 'Slash'],
                                'Brick Break': ['U-turn', 'Shadow Claw', 'Sucker Punch'],
                                'Slash': ['U-turn', 'Shadow Claw', 'Sucker Punch'],
                                'Assist': ['Aqua Tail', 'Slash', 'Brick Break', 'Helping Hand'],
                                'Iron Tail': ['Helping Hand', 'Aqua Tail', 'Slash']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Trick', 'Trick', 'Assist', 'Iron Tail'],
                                'Trick': ['Brick Break', 'Slash'],
                                'Brick Break': ['U-turn', 'Shadow Claw', 'Sucker Punch'],
                                'Slash': ['U-turn', 'Shadow Claw', 'Sucker Punch'],
                                'Assist': ['Aqua Tail', 'Slash', 'Brick Break', 'Helping Hand'],
                                'Iron Tail': ['Helping Hand', 'Aqua Tail', 'Slash']
                            }
                        )
                    ), baseStats=(85, 76, 64, 45, 55, 90), genders=('M', 'F'), images=('162.gif', '162.png', '162 (1).png')
                )
            if 'Dunsparce':
                root.pokesets['Dunsparce'] = pokemon_ddl.PokemonSet(
                    name='Dunsparce', species='Dunsparce', abilities=('Serene Grace',), pkTypes=('Normal',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Body Slam', 'Thunder Wave', 'Ancient Power', 'Spite'],
                                'Body Slam': ['Bite', 'Zen Headbutt'],
                                'Bite': ['Earthquake', 'Rock Slide', 'Roost'],
                                'Zen Headbutt': ['Earthquake', 'Rock Slide', 'Roost'],
                                'Thunder Wave': ['Headbutt'],
                                'Headbutt': ['Bite', 'Zen Headbutt', 'Gyro Ball', 'Roost'],
                                'Ancient Power': ['Fire Blast', 'Ice Beam', 'Thunderbolt', 'Water Pulse', 'Shadow Ball'],
                                'Spite': ['Ancient Power', 'Stealth Rock', 'Body Slam', 'Stealth Rock', 'Thunder Wave']
                            }
                        ),
                    ), baseStats=(100, 70, 70, 65, 65, 45), genders=('M', 'F'), images=('206.gif', '206.png', '206 (1).png')
                )
            if 'Granbull':
                root.pokesets['Granbull'] = pokemon_ddl.PokemonSet(
                    name='Granbull', species='Granbull', abilities=('Intimidate', 'Quick Feet'), pkTypes=('Normal',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Thunder Wave', 'Toxic', 'Crunch'],
                                'Thunder Wave': ['Return', 'Body Slam'],
                                'Return': ['Earthquake', 'Crunch', 'Heal Bell', 'Close Combat'],
                                'Body Slam': ['Earthquake', 'Crunch', 'Heal Bell', 'Close Combat'],
                                'Crunch': ['Return', 'Fire Fang', 'Ice Fang', 'Thunder Fang', 'Close Combat']
                            }
                        ),
                    ), baseStats=(90, 120, 75, 60, 60, 45), genders=('M', 'F'), images=('210.gif', '210.png', '210 (1).png')
                )
            if 'Ursaring':
                root.pokesets['Ursaring'] = pokemon_ddl.PokemonSet(
                    name='Ursaring', species='Ursaring', abilities=('Guts', 'Quick Feet'), pkTypes=('Normal',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Facade', 'Facade', 'Counter'],
                                'Facade': ['Swords Dance', 'Close Combat', 'Ice Punch', 'Crunch'],
                                'Swords Dance': ['Close Combat', 'Crunch'],
                                'Close Combat': ['Crunch', 'Earthquake'],
                                'Crunch': ['Close Combat', 'Earthquake', 'Ice Punch', 'Aerial Ace'],
                                'Counter': ['Avalanche', 'Payback']
                            }
                        ),
                    ), baseStats=(90, 130, 75, 75, 75, 55), genders=('M', 'F'), images=('217.gif', '217-m.png', '217-m (1).png')
                )
            if 'Porygon2':
                root.pokesets['Porygon2'] = pokemon_ddl.PokemonSet(
                    name='Porygon2', species='Porygon2', abilities=('Trace', 'Download'), pkTypes=('Normal',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Recover', 'Protect'],
                            {
                                'Recover': ['Thunderbolt', 'Discharge', 'Tri Attack'],
                                'Thunderbolt': ['Ice Beam', 'Tri Attack'],
                                'Discharge': ['Ice Beam', 'Tri Attack'],
                                'Ice Beam': ['Thunder Wave', 'Toxic', 'Trick Room'],
                                'Protect': ['Trick Room', 'Icy Wind', 'Gravity', 'Trick Room'],
                                'Trick Room': ['Recover', 'Recover', 'Thunderbolt', 'Discharge', 'Charge Beam'],
                                'Icy Wind': ['Recover', 'Thunderbolt', 'Tri Attack'],
                                'Tri Attack': ['Shadow Ball', 'Hidden Power [Fighting]'],
                                'Charge Beam': ['Tri Attack'],
                                'Gravity': ['Blizzard'],
                                'Blizzard': ['Thunder', 'Zap Cannon']
                            }
                        ),
                    ), baseStats=(85, 80, 90, 105, 95, 60), genders=('',), images=('233.gif', '233.png', '233 (1).png')
                )
            if 'Stantler':
                root.pokesets['Stantler'] = pokemon_ddl.PokemonSet(
                    name='Stantler', species='Stantler', abilities=('Intimidate', 'Frisk'), pkTypes=('Normal',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Confuse Ray', 'Headbutt', 'Gravity'],
                                'Confuse Ray': ['Thunder Wave'],
                                'Thunder Wave': ['Headbutt'],
                                'Headbutt': ['Megahorn'],
                                'Megahorn': ['Earthquake', 'Sucker Punch', 'Bite'],
                                'Gravity': ['Hypnosis'],
                                'Hypnosis': ['Megahorn']
                            }
                        ),
                    ), baseStats=(73, 95, 62, 85, 65, 85), genders=('M', 'F'), images=('234.gif', '234.png', '234 (1).png')
                )
            if 'Smeargle':
                root.pokesets['Smeargle'] = pokemon_ddl.PokemonSet(
                    name='Smeargle', species='Smeargle', abilities=('Own Tempo', 'Technician'), pkTypes=('Normal',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Stealth Rock', 'Spikes'],
                                'Stealth Rock': ['Spore'],
                                'Spikes': ['Spore'],
                                'Spore': ['U-turn', 'Trick', 'Spikes', 'Lunar Dance']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Dark Void'],
                                'Dark Void': ['Icy Wind'],
                                'Icy Wind': ['Explosion', 'Destiny Bond']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Baton Pass'],
                                'Baton Pass': ['Spore'],
                                'Spore': ['Belly Drum', 'Substitute', 'Ingrain', 'Agility', 'Nasty Plot', 'Belly Drum', 'Belly Drum', 'Ancient Power']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Super Fang', 'Endeavor'],
                                'Super Fang': ['Icy Wind', 'Recover'],
                                'Endeavor': ['Quick Attack', 'Destiny Bond'],
                                'Icy Wind': ['Recover'],
                                'Recover': ['Mirror Coat', 'Counter']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Perish Song', 'Belly Drum'],
                                'Perish Song': ['Dark Void'],
                                'Dark Void': ['Spider Web'],
                                'Belly Drum': ['Explosion', 'Extreme Speed']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Dark Void'],
                                'Dark Void': ['Fake Out'],
                                'Fake Out': ['Follow Me', 'Transform', 'Super Fang', 'Endeavor']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Fake Out'],
                                'Fake Out': ['Sacred Fire'],
                                'Sacred Fire': ['Transform', 'Dark Void', 'Explosion']
                            }
                        )
                    ), baseStats=(55, 20, 35, 20, 45, 75), genders=('M', 'F'), images=('235.gif', '235.png', '235 (1).png')
                )
            if 'Miltank':
                root.pokesets['Miltank'] = pokemon_ddl.PokemonSet(
                    name='Miltank', species='Miltank', abilities=('Thick Fat', 'Scrappy'), pkTypes=('Normal',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Milk Drink'],
                                'Milk Drink': ['Toxic', 'Thunder Wave', 'Body Slam'],
                                'Thunder Wave': ['Iron Head', 'Dizzy Punch'],
                                'Body Slam': ['Iron Head', 'Fire Punch', 'Ice Punch'],
                                'Toxic': ['Stealth Rock', 'Rock Slide']
                            }
                        ),
                    ), baseStats=(95, 80, 105, 40, 70, 100), genders=('F',), images=('241.gif', '241.png', '241 (1).png')
                )
            if 'Blissey':
                root.pokesets['Blissey'] = pokemon_ddl.PokemonSet(
                    name='Blissey', species='Blissey', abilities=('Natural Cure', 'Serene Grace'), pkTypes=('Normal',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Soft-Boiled', 'Wish'],
                                'Soft-Boiled': ['Hyper Beam', 'Toxic', 'Thunder Wave', 'Wish', 'Shadow Ball', 'Helping Hand'],
                                'Hyper Beam': ['Shadow Ball', 'Thunderbolt', 'Ice Beam', 'Psychic'],
                                'Toxic': ['Seismic Toss', 'Aromatherapy', 'Stealth Rock', 'Healing Wish', 'Shadow Ball'],
                                'Thunder Wave': ['Stealth Rock', 'Seismic Toss'],
                                'Wish': ['Seismic Toss'],
                                'Seismic Toss': ['Toxic'],
                                'Shadow Ball': ['Flamethrower', 'Focus Blast'],
                                'Helping Hand': ['Icy Wind', 'Healing Wish', 'Psychic']
                            }
                        ),
                    ), baseStats=(255, 10, 10, 75, 135, 55), genders=('F',), images=('242.gif', '242.png', '242 (1).png')
                )
            if 'Linoone':
                root.pokesets['Linoone'] = pokemon_ddl.PokemonSet(
                    name='Linoone', species='Linoone', abilities=('Gluttony',), pkTypes=('Normal',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {'Protect': ['Belly Drum', 'Belly Drum', 'Switcheroo', 'Helping Hand', 'Gunk Shot', 'Extreme Speed'],
                             'Belly Drum': ['Extreme Speed'],
                             'Extreme Speed': ['Seed Bomb', 'Shadow Claw'],
                             'Switcheroo': ['Extreme Speed'],
                             'Helping Hand': ['Icy Wind', 'Extreme Speed'],
                             'Icy Wind': ['Extreme Speed']}
                        ),
                    ), baseStats=(78, 70, 61, 50, 61, 100), genders=('M', 'F'), images=('264.gif', '264.png', '264 (1).png')
                )
            if 'Slaking':
                root.pokesets['Slaking'] = pokemon_ddl.PokemonSet(
                    name='Slaking', species='Slaking', abilities=('Truant',), pkTypes=('Normal',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Slack Off', 'Protect', 'Return'],
                            {
                                'Slack Off': ['Return', 'Double-Edge', 'Giga Impact', 'Thunder', 'Yawn'],
                                'Protect': ['Return', 'Double-Edge', 'Giga Impact'],
                                'Return': ['Earthquake', 'Night Slash', 'Earthquake'],
                                'Double-Edge': ['Earthquake', 'Rock Slide'],
                                'Giga Impact': ['Earthquake'],
                                'Earthquake': ['Fire Punch', 'Ice Punch', 'Dynamic Punch', 'Gunk Shot', 'Hammer Arm', 'Shadow Claw', 'Thunder Punch'],
                                'Rock Slide': ['Earthquake', 'Shadow Claw', 'Fire Punch'],
                                'Night Slash': ['Earthquake', 'Fire Punch', 'Ice Punch', 'Dynamic Punch', 'Gunk Shot', 'Hammer Arm'],
                                'Thunder': ['Blizzard', 'Fire Blast', 'Focus Blast', 'Hyper Beam', 'Shadow Ball']
                            }
                        ),
                    ), baseStats=(150, 160, 100, 95, 65, 100), genders=('M', 'F'), images=('289.gif', '289.png', '289 (1).png')
                )
            if 'Exploud':
                root.pokesets['Exploud'] = pokemon_ddl.PokemonSet(
                    name='Exploud', species='Exploud', abilities=('Soundproof',), pkTypes=('Normal',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Return', 'Hyper Voice', 'Hyper Voice', 'Teeter Dance', 'Return', 'Hyper Voice'],
                                'Return': ['Earthquake', 'Crunch'],
                                'Earthquake': ['Crunch', 'Surf', 'Ice Beam'],
                                'Crunch': ['Earthquake', 'Surf', 'Ice Beam'],
                                'Hyper Voice': ['Blizzard', 'Ice Beam'],
                                'Blizzard': ['Thunder', 'Thunderbolt', 'Fire Fang', 'Crunch', 'Surf', 'Overheat', 'Shadow Ball',
                                             'Thunder Fang', 'Extrasensory'],
                                'Teeter Dance': ['Icy Wind'],
                                'Icy Wind': ['Return', 'Hyper Voice'],
                                'Ice Beam': ['Thunder', 'Thunderbolt', 'Fire Fang', 'Crunch', 'Surf', 'Overheat', 'Shadow Ball',
                                             'Thunder Fang', 'Extrasensory']
                            }
                        ),
                    ), baseStats=(104, 91, 63, 91, 63, 68), genders=('M', 'F'), images=('295.gif', '295.png', '295 (1).png')
                )
            if 'Delcatty':
                root.pokesets['Delcatty'] = pokemon_ddl.PokemonSet(
                    name='Delcatty', species='Delcatty', abilities=('Cute Charm', 'Normalize'), pkTypes=('Normal',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Thunder Wave', 'Thunder Wave', 'Body Slam', 'Fake Out', 'Sing', 'Attract'],
                                'Thunder Wave': ['Heal Bell', 'Baton Pass', 'Wish'],
                                'Heal Bell': ['Return', 'Double-Edge', 'Fake Out', 'Sucker Punch'],
                                'Baton Pass': ['Return', 'Double-Edge', 'Fake Out', 'Sucker Punch'],
                                'Wish': ['Return', 'Double-Edge', 'Fake Out', 'Sucker Punch', 'Baton Pass'],
                                'Sing': ['Calm Mind', 'Charge Beam', 'Wish', 'Substitute'],
                                'Calm Mind': ['Baton Pass'],
                                'Charge Beam': ['Baton Pass'],
                                'Substitute': ['Baton Pass'],
                                'Fake Out': ['Calm Mind', 'Charge Beam', 'Wish', 'Substitute'],
                                'Body Slam': ['Calm Mind', 'Charge Beam', 'Wish', 'Substitute'],
                                'Attract': ['Thunder Wave']
                            }
                        ),
                    ), baseStats=(70, 65, 65, 55, 55, 70), genders=('M', 'F'), images=('301.gif', '301.png', '301 (1).png')
                )
            if 'Spinda':
                root.pokesets['Spinda'] = pokemon_ddl.PokemonSet(
                    name='Spinda', species='Spinda', abilities=('Own Tempo', 'Tangled Feet'), pkTypes=('Normal',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Teeter Dance', 'Wish', 'Calm Mind', 'Teeter Dance'],
                                'Teeter Dance': ['Body Slam'],
                                'Body Slam': ['Substitute', 'Rock Slide'],
                                'Wish': ['Baton Pass'],
                                'Calm Mind': ['Baton Pass'],
                                'Baton Pass': ['Hypnosis', 'Teeter Dance']
                            }
                        ),
                    ), baseStats=(60, 60, 60, 60, 60, 60), genders=('M', 'F'), images=('327.gif', '327.png', '327 (1).png')
                )
            if 'Zangoose':
                root.pokesets['Zangoose'] = pokemon_ddl.PokemonSet(
                    name='Zangoose', species='Zangoose', abilities=('Immunity',), pkTypes=('Normal',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Swords Dance', 'Crush Claw', 'Swords Dance', 'Slash'],
                                'Swords Dance': ['Return', 'Quick Attack'],
                                'Return': ['Close Combat', 'Shadow Claw', 'Close Combat'],
                                'Quick Attack': ['Close Combat'],
                                'Crush Claw': ['Aerial Ace', 'Knock Off'],
                                'Aerial Ace': ['Close Combat'],
                                'Knock Off': ['Ice Punch', 'Iron Tail'],
                                'Slash': ['Night Slash'],
                                'Night Slash': ['Shadow Claw', 'Poison Jab', 'Rock Slide', 'Roar', 'X-Scissor']
                            }
                        ),
                    ), baseStats=(73, 115, 60, 60, 60, 90), genders=('M', 'F'), images=('335.gif', '335.png', '335 (1).png')
                )
            if 'Castform':
                root.pokesets['Castform'] = pokemon_ddl.PokemonSet(
                    name='Castform', species='Castform', abilities=('Forecast',), pkTypes=('Normal',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Rain Dance', 'Hail', 'Sunny Day', 'Weather Ball'],
                                'Rain Dance': ['Thunder'],
                                'Thunder': ['Weather Ball'],
                                'Weather Ball': ['Energy Ball', 'Shadow Ball', 'Ominous Wind', 'Thunder Wave'],
                                'Hail': ['Blizzard'],
                                'Blizzard': ['Thunderbolt', 'Thunder'],
                                'Thunderbolt': ['Energy Ball', 'Shadow Ball', 'Ominous Wind'],
                                'Sunny Day': ['Fire Blast', 'Flamethrower', 'Weather Ball'],
                                'Fire Blast': ['Energy Ball', 'Shadow Ball', 'Ominous Wind', 'Thunder Wave'],
                                'Flamethrower': ['Energy Ball', 'Shadow Ball', 'Ominous Wind', 'Thunder Wave']
                            }
                        ),
                    ), baseStats=(73, 115, 60, 60, 60, 90), genders=('M', 'F'), images=('335.gif', '335.png', '335 (1).png')
                )
            if 'Kecleon':
                root.pokesets['Kecleon'] = pokemon_ddl.PokemonSet(
                    name='Kecleon', species='Kecleon', abilities=('Color Change',), pkTypes=('Normal',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Stealth Rock', 'Thunder Wave', 'Trick', 'Trick Room', 'Trick Room'],
                                'Stealth Rock': ['Recover'],
                                'Thunder Wave': ['Recover'],
                                'Recover': ['Aqua Tail', 'Shadow Sneak', 'Return', 'Low Kick'],
                                'Trick': ['Aqua Tail', 'Return', 'Low Kick', 'Shadow Sneak'],
                                'Trick Room': ['Recover', 'Dizzy Punch'],
                                'Dizzy Punch': ['Shadow Sneak']
                            }
                        ),
                    ), baseStats=(60, 90, 70, 60, 120, 40), genders=('M', 'F'), images=('352.gif', '352.png', '352 (1).png')
                )
            if 'Bibarel':
                root.pokesets['Bibarel'] = pokemon_ddl.PokemonSet(
                    name='Bibarel', species='Bibarel', abilities=('Simple', 'Unaware'), pkTypes=('Normal', 'Water'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Curse', 'Stealth Rock', 'Curse'],
                                'Curse': ['Waterfall'],
                                'Waterfall': ['Quick Attack', 'Return'],
                                'Stealth Rock': ['Toxic', 'Taunt'],
                                'Toxic': ['Waterfall', 'Return'],
                                'Taunt': ['Waterfall', 'Return']
                            }
                        ),
                    ), baseStats=(79, 85, 60, 55, 60, 71), genders=('M', 'F'), images=('400.gif', '400-m.png', '400-m (1).png'),
                    ability_weights=(0.7, 0.3)
                )
            if 'Ambipom':
                root.pokesets['Ambipom'] = pokemon_ddl.PokemonSet(
                    name='Ambipom', species='Ambipom', abilities=('Technician',), pkTypes=('Normal',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Fake Out', 'Fake Out', 'Fake Out', 'Baton Pass', 'Gunk Shot'],
                                'Fake Out': ['Taunt', 'Double Hit'],
                                'Taunt': ['U-turn', 'Low Kick', 'Pursuit', 'Payback', 'Double Hit', 'Knock Off'],
                                'Double Hit': ['U-turn', 'Low Kick', 'Payback', 'Brick Break', 'Shadow Claw', 'Knock Off'],
                                'Baton Pass': ['Agility', 'Nasty Plot', 'Taunt'],
                                'Nasty Plot': ['Water Pulse', 'Swift'],
                                'Gunk Shot': ['Seed Bomb', 'Brick Break'],
                                'Seed Bomb': ['Double Hit'],
                                'Brick Break': ['Double Hit']
                            }
                        ),
                    ), baseStats=(75, 100, 66, 60, 66, 115), genders=('M', 'F'), images=('424.gif', '424-m.png', '424-m (1).png')
                )
            if 'Lopunny':
                root.pokesets['Lopunny'] = pokemon_ddl.PokemonSet(
                    name='Lopunny', species='Lopunny', abilities=('Cute Charm', 'Klutz'), pkTypes=('Normal',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Fake Out'],
                            {
                                'Fake Out': ['Protect', 'Last Resort']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Fake Out'],
                                'Fake Out': ['Dizzy Punch', 'Return'],
                                'Return': ['Drain Punch'],
                                'Dizzy Punch': ['Drain Punch']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Switcheroo', 'Fling'],
                                'Switcheroo': ['Fake Out'],
                                'Fling': ['Fake Out'],
                                'Fake Out': ['Encore', 'Dizzy Punch', 'Return', 'Bounce', 'Jump Kick', 'Sky Uppercut']
                            }
                        ),
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Baton Pass'],
                                'Baton Pass': ['Agility', 'Substitute'],
                                'Agility': ['Fake Out', 'Encore'],
                                'Substitute': ['Fake Out', 'Encore']
                            }
                        )
                    ), baseStats=(65, 76, 84, 54, 96, 105), genders=('M', 'F'), images=('428.gif', '428.png', '428 (1).png')
                )
            if 'Purugly':
                root.pokesets['Purugly'] = pokemon_ddl.PokemonSet(
                    name='Purugly', species='Purugly', abilities=('Thick Fat', 'Own Tempo'), pkTypes=('Normal',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Fake Out'],
                                'Fake Out': ['Sunny Day', 'Rain Dance', 'U-turn', 'U-turn'],
                                'U-turn': ['Body Slam', 'Return', 'Taunt', 'Shadow Claw'],
                                'Rain Dance': ['Thunder', 'Body Slam', 'Return', 'Taunt', 'Shadow Claw'],
                                'Sunny Day': ['Bite', 'Body Slam', 'Return', 'Taunt', 'Shadow Claw']
                            }
                        ),
                    ), baseStats=(71, 82, 64, 64, 59, 112), genders=('M', 'F'), images=('432.gif', '432.png', '432 (1).png')
                )
            if 'Lickilicky':
                root.pokesets['Lickilicky'] = pokemon_ddl.PokemonSet(
                    name='Lickilicky', species='Lickilicky', abilities=('Own Tempo', 'Oblivious'), pkTypes=('Normal',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Belly Drum', 'Curse', 'Power Whip', 'Hyper Beam', 'Power Whip', 'Wring Out'],
                                'Belly Drum': ['Return', 'Earthquake'],
                                'Curse': ['Gyro Ball'],
                                'Gyro Ball': ['Giga Impact', 'Return'],
                                'Power Whip': ['Aqua Tail', 'Return', 'Body Slam', 'Knock Off', 'Brick Break', 'Earthquake',
                                               'Fire Punch', 'Giga Impact', 'Explosion', 'Hammer Arm', 'Ice Punch', 'Iron Tail',
                                               'Lick', 'Rock Slide', 'Zen Headbutt', 'Surf', 'Ice Beam', 'Thunderbolt'],
                                'Hyper Beam': ['Surf', 'Muddy Water', 'Water Pulse', 'Muddy Water', 'Ice Punch'],
                                'Wring Out': ['Surf', 'Muddy Water', 'Water Pulse', 'Muddy Water', 'Ice Punch'],
                                'Surf': ['Ice Beam', 'Blizzard', 'Thunderbolt', 'Focus Blast', 'Icy Wind', 'Knock Off',
                                         'Shadow Ball', 'Thunder'],
                                'Muddy Water': ['Ice Beam', 'Blizzard', 'Thunderbolt', 'Focus Blast', 'Icy Wind', 'Knock Off',
                                         'Shadow Ball', 'Thunder'],
                                'Water Pulse': ['Ice Beam', 'Blizzard', 'Thunderbolt', 'Focus Blast', 'Icy Wind', 'Knock Off',
                                         'Shadow Ball', 'Thunder'],
                                'Ice Punch': ['Thunderbolt', 'Thunder', 'Surf', 'Muddy Water', 'Water Pulse']
                            }
                        ),
                    ), baseStats=(110, 85, 95, 80, 95, 50), genders=('M', 'F'), images=('463.gif', '463.png', '463 (1).png')
                )
            if 'Porygon-Z':
                root.pokesets['Porygon-Z'] = pokemon_ddl.PokemonSet(
                    name='Porygon-Z', species='Porygon-Z', abilities=('Adaptability', 'Download'), pkTypes=('Normal',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Nasty Plot', 'Hyper Beam', 'Tri Attack'],
                                'Nasty Plot': ['Tri Attack'],
                                'Hyper Beam': ['Tri Attack'],
                                'Tri Attack': ['Ice Beam', 'Dark Pulse', 'Discharge', 'Charge Beam', 'Blizzard', 'Psychic',
                                               'Shadow Ball', 'Signal Beam', 'Thunderbolt', 'Zap Cannon', 'Hidden Power [Ground]']
                            }
                        ),
                    ), baseStats=(85, 80, 70, 135, 75, 90), genders=('',), images=('474.gif', '474.png', '474 (1).png')
                )
            if 'Regigigas':
                root.pokesets['Regigigas'] = pokemon_ddl.PokemonSet(
                    name='Regigigas', species='Regigigas', abilities=('Slow Start',), pkTypes=('Normal',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Body Slam', 'Thunder Wave', 'Knock Off'],
                            {
                                'Thunder Wave': ['Return', 'Crush Grip'],
                                'Return': ['Earthquake', 'Fire Punch', 'Drain Punch'],
                                'Earthquake': ['Substitute', 'Confuse Ray'],
                                'Fire Punch': ['Substitute', 'Confuse Ray'],
                                'Body Slam': ['Earthquake', 'Fire Punch', 'Drain Punch'],
                                'Knock Off': ['Thunder Wave', 'Toxic'],
                                'Toxic': ['Return'],
                                'Drain Punch': ['Substitute', 'Confuse Ray'],
                                'Crush Grip': ['Earthquake', 'Fire Punch', 'Drain Punch']
                            }
                        ),
                    ), baseStats=(110, 160, 110, 80, 110, 100), genders=('',), images=('486.gif', '486.png', '486 (1).png')
                )
            if 'Arceus':
                root.pokesets['Arceus'] = pokemon_ddl.PokemonSet(
                    name='Arceus', species='Arceus', abilities=('Multitype',), pkTypes=('Normal',),
                    sets=(
                        # MoveSet 1: "The Chaotic Bulwark". Guaranteed Protect + Judgement, then maximum variance.
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Judgement'],

                                # Judgement is the central hub for a chaotic web of possibilities.
                                'Judgement': [
                                    'Calm Mind', 'Swords Dance', 'Recover', 'Cosmic Power', 'Will-O-Wisp',
                                    'Thunder Wave', 'Extreme Speed', 'Earth Power', 'Ice Beam', 'Thunderbolt',
                                    'Flamethrower', 'Shadow Claw', 'Gravity', 'Substitute'
                                ],

                                # Every node below is heavily interconnected to create unpredictable sets.
                                'Calm Mind': ['Ice Beam', 'Thunderbolt', 'Earthquake', 'Shadow Claw', 'Recover',
                                              'Swords Dance', 'Will-O-Wisp'],
                                'Swords Dance': ['Extreme Speed', 'Dragon Claw', 'Shadow Claw', 'Earthquake', 'Surf',
                                                 'Ice Beam', 'Calm Mind'],
                                'Recover': ['Calm Mind', 'Will-O-Wisp', 'Ice Beam', 'Flamethrower', 'Substitute',
                                            'Swords Dance', 'Judgement'],
                                'Cosmic Power': ['Recover', 'Will-O-Wisp', 'Toxic', 'Flamethrower', 'Judgement'],
                                'Will-O-Wisp': ['Recover', 'Calm Mind', 'Extreme Speed', 'Dragon Claw'],
                                'Extreme Speed': ['Swords Dance', 'Shadow Claw', 'Draco Meteor', 'Overheat',
                                                  'Judgement',
                                                  'Recover'],
                                'Earth Power': ['Ice Beam', 'Thunderbolt', 'Calm Mind', 'Swords Dance', 'Dragon Claw'],
                                'Ice Beam': ['Thunderbolt', 'Earth Power', 'Judgement', 'Calm Mind', 'Swords Dance'],
                                'Thunderbolt': ['Ice Beam', 'Surf', 'Judgement', 'Calm Mind', 'Swords Dance'],
                                'Dragon Claw': ['Earthquake', 'Shadow Claw', 'Swords Dance', 'Calm Mind', 'Ice Beam'],
                                'Substitute': ['Calm Mind', 'Swords Dance', 'Recover', 'Will-O-Wisp', 'Judgement'],
                                'Gravity': ['Thunder', 'Blizzard', 'Focus Blast', 'Earthquake', 'Judgement'],
                            }
                        ),

                        # MoveSet 2: "The Chaotic Gambler". No Protect, starts with Judgement into chaos.
                        pokemon_ddl.MoveSet(
                            ['Judgement'],
                            {
                                'Judgement': [
                                    'Extreme Speed', 'Draco Meteor', 'Outrage', 'Calm Mind', 'Swords Dance',
                                    'Gravity', 'Trick Room', 'Fire Blast', 'Thunder', 'Ice Beam', 'Earthquake',
                                    'Shadow Claw', 'Will-O-Wisp', 'Recover'
                                ],

                                'Draco Meteor': ['Extreme Speed', 'Overheat', 'Earthquake', 'Fire Blast', 'Steel Wing'],
                                'Outrage': ['Extreme Speed', 'Aqua Tail', 'Iron Head', 'Ice Beam', 'Giga Drain'],
                                'Calm Mind': ['Ice Beam', 'Thunder', 'Focus Blast', 'Shadow Claw', 'Recover',
                                              'Swords Dance'],
                                'Swords Dance': ['Extreme Speed', 'Shadow Claw', 'Dragon Claw', 'Giga Drain',
                                                 'Calm Mind'],
                                'Gravity': ['Thunder', 'Blizzard', 'Focus Blast', 'Draco Meteor', 'Judgement'],
                                'Trick Room': ['Judgement', 'Draco Meteor', 'Fire Blast', 'Thunder', 'Focus Blast'],
                                'Extreme Speed': ['Judgement', 'Swords Dance', 'Draco Meteor', 'Will-O-Wisp',
                                                  'Recover'],
                                'Fire Blast': ['Draco Meteor', 'Thunder', 'Ice Beam', 'Earthquake'],
                                'Earthquake': ['Stone Edge', 'Outrage', 'Dragon Claw', 'Flamethrower'],
                                'Recover': ['Judgement', 'Calm Mind', 'Swords Dance', 'Will-O-Wisp', 'Toxic']
                            }
                        ),

                        # MoveSet 3: "The Perish Trapper". A specific, high-risk alternate strategy.
                        pokemon_ddl.MoveSet(
                            ['Perish Song'],
                            {
                                'Mean Look': ['Protect', 'Recover', 'Judgement'],
                                'Perish Song': ['Mean Look']
                            }
                        )
                    ), baseStats=(120, 120, 120, 120, 120, 120), genders=('',), images=('493.gif', 'arceus.png', 'arceus (1).png'),
                    stat_key='arcStat'
                )

        # Water type pokemon
        if 'Water':
            if 'Blastoise':
                root.pokesets['Blastoise'] = pokemon_ddl.PokemonSet(
                    name='Blastoise', species='Blastoise', abilities=('Torrent',), pkTypes=('Water',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Rapid Spin', 'Double Team', 'Hydro Pump', 'Water Spout', 'Aqua Tail', 'Waterfall', 'Rapid Spin', 'Water Spout', 'Double Team'],
                                'Rapid Spin': ['Roar', 'Rest', 'Ice Beam', 'Signal Beam'],
                                'Roar': ['Hydro Pump', 'Surf', 'Water Spout', 'Muddy Water'],
                                'Rest': ['Hydro Pump', 'Surf', 'Water Spout', 'Muddy Water'],
                                'Ice Beam': ['Hydro Pump', 'Surf', 'Water Spout', 'Muddy Water'],
                                'Signal Beam': ['Hydro Pump', 'Surf', 'Water Spout', 'Muddy Water'],
                                'Double Team': ['Focus Punch', 'Hydro Cannon'],
                                'Focus Punch': ['Hydro Cannon', 'Skull Bash', 'Aqua Ring', 'Aqua Tail', 'Earthquake', 'Waterfall'],
                                'Hydro Cannon': ['Flash Cannon', 'Signal Beam', 'Ice Beam', 'Blizzard', 'Focus Blast', 'Hidden Power [Grass]',],
                                'Hydro Pump': ['Mirror Coat', 'Flash Cannon', 'Signal Beam', 'Focus Blast', 'Hidden Power [Grass]', 'Rapid Spin', 'Icy Wind'],
                                'Water Spout': ['Mirror Coat', 'Flash Cannon', 'Signal Beam', 'Focus Blast', 'Hidden Power [Grass]', 'Rapid Spin', 'Icy Wind'],
                                'Mirror Coat': ['Ice Beam', 'Blizzard', 'Signal Beam', 'Rest'],
                                'Flash Cannon': ['Hidden Power [Grass]', 'Icy Wind'],
                                'Aqua Tail': ['Earthquake', 'Avalanche', 'Zen Headbutt', 'Bite', 'Skull Bash', 'Rest', 'Outrage'],
                                'Waterfall': ['Earthquake', 'Avalanche', 'Zen Headbutt', 'Bite', 'Skull Bash', 'Rest', 'Outrage']
                            }
                        ),
                    ), baseStats=(79, 83, 100, 85, 105, 78), genders=('M', 'F'), images=('009.gif', '009.png', '009 (1).png')
                )
            if 'Golduck':
                root.pokesets['Golduck'] = pokemon_ddl.PokemonSet(
                    name='Golduck', species='Golduck', abilities=('Damp', 'Cloud Nine'), pkTypes=('Water',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Encore', 'Calm Mind', 'Confuse Ray', 'Aqua Tail'],
                                'Encore': ['Hidden Power [Grass]'],
                                'Hidden Power [Grass]': ['Surf', 'Hydro Pump'],
                                'Calm Mind': ['Surf', 'Hydro Pump'],
                                'Surf': ['Psychic', 'Ice Beam', 'Hidden Power [Grass]', 'Encore'],
                                'Hydro Pump': ['Psychic', 'Ice Beam', 'Hidden Power [Grass]', 'Encore', 'Cross Chop'],
                                'Confuse Ray': ['Surf', 'Hydro Pump'],
                                'Aqua Tail': ['Cross Chop'],
                                'Cross Chop': ['Shadow Claw', 'Ice Punch', 'Zen Headbutt']
                            }
                        ),
                    ), baseStats=(80, 82, 78, 95, 80, 85), genders=('M', 'F'), images=('055.gif', '055.png', '055 (1).png')
                )
            if 'Kingler':
                root.pokesets['Kingler'] = pokemon_ddl.PokemonSet(
                    name='Kingler', species='Kingler', abilities=('Hyper Cutter', 'Shell Armor'), pkTypes=('Water',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Agility', 'Swords Dance', 'Crabhammer', 'Icy Wind'],
                                'Agility': ['Crabhammer'],
                                'Swords Dance': ['Crabhammer'],
                                'Crabhammer': ['Return', 'X-Scissor', 'Rock Slide', 'Superpower'],
                                'Icy Wind': ['Haze', 'Guillotine', 'Knock Off'],
                                'Haze': ['Crabhammer'],
                                'Guillotine': ['Crabhammer'],
                                'Knock Off': ['Crabhammer']
                            }
                        ),
                    ), baseStats=(55, 130, 115, 50, 50, 75), genders=('M', 'F'), images=('099.gif', '099.png', '099 (1).png')
                )
            if 'Seaking':
                root.pokesets['Seaking'] = pokemon_ddl.PokemonSet(
                    name='Seaking', species='Seaking', abilities=('Swift Swim', 'Water Veil'), pkTypes=('Water',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Waterfall', 'Aqua Tail'],
                                'Waterfall': ['Megahorn', 'Poison Jab'],
                                'Aqua Tail': ['Megahorn', 'Poison Jab'],
                                'Megahorn': ['Return', 'Ice Beam', 'Rain Dance', 'Horn Drill'],
                                'Poison Jab': ['Megahorn', 'Knock Off', 'Rain Dance']
                            }
                        ),
                    ), baseStats=(80, 92, 65, 65, 80, 68), genders=('M', 'F'), images=('119.gif', '119-m.png', '119-m (1).png'),
                    ability_weights=(0.7, 0.3)
                )
            if 'Vaporeon':
                root.pokesets['Vaporeon'] = pokemon_ddl.PokemonSet(
                    name='Vaporeon', species='Vaporeon', abilities=('Water Absorb',), pkTypes=('Water',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Wish'],
                            {
                                'Protect': ['Surf', 'Hydro Pump', 'Shadow Ball'],
                                'Surf': ['Substitute', 'Ice Beam'],
                                'Hydro Pump': ['Substitute', 'Ice Beam'],
                                'Substitute': ['Ice Beam', 'Baton Pass'],
                                'Ice Beam': ['Baton Pass', 'Substitute'],
                                'Wish': ['Baton Pass'],
                                'Baton Pass': ['Acid Armor', 'Helping Hand', 'Yawn'],
                                'Acid Armor': ['Surf', 'Hydro Pump', 'Muddy Water', 'Water Pulse'],
                                'Helping Hand': ['Muddy Water', 'Icy Wind', 'Brine'],
                                'Shadow Ball': ['Hyper Beam', 'Ice Beam', 'Signal Beam', 'Hidden Power [Electric]'],
                                'Yawn': ['Hydro Pump', 'Muddy Water', 'Water Pulse'],
                                'Hyper Beam': ['Brine', 'Muddy Water', 'Surf', 'Hydro Pump'],
                                'Signal Beam': ['Brine', 'Muddy Water', 'Water Pulse', 'Hydro Pump'],
                                'Hidden Power [Electric]': ['Hydro Pump', 'Surf']
                            }
                        ),
                    ), baseStats=(130, 65, 60, 110, 95, 65), genders=('M', 'F'), images=('134.gif', '134.png', '134 (1).png')
                )
            if 'Feraligatr':
                root.pokesets['Feraligatr'] = pokemon_ddl.PokemonSet(
                    name='Feraligatr', species='Feraligatr', abilities=('Torrent',), pkTypes=('Water',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Dragon Dance', 'Rock Slide' , 'Hydro Cannon', 'Waterfall', 'Aqua Tail', 'Swords Dance'],
                                'Dragon Dance': ['Earthquake', 'Low Kick'],
                                'Earthquake': ['Waterfall'],
                                'Low Kick': ['Waterfall'],
                                'Rock Slide': ['Ice Fang'],
                                'Ice Fang': ['Waterfall'],
                                'Waterfall': ['Return', 'Earthquake', 'Crunch', 'Dragon Claw', 'Ice Fang', 'Outrage', 'Superpower'],
                                'Aqua Tail': ['Return', 'Earthquake', 'Crunch', 'Dragon Claw', 'Ice Fang', 'Outrage', 'Superpower'],
                                'Swords Dance': ['Aqua Jet'],
                                'Aqua Jet': ['Waterfall', 'Aqua Tail', 'Metal Claw', 'Dragon Claw', 'Outrage'],
                                'Hydro Cannon': ['Ice Beam', 'Dragon Pulse', 'Hyper Beam', 'Focus Blast', 'Ancient Power']
                            }
                        ),
                    ), baseStats=(85, 105, 100, 79, 83, 78), genders=('M', 'F'), images=('160.gif', '160.png', '160 (1).png')
                )
            if 'Azumarill':
                root.pokesets['Azumarill'] = pokemon_ddl.PokemonSet(
                    name='Azumarill', species='Azumarill', abilities=('Thick Fat', 'Huge Power'), pkTypes=('Water',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Protect', 'Substitute', 'Rest'],
                            {
                                'Protect': ['Waterfall', 'Aqua Jet'],
                                'Waterfall': ['Ice Punch', 'Superpower'],
                                'Aqua Jet': ['Waterfall', 'Ice Punch', 'Superpower'],
                                'Ice Punch': ['Return', 'Double-Edge'],
                                'Superpower': ['Return', 'Double-Edge'],
                                'Substitute': ['Focus Punch'],
                                'Focus Punch': ['Aqua Jet', 'Encore', 'Toxic'],
                                'Encore': ['Ice Punch', 'Waterfall'],
                                'Toxic': ['Ice Punch', 'Waterfall'],
                                'Rest': ['Sleep Talk'],
                                'Sleep Talk': ['Waterfall']
                            }
                        ),
                    ), baseStats=(100, 50, 80, 50, 80, 50), genders=('M', 'F'), images=('184.gif', '184.png', '184 (1).png'),
                    ability_weights=(0.2, 0.8)
                )
            if 'Politoed':
                root.pokesets['Politoed'] = pokemon_ddl.PokemonSet(
                    name='Politoed', species='Politoed', abilities=('Water Absorb', 'Damp'), pkTypes=('Water',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Toxic', 'Ice Beam', 'Hyper Voice', 'Toxic', 'Ice Beam', 'Mud Bomb', 'Perish Song', 'Belly Drum', 'Hypnosis'],
                                'Toxic': ['Encore', 'Ice Beam', 'Refresh'],
                                'Encore': ['Surf'],
                                'Ice Beam': ['Encore', 'Surf', 'Hydro Pump'],
                                'Refresh': ['Encore'],
                                'Surf': ['Psychic', 'Focus Blast'],
                                'Hydro Pump': ['Psychic', 'Focus Blast'],
                                'Perish Song': ['Whirlpool'],
                                'Whirlpool': ['Refresh', 'Rest'],
                                'Belly Drum': ['Waterfall'],
                                'Waterfall': ['Brick Break', 'Earthquake'],
                                'Hyper Voice': ['Toxic', 'Ice Beam', 'Mud Bomb', 'Hypnosis'],
                                'Mud Bomb': ['Toxic', 'Ice Beam', 'Mud Bomb', 'Hypnosis'],
                                'Hypnosis': ['Ice Beam', 'Mud Bomb', 'Surf', 'Hydro Pump', 'Perish Song']
                            }
                        ),
                    ), baseStats=(90, 75, 75, 90, 100, 70), genders=('M', 'F'), images=('186.gif', '186-m.png', '186-m (1).png')
                )
            if 'Qwilfish':
                root.pokesets['Qwilfish'] = pokemon_ddl.PokemonSet(
                    name='Qwilfish', species='Qwilfish', abilities=('Poison Point', 'Swift Swim'),
                    pkTypes=('Water', 'Poison'),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Toxic Spikes', 'Spikes', 'Swords Dance', 'Rain Dance', 'Spikes', 'Toxic Spikes'],
                                'Toxic Spikes': ['Explosion'],
                                'Explosion': ['Waterfall', 'Poison Jab'],
                                'Spikes': ['Explosion', 'Pain Split'],
                                'Swords Dance': ['Poison Jab'],
                                'Rain Dance': ['Waterfall'],
                                'Waterfall': ['Poison Jab', 'Explosion', 'Taunt', 'Destiny Bond'],
                                'Pain Split': ['Taunt', 'Poison Jab', 'Aqua Jet'],
                                'Poison Jab': ['Waterfall']
                            }
                        ),
                    ), baseStats=(65, 95, 75, 55, 55, 85), genders=('M', 'F'), images=('211.gif', '211.png', '211 (1).png')
                )
            if 'Octillery':
                root.pokesets['Octillery'] = pokemon_ddl.PokemonSet(
                    name='Octillery', species='Octillery', abilities=('Suction Cups', 'Sniper'), pkTypes=('Water',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Surf', 'Octazooka', 'Water Spout', 'Water Spout'],
                                'Surf': ['Ice Beam', 'Energy Ball', 'Flash Cannon', 'Aurora Beam', 'Charge Beam', 'Fire Blast',
                                         'Flamethrower', 'Hyper Beam', 'Psychic', 'Signal Beam', 'Sludge Bomb'],
                                'Octazooka': ['Ice Beam', 'Energy Ball', 'Flash Cannon', 'Aurora Beam', 'Charge Beam', 'Fire Blast',
                                         'Flamethrower', 'Hyper Beam', 'Psychic', 'Signal Beam', 'Sludge Bomb'],
                                'Water Spout': ['Ice Beam', 'Energy Ball', 'Flash Cannon', 'Aurora Beam', 'Charge Beam', 'Fire Blast',
                                         'Flamethrower', 'Hyper Beam', 'Psychic', 'Signal Beam', 'Sludge Bomb']
                            }
                        ),
                    ), baseStats=(75, 105, 75, 105, 75, 45), genders=('M', 'F'), images=('224.gif', '224-m.png', '224-m (1).png')
                )
            if 'Suicune':
                root.pokesets['Suicune'] = pokemon_ddl.PokemonSet(
                    name='Suicune', species='Suicune', abilities=('Pressure',), pkTypes=('Water',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Rest'],
                            {
                                'Protect': ['Hail', 'Calm Mind', 'Mirror Coat'],
                                'Rest': ['Sleep Talk'],
                                'Sleep Talk': ['Calm Mind'],
                                'Calm Mind': ['Surf', 'Hydro Pump'],
                                'Surf': ['Air Slash', 'Ice Beam'],
                                'Hydro Pump': ['Air Slash', 'Ice Beam'],
                                'Hail': ['Blizzard'],
                                'Blizzard': ['Hydro Pump', 'Extrasensory'],
                                'Mirror Coat': ['Ominous Wind', 'Aurora Beam'],
                                'Ominous Wind': ['Sheer Cold', 'Signal Beam', 'Tailwind', 'Hydro Pump'],
                                'Aurora Beam': ['Hydro Pump']
                            }
                        ),
                    ), baseStats=(100, 75, 115, 90, 115, 85), genders=('',), images=('245.gif', '245.png', '245 (1).png')
                )
            if 'Wailord':
                root.pokesets['Wailord'] = pokemon_ddl.PokemonSet(
                    name='Wailord', species='Wailord', abilities=('Water Veil', 'Oblivious'), pkTypes=('Water',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Water Spout'],
                                'Water Spout': ['Self-Destruct', 'Bounce', 'Attract'],
                                'Self-Destruct': ['Ice Beam', 'Hidden Power [Grass]'],
                                'Bounce': ['Body Slam', 'Earthquake', 'Fissure', 'Iron Head', 'Self-Destruct', 'Giga Impact'],
                                'Attract': ['Icy Wind', 'Blizzard', 'Icy Wind', 'Giga Impact']
                            }
                        ),
                    ), baseStats=(170, 90, 45, 90, 45, 60), genders=('M', 'F'), images=('321.gif', '321.png', '321 (1).png')
                )
            if 'Milotic':
                root.pokesets['Milotic'] = pokemon_ddl.PokemonSet(
                    name='Milotic', species='Milotic', abilities=('Marvel Scale',), pkTypes=('Water',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Surf', 'Hidden Power [Grass]', 'Mirror Coat', 'Hydro Pump', 'Confuse Ray', 'Dragon Pulse'],
                                'Surf': ['Recover'],
                                'Recover': ['Ice Beam', 'Haze', 'Toxic'],
                                'Mirror Coat': ['Surf', 'Ice Beam'],
                                'Ice Beam': ['Recover'],
                                'Hydro Pump': ['Recover'],
                                'Confuse Ray': ['Toxic'],
                                'Toxic': ['Double Team', 'Attract'],
                                'Dragon Pulse': ['Surf', 'Ice Beam', 'Hydro Pump']
                            }
                        ),
                    ), baseStats=(95, 60, 79, 100, 125, 81), genders=('M', 'F'), images=('350.gif', '350-m.png', '350-m (1).png')
                )
            if 'Huntail':
                root.pokesets['Huntail'] = pokemon_ddl.PokemonSet(
                    name='Huntail', species='Huntail', abilities=('Swift Swim',), pkTypes=('Water',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Aqua Tail', 'Waterfall', 'Rain Dance'],
                                'Aqua Tail': ['Hydro Pump', 'Ice Beam', 'Double-Edge'],
                                'Hydro Pump': ['Hidden Power [Grass]'],
                                'Ice Beam': ['Hidden Power [Grass]'],
                                'Waterfall': ['Hydro Pump', 'Ice Beam', 'Double-Edge'],
                                'Double-Edge': ['Crunch', 'Sucker Punch', 'Ice Beam']
                            }
                        ),
                    ), baseStats=(55, 104, 105, 94, 75, 52), genders=('M', 'F'), images=('367.gif', '367.png', '367 (1).png')
                )
            if 'Gorebyss':
                root.pokesets['Gorebyss'] = pokemon_ddl.PokemonSet(
                    name='Gorebyss', species='Gorebyss', abilities=('Swift Swim',), pkTypes=('Water',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Hydro Pump', 'Surf', 'Water Pulse', 'Baton Pass', 'Baton Pass'],
                                'Hydro Pump': ['Psychic'],
                                'Psychic': ['Ice Beam', 'Hidden Power [Grass]', 'Hidden Power [Electric]', 'Hidden Power [Dragon]',
                                            'Shadow Ball', 'Signal Beam'],
                                'Surf': ['Psychic'],
                                'Water Pulse': ['Psychic'],
                                'Baton Pass': ['Agility', 'Substitute'],
                                'Agility': ['Substitute', 'Surf', 'Hydro Pump', 'Psychic', 'Water Pulse'],
                                'Substitute': ['Agility', 'Water Pulse', 'Hydro Pump', 'Psychic']
                            }
                        ),
                    ), baseStats=(55, 84, 105, 114, 75, 52), genders=('M', 'F'), images=('368.gif', '368.png', '368 (1).png')
                )
            if 'Luvdisc':
                root.pokesets['Luvdisc'] = pokemon_ddl.PokemonSet(
                    name='Luvdisc', species='Luvdisc', abilities=('Swift Swim',), pkTypes=('Water',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect', 'Endure'],
                            {
                                'Protect': ['Rain Dance', 'Whirlpool'],
                                'Rain Dance': ['Toxic'],
                                'Toxic': ['Sweet Kiss', 'Attract'],
                                'Endure': ['Flail'],
                                'Flail': ['Agility', 'Rain Dance', 'Safeguard', 'Waterfall', 'Surf'],
                                'Whirlpool': ['Toxic']
                            }
                        ),
                    ), baseStats=(43, 30, 55, 40, 65, 97), genders=('M', 'F'), images=('370.gif', '370.png', '370 (1).png')
                )
            if 'Kyogre':
                root.pokesets['Kyogre'] = pokemon_ddl.PokemonSet(
                    name='Kyogre', species='Kyogre', abilities=('Drizzle',), pkTypes=('Water',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Water Spout', 'Water Pulse', 'Water Spout'],
                            {
                                'Water Spout': ['Ancient Power', 'Aqua Ring', 'Aqua Tail', 'Avalanche', 'Blizzard', 'Block',
                                                'Body Slam', 'Brick Break', 'Brine', 'Calm Mind', 'Defense Curl', 'Dive',
                                                'Double-Edge', 'Double Team', 'Earthquake', 'Endure', 'Facade', 'Giga Impact',
                                                'Hail', 'Headbutt', 'Hydro Pump', 'Hyper Beam', 'Ice Beam', 'Icy Wind',
                                                'Iron Head', 'Mimic', 'Muddy Water', 'Mud-Slap', 'Protect', 'Psych Up',
                                                'Rest', 'Return', 'Roar', 'Rock Slide', 'Rock Smash', 'Rock Tomb', 'Safeguard',
                                                'Scary Face', 'Secret Power', 'Sheer Cold', 'Shock Wave', 'Signal Beam',
                                                'Strength', 'Substitute', 'Surf', 'Swagger', 'Swift', 'Thunder', 'Thunderbolt',
                                                'Thunder Wave', 'Toxic', 'Uproar', 'Waterfall', 'Water Pulse', 'Water Spout',
                                                'Whirlpool'],
                                'Water Pulse': ['Ancient Power', 'Aqua Ring', 'Aqua Tail', 'Avalanche', 'Blizzard', 'Block',
                                                'Body Slam', 'Brick Break', 'Brine', 'Calm Mind', 'Defense Curl', 'Dive',
                                                'Double-Edge', 'Double Team', 'Earthquake', 'Endure', 'Facade', 'Giga Impact',
                                                'Hail', 'Headbutt', 'Hydro Pump', 'Hyper Beam', 'Ice Beam', 'Icy Wind',
                                                'Iron Head', 'Mimic', 'Muddy Water', 'Mud-Slap', 'Protect', 'Psych Up',
                                                'Rest', 'Return', 'Roar', 'Rock Slide', 'Rock Smash', 'Rock Tomb', 'Safeguard',
                                                'Scary Face', 'Secret Power', 'Sheer Cold', 'Shock Wave', 'Signal Beam',
                                                'Strength', 'Substitute', 'Surf', 'Swagger', 'Swift', 'Thunder', 'Thunderbolt',
                                                'Thunder Wave', 'Toxic', 'Uproar', 'Waterfall', 'Water Pulse', 'Water Spout',
                                                'Whirlpool']
                            }
                        ),
                    ), baseStats=(100, 100, 90, 150, 140, 90), genders=('',), images=('382.gif', '382.png', '382 (1).png')
                )
            if 'Floatzel':
                root.pokesets['Floatzel'] = pokemon_ddl.PokemonSet(
                    name='Floatzel', species='Floatzel', abilities=('Swift Swim',), pkTypes=('Water',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Waterfall', 'Bulk Up', 'Double Team'],
                                'Bulk Up': ['Baton Pass'],
                                'Baton Pass': ['Substitute', 'Waterfall', 'Aqua Tail'],
                                'Double Team': ['Focus Punch'],
                                'Focus Punch': ['Waterfall', 'Aqua Tail'],
                                'Waterfall': ['Ice Punch', 'Blizzard', 'Brick Break', 'Bulk Up', 'Crunch', 'Secret Power', 'Rain Dance',
                                              'Quick Attack', 'Return', 'Focus Blast']
                            }
                        ),
                    ), baseStats=(85, 105, 55, 85, 50, 115), genders=('M', 'F'), images=('419.gif', '419.png', '419 (1).png')
                )
            if 'Lumineon':
                root.pokesets['Lumineon'] = pokemon_ddl.PokemonSet(
                    name='Lumineon', species='Lumineon', abilities=('Swift Swim', 'Storm Drain'), pkTypes=('Water',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Rain Dance', 'Safeguard', 'Swagger', 'Tailwind', 'Icy Wind'],
                                'Rain Dance': ['Surf'],
                                'Safeguard': ['Surf'],
                                'Surf': ['Silver Wind', 'Silver Wind', 'U-turn'],
                                'Swagger': ['Ominous Wind', 'Silver Wind', 'Surf'],
                                'Tailwind': ['Surf'],
                                'Icy Wind': ['Surf']
                            }
                        ),
                    ), baseStats=(69, 69, 76, 69, 86, 91), genders=('M', 'F'), images=('457.gif', '457-m.png', '457-m (1).png')
                )
            if 'Phione':
                root.pokesets['Phione'] = pokemon_ddl.PokemonSet(
                    name='Phione', species='Phione', abilities=('Hydration',), pkTypes=('Water',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Rest'],
                            {
                                'Rest': ['Rain Dance'],
                                'Rain Dance': ['Waterfall', 'Surf'],
                                'Waterfall': ['U-turn', 'Secret Power', 'Knock Off', 'Helping Hand'],
                                'Surf': ['Grass Knot', 'Ice Beam', 'Toxic', 'Knock Off', 'Icy Wind', 'Helping Hand', 'Ancient Power']
                            }
                        ),
                    ), baseStats=(80, 80, 80, 80, 80, 80), genders=('',), images=('489.gif', '489.png', '489 (1).png')
                )
            if 'Manaphy':
                root.pokesets['Manaphy'] = pokemon_ddl.PokemonSet(
                    name='Manaphy', species='Manaphy', abilities=('Hydration',), pkTypes=('Water',),
                    sets=(
                        pokemon_ddl.MoveSet(
                            ['Rest'],
                            {
                                'Rest': ['Rain Dance'],
                                'Rain Dance': ['Tail Glow', 'Toxic', 'Calm Mind', 'Bounce', 'Surf'],
                                'Tail Glow': ['Surf', 'Ice Beam', 'Grass Knot'],
                                'Toxic': ['Surf', 'Grass Knot', 'Ice Beam', 'Energy Ball'],
                                'Calm Mind': ['Surf', 'Grass Knot', 'Ice Beam', 'Energy Ball'],
                                'Bounce': ['Waterfall', 'U-turn'],
                                'Surf': ['Shadow Ball', 'Signal Beam', 'Energy Ball', 'Psychic']
                            }
                        ),
                    ), baseStats=(100, 100, 100, 100, 100, 100), genders=('',), images=('490.gif', '490.png', '490 (1).png')
                )
            if 'Arceus-Water':
                root.pokesets['Arceus-Water'] = pokemon_ddl.PokemonSet(
                    name='Arceus-Water', species='Arceus', abilities=('Multitype',), pkTypes=('Water',),
                    sets=(
                        # MoveSet 1: "The Chaotic Bulwark". Guaranteed Protect + Judgement, then maximum variance.
                        pokemon_ddl.MoveSet(
                            ['Protect'],
                            {
                                'Protect': ['Judgement'],

                                # Judgement is the central hub for a chaotic web of possibilities.
                                'Judgement': [
                                    'Calm Mind', 'Swords Dance', 'Recover', 'Cosmic Power', 'Will-O-Wisp',
                                    'Thunder Wave', 'Extreme Speed', 'Earth Power', 'Ice Beam', 'Thunderbolt',
                                    'Flamethrower', 'Shadow Claw', 'Gravity', 'Substitute'
                                ],

                                # Every node below is heavily interconnected to create unpredictable sets.
                                'Calm Mind': ['Ice Beam', 'Thunderbolt', 'Earthquake', 'Shadow Claw', 'Recover',
                                              'Swords Dance', 'Will-O-Wisp'],
                                'Swords Dance': ['Extreme Speed', 'Dragon Claw', 'Shadow Claw', 'Earthquake', 'Surf',
                                                 'Ice Beam', 'Calm Mind'],
                                'Recover': ['Calm Mind', 'Will-O-Wisp', 'Ice Beam', 'Flamethrower', 'Substitute',
                                            'Swords Dance', 'Judgement'],
                                'Cosmic Power': ['Recover', 'Will-O-Wisp', 'Toxic', 'Flamethrower', 'Judgement'],
                                'Will-O-Wisp': ['Recover', 'Calm Mind', 'Extreme Speed', 'Dragon Claw'],
                                'Extreme Speed': ['Swords Dance', 'Shadow Claw', 'Draco Meteor', 'Overheat',
                                                  'Judgement',
                                                  'Recover'],
                                'Earth Power': ['Ice Beam', 'Thunderbolt', 'Calm Mind', 'Swords Dance', 'Dragon Claw'],
                                'Ice Beam': ['Thunderbolt', 'Earth Power', 'Judgement', 'Calm Mind', 'Swords Dance'],
                                'Thunderbolt': ['Ice Beam', 'Surf', 'Judgement', 'Calm Mind', 'Swords Dance'],
                                'Dragon Claw': ['Earthquake', 'Shadow Claw', 'Swords Dance', 'Calm Mind', 'Ice Beam'],
                                'Substitute': ['Calm Mind', 'Swords Dance', 'Recover', 'Will-O-Wisp', 'Judgement'],
                                'Gravity': ['Thunder', 'Blizzard', 'Focus Blast', 'Earthquake', 'Judgement'],
                            }
                        ),

                        # MoveSet 2: "The Chaotic Gambler". No Protect, starts with Judgement into chaos.
                        pokemon_ddl.MoveSet(
                            ['Judgement'],
                            {
                                'Judgement': [
                                    'Extreme Speed', 'Draco Meteor', 'Outrage', 'Calm Mind', 'Swords Dance',
                                    'Gravity', 'Trick Room', 'Fire Blast', 'Thunder', 'Ice Beam', 'Earthquake',
                                    'Shadow Claw', 'Will-O-Wisp', 'Recover'
                                ],

                                'Draco Meteor': ['Extreme Speed', 'Overheat', 'Earthquake', 'Fire Blast', 'Steel Wing'],
                                'Outrage': ['Extreme Speed', 'Aqua Tail', 'Iron Head', 'Ice Beam', 'Giga Drain'],
                                'Calm Mind': ['Ice Beam', 'Thunder', 'Focus Blast', 'Shadow Claw', 'Recover',
                                              'Swords Dance'],
                                'Swords Dance': ['Extreme Speed', 'Shadow Claw', 'Dragon Claw', 'Giga Drain',
                                                 'Calm Mind'],
                                'Gravity': ['Thunder', 'Blizzard', 'Focus Blast', 'Draco Meteor', 'Judgement'],
                                'Trick Room': ['Judgement', 'Draco Meteor', 'Fire Blast', 'Thunder', 'Focus Blast'],
                                'Extreme Speed': ['Judgement', 'Swords Dance', 'Draco Meteor', 'Will-O-Wisp',
                                                  'Recover'],
                                'Fire Blast': ['Draco Meteor', 'Thunder', 'Ice Beam', 'Earthquake'],
                                'Earthquake': ['Stone Edge', 'Outrage', 'Dragon Claw', 'Flamethrower'],
                                'Recover': ['Judgement', 'Calm Mind', 'Swords Dance', 'Will-O-Wisp', 'Toxic']
                            }
                        ),

                        # MoveSet 3: "The Perish Trapper". A specific, high-risk alternate strategy.
                        pokemon_ddl.MoveSet(
                            ['Perish Song'],
                            {
                                'Mean Look': ['Protect', 'Recover', 'Judgement'],
                                'Perish Song': ['Mean Look']
                            }
                        )
                    ), baseStats=(120, 120, 120, 120, 120, 120), genders=('',), images=('493.gif', 'arceus-water.png', 'arceus-water (1).png'),
                    item_key='arcWater', stat_key='arcStat'
                )

    if 'Pokemon Probabilities':
        pokemon_weights = {
            # Dragon
            'Dragonite': 2.25, 'Kingdra': 2.35, 'Flygon': 2.35, 'Salamence': 2.15, 'Latias': 0.6, 'Latios': 0.6,
            'Rayquaza': 0.25,
            'Dialga': 0.25, 'Palkia': 0.25, 'Giratina': 0.25, 'Arceus-Dragon': 0.016,

            # Ice
            'Dewgong': 1.5, 'Cloyster': 2.0, 'Jynx': 1.2, 'Lapras': 2.0, 'Articuno': 2.0, 'Delibird': 0.1,
            'Glalie': 2.0,
            'Walrein': 2.0, 'Regice': 2.0, 'Abomasnow': 3.0, 'Weavile': 2.0, 'Glaceon': 2.0, 'Mamoswine': 2.0,
            'Froslass': 2.0,
            'Arceus-Ice': 0.015,

            # Fighting
            'Primeape': 1.0, 'Poliwrath': 2.0, 'Machamp': 2.0, 'Hitmonlee': 1.6, 'Hitmonchan': 1.6, 'Heracross': 2.0,
            'Hitmontop': 2.0, 'Blaziken': 2.0, 'Breloom': 2.0, 'Hariyama': 2.0, 'Medicham': 2.0, 'Infernape': 2.0,
            'Lucario': 2.0, 'Toxicroak': 2.0, 'Gallade': 2.0, 'Arceus-Fighting': 0.015,

            # Dark
            'Umbreon': 2.0, 'Houndoom': 2.0, 'Tyranitar': 2.2, 'Mightyena': 1.1, 'Shiftry': 2.0, 'Sableye': 1.0,
            'Sharpedo': 2.0, 'Cacturne': 1.2, 'Crawdaunt': 2.0, 'Absol': 2.0, 'Honchkrow': 2.0, 'Skuntank': 2.0,
            'Spiritomb': 2.0, 'Drapion': 2.0, 'Darkrai': 0.2, 'Arceus-Dark': 0.015,

            # Fire
            'Charizard': 2.0, 'Ninetales': 2.0, 'Arcanine': 2.0, 'Rapidash': 2.0, 'Flareon': 2.0, 'Moltres': 2.0,
            'Typhlosion': 2.0, 'Magcargo': 0.5, 'Entei': 1.5, 'Ho-oh': 0.2, 'Camerupt': 1.5, 'Torkoal': 0.5,
            'Magmortar': 2.0,
            'Heatran': 1.6, 'Arceus-Fire': 0.015,

            # Ghost
            'Gengar': 2.05, 'Shedinja': 1.85, 'Banette': 1.1, 'Drifblim': 1.55, 'Mismagius': 1.05, 'Dusknoir': 2.05,
            'Rotom': 0.25,
            'Rotom-Fan': 0.6, 'Rotom-Frost': 0.6, 'Rotom-Heat': 0.6, 'Rotom-Mow': 0.6, 'Rotom-Wash': 0.6,
            'Arceus-Ghost': 0.0155,

            # Steel
            'Forretress': 2.0, 'Steelix': 2.0, 'Scizor': 2.0, 'Skarmory': 2.0, 'Mawile': 1.0, 'Aggron': 2.0,
            'Metagross': 2.0,
            'Registeel': 1.0, 'Jirachi': 0.5, 'Empoleon': 2.0, 'Bastiodon': 1.0,
            'Wormadam-Trash': 0.2,
            'Bronzong': 2.0, 'Magnezone': 2.0, 'Probopass': 1.2, 'Arceus-Steel': 0.015,

            # Electric
            'Pikachu': 1.0, 'Raichu': 2.0, 'Electrode': 2.0, 'Jolteon': 2.0, 'Zapdos': 2.0, 'Lanturn': 1.5, 'Ampharos': 2.0,
            'Raikou': 1.5,
            'Manectric': 2.0,
            'Plusle': 0.25, 'Minun': 0.25,
            'Luxray': 2.0, 'Pachirisu': 1.0, 'Electivire': 2.0, 'Arceus-Electric': 0.015,

            # Rock
            'Golem': 2.0, 'Omastar': 2.0, 'Kabutops': 2.0, 'Aerodactyl': 2.0, 'Sudowoodo': 1.0, 'Shuckle': 1.0,
            'Corsola': 0.1,
            'Lunatone': 0.3, 'Solrock': 0.3,  # Paired set -> 1.0 each
            'Cradily': 2.0, 'Armaldo': 2.0, 'Relicanth': 2.0, 'Regirock': 2.0, 'Rampardos': 2.0, 'Rhyperior': 2.0,
            'Arceus-Rock': 0.015,

            # Poison
            'Venusaur': 2.0, 'Beedrill': 1.0, 'Arbok': 1.1, 'Nidoqueen': 2.0, 'Nidoking': 2.0, 'Vileplume': 2.0,
            'Venomoth': 1.0, 'Victreebel': 2.0, 'Tentacruel': 2.0, 'Muk': 2.0, 'Weezing': 2.0, 'Ariados': 0.6,
            'Crobat': 2.0,
            'Dustox': 0.5, 'Swalot': 1.0, 'Seviper': 1.5, 'Roserade': 2.0, 'Arceus-Poison': 0.015,

            # Ground
            'Sandslash': 2.0, 'Dugtrio': 1.5, 'Marowak': 2.0, 'Quagsire': 2.0, 'Donphan': 2.0, 'Swampert': 2.0,
            'Whiscash': 1.5,
            'Claydol': 2.0, 'Groudon': 0.2, 'Torterra': 2.0,
            'Wormadam-Sandy': 0.2,
            'Gastrodon': 1.0, 'Gastrodon-East': 1.0,  # Set value 2 -> 1 each
            'Garchomp': 2.25, 'Hippowdon': 2.2, 'Gliscor': 2.0, 'Arceus-Ground': 0.015,

            # Bug
            'Butterfree': 1.0, 'Parasect': 0.5, 'Pinsir': 2.0, 'Ledian': 0.1, 'Beautifly': 1.0, 'Masquerain': 1.0,
            'Ninjask': 2.0, 'Volbeat': 0.5, 'Illumise': 0.5, 'Kricketune': 0.5,
            'Wormadam': 0.2,
            'Mothim': 0.4, 'Vespiquen': 2.0, 'Yanmega': 2.0, 'Arceus-Bug': 0.02,

            # Grass
            'Exeggutor': 2.0, 'Meganium': 2.0, 'Bellossom': 0.8, 'Jumpluff': 1.0, 'Sunflora': 0.1, 'Celebi': 0.5,
            'Sceptile': 2.0, 'Ludicolo': 2.0, 'Tropius': 0.7, 'Cherrim': 2.0, 'Carnivine': 0.8, 'Tangrowth': 2.0,
            'Leafeon': 2.0, 'Shaymin': 1.5, 'Arceus-Grass': 0.015,

            # Psychic
            'Alakazam': 2.0, 'Slowbro': 2.0, 'Hypno': 1.2, 'Starmie': 2.0, 'Mr. Mime': 2.0, 'Mewtwo': 0.2, 'Mew': 0.5,
            'Xatu': 1.0, 'Espeon': 2.0, 'Slowking': 2.0, 'Unown': 0.1, 'Wobbuffet': 1.5, 'Girafarig': 1.0, 'Lugia': 0.2,
            'Gardevoir': 2.0, 'Grumpig': 1.0, 'Chimecho': 0.5,
            'Deoxys': 0.1, 'Deoxys-Attack': 0.2, 'Deoxys-Defense': 0.2, 'Deoxys-Speed': 0.2,
            'Uxie': 0.7, 'Mesprit': 0.7, 'Azelf': 0.7,
            'Cresselia': 2.0, 'Arceus-Psychic': 0.015,

            # Flying
            'Pidgeot': 1.3, 'Fearow': 1.3, 'Farfetch\'d': 0.5, 'Dodrio': 2.0, 'Gyarados': 2.0, 'Noctowl': 1.0,
            'Mantine': 1.5,
            'Swellow': 2.0, 'Pelipper': 1.0, 'Altaria': 2.22, 'Staraptor': 2.0, 'Chatot': 0.5, 'Togekiss': 2.0,
            'Arceus-Flying': 0.015,

            # Normal
            'Raticate': 0.8, 'Clefable': 2.1, 'Wigglytuff': 1.0, 'Persian': 2.0, 'Kangaskhan': 2.1, 'Ditto': 1.2,
            'Tauros': 2.1,
            'Snorlax': 2.1, 'Furret': 1.0, 'Dunsparce': 1.1, 'Granbull': 1.2, 'Ursaring': 2.1, 'Porygon2': 2.0,
            'Stantler': 1.0,
            'Smeargle': 2.0, 'Miltank': 2.0, 'Blissey': 2.1, 'Linoone': 1.0, 'Slaking': 1.5, 'Exploud': 2.0,
            'Delcatty': 0.5,
            'Spinda': 0.6, 'Zangoose': 2.1, 'Castform': 1.2,
            'Kecleon': 1.1, 'Bibarel': 1.1, 'Ambipom': 2.0, 'Lopunny': 2.1,
            'Purugly': 1.0,
            'Lickilicky': 2.0, 'Porygon-Z': 2.1, 'Regigigas': 2.0, 'Arceus': 0.016,

            # Water
            'Blastoise': 2.0, 'Golduck': 1.0, 'Kingler': 2.0, 'Seaking': 1.0, 'Vaporeon': 2.0, 'Feraligatr': 2.0,
            'Azumarill': 2.0, 'Politoed': 1.2, 'Qwilfish': 1.1, 'Octillery': 1.3, 'Suicune': 1.5, 'Wailord': 2.0,
            'Milotic': 2.0,
            'Huntail': 0.8, 'Gorebyss': 0.8,
            'Luvdisc': 0.1, 'Kyogre': 0.25, 'Floatzel': 2.0, 'Lumineon': 1.0, 'Phione': 1.0, 'Manaphy': 0.5,
            'Arceus-Water': 0.015,
        }
        pokemon_to_types_map = {
            'Pikachu': ['Electric'], 'Castform': ['Normal'],
            'Quagsire': ['Water', 'Ground'], 'Tangrowth': ['Grass'], 'Wailord': ['Water'],
            'Sharpedo': ['Water', 'Dark'], 'Drapion': ['Dark', 'Poison'], 'Rampardos': ['Rock'],
            'Venusaur': ['Grass', 'Poison'], 'Charizard': ['Fire', 'Flying'], 'Blastoise': ['Water'],
            'Butterfree': ['Bug', 'Flying'], 'Beedrill': ['Bug', 'Poison'], 'Pidgeot': ['Normal', 'Flying'],
            'Raticate': ['Normal'], 'Fearow': ['Normal', 'Flying'], 'Arbok': ['Poison'], 'Raichu': ['Electric'],
            'Sandslash': ['Ground'], 'Nidoqueen': ['Poison', 'Ground'], 'Nidoking': ['Poison', 'Ground'],
            'Clefable': ['Normal'], 'Ninetales': ['Fire'], 'Wigglytuff': ['Normal'], 'Vileplume': ['Grass', 'Poison'],
            'Parasect': ['Bug', 'Grass'], 'Venomoth': ['Bug', 'Poison'], 'Dugtrio': ['Ground'], 'Persian': ['Normal'],
            'Golduck': ['Water'], 'Primeape': ['Fighting'], 'Arcanine': ['Fire'], 'Poliwrath': ['Water', 'Fighting'],
            'Alakazam': ['Psychic'], 'Machamp': ['Fighting'], 'Victreebel': ['Grass', 'Poison'],
            'Tentacruel': ['Water', 'Poison'], 'Golem': ['Rock', 'Ground'], 'Rapidash': ['Fire'],
            'Slowbro': ['Water', 'Psychic'], 'Farfetch\'d': ['Normal', 'Flying'], 'Dodrio': ['Normal', 'Flying'],
            'Dewgong': ['Water', 'Ice'], 'Muk': ['Poison'], 'Cloyster': ['Water', 'Ice'], 'Gengar': ['Ghost', 'Poison'],
            'Hypno': ['Psychic'], 'Kingler': ['Water'], 'Electrode': ['Electric'], 'Exeggutor': ['Grass', 'Psychic'],
            'Marowak': ['Ground'], 'Hitmonlee': ['Fighting'], 'Hitmonchan': ['Fighting'], 'Lickilicky': ['Normal'],
            'Weezing': ['Poison'], 'Rhyperior': ['Rock', 'Ground'], 'Kangaskhan': ['Normal'], 'Seaking': ['Water'],
            'Starmie': ['Water', 'Psychic'], 'Mr. Mime': ['Psychic'], 'Scizor': ['Bug', 'Steel'],
            'Jynx': ['Ice', 'Psychic'],
            'Pinsir': ['Bug'], 'Tauros': ['Normal'], 'Gyarados': ['Water', 'Flying'], 'Lapras': ['Water', 'Ice'],
            'Ditto': ['Normal'], 'Vaporeon': ['Water'], 'Jolteon': ['Electric'], 'Flareon': ['Fire'],
            'Porygon2': ['Normal'],
            'Omastar': ['Rock', 'Water'], 'Kabutops': ['Rock', 'Water'], 'Aerodactyl': ['Rock', 'Flying'],
            'Snorlax': ['Normal'], 'Articuno': ['Ice', 'Flying'], 'Zapdos': ['Electric', 'Flying'],
            'Moltres': ['Fire', 'Flying'], 'Dragonite': ['Dragon', 'Flying'], 'Mewtwo': ['Psychic'], 'Mew': ['Psychic'],
            'Meganium': ['Grass'], 'Typhlosion': ['Fire'], 'Feraligatr': ['Water'], 'Furret': ['Normal'],
            'Noctowl': ['Normal', 'Flying'], 'Ledian': ['Bug', 'Flying'], 'Ariados': ['Bug', 'Poison'],
            'Crobat': ['Poison', 'Flying'], 'Lanturn': ['Water', 'Electric'], 'Xatu': ['Psychic', 'Flying'],
            'Ampharos': ['Electric'], 'Bellossom': ['Grass'], 'Azumarill': ['Water'], 'Sudowoodo': ['Rock'],
            'Politoed': ['Water'], 'Jumpluff': ['Grass', 'Flying'], 'Sunflora': ['Grass'], 'Espeon': ['Psychic'],
            'Umbreon': ['Dark'], 'Slowking': ['Water', 'Psychic'], 'Unown': ['Psychic'], 'Wobbuffet': ['Psychic'],
            'Girafarig': ['Normal', 'Psychic'], 'Forretress': ['Bug', 'Steel'], 'Dunsparce': ['Normal'],
            'Gligar': ['Ground', 'Flying'], 'Steelix': ['Steel', 'Ground'], 'Granbull': ['Normal'],
            'Qwilfish': ['Water', 'Poison'], 'Shuckle': ['Bug', 'Rock'], 'Heracross': ['Bug', 'Fighting'],
            'Sneasel': ['Dark', 'Ice'], 'Ursaring': ['Normal'], 'Magcargo': ['Fire', 'Rock'],
            'Swinub': ['Ice', 'Ground'],
            'Corsola': ['Water', 'Rock'], 'Octillery': ['Water'], 'Delibird': ['Ice', 'Flying'],
            'Mantine': ['Water', 'Flying'],
            'Skarmory': ['Steel', 'Flying'], 'Houndoom': ['Dark', 'Fire'], 'Kingdra': ['Water', 'Dragon'],
            'Donphan': ['Ground'], 'Porygon-Z': ['Normal'], 'Stantler': ['Normal'], 'Smeargle': ['Normal'],
            'Hitmontop': ['Fighting'], 'Miltank': ['Normal'], 'Blissey': ['Normal'], 'Raikou': ['Electric'],
            'Entei': ['Fire'],
            'Suicune': ['Water'], 'Tyranitar': ['Rock', 'Dark'], 'Lugia': ['Psychic', 'Flying'],
            'Ho-oh': ['Fire', 'Flying'],
            'Celebi': ['Psychic', 'Grass'], 'Sceptile': ['Grass'], 'Blaziken': ['Fire', 'Fighting'],
            'Swampert': ['Water', 'Ground'], 'Mightyena': ['Dark'], 'Linoone': ['Normal'],
            'Beautifly': ['Bug', 'Flying'],
            'Dustox': ['Bug', 'Poison'], 'Ludicolo': ['Water', 'Grass'], 'Shiftry': ['Grass', 'Dark'],
            'Swellow': ['Normal', 'Flying'], 'Pelipper': ['Water', 'Flying'], 'Gardevoir': ['Psychic'],
            'Masquerain': ['Bug', 'Flying'], 'Breloom': ['Grass', 'Fighting'], 'Slaking': ['Normal'],
            'Ninjask': ['Bug', 'Flying'], 'Shedinja': ['Bug', 'Ghost'], 'Exploud': ['Normal'], 'Hariyama': ['Fighting'],
            'Delcatty': ['Normal'], 'Sableye': ['Dark', 'Ghost'], 'Mawile': ['Steel'], 'Aggron': ['Steel', 'Rock'],
            'Medicham': ['Fighting', 'Psychic'], 'Manectric': ['Electric'], 'Plusle': ['Electric'],
            'Minun': ['Electric'],
            'Volbeat': ['Bug'], 'Illumise': ['Bug'], 'Roserade': ['Grass', 'Poison'], 'Swalot': ['Poison'],
            'Camerupt': ['Fire', 'Ground'], 'Torkoal': ['Fire'], 'Grumpig': ['Psychic'], 'Spinda': ['Normal'],
            'Flygon': ['Ground', 'Dragon'], 'Cacturne': ['Grass', 'Dark'], 'Altaria': ['Dragon', 'Flying'],
            'Zangoose': ['Normal'], 'Seviper': ['Poison'], 'Lunatone': ['Rock', 'Psychic'],
            'Solrock': ['Rock', 'Psychic'],
            'Whiscash': ['Water', 'Ground'], 'Crawdaunt': ['Water', 'Dark'], 'Claydol': ['Ground', 'Psychic'],
            'Cradily': ['Rock', 'Grass'], 'Armaldo': ['Rock', 'Bug'], 'Milotic': ['Water'], 'Kecleon': ['Normal'],
            'Banette': ['Ghost'], 'Tropius': ['Grass', 'Flying'], 'Chimecho': ['Psychic'], 'Absol': ['Dark'],
            'Glalie': ['Ice'],
            'Walrein': ['Ice', 'Water'], 'Huntail': ['Water'], 'Gorebyss': ['Water'], 'Relicanth': ['Water', 'Rock'],
            'Luvdisc': ['Water'], 'Salamence': ['Dragon', 'Flying'], 'Metagross': ['Steel', 'Psychic'],
            'Regirock': ['Rock'],
            'Regice': ['Ice'], 'Registeel': ['Steel'], 'Latias': ['Dragon', 'Psychic'], 'Latios': ['Dragon', 'Psychic'],
            'Kyogre': ['Water'], 'Groudon': ['Ground'], 'Rayquaza': ['Dragon', 'Flying'],
            'Jirachi': ['Steel', 'Psychic'],
            'Deoxys': ['Psychic'], 'Deoxys-Attack': ['Psychic'], 'Deoxys-Defense': ['Psychic'],
            'Deoxys-Speed': ['Psychic'],
            'Torterra': ['Grass', 'Ground'], 'Infernape': ['Fire', 'Fighting'], 'Empoleon': ['Water', 'Steel'],
            'Staraptor': ['Normal', 'Flying'], 'Bibarel': ['Normal', 'Water'], 'Kricketune': ['Bug'],
            'Luxray': ['Electric'],
            'Bastiodon': ['Rock', 'Steel'], 'Wormadam': ['Bug', 'Grass'], 'Wormadam-Sandy': ['Bug', 'Ground'],
            'Wormadam-Trash': ['Bug', 'Steel'], 'Mothim': ['Bug', 'Flying'], 'Vespiquen': ['Bug', 'Flying'],
            'Pachirisu': ['Electric'], 'Floatzel': ['Water'], 'Cherrim': ['Grass'], 'Gastrodon': ['Water', 'Ground'],
            'Gastrodon-East': ['Water', 'Ground'], 'Ambipom': ['Normal'], 'Drifblim': ['Ghost', 'Flying'],
            'Lopunny': ['Normal'], 'Mismagius': ['Ghost'], 'Honchkrow': ['Dark', 'Flying'], 'Purugly': ['Normal'],
            'Skuntank': ['Poison', 'Dark'], 'Bronzong': ['Steel', 'Psychic'], 'Chatot': ['Normal', 'Flying'],
            'Spiritomb': ['Ghost', 'Dark'], 'Garchomp': ['Dragon', 'Ground'], 'Lucario': ['Fighting', 'Steel'],
            'Hippowdon': ['Ground'], 'Toxicroak': ['Poison', 'Fighting'], 'Carnivine': ['Grass'], 'Lumineon': ['Water'],
            'Abomasnow': ['Grass', 'Ice'], 'Weavile': ['Dark', 'Ice'], 'Magnezone': ['Electric', 'Steel'],
            'Electivire': ['Electric'], 'Magmortar': ['Fire'], 'Togekiss': ['Normal', 'Flying'],
            'Yanmega': ['Bug', 'Flying'],
            'Leafeon': ['Grass'], 'Glaceon': ['Ice'], 'Gliscor': ['Ground', 'Flying'], 'Mamoswine': ['Ice', 'Ground'],
            'Gallade': ['Psychic', 'Fighting'], 'Probopass': ['Rock', 'Steel'], 'Dusknoir': ['Ghost'],
            'Froslass': ['Ice', 'Ghost'], 'Rotom': ['Electric', 'Ghost'], 'Rotom-Heat': ['Electric', 'Fire'],
            'Rotom-Wash': ['Electric', 'Water'], 'Rotom-Frost': ['Electric', 'Ice'], 'Rotom-Mow': ['Electric', 'Grass'],
            'Rotom-Fan': ['Electric', 'Flying'], 'Uxie': ['Psychic'], 'Mesprit': ['Psychic'], 'Azelf': ['Psychic'],
            'Dialga': ['Steel', 'Dragon'], 'Palkia': ['Water', 'Dragon'], 'Heatran': ['Fire', 'Steel'],
            'Regigigas': ['Normal'],
            'Giratina': ['Ghost', 'Dragon'], 'Cresselia': ['Psychic'], 'Phione': ['Water'], 'Manaphy': ['Water'],
            'Darkrai': ['Dark'], 'Shaymin': ['Grass'], 'Arceus': ['Normal'], 'Arceus-Fighting': ['Fighting'],
            'Arceus-Flying': ['Flying'], 'Arceus-Poison': ['Poison'], 'Arceus-Ground': ['Ground'],
            'Arceus-Rock': ['Rock'],
            'Arceus-Bug': ['Bug'], 'Arceus-Ghost': ['Ghost'], 'Arceus-Steel': ['Steel'], 'Arceus-Fire': ['Fire'],
            'Arceus-Water': ['Water'], 'Arceus-Grass': ['Grass'], 'Arceus-Electric': ['Electric'],
            'Arceus-Psychic': ['Psychic'], 'Arceus-Ice': ['Ice'], 'Arceus-Dragon': ['Dragon'], 'Arceus-Dark': ['Dark']
        }

        type_names = ['Dragon', 'Ice', 'Fighting', 'Dark', 'Fire', 'Ghost', 'Steel', 'Electric', 'Rock', 'Poison',
                      'Ground',
                      'Bug', 'Grass', 'Psychic', 'Flying', 'Normal', 'Water']
        smoothing = 1.5

        raw_type_totals = {name: 0.0 for name in type_names}
        for pokemon, weight in pokemon_weights.items():
            num_types = len(pokemon_to_types_map[pokemon])
            for p_type in pokemon_to_types_map[pokemon]:
                raw_type_totals[p_type] += 1 / num_types




        smoothed_type_totals = {k: (float(np.median(list(raw_type_totals.values()))) - v) * smoothing + v for k, v in
                                raw_type_totals.items()}


        # total_smoothed_weight = sum(smoothed_type_totals.values())
        # percentage_type_totals = {k: v / total_smoothed_weight for k, v in smoothed_type_totals.items()}
        # pprint.pprint(sorted(percentage_type_totals.items(), key=lambda item: item[1]))

        total_scaled_weights = 0
        pokemon_scaled_weights = {}
        for name, weight in pokemon_weights.items():
            scaler = 0
            for x in pokemon_to_types_map[name]:
                scaler += smoothed_type_totals[x]
            scaler /= len(pokemon_to_types_map[name])
            pokemon_scaled_weights[name] = scaler * weight
            total_scaled_weights += scaler * weight
        pokemon_scaled_weights = {k: v / total_scaled_weights for k, v in pokemon_scaled_weights.items()}
        # pprint.pprint(pokemon_scaled_weights)

        poke_key = list(pokemon_scaled_weights.keys())
        poke_value = list(pokemon_scaled_weights.values())
        root.pokeprobability['pokemon'] = (poke_key, poke_value)
        root.pokeprobability['pokemon_to_types_map'] = pokemon_to_types_map
        root.pokeprobability['type_names'] = type_names
        root.pokeprobability['abilities'] = ['Snow Warning', 'Pressure', 'Super Luck', 'Rock Head', 'Sturdy',
                                             'Synchronize', 'Inner Focus', 'Natural Cure', 'Technician', 'Static',
                                             'Intimidate', 'Shed Skin', 'Flash Fire', 'Multitype', 'Swarm', 'Insomnia',
                                             'Battle Armor', 'Levitate', 'Thick Fat', 'Huge Power', 'Frisk',
                                             'Chlorophyll', 'Simple', 'Unaware', 'Torrent', 'Blaze', 'Serene Grace',
                                             'Effect Spore', 'Poison Heal', 'Heatproof', 'Compound Eyes', 'Sand Veil',
                                             'Magma Armor', 'Solid Rock', 'Keen Eye', 'Tangled Feet', 'Flower Gift',
                                             'Cute Charm', 'Magic Guard', 'Shell Armor', 'Skill Link', 'Hustle',
                                             'Suction Cups', 'Hyper Cutter', 'Bad Dreams', 'Normalize', 'Vital Spirit',
                                             'Hydration', 'Limber', 'Run Away', 'Early Bird', 'Sniper', 'Aftermath',
                                             'Unburden', 'Arena Trap', 'Shield Dust', 'Motor Drive', 'Soundproof',
                                             'Swift Swim', 'Snow Cloak', 'Steadfast', 'Trace', 'Sticky Hold',
                                             'Storm Drain', 'Ice Body', 'Damp', 'Cloud Nine', 'Quick Feet', 'Drought',
                                             'Own Tempo', 'Guts', 'Sand Stream', 'Iron Fist', 'Reckless', 'Forewarn',
                                             'Oblivious', 'Tinted Lens', 'Volt Absorb', 'Leaf Guard', 'Scrappy',
                                             'Color Change', 'Drizzle', 'Water Absorb', 'Gluttony', 'Klutz', 'Rain Dish',
                                             'Rivalry', 'No Guard', 'Flame Body', 'Magnet Pull', 'Lightning Rod',
                                             'Pure Power', 'Overgrow', 'Clear Body', 'Marvel Scale', 'Minus', 'Filter',
                                             'Poison Point', 'Speed Boost', 'Pick Up', 'Dry Skin', 'Mold Breaker',
                                             'Plus', 'Adaptability', 'Download', 'Anger Point', 'Air Lock', 'Slow Start',
                                             'Stall', 'Water Veil', 'Rough Skin', 'Wonder Guard', 'Truant', 'Immunity',
                                             'Solar Power', 'Liquid Ooze', 'White Smoke', 'Anticipation', 'Competitive',
                                             'Shadow Tag', 'Forecast']

    if 'Physical Moves':
        # Normal-type moves
        root.moves['Barrage'] = pokemon_ddl.Move('Barrage', 15, 0.85, 'Phys', 'Normal')
        root.moves['Bide'] = pokemon_ddl.Move('Bide', 0, 1.0, 'Phys', 'Normal')
        root.moves['Bind'] = pokemon_ddl.Move('Bind', 15, 0.75, 'Phys', 'Normal')
        root.moves['Body Slam'] = pokemon_ddl.Move('Body Slam', 85, 1.0, 'Phys', 'Normal')
        root.moves['Comet Punch'] = pokemon_ddl.Move('Comet Punch', 18, .85, 'Phys', 'Normal')
        root.moves['Constrict'] = pokemon_ddl.Move('Constrict', 10, 1.0, 'Phys', 'Normal')
        root.moves['Covet'] = pokemon_ddl.Move('Covet', 40, 1.0, 'Phys', 'Normal')
        root.moves['Crush Claw'] = pokemon_ddl.Move('Crush Claw', 75, .95, 'Phys', 'Normal')
        root.moves['Crush Grip'] = pokemon_ddl.Move('Crush Grip', 0, 1.0, 'Phys', 'Normal')
        root.moves['Cut'] = pokemon_ddl.Move('Cut', 50, 0.95, 'Phys', 'Normal')
        root.moves['Dizzy Punch'] = pokemon_ddl.Move('Dizzy Punch', 70, 1.0, 'Phys', 'Normal')
        root.moves['Double-Edge'] = pokemon_ddl.Move('Double-Edge', 120, 1.0, 'Phys', 'Normal')
        root.moves['Double Hit'] = pokemon_ddl.Move('Double Hit', 35, 0.9, 'Phys', 'Normal')
        root.moves['Double Slap'] = pokemon_ddl.Move('Double Slap', 15, 0.85, 'Phys', 'Normal')
        root.moves['Egg Bomb'] = pokemon_ddl.Move('Egg Bomb', 100, 0.75, 'Phys', 'Normal')
        root.moves['Endeavor'] = pokemon_ddl.Move('Endeavor', 0, 1.0, 'Phys', 'Normal')
        root.moves['Explosion'] = pokemon_ddl.Move('Explosion', 250, 1.0, 'Phys', 'Normal')
        root.moves['Extreme Speed'] = pokemon_ddl.Move('Extreme Speed', 80, 1.0, 'Phys', 'Normal')
        root.moves['Facade'] = pokemon_ddl.Move('Facade', 70, 1.0, 'Phys', 'Normal')
        root.moves['Fake Out'] = pokemon_ddl.Move('Fake Out', 40, 1.0, 'Phys', 'Normal')
        root.moves['False Swipe'] = pokemon_ddl.Move('False Swipe', 40, 1.0, 'Phys', 'Normal')
        root.moves['Flail'] = pokemon_ddl.Move('Flail', 0, 1.0, 'Phys', 'Normal')
        root.moves['Frustration'] = pokemon_ddl.Move('Frustration', 0, 1.0, 'Phys', 'Normal')
        root.moves['Fury Attack'] = pokemon_ddl.Move('Fury Attack', 15, 0.85, 'Phys', 'Normal')
        root.moves['Fury Swipes'] = pokemon_ddl.Move('Fury Swipes', 18, 0.8, 'Phys', 'Normal')
        root.moves['Giga Impact'] = pokemon_ddl.Move('Giga Impact', 150, 0.9, 'Phys', 'Normal')
        root.moves['Guillotine'] = pokemon_ddl.Move('Guillotine', 0, 0.3, 'Phys', 'Normal')
        root.moves['Headbutt'] = pokemon_ddl.Move('Headbutt', 70, 1.0, 'Phys', 'Normal')
        root.moves['Horn Attack'] = pokemon_ddl.Move('Horn Attack', 65, 1.0, 'Phys', 'Normal')
        root.moves['Horn Drill'] = pokemon_ddl.Move('Horn Drill', 0, 0.3, 'Phys', 'Normal')
        root.moves['Hyper Fang'] = pokemon_ddl.Move('Hyper Fang', 80, 0.9, 'Phys', 'Normal')
        root.moves['Last Resort'] = pokemon_ddl.Move('Last Resort', 130, 1.0, 'Phys', 'Normal')
        root.moves['Mega Kick'] = pokemon_ddl.Move('Mega Kick', 120, 0.75, 'Phys', 'Normal')
        root.moves['Mega Punch'] = pokemon_ddl.Move('Mega Punch', 80, 0.85, 'Phys', 'Normal')
        root.moves['Natural Gift'] = pokemon_ddl.Move('Natural Gift', 0, 1.0, 'Phys', 'Normal')
        root.moves['Pay Day'] = pokemon_ddl.Move('Pay Day', 40, 1.0, 'Phys', 'Normal')
        root.moves['Pound'] = pokemon_ddl.Move('Pound', 40, 1.0, 'Phys', 'Normal')
        root.moves['Present'] = pokemon_ddl.Move('Present', 0, 0.9, 'Phys', 'Normal')
        root.moves['Quick Attack'] = pokemon_ddl.Move('Quick Attack', 40, 1.0, 'Phys', 'Normal')
        root.moves['Rage'] = pokemon_ddl.Move('Rage', 20, 1.0, 'Phys', 'Normal')
        root.moves['Rapid Spin'] = pokemon_ddl.Move('Rapid Spin', 20, 1.0, 'Phys', 'Normal')
        root.moves['Return'] = pokemon_ddl.Move('Return', 0, 1.0, 'Phys', 'Normal')
        root.moves['Rock Climb'] = pokemon_ddl.Move('Rock Climb', 90, 0.85, 'Phys', 'Normal')
        root.moves['Scratch'] = pokemon_ddl.Move('Scratch', 40, 1.0, 'Phys', 'Normal')
        root.moves['Secret Power'] = pokemon_ddl.Move('Secret Power', 70, 1.0, 'Phys', 'Normal')
        root.moves['Self-Destruct'] = pokemon_ddl.Move('Self-Destruct', 200, 1.0, 'Phys', 'Normal')
        root.moves['Skull Bash'] = pokemon_ddl.Move('Skull Bash', 100, 1.0, 'Phys', 'Normal')
        root.moves['Slam'] = pokemon_ddl.Move('Slam', 80, 0.75, 'Phys', 'Normal')
        root.moves['Slash'] = pokemon_ddl.Move('Slash', 70, 1.0, 'Phys', 'Normal')
        root.moves['Smelling Salts'] = pokemon_ddl.Move('Smelling Salts', 60, 1, 'Phys', 'Normal')
        root.moves['Spike Cannon'] = pokemon_ddl.Move('Spike Cannon', 20, 1.0, 'Phys', 'Normal')
        root.moves['Stomp'] = pokemon_ddl.Move('Stomp', 65, 1.0, 'Phys', 'Normal')
        root.moves['Strength'] = pokemon_ddl.Move('Strength', 80, 1.0, 'Phys', 'Normal')
        root.moves['Struggle'] = pokemon_ddl.Move('Struggle', 50, 1.0, 'Phys', 'Normal')
        root.moves['Super Fang'] = pokemon_ddl.Move('Super Fang', 0, 0.9, 'Phys', 'Normal')
        root.moves['Tackle'] = pokemon_ddl.Move('Tackle', 35, 0.95, 'Phys', 'Normal')
        root.moves['Take Down'] = pokemon_ddl.Move('Take Down', 90, 0.85, 'Phys', 'Normal')
        root.moves['Thrash'] = pokemon_ddl.Move('Thrash', 90, 1.0, 'Phys', 'Normal')
        root.moves['Vicegrip'] = pokemon_ddl.Move('Vicegrip', 55, 1.0, 'Phys', 'Normal')
        root.moves['Wrap'] = pokemon_ddl.Move('Wrap', 15, 0.85, 'Phys', 'Normal')

        # Fighting-type moves
        root.moves['Arm Thrust'] = pokemon_ddl.Move('Arm Thrust', 15, 1.0, 'Phys', 'Fighting')
        root.moves['Brick Break'] = pokemon_ddl.Move('Brick Break', 75, 1.0, 'Phys', 'Fighting')
        root.moves['Close Combat'] = pokemon_ddl.Move('Close Combat', 120, 1.0, 'Phys', 'Fighting')
        root.moves['Counter'] = pokemon_ddl.Move('Counter', 0, 1.0, 'Phys', 'Fighting')
        root.moves['Cross Chop'] = pokemon_ddl.Move('Cross Chop', 100, 0.8, 'Phys', 'Fighting')
        root.moves['Double Kick'] = pokemon_ddl.Move('Double Kick', 30, 1.0, 'Phys', 'Fighting')
        root.moves['Drain Punch'] = pokemon_ddl.Move('Drain Punch', 60, 1.0, 'Phys', 'Fighting')
        root.moves['Dynamic Punch'] = pokemon_ddl.Move('Dynamic Punch', 100, 0.5, 'Phys', 'Fighting')
        root.moves['Focus Punch'] = pokemon_ddl.Move('Focus Punch', 150, 1.0, 'Phys', 'Fighting')
        root.moves['Force Palm'] = pokemon_ddl.Move('Force Palm', 60, 1.0, 'Phys', 'Fighting')
        root.moves['Hammer Arm'] = pokemon_ddl.Move('Hammer Arm', 100, 0.9, 'Phys', 'Fighting')
        root.moves['High Jump Kick'] = pokemon_ddl.Move('High Jump Kick', 100, 0.9, 'Phys', 'Fighting')
        root.moves['Jump Kick'] = pokemon_ddl.Move('Jump Kick', 85, 0.95, 'Phys', 'Fighting')
        root.moves['Karate Chop'] = pokemon_ddl.Move('Karate Chop', 50, 1.0, 'Phys', 'Fighting')
        root.moves['Low Kick'] = pokemon_ddl.Move('Low Kick', 0, 1.0, 'Phys', 'Fighting')
        root.moves['Mach Punch'] = pokemon_ddl.Move('Mach Punch', 40, 1.0, 'Phys', 'Fighting')
        root.moves['Revenge'] = pokemon_ddl.Move('Revenge', 60, 1.0, 'Phys', 'Fighting')
        root.moves['Reversal'] = pokemon_ddl.Move('Reversal', 0, 1.0, 'Phys', 'Fighting')
        root.moves['Rock Smash'] = pokemon_ddl.Move('Rock Smash', 40, 1.0, 'Phys', 'Fighting')
        root.moves['Rolling Kick'] = pokemon_ddl.Move('Rolling Kick', 60, 0.85, 'Phys', 'Fighting')
        root.moves['Seismic Toss'] = pokemon_ddl.Move('Seismic Toss', 0, 1.0, 'Phys', 'Fighting')
        root.moves['Sky Uppercut'] = pokemon_ddl.Move('Sky Uppercut', 85, 0.9, 'Phys', 'Fighting')
        root.moves['Submission'] = pokemon_ddl.Move('Submission', 80, 0.8, 'Phys', 'Fighting')
        root.moves['Superpower'] = pokemon_ddl.Move('Superpower', 120, 1.0, 'Phys', 'Fighting')
        root.moves['Triple Kick'] = pokemon_ddl.Move('Triple Kick', 10, 0.9, 'Phys', 'Fighting')
        root.moves['Vital Throw'] = pokemon_ddl.Move('Vital Throw', 70, 1.0, 'Phys', 'Fighting')
        root.moves['Wake-Up Slap'] = pokemon_ddl.Move('Wake-Up Slap', 60, 1.0, 'Phys', 'Fighting')

        # Flying-type moves
        root.moves['Aerial Ace'] = pokemon_ddl.Move('Aerial Ace', 60, 1.0, 'Phys', 'Flying')
        root.moves['Bounce'] = pokemon_ddl.Move('Bounce', 85, 0.85, 'Phys', 'Flying')
        root.moves['Brave Bird'] = pokemon_ddl.Move('Brave Bird', 120, 1.0, 'Phys', 'Flying')
        root.moves['Drill Peck'] = pokemon_ddl.Move('Drill Peck', 80, 1.0, 'Phys', 'Flying')
        root.moves['Fly'] = pokemon_ddl.Move('Fly', 90, 0.95, 'Phys', 'Flying')
        root.moves['Peck'] = pokemon_ddl.Move('Peck', 35, 1.0, 'Phys', 'Flying')
        root.moves['Pluck'] = pokemon_ddl.Move('Pluck', 60, 1.0, 'Phys', 'Flying')
        root.moves['Sky Attack'] = pokemon_ddl.Move('Sky Attack', 140, 0.9, 'Phys', 'Flying')
        root.moves['Wing Attack'] = pokemon_ddl.Move('Wing Attack', 60, 1.0, 'Phys', 'Flying')

        # Poison-type moves
        root.moves['Cross Poison'] = pokemon_ddl.Move('Cross Poison', 70, 1.0, 'Phys', 'Poison')
        root.moves['Gunk Shot'] = pokemon_ddl.Move('Gunk Shot', 120, 0.7, 'Phys', 'Poison')
        root.moves['Poison Fang'] = pokemon_ddl.Move('Poison Fang', 50, 1.0, 'Phys', 'Poison')
        root.moves['Poison Jab'] = pokemon_ddl.Move('Poison Jab', 80, 1.0, 'Phys', 'Poison')
        root.moves['Poison Sting'] = pokemon_ddl.Move('Poison Sting', 15, 1.0, 'Phys', 'Poison')
        root.moves['Poison Tail'] = pokemon_ddl.Move('Poison Tail', 50, 1.0, 'Phys', 'Poison')

        # Ground-type moves
        root.moves['Bone Club'] = pokemon_ddl.Move('Bone Club', 65, 0.85, 'Phys', 'Ground')
        root.moves['Bone Rush'] = pokemon_ddl.Move('Bone Rush', 25, 0.8, 'Phys', 'Ground')
        root.moves['Bonemerang'] = pokemon_ddl.Move('Bonemerang', 50, 0.9, 'Phys', 'Ground')
        root.moves['Dig'] = pokemon_ddl.Move('Dig', 80, 1.0, 'Phys', 'Ground')
        root.moves['Earthquake'] = pokemon_ddl.Move('Earthquake', 100, 1.0, 'Phys', 'Ground')
        root.moves['Fissure'] = pokemon_ddl.Move('Fissure', 0, 0.3, 'Phys', 'Ground')
        root.moves['Magnitude'] = pokemon_ddl.Move('Magnitude', 0, 1.0, 'Phys', 'Ground')
        root.moves['Sand Tomb'] = pokemon_ddl.Move('Sand Tomb', 15, 0.7, 'Phys', 'Ground')

        # Rock-type moves
        root.moves['Head Smash'] = pokemon_ddl.Move('Head Smash', 150, 0.8, 'Phys', 'Rock')
        root.moves['Rock Blast'] = pokemon_ddl.Move('Rock Blast', 25, 0.8, 'Phys', 'Rock')
        root.moves['Rock Slide'] = pokemon_ddl.Move('Rock Slide', 75, 0.9, 'Phys', 'Rock')
        root.moves['Rock Throw'] = pokemon_ddl.Move('Rock Throw', 50, 0.9, 'Phys', 'Rock')
        root.moves['Rock Tomb'] = pokemon_ddl.Move('Rock Tomb', 50, 0.8, 'Phys', 'Rock')
        root.moves['Rock Wrecker'] = pokemon_ddl.Move('Rock Wrecker', 150, 0.9, 'Phys', 'Rock')
        root.moves['Rollout'] = pokemon_ddl.Move('Rollout', 30, 0.9, 'Phys', 'Rock')
        root.moves['Stone Edge'] = pokemon_ddl.Move('Stone Edge', 100, 0.8, 'Phys', 'Rock')

        # Bug-type moves
        root.moves['Attack Order'] = pokemon_ddl.Move('Attack Order', 90, 1.0, 'Phys', 'Bug')
        root.moves['Bug Bite'] = pokemon_ddl.Move('Bug Bite', 60, 1.0, 'Phys', 'Bug')
        root.moves['Fury Cutter'] = pokemon_ddl.Move('Fury Cutter', 10, 0.95, 'Phys', 'Bug')
        root.moves['Leech Life'] = pokemon_ddl.Move('Leech Life', 20, 1.0, 'Phys', 'Bug')
        root.moves['Megahorn'] = pokemon_ddl.Move('Megahorn', 120, 0.85, 'Phys', 'Bug')
        root.moves['Pin Missile'] = pokemon_ddl.Move('Pin Missile', 14, 0.85, 'Phys', 'Bug')
        root.moves['Twineedle'] = pokemon_ddl.Move('Twineedle', 25, 1.0, 'Phys', 'Bug')
        root.moves['U-turn'] = pokemon_ddl.Move('U-turn', 70, 1.0, 'Phys', 'Bug')
        root.moves['X-Scissor'] = pokemon_ddl.Move('X-Scissor', 80, 1.0, 'Phys', 'Bug')

        # Ghost-type moves
        root.moves['Astonish'] = pokemon_ddl.Move('Astonish', 30, 1.0, 'Phys', 'Ghost')
        root.moves['Lick'] = pokemon_ddl.Move('Lick', 20, 1.0, 'Phys', 'Ghost')
        root.moves['Shadow Claw'] = pokemon_ddl.Move('Shadow Claw', 70, 1.0, 'Phys', 'Ghost')
        root.moves['Shadow Force'] = pokemon_ddl.Move('Shadow Force', 120, 1.0, 'Phys', 'Ghost')
        root.moves['Shadow Punch'] = pokemon_ddl.Move('Shadow Punch', 60, 1.0, 'Phys', 'Ghost')
        root.moves['Shadow Sneak'] = pokemon_ddl.Move('Shadow Sneak', 40, 1.0, 'Phys', 'Ghost')

        # Steel-type moves
        root.moves['Bullet Punch'] = pokemon_ddl.Move('Bullet Punch', 40, 1.0, 'Phys', 'Steel')
        root.moves['Gyro Ball'] = pokemon_ddl.Move('Gyro Ball', 0, 1.0, 'Phys', 'Steel')
        root.moves['Iron Head'] = pokemon_ddl.Move('Iron Head', 80, 1.0, 'Phys', 'Steel')
        root.moves['Iron Tail'] = pokemon_ddl.Move('Iron Tail', 100, 0.75, 'Phys', 'Steel')
        root.moves['Magnet Bomb'] = pokemon_ddl.Move('Magnet Bomb', 60, 1.0, 'Phys', 'Steel')
        root.moves['Metal Burst'] = pokemon_ddl.Move('Metal Burst', 0, 1.0, 'Phys', 'Steel')
        root.moves['Metal Claw'] = pokemon_ddl.Move('Metal Claw', 50, 0.95, 'Phys', 'Steel')
        root.moves['Meteor Mash'] = pokemon_ddl.Move('Meteor Mash', 100, 0.85, 'Phys', 'Steel')
        root.moves['Steel Wing'] = pokemon_ddl.Move('Steel Wing', 70, 0.9, 'Phys', 'Steel')

        # Fire-type moves
        root.moves['Blaze Kick'] = pokemon_ddl.Move('Blaze Kick', 85, 0.9, 'Phys', 'Fire')
        root.moves['Fire Fang'] = pokemon_ddl.Move('Fire Fang', 65, 0.95, 'Phys', 'Fire')
        root.moves['Fire Punch'] = pokemon_ddl.Move('Fire Punch', 75, 1.0, 'Phys', 'Fire')
        root.moves['Flame Wheel'] = pokemon_ddl.Move('Flame Wheel', 60, 1.0, 'Phys', 'Fire')
        root.moves['Flare Blitz'] = pokemon_ddl.Move('Flare Blitz', 120, 1.0, 'Phys', 'Fire')
        root.moves['Sacred Fire'] = pokemon_ddl.Move('Sacred Fire', 100, 0.95, 'Phys', 'Fire')

        # Water-type moves
        root.moves['Aqua Jet'] = pokemon_ddl.Move('Aqua Jet', 40, 1.0, 'Phys', 'Water')
        root.moves['Aqua Tail'] = pokemon_ddl.Move('Aqua Tail', 90, 0.9, 'Phys', 'Water')
        root.moves['Clamp'] = pokemon_ddl.Move('Clamp', 35, 0.75, 'Phys', 'Water')
        root.moves['Crabhammer'] = pokemon_ddl.Move('Crabhammer', 90, 0.85, 'Phys', 'Water')
        root.moves['Dive'] = pokemon_ddl.Move('Dive', 80, 1.0, 'Phys', 'Water')
        root.moves['Waterfall'] = pokemon_ddl.Move('Waterfall', 80, 1.0, 'Phys', 'Water')

        # Grass-type moves
        root.moves['Bullet Seed'] = pokemon_ddl.Move('Bullet Seed', 10, 1.0, 'Phys', 'Grass')
        root.moves['Leaf Blade'] = pokemon_ddl.Move('Leaf Blade', 90, 1.0, 'Phys', 'Grass')
        root.moves['Needle Arm'] = pokemon_ddl.Move('Needle Arm', 60, 1.0, 'Phys', 'Grass')
        root.moves['Power Whip'] = pokemon_ddl.Move('Power Whip', 120, 0.85, 'Phys', 'Grass')
        root.moves['Razor Leaf'] = pokemon_ddl.Move('Razor Leaf', 55, 0.95, 'Phys', 'Grass')
        root.moves['Seed Bomb'] = pokemon_ddl.Move('Seed Bomb', 80, 1.0, 'Phys', 'Grass')
        root.moves['Vine Whip'] = pokemon_ddl.Move('Vine Whip', 35, 1.0, 'Phys', 'Grass')
        root.moves['Wood Hammer'] = pokemon_ddl.Move('Wood Hammer', 120, 1.0, 'Phys', 'Grass')

        # Electric-type moves
        root.moves['Spark'] = pokemon_ddl.Move('Spark', 65, 1.0, 'Phys', 'Electric')
        root.moves['Thunder Fang'] = pokemon_ddl.Move('Thunder Fang', 65, 0.95, 'Phys', 'Electric')
        root.moves['Thunder Punch'] = pokemon_ddl.Move('Thunder Punch', 75, 1.0, 'Phys', 'Electric')
        root.moves['Volt Tackle'] = pokemon_ddl.Move('Volt Tackle', 120, 1.0, 'Phys', 'Electric')

        # Psychic-type moves
        root.moves['Psycho Cut'] = pokemon_ddl.Move('Psycho Cut', 70, 1.0, 'Phys', 'Psychic')
        root.moves['Zen Headbutt'] = pokemon_ddl.Move('Zen Headbutt', 80, 0.9, 'Phys', 'Psychic')

        # Ice-type moves
        root.moves['Avalanche'] = pokemon_ddl.Move('Avalanche', 60, 1.0, 'Phys', 'Ice')
        root.moves['Ice Ball'] = pokemon_ddl.Move('Ice Ball', 30, 0.9, 'Phys', 'Ice')
        root.moves['Ice Fang'] = pokemon_ddl.Move('Ice Fang', 65, 0.95, 'Phys', 'Ice')
        root.moves['Ice Punch'] = pokemon_ddl.Move('Ice Punch', 75, 1.0, 'Phys', 'Ice')
        root.moves['Ice Shard'] = pokemon_ddl.Move('Ice Shard', 40, 1.0, 'Phys', 'Ice')
        root.moves['Icicle Spear'] = pokemon_ddl.Move('Icicle Spear', 10, 1.0, 'Phys', 'Ice')

        # Dragon-type moves
        root.moves['Dragon Claw'] = pokemon_ddl.Move('Dragon Claw', 80, 1.0, 'Phys', 'Dragon')
        root.moves['Dragon Rush'] = pokemon_ddl.Move('Dragon Rush', 100, 0.75, 'Phys', 'Dragon')
        root.moves['Outrage'] = pokemon_ddl.Move('Outrage', 120, 1.0, 'Phys', 'Dragon')

        # Dark-type moves
        root.moves['Assurance'] = pokemon_ddl.Move('Assurance', 50, 1.0, 'Phys', 'Dark')
        root.moves['Beat Up'] = pokemon_ddl.Move('Beat Up', 10, 1.0, 'Phys', 'Dark')
        root.moves['Bite'] = pokemon_ddl.Move('Bite', 60, 1.0, 'Phys', 'Dark')
        root.moves['Crunch'] = pokemon_ddl.Move('Crunch', 80, 1.0, 'Phys', 'Dark')
        root.moves['Feint Attack'] = pokemon_ddl.Move('Feint Attack', 60, 1.0, 'Phys', 'Dark')
        root.moves['Feint'] = pokemon_ddl.Move('Feint', 50, 1.0, 'Phys', 'Dark')
        root.moves['Fling'] = pokemon_ddl.Move('Fling', 0, 1.0, 'Phys', 'Dark')
        root.moves['Knock Off'] = pokemon_ddl.Move('Knock Off', 20, 1.0, 'Phys', 'Dark')
        root.moves['Night Slash'] = pokemon_ddl.Move('Night Slash', 70, 1.0, 'Phys', 'Dark')
        root.moves['Payback'] = pokemon_ddl.Move('Payback', 50, 1.0, 'Phys', 'Dark')
        root.moves['Punishment'] = pokemon_ddl.Move('Punishment', 0, 1.0, 'Phys', 'Dark')
        root.moves['Pursuit'] = pokemon_ddl.Move('Pursuit', 40, 1.0, 'Phys', 'Dark')
        root.moves['Sucker Punch'] = pokemon_ddl.Move('Sucker Punch', 80, 1.0, 'Phys', 'Dark')
        root.moves['Thief'] = pokemon_ddl.Move('Thief', 40, 1.0, 'Phys', 'Dark')

    if 'Special Moves':
        # Hidden Powers
        root.moves['Hidden Power [Fire]'] = pokemon_ddl.Move('Hidden Power [Fire]', 60, 1.0, 'Spec', 'Fire')
        root.moves['Hidden Power [Ice]'] = pokemon_ddl.Move('Hidden Power [Ice]', 60, 1.0, 'Spec', 'Ice')
        root.moves['Hidden Power [Grass]'] = pokemon_ddl.Move('Hidden Power [Grass]', 60, 1.0, 'Spec', 'Grass')
        root.moves['Hidden Power [Ground]'] = pokemon_ddl.Move('Hidden Power [Ground]', 60, 1.0, 'Spec', 'Ground')
        root.moves['Hidden Power [Fighting]'] = pokemon_ddl.Move('Hidden Power [Fighting]', 60, 1.0, 'Spec', 'Fighting')
        root.moves['Hidden Power [Water]'] = pokemon_ddl.Move('Hidden Power [Water]', 60, 1.0, 'Spec', 'Water')
        root.moves['Hidden Power [Electric]'] = pokemon_ddl.Move('Hidden Power [Electric]', 60, 1.0, 'Spec', 'Electric')
        root.moves['Hidden Power [Poison]'] = pokemon_ddl.Move('Hidden Power [Poison]', 60, 1.0, 'Spec', 'Poison')
        root.moves['Hidden Power [Flying]'] = pokemon_ddl.Move('Hidden Power [Flying]', 60, 1.0, 'Spec', 'Flying')
        root.moves['Hidden Power [Psychic]'] = pokemon_ddl.Move('Hidden Power [Psychic]', 60, 1.0, 'Spec', 'Psychic')
        root.moves['Hidden Power [Bug]'] = pokemon_ddl.Move('Hidden Power [Bug]', 60, 1.0, 'Spec', 'Bug')
        root.moves['Hidden Power [Rock]'] = pokemon_ddl.Move('Hidden Power [Rock]', 60, 1.0, 'Spec', 'Rock')
        root.moves['Hidden Power [Ghost]'] = pokemon_ddl.Move('Hidden Power [Ghost]', 60, 1.0, 'Spec', 'Ghost')
        root.moves['Hidden Power [Dragon]'] = pokemon_ddl.Move('Hidden Power [Dragon]', 60, 1.0, 'Spec', 'Dragon')
        root.moves['Hidden Power [Dark]'] = pokemon_ddl.Move('Hidden Power [Dark]', 60, 1.0, 'Spec', 'Dark')
        root.moves['Hidden Power [Steel]'] = pokemon_ddl.Move('Hidden Power [Steel]', 60, 1.0, 'Spec', 'Steel')

        # Grass-type moves
        root.moves['Absorb'] = pokemon_ddl.Move('Absorb', 20, 1.0, 'Spec', 'Grass')
        root.moves['Energy Ball'] = pokemon_ddl.Move('Energy Ball', 80, 1.0, 'Spec', 'Grass')
        root.moves['Frenzy Plant'] = pokemon_ddl.Move('Frenzy Plant', 150, 0.9, 'Spec', 'Grass')
        root.moves['Giga Drain'] = pokemon_ddl.Move('Giga Drain', 60, 1.0, 'Spec', 'Grass')
        root.moves['Grass Knot'] = pokemon_ddl.Move('Grass Knot', 0, 1.0, 'Spec', 'Grass')
        root.moves['Leaf Storm'] = pokemon_ddl.Move('Leaf Storm', 140, 0.9, 'Spec', 'Grass')
        root.moves['Magical Leaf'] = pokemon_ddl.Move('Magical Leaf', 60, 1.0, 'Spec', 'Grass')
        root.moves['Mega Drain'] = pokemon_ddl.Move('Mega Drain', 40, 1.0, 'Spec', 'Grass')
        root.moves['Petal Dance'] = pokemon_ddl.Move('Petal Dance', 90, 1.0, 'Spec', 'Grass')
        root.moves['Seed Flare'] = pokemon_ddl.Move('Seed Flare', 120, 0.85, 'Spec', 'Grass')
        root.moves['Solar Beam'] = pokemon_ddl.Move('Solar Beam', 120, 1.0, 'Spec', 'Grass')

        # Poison-type moves
        root.moves['Acid'] = pokemon_ddl.Move('Acid', 40, 1.0, 'Spec', 'Poison')
        root.moves['Sludge'] = pokemon_ddl.Move('Sludge', 65, 1.0, 'Spec', 'Poison')
        root.moves['Sludge Bomb'] = pokemon_ddl.Move('Sludge Bomb', 90, 1.0, 'Spec', 'Poison')
        root.moves['Smog'] = pokemon_ddl.Move('Smog', 20, 0.7, 'Spec', 'Poison')

        # Flying-type moves
        root.moves['Aeroblast'] = pokemon_ddl.Move('Aeroblast', 100, 0.95, 'Spec', 'Flying')
        root.moves['Air Cutter'] = pokemon_ddl.Move('Air Cutter', 55, 0.95, 'Spec', 'Flying')
        root.moves['Air Slash'] = pokemon_ddl.Move('Air Slash', 75, 0.95, 'Spec', 'Flying')
        root.moves['Chatter'] = pokemon_ddl.Move('Chatter', 60, 1.0, 'Spec', 'Flying')
        root.moves['Gust'] = pokemon_ddl.Move('Gust', 40, 1.0, 'Spec', 'Flying')
        root.moves['Razor Wind'] = pokemon_ddl.Move('Razor Wind', 80, 1.0, 'Spec', 'Flying')

        # Rock-type moves
        root.moves['Ancient Power'] = pokemon_ddl.Move('Ancient Power', 60, 1.0, 'Spec', 'Rock')
        root.moves['Power Gem'] = pokemon_ddl.Move('Power Gem', 70, 1.0, 'Spec', 'Rock')

        # Fighting-type moves
        root.moves['Aura Sphere'] = pokemon_ddl.Move('Aura Sphere', 90, 1.0, 'Spec', 'Fighting')
        root.moves['Focus Blast'] = pokemon_ddl.Move('Focus Blast', 120, 0.7, 'Spec', 'Fighting')
        root.moves['Vacuum Wave'] = pokemon_ddl.Move('Vacuum Wave', 40, 1.0, 'Spec', 'Fighting')

        # Ice-type moves
        root.moves['Aurora Beam'] = pokemon_ddl.Move('Aurora Beam', 65, 1.0, 'Spec', 'Ice')
        root.moves['Blizzard'] = pokemon_ddl.Move('Blizzard', 120, 0.7, 'Spec', 'Ice')
        root.moves['Ice Beam'] = pokemon_ddl.Move('Ice Beam', 95, 1.0, 'Spec', 'Ice')
        root.moves['Icy Wind'] = pokemon_ddl.Move('Icy Wind', 55, 0.95, 'Spec', 'Ice')
        root.moves['Powder Snow'] = pokemon_ddl.Move('Powder Snow', 40, 1.0, 'Spec', 'Ice')
        root.moves['Sheer Cold'] = pokemon_ddl.Move('Sheer Cold', 0, 0.3, 'Spec', 'Ice')

        # Water-type moves
        root.moves['Brine'] = pokemon_ddl.Move('Brine', 65, 1.0, 'Spec', 'Water')
        root.moves['Bubble'] = pokemon_ddl.Move('Bubble', 20, 1.0, 'Spec', 'Water')
        root.moves['Bubble Beam'] = pokemon_ddl.Move('Bubble Beam', 65, 1.0, 'Spec', 'Water')
        root.moves['Hydro Cannon'] = pokemon_ddl.Move('Hydro Cannon', 150, 0.9, 'Spec', 'Water')
        root.moves['Hydro Pump'] = pokemon_ddl.Move('Hydro Pump', 120, 0.8, 'Spec', 'Water')
        root.moves['Muddy Water'] = pokemon_ddl.Move('Muddy Water', 95, 0.85, 'Spec', 'Water')
        root.moves['Octazooka'] = pokemon_ddl.Move('Octazooka', 65, 0.85, 'Spec', 'Water')
        root.moves['Surf'] = pokemon_ddl.Move('Surf', 95, 1.0, 'Spec', 'Water')
        root.moves['Water Gun'] = pokemon_ddl.Move('Water Gun', 40, 1.0, 'Spec', 'Water')
        root.moves['Water Pulse'] = pokemon_ddl.Move('Water Pulse', 60, 1.0, 'Spec', 'Water')
        root.moves['Water Spout'] = pokemon_ddl.Move('Water Spout', 150, 1.0, 'Spec', 'Water')
        root.moves['Whirlpool'] = pokemon_ddl.Move('Whirlpool', 15, 0.7, 'Spec', 'Water')

        # Bug-type moves
        root.moves['Bug Buzz'] = pokemon_ddl.Move('Bug Buzz', 90, 1.0, 'Spec', 'Bug')
        root.moves['Signal Beam'] = pokemon_ddl.Move('Signal Beam', 75, 1.0, 'Spec', 'Bug')
        root.moves['Silver Wind'] = pokemon_ddl.Move('Silver Wind', 60, 1.0, 'Spec', 'Bug')

        # Electric-type moves
        root.moves['Charge Beam'] = pokemon_ddl.Move('Charge Beam', 50, 0.9, 'Spec', 'Electric')
        root.moves['Discharge'] = pokemon_ddl.Move('Discharge', 80, 1.0, 'Spec', 'Electric')
        root.moves['Shock Wave'] = pokemon_ddl.Move('Shock Wave', 60, 1.0, 'Spec', 'Electric')
        root.moves['Thunder'] = pokemon_ddl.Move('Thunder', 120, 0.7, 'Spec', 'Electric')
        root.moves['Thunderbolt'] = pokemon_ddl.Move('Thunderbolt', 95, 1.0, 'Spec', 'Electric')
        root.moves['Thundershock'] = pokemon_ddl.Move('Thundershock', 40, 1.0, 'Spec', 'Electric')
        root.moves['Zap Cannon'] = pokemon_ddl.Move('Zap Cannon', 120, 0.5, 'Spec', 'Electric')

        # Psychic-type moves
        root.moves['Confusion'] = pokemon_ddl.Move('Confusion', 50, 1.0, 'Spec', 'Psychic')
        root.moves['Dream Eater'] = pokemon_ddl.Move('Dream Eater', 100, 1.0, 'Spec', 'Psychic')
        root.moves['Extrasensory'] = pokemon_ddl.Move('Extrasensory', 80, 1.0, 'Spec', 'Psychic')
        root.moves['Future Sight'] = pokemon_ddl.Move('Future Sight', 80, 0.9, 'Spec', 'Psychic')
        root.moves['Luster Purge'] = pokemon_ddl.Move('Luster Purge', 70, 1.0, 'Spec', 'Psychic')
        root.moves['Mirror Coat'] = pokemon_ddl.Move('Mirror Coat', 0, 1.0, 'Spec', 'Psychic')
        root.moves['Mist Ball'] = pokemon_ddl.Move('Mist Ball', 70, 1.0, 'Spec', 'Psychic')
        root.moves['Psybeam'] = pokemon_ddl.Move('Psybeam', 65, 1.0, 'Spec', 'Psychic')
        root.moves['Psychic'] = pokemon_ddl.Move('Psychic', 90, 1.0, 'Spec', 'Psychic')
        root.moves['Psycho Boost'] = pokemon_ddl.Move('Psycho Boost', 140, 0.9, 'Spec', 'Psychic')
        root.moves['Psywave'] = pokemon_ddl.Move('Psywave', 0, 0.8, 'Spec', 'Psychic')

        # Dark-type moves
        root.moves['Dark Pulse'] = pokemon_ddl.Move('Dark Pulse', 80, 1.0, 'Spec', 'Dark')

        # Steel-type moves
        root.moves['Doom Desire'] = pokemon_ddl.Move('Doom Desire', 120, 0.85, 'Spec', 'Steel')
        root.moves['Flash Cannon'] = pokemon_ddl.Move('Flash Cannon', 80, 1.0, 'Spec', 'Steel')
        root.moves['Mirror Shot'] = pokemon_ddl.Move('Mirror Shot', 65, 0.85, 'Spec', 'Steel')

        # Dragon-type moves
        root.moves['Draco Meteor'] = pokemon_ddl.Move('Draco Meteor', 140, 0.9, 'Spec', 'Dragon')
        root.moves['Dragon Pulse'] = pokemon_ddl.Move('Dragon Pulse', 90, 1.0, 'Spec', 'Dragon')
        root.moves['Dragon Rage'] = pokemon_ddl.Move('Dragon Rage', 0, 1.0, 'Spec', 'Dragon')
        root.moves['Dragon Breath'] = pokemon_ddl.Move('Dragon Breath', 60, 1.0, 'Spec', 'Dragon')
        root.moves['Roar of Time'] = pokemon_ddl.Move('Roar of Time', 150, 0.9, 'Spec', 'Dragon')
        root.moves['Spacial Rend'] = pokemon_ddl.Move('Spacial Rend', 100, 0.95, 'Spec', 'Dragon')
        root.moves['Twister'] = pokemon_ddl.Move('Twister', 40, 1.0, 'Spec', 'Dragon')

        # Ground-type moves
        root.moves['Earth Power'] = pokemon_ddl.Move('Earth Power', 90, 1.0, 'Spec', 'Ground')
        root.moves['Mud Bomb'] = pokemon_ddl.Move('Mud Bomb', 65, 0.85, 'Spec', 'Ground')
        root.moves['Mud Shot'] = pokemon_ddl.Move('Mud Shot', 55, 0.95, 'Spec', 'Ground')
        root.moves['Mud-Slap'] = pokemon_ddl.Move('Mud-Slap', 20, 1.0, 'Spec', 'Ground')

        # Fire-type moves
        root.moves['Blast Burn'] = pokemon_ddl.Move('Blast Burn', 150, 0.9, 'Spec', 'Fire')
        root.moves['Ember'] = pokemon_ddl.Move('Ember', 40, 1.0, 'Spec', 'Fire')
        root.moves['Eruption'] = pokemon_ddl.Move('Eruption', 150, 1.0, 'Spec', 'Fire')
        root.moves['Fire Blast'] = pokemon_ddl.Move('Fire Blast', 120, 0.85, 'Spec', 'Fire')
        root.moves['Fire Spin'] = pokemon_ddl.Move('Fire Spin', 15, 0.7, 'Spec', 'Fire')
        root.moves['Flamethrower'] = pokemon_ddl.Move('Flamethrower', 95, 1.0, 'Spec', 'Fire')
        root.moves['Heat Wave'] = pokemon_ddl.Move('Heat Wave', 100, 0.9, 'Spec', 'Fire')
        root.moves['Lava Plume'] = pokemon_ddl.Move('Lava Plume', 80, 1.0, 'Spec', 'Fire')
        root.moves['Magma Storm'] = pokemon_ddl.Move('Magma Storm', 120, 0.7, 'Spec', 'Fire')
        root.moves['Overheat'] = pokemon_ddl.Move('Overheat', 140, 0.9, 'Spec', 'Fire')

        # Ghost-type moves
        root.moves['Night Shade'] = pokemon_ddl.Move('Night Shade', 0, 1.0, 'Spec', 'Ghost')
        root.moves['Ominous Wind'] = pokemon_ddl.Move('Ominous Wind', 60, 1.0, 'Spec', 'Ghost')
        root.moves['Shadow Ball'] = pokemon_ddl.Move('Shadow Ball', 80, 1.0, 'Spec', 'Ghost')

        # Normal-type moves
        root.moves['Hyper Beam'] = pokemon_ddl.Move('Hyper Beam', 150, 0.9, 'Spec', 'Normal')
        root.moves['Hyper Voice'] = pokemon_ddl.Move('Hyper Voice', 90, 1.0, 'Spec', 'Normal')
        root.moves['Judgement'] = pokemon_ddl.Move('Judgement', 100, 1.0, 'Spec', 'Normal')
        root.moves['Snore'] = pokemon_ddl.Move('Snore', 40, 1.0, 'Spec', 'Normal')
        root.moves['SonicBoom'] = pokemon_ddl.Move('SonicBoom', 0, 0.9, 'Spec', 'Normal')
        root.moves['Spit Up'] = pokemon_ddl.Move('Spit Up', 0, 1.0, 'Spec', 'Normal')
        root.moves['Swift'] = pokemon_ddl.Move('Swift', 60, 1.0, 'Spec', 'Normal')
        root.moves['Tri Attack'] = pokemon_ddl.Move('Tri Attack', 80, 1.0, 'Spec', 'Normal')
        root.moves['Trump Card'] = pokemon_ddl.Move('Trump Card', 0, 1.0, 'Spec', 'Normal')
        root.moves['Uproar'] = pokemon_ddl.Move('Uproar', 50, 1.0, 'Spec', 'Normal')
        root.moves['Weather Ball'] = pokemon_ddl.Move('Weather Ball', 50, 1.0, 'Spec', 'Normal')
        root.moves['Wring Out'] = pokemon_ddl.Move('Wring Out', 0, 1.0, 'Spec', 'Normal')

    if 'Status Move':
        # Normal-type moves
        root.moves['Acupressure'] = pokemon_ddl.Move('Acupressure', 0, 1.0, 'Stat', 'Normal')
        root.moves['Assist'] = pokemon_ddl.Move('Assist', 0, 1.0, 'Stat', 'Normal')
        root.moves['Attract'] = pokemon_ddl.Move('Attract', 0, 1.0, 'Stat', 'Normal')
        root.moves['Baton Pass'] = pokemon_ddl.Move('Baton Pass', 0, 1.0, 'Stat', 'Normal')
        root.moves['Belly Drum'] = pokemon_ddl.Move('Belly Drum', 0, 1.0, 'Stat', 'Normal')
        root.moves['Block'] = pokemon_ddl.Move('Block', 0, 1.0, 'Stat', 'Normal')
        root.moves['Camouflage'] = pokemon_ddl.Move('Camouflage', 0, 1.0, 'Stat', 'Normal')
        root.moves['Captivate'] = pokemon_ddl.Move('Captivate', 0, 1.0, 'Stat', 'Normal')
        root.moves['Charm'] = pokemon_ddl.Move('Charm', 0, 1.0, 'Stat', 'Normal')
        root.moves['Conversion'] = pokemon_ddl.Move('Conversion', 0, 1.0, 'Stat', 'Normal')
        root.moves['Conversion 2'] = pokemon_ddl.Move('Conversion 2', 0, 1.0, 'Stat', 'Normal')
        root.moves['Copycat'] = pokemon_ddl.Move('Copycat', 0, 1.0, 'Stat', 'Normal')
        root.moves['Defense Curl'] = pokemon_ddl.Move('Defense Curl', 0, 1.0, 'Stat', 'Normal')
        root.moves['Disable'] = pokemon_ddl.Move('Disable', 0, 0.8, 'Stat', 'Normal')
        root.moves['Double Team'] = pokemon_ddl.Move('Double Team', 0, 1.0, 'Stat', 'Normal')
        root.moves['Encore'] = pokemon_ddl.Move('Encore', 0, 1.0, 'Stat', 'Normal')
        root.moves['Endure'] = pokemon_ddl.Move('Endure', 0, 1.0, 'Stat', 'Normal')
        root.moves['Flash'] = pokemon_ddl.Move('Flash', 0, 1.0, 'Stat', 'Normal')
        root.moves['Focus Energy'] = pokemon_ddl.Move('Focus Energy', 0, 1.0, 'Stat', 'Normal')
        root.moves['Follow Me'] = pokemon_ddl.Move('Follow Me', 0, 1.0, 'Stat', 'Normal')
        root.moves['Foresight'] = pokemon_ddl.Move('Foresight', 0, 1.0, 'Stat', 'Normal')
        root.moves['Glare'] = pokemon_ddl.Move('Glare', 0, 0.75, 'Stat', 'Normal')
        root.moves['Growl'] = pokemon_ddl.Move('Growl', 0, 1.0, 'Stat', 'Normal')
        root.moves['Growth'] = pokemon_ddl.Move('Growth', 0, 1.0, 'Stat', 'Normal')
        root.moves['Harden'] = pokemon_ddl.Move('Harden', 0, 1.0, 'Stat', 'Normal')
        root.moves['Heal Bell'] = pokemon_ddl.Move('Heal Bell', 0, 1.0, 'Stat', 'Normal')
        root.moves['Helping Hand'] = pokemon_ddl.Move('Helping Hand', 0, 1.0, 'Stat', 'Normal')
        root.moves['Howl'] = pokemon_ddl.Move('Howl', 0, 1.0, 'Stat', 'Normal')
        root.moves['Leer'] = pokemon_ddl.Move('Leer', 0, 1.0, 'Stat', 'Normal')
        root.moves['Lock-On'] = pokemon_ddl.Move('Lock-On', 0, 1.0, 'Stat', 'Normal')
        root.moves['Lovely Kiss'] = pokemon_ddl.Move('Lovely Kiss', 0, 0.75, 'Stat', 'Normal')
        root.moves['Lucky Chant'] = pokemon_ddl.Move('Lucky Chant', 0, 1.0, 'Stat', 'Normal')
        root.moves['Me First'] = pokemon_ddl.Move('Me First', 0, 1.0, 'Stat', 'Normal')
        root.moves['Mean Look'] = pokemon_ddl.Move('Mean Look', 0, 1.0, 'Stat', 'Normal')
        root.moves['Metronome'] = pokemon_ddl.Move('Metronome', 0, 1.0, 'Stat', 'Normal')
        root.moves['Milk Drink'] = pokemon_ddl.Move('Milk Drink', 0, 1.0, 'Stat', 'Normal')
        root.moves['Mimic'] = pokemon_ddl.Move('Mimic', 0, 1.0, 'Stat', 'Normal')
        root.moves['Mind Reader'] = pokemon_ddl.Move('Mind Reader', 0, 1.0, 'Stat', 'Normal')
        root.moves['Minimize'] = pokemon_ddl.Move('Minimize', 0, 1.0, 'Stat', 'Normal')
        root.moves['Moonlight'] = pokemon_ddl.Move('Moonlight', 0, 1.0, 'Stat', 'Normal')
        root.moves['Morning Sun'] = pokemon_ddl.Move('Morning Sun', 0, 1.0, 'Stat', 'Normal')
        root.moves['Nature Power'] = pokemon_ddl.Move('Nature Power', 0, 1.0, 'Stat', 'Normal')
        root.moves['Odor Sleuth'] = pokemon_ddl.Move('Odor Sleuth', 0, 1.0, 'Stat', 'Normal')
        root.moves['Pain Split'] = pokemon_ddl.Move('Pain Split', 0, 1.0, 'Stat', 'Normal')
        root.moves['Perish Song'] = pokemon_ddl.Move('Perish Song', 0, 1.0, 'Stat', 'Normal')
        root.moves['Protect'] = pokemon_ddl.Move('Protect', 0, 1.0, 'Stat', 'Normal')
        root.moves['Psych Up'] = pokemon_ddl.Move('Psych Up', 0, 1.0, 'Stat', 'Normal')
        root.moves['Recover'] = pokemon_ddl.Move('Recover', 0, 1.0, 'Stat', 'Normal')
        root.moves['Recycle'] = pokemon_ddl.Move('Recycle', 0, 1.0, 'Stat', 'Normal')
        root.moves['Refresh'] = pokemon_ddl.Move('Refresh', 0, 1.0, 'Stat', 'Normal')
        root.moves['Roar'] = pokemon_ddl.Move('Roar', 0, 1.0, 'Stat', 'Normal')
        root.moves['Safeguard'] = pokemon_ddl.Move('Safeguard', 0, 1.0, 'Stat', 'Normal')
        root.moves['Scary Face'] = pokemon_ddl.Move('Scary Face', 0, 0.9, 'Stat', 'Normal')
        root.moves['Screech'] = pokemon_ddl.Move('Screech', 0, 0.85, 'Stat', 'Normal')
        root.moves['Sharpen'] = pokemon_ddl.Move('Sharpen', 0, 1.0, 'Stat', 'Normal')
        root.moves['Sing'] = pokemon_ddl.Move('Sing', 0, 0.55, 'Stat', 'Normal')
        root.moves['Sketch'] = pokemon_ddl.Move('Sketch', 0, 1.0, 'Stat', 'Normal')
        root.moves['Slack Off'] = pokemon_ddl.Move('Slack Off', 0, 1.0, 'Stat', 'Normal')
        root.moves['Sleep Talk'] = pokemon_ddl.Move('Sleep Talk', 0, 1.0, 'Stat', 'Normal')
        root.moves['Smokescreen'] = pokemon_ddl.Move('Smokescreen', 0, 1.0, 'Stat', 'Normal')
        root.moves['Soft-Boiled'] = pokemon_ddl.Move('Soft-Boiled', 0, 1.0, 'Stat', 'Normal')
        root.moves['Splash'] = pokemon_ddl.Move('Splash', 0, 1.0, 'Stat', 'Normal')
        root.moves['Stockpile'] = pokemon_ddl.Move('Stockpile', 0, 1.0, 'Stat', 'Normal')
        root.moves['Substitute'] = pokemon_ddl.Move('Substitute', 0, 1.0, 'Stat', 'Normal')
        root.moves['Supersonic'] = pokemon_ddl.Move('Supersonic', 0, 0.55, 'Stat', 'Normal')
        root.moves['Swagger'] = pokemon_ddl.Move('Swagger', 0, 0.9, 'Stat', 'Normal')
        root.moves['Swallow'] = pokemon_ddl.Move('Swallow', 0, 1.0, 'Stat', 'Normal')
        root.moves['Sweet Kiss'] = pokemon_ddl.Move('Sweet Kiss', 0, 0.75, 'Stat', 'Normal')
        root.moves['Sweet Scent'] = pokemon_ddl.Move('Sweet Scent', 0, 1.0, 'Stat', 'Normal')
        root.moves['Swords Dance'] = pokemon_ddl.Move('Swords Dance', 0, 1.0, 'Stat', 'Normal')
        root.moves['Tail Whip'] = pokemon_ddl.Move('Tail Whip', 0, 1.0, 'Stat', 'Normal')
        root.moves['Teeter Dance'] = pokemon_ddl.Move('Teeter Dance', 0, 1.0, 'Stat', 'Normal')
        root.moves['Tickle'] = pokemon_ddl.Move('Tickle', 0, 1.0, 'Stat', 'Normal')
        root.moves['Transform'] = pokemon_ddl.Move('Transform', 0, 1.0, 'Stat', 'Normal')
        root.moves['Whirlwind'] = pokemon_ddl.Move('Whirlwind', 0, 1.0, 'Stat', 'Normal')
        root.moves['Wish'] = pokemon_ddl.Move('Wish', 0, 1.0, 'Stat', 'Normal')
        root.moves['Yawn'] = pokemon_ddl.Move('Yawn', 0, 1.0, 'Stat', 'Normal')

        # Psychic-type moves
        root.moves['Agility'] = pokemon_ddl.Move('Agility', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Amnesia'] = pokemon_ddl.Move('Amnesia', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Barrier'] = pokemon_ddl.Move('Barrier', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Calm Mind'] = pokemon_ddl.Move('Calm Mind', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Cosmic Power'] = pokemon_ddl.Move('Cosmic Power', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Gravity'] = pokemon_ddl.Move('Gravity', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Guard Swap'] = pokemon_ddl.Move('Guard Swap', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Heal Block'] = pokemon_ddl.Move('Heal Block', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Healing Wish'] = pokemon_ddl.Move('Healing Wish', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Heart Swap'] = pokemon_ddl.Move('Heart Swap', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Hypnosis'] = pokemon_ddl.Move('Hypnosis', 0, 0.7, 'Stat', 'Psychic')
        root.moves['Imprison'] = pokemon_ddl.Move('Imprison', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Kinesis'] = pokemon_ddl.Move('Kinesis', 0, 0.8, 'Stat', 'Psychic')
        root.moves['Light Screen'] = pokemon_ddl.Move('Light Screen', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Lunar Dance'] = pokemon_ddl.Move('Lunar Dance', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Magic Coat'] = pokemon_ddl.Move('Magic Coat', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Meditate'] = pokemon_ddl.Move('Meditate', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Miracle Eye'] = pokemon_ddl.Move('Miracle Eye', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Power Swap'] = pokemon_ddl.Move('Power Swap', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Power Trick'] = pokemon_ddl.Move('Power Trick', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Psycho Shift'] = pokemon_ddl.Move('Psycho Shift', 0, 0.9, 'Stat', 'Psychic')
        root.moves['Reflect'] = pokemon_ddl.Move('Reflect', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Rest'] = pokemon_ddl.Move('Rest', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Role Play'] = pokemon_ddl.Move('Role Play', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Skill Swap'] = pokemon_ddl.Move('Skill Swap', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Teleport'] = pokemon_ddl.Move('Teleport', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Trick'] = pokemon_ddl.Move('Trick', 0, 1.0, 'Stat', 'Psychic')
        root.moves['Trick Room'] = pokemon_ddl.Move('Trick Room', 0, 1.0, 'Stat', 'Psychic')

        # Poison-type moves
        root.moves['Acid Armor'] = pokemon_ddl.Move('Acid Armor', 0, 1.0, 'Stat', 'Poison')
        root.moves['Gastro Acid'] = pokemon_ddl.Move('Gastro Acid', 0, 1.0, 'Stat', 'Poison')
        root.moves['Poison Gas'] = pokemon_ddl.Move('Poison Gas', 0, 0.55, 'Stat', 'Poison')
        root.moves['Poisonpowder'] = pokemon_ddl.Move('Poisonpowder', 0, 0.75, 'Stat', 'Poison')
        root.moves['Toxic'] = pokemon_ddl.Move('Toxic', 0, 0.85, 'Stat', 'Poison')
        root.moves['Toxic Spikes'] = pokemon_ddl.Move('Toxic Spikes', 0, 1.0, 'Stat', 'Poison')

        # Grass-type moves
        root.moves['Aromatherapy'] = pokemon_ddl.Move('Aromatherapy', 0, 1.0, 'Stat', 'Grass')
        root.moves['Cotton Spore'] = pokemon_ddl.Move('Cotton Spore', 0, 0.85, 'Stat', 'Grass')
        root.moves['Grass Whistle'] = pokemon_ddl.Move('Grass Whistle', 0, 0.55, 'Stat', 'Grass')
        root.moves['Ingrain'] = pokemon_ddl.Move('Ingrain', 0, 1.0, 'Stat', 'Grass')
        root.moves['Leech Seed'] = pokemon_ddl.Move('Leech Seed', 0, 0.9, 'Stat', 'Grass')
        root.moves['Sleep Powder'] = pokemon_ddl.Move('Sleep Powder', 0, 0.75, 'Stat', 'Grass')
        root.moves['Spore'] = pokemon_ddl.Move('Spore', 0, 1.0, 'Stat', 'Grass')
        root.moves['Stun Spore'] = pokemon_ddl.Move('Stun Spore', 0, 0.75, 'Stat', 'Grass')
        root.moves['Synthesis'] = pokemon_ddl.Move('Synthesis', 0, 1.0, 'Stat', 'Grass')
        root.moves['Worry Seed'] = pokemon_ddl.Move('Worry Seed', 0, 1.0, 'Stat', 'Grass')

        # Water-type moves
        root.moves['Aqua Ring'] = pokemon_ddl.Move('Aqua Ring', 0, 1.0, 'Stat', 'Water')
        root.moves['Rain Dance'] = pokemon_ddl.Move('Rain Dance', 0, 1.0, 'Stat', 'Water')
        root.moves['Water Sport'] = pokemon_ddl.Move('Water Sport', 0, 1.0, 'Stat', 'Water')
        root.moves['Withdraw'] = pokemon_ddl.Move('Withdraw', 0, 1.0, 'Stat', 'Water')

        # Ghost-type moves
        root.moves['Confuse Ray'] = pokemon_ddl.Move('Confuse Ray', 0, 1.0, 'Stat', 'Ghost')
        root.moves['Curse'] = pokemon_ddl.Move('Curse', 0, 1.0, 'Stat', 'Ghost')
        root.moves['Destiny Bond'] = pokemon_ddl.Move('Destiny Bond', 0, 1.0, 'Stat', 'Ghost')
        root.moves['Grudge'] = pokemon_ddl.Move('Grudge', 0, 1.0, 'Stat', 'Ghost')
        root.moves['Nightmare'] = pokemon_ddl.Move('Nightmare', 0, 1.0, 'Stat', 'Ghost')
        root.moves['Spite'] = pokemon_ddl.Move('Spite', 0, 1.0, 'Stat', 'Ghost')

        # Dark-type moves
        root.moves['Dark Void'] = pokemon_ddl.Move('Dark Void', 0, 0.8, 'Stat', 'Dark')
        root.moves['Embargo'] = pokemon_ddl.Move('Embargo', 0, 1.0, 'Stat', 'Dark')
        root.moves['Fake Tears'] = pokemon_ddl.Move('Fake Tears', 0, 1.0, 'Stat', 'Dark')
        root.moves['Flatter'] = pokemon_ddl.Move('Flatter', 0, 1.0, 'Stat', 'Dark')
        root.moves['Memento'] = pokemon_ddl.Move('Memento', 0, 1.0, 'Stat', 'Dark')
        root.moves['Nasty Plot'] = pokemon_ddl.Move('Nasty Plot', 0, 1.0, 'Stat', 'Dark')
        root.moves['Snatch'] = pokemon_ddl.Move('Snatch', 0, 1.0, 'Stat', 'Dark')
        root.moves['Switcheroo'] = pokemon_ddl.Move('Switcheroo', 0, 1.0, 'Stat', 'Dark')
        root.moves['Taunt'] = pokemon_ddl.Move('Taunt', 0, 1.0, 'Stat', 'Dark')
        root.moves['Torment'] = pokemon_ddl.Move('Torment', 0, 1.0, 'Stat', 'Dark')

        # Bug-type moves
        root.moves['Defend Order'] = pokemon_ddl.Move('Defend Order', 0, 1.0, 'Stat', 'Bug')
        root.moves['Heal Order'] = pokemon_ddl.Move('Heal Order', 0, 1.0, 'Stat', 'Bug')
        root.moves['Spider Web'] = pokemon_ddl.Move('Spider Web', 0, 1.0, 'Stat', 'Bug')
        root.moves['String Shot'] = pokemon_ddl.Move('String Shot', 0, 0.95, 'Stat', 'Bug')
        root.moves['Tail Glow'] = pokemon_ddl.Move('Tail Glow', 0, 1.0, 'Stat', 'Bug')

        # Fighting-type moves
        root.moves['Bulk Up'] = pokemon_ddl.Move('Bulk Up', 0, 1.0, 'Stat', 'Fighting')
        root.moves['Detect'] = pokemon_ddl.Move('Detect', 0, 1.0, 'Stat', 'Fighting')

        # Electric-type moves
        root.moves['Charge'] = pokemon_ddl.Move('Charge', 0, 1.0, 'Stat', 'Electric')
        root.moves['Magnet Rise'] = pokemon_ddl.Move('Magnet Rise', 0, 1.0, 'Stat', 'Electric')
        root.moves['Thunder Wave'] = pokemon_ddl.Move('Thunder Wave', 0, 1.0, 'Stat', 'Electric')

        # Flying-type moves
        root.moves['Defog'] = pokemon_ddl.Move('Defog', 0, 1.0, 'Stat', 'Flying')
        root.moves['Feather Dance'] = pokemon_ddl.Move('Feather Dance', 0, 1.0, 'Stat', 'Flying')
        root.moves['Mirror Move'] = pokemon_ddl.Move('Mirror Move', 0, 1.0, 'Stat', 'Flying')
        root.moves['Roost'] = pokemon_ddl.Move('Roost', 0, 1.0, 'Stat', 'Flying')
        root.moves['Tailwind'] = pokemon_ddl.Move('Tailwind', 0, 1.0, 'Stat', 'Flying')

        # Dragon-type moves
        root.moves['Dragon Dance'] = pokemon_ddl.Move('Dragon Dance', 0, 1.0, 'Stat', 'Dragon')

        # Ice-type moves
        root.moves['Hail'] = pokemon_ddl.Move('Hail', 0, 1.0, 'Stat', 'Ice')
        root.moves['Haze'] = pokemon_ddl.Move('Haze', 0, 1.0, 'Stat', 'Ice')
        root.moves['Mist'] = pokemon_ddl.Move('Mist', 0, 1.0, 'Stat', 'Ice')

        # Steel-type moves
        root.moves['Iron Defense'] = pokemon_ddl.Move('Iron Defense', 0, 1.0, 'Stat', 'Steel')
        root.moves['Metal Sound'] = pokemon_ddl.Move('Metal Sound', 0, 0.85, 'Stat', 'Steel')

        # Ground-type moves
        root.moves['Mud Sport'] = pokemon_ddl.Move('Mud Sport', 0, 1.0, 'Stat', 'Ground')
        root.moves['Sand Attack'] = pokemon_ddl.Move('Sand Attack', 0, 1.0, 'Stat', 'Ground')
        root.moves['Spikes'] = pokemon_ddl.Move('Spikes', 0, 1.0, 'Stat', 'Ground')

        # Rock-type moves
        root.moves['Rock Polish'] = pokemon_ddl.Move('Rock Polish', 0, 1.0, 'Stat', 'Rock')
        root.moves['Sandstorm'] = pokemon_ddl.Move('Sandstorm', 0, 1.0, 'Stat', 'Rock')
        root.moves['Stealth Rock'] = pokemon_ddl.Move('Stealth Rock', 0, 1.0, 'Stat', 'Rock')

        # Fire-type moves
        root.moves['Sunny Day'] = pokemon_ddl.Move('Sunny Day', 0, 1.0, 'Stat', 'Fire')
        root.moves['Will-O-Wisp'] = pokemon_ddl.Move('Will-O-Wisp', 0, 0.75, 'Stat', 'Fire')

    if 'items':
        root.items['items'] = ['Big Root', 'Binding Band', 'Bright Powder', 'Choice Band', 'Choice Scarf', 'Choice Specs',
                               'Damp Rock', 'Expert Belt', 'Flame Orb', 'Focus Band', 'Focus Sash', 'Grip Claw',
                               'Heat Rock', 'Icy Rock', 'Iron Ball', 'Lagging Tail',
                               'Life Orb', 'Light Clay', 'Metronome', 'Muscle Band', 'Power Herb', 'Quick Claw', 'Razor Claw',
                               'Razor Fang', 'Scope Lens', 'Shed Shell', 'Smooth Rock', 'Sticky Barb', 'Toxic Orb', 'White Herb',
                               'Wide Lens', 'Wise Glasses', 'Zoom Lens', 'Draco Plate', 'Dread Plate', 'Earth Plate', 'Fist Plate',
                               'Flame Plate', 'Icicle Plate', 'Insect Plate', 'Iron Plate', 'Meadow Plate', 'Mind Plate',
                               'Sky Plate', 'Splash Plate', 'Spooky Plate', 'Stone Plate', 'Toxic Plate', 'Zap Plate', 'Leftovers',
                               'Black Sludge', 'Custap Berry', 'Leichi Berry', 'Salac Berry', 'Starf Berry',
                               'Sitrus Berry', 'Apicot Berry', 'Petaya Berry', 'Jaboca Berry',
                               'Rowap Berry', 'Big Nugget', 'Black Glasses', 'Charcoal', 'Mystic Water', 'Silk Scarf', 'Magnet',
                               'Miracle Seed', 'Never-Melt Ice', 'Sharp Beak', 'Soft Sand', 'Spell Tag', 'Twisted Spoon',
                               'Poison Barb', 'Hard Stone', 'Dragon Fang', 'Silver Powder', 'Shell Bell', 'Lum Berry', 'Chesto Berry', 'Black Belt',
                               'Metal Coat', 'Ganlon Berry', 'Apicot Berry']
        root.items['Berries'] = ['Barbiri Berry', 'Charti Berry', 'Chilan Berry', 'Chople Berry', 'Coba Berry', 'Colbur Berry',
                                 'Haban Berry', 'Kasib Berry', 'Kebia Berry', 'Occa Berry', 'Passho Berry', 'Payapa Berry',
                                 'Rindo Berry', 'Shuka Berry', 'Tanga Berry', 'Wacan Berry', 'Yache Berry']

    transaction.commit()

    print(root.pokesets['Dragonite'].toString())
    connection.close()
    db.close()
    storage.close()

    with open(config.DML_VERSION_FILE, 'w') as f:
        f.write(current_dml_hash)


if __name__ == '__main__':
    runDML()
