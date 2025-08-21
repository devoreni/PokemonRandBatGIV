from BTrees.OOBTree import OOBTree
import ZODB, ZODB.FileStorage
import persistent
import pokemon_ddl
import transaction
import numpy as np
import random
import pprint


def runDML():
    storage = ZODB.FileStorage.FileStorage('./data/PokeData.fs')
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root

    if not hasattr(root, 'moves'):
        root.moves = OOBTree()
    if not hasattr(root, 'pokesets'):
        root.pokesets = OOBTree()
    if not hasattr(root, 'pokeprobability'):
        root.pokeprobability = OOBTree()

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
                         'Fire Fang': ['Scary Face', 'Dragon Claw', 'Double-edge', 'Thunder Fang', 'Dragon Dance'],
                         'Thunder Fang': ['Aerial Ace', 'Fire Fang', 'Zen Headbutt', 'Rain Dance', 'Roar'],
                         'Crunch': ['Brick Break', 'Facade', 'Rest', 'Substitute', 'Earthquake'],
                         'Rest': ['Sleep Talk', 'Snore'],
                         'Headbutt': ['Outrage', 'Rollout', 'Aqua Tail', 'Fury Cutter', 'Shadow Claw', 'Dragon Dance'],
                         'Hydro Pump': ['Dragon Pulse', 'Draco Meteor', 'Heat Wave', 'Swift', 'Air Cutter'],
                         'Dragon Breath': ['Flamethrower', 'Fire Blast'],
                         'Flamethrower': ['Hidden Power [Ice]', 'Sunny Day', 'Hidden Power [Bug]'],
                         'Fire Blast': ['Sunny Day', 'Giga Impact', 'Double Team', 'Mud-slap'],
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
                    ),), baseStats=(80, 80, 90, 110, 130, 110), genders=('F',), images=('380.gif', '380.png', '380 (1).png')
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
                    genders=('M',), images=('381.gif', '381.png', '381 (1).png')
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
                    genders=('',), images=('483.gif', '483.png', '483 (1).png')
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
                    genders=('',), images=('384.gif', '384.png', '384 (1).png')
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
                    genders=('',), images=('493.gif', 'arceus-dragon.png', 'arceus-dragon (1).png')
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
                            ['Protect', 'Rest', 'Lock-on'],
                            {
                                'Protect': ['Ancient Power', 'Icy Wind', 'Thunder Wave', 'Toxic', 'Seismic Toss', 'Hyper Beam'],
                                'Rest': ['Charge Beam', 'Amnesia', 'Sleep Talk'],
                                'Lock-on': ['Zap Cannon'],
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
                    ), baseStats=(120, 120, 120, 120, 120, 120), genders=('',), images=('493.gif', 'arceus-ice.png', 'arceus-ice (1).png')
                )

        #Fighting type pokemon
        if 'Fighting':
            if 'Primape':
                root.pokesets['Primape'] = pokemon_ddl.PokemonSet(
                    name='Primape', species='Primape', abilities=('Vital Spirit', 'Anger Point'), pkTypes=('Fighting',),
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
                    ), baseStats=(120, 120, 120, 120, 120, 120), genders=('',), images=('493.gif', 'arceus-fighting.png', 'arceus-fighting (1).png')
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
                                'Psych Up': ['Faint Attack', 'Payback']
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
                                'Fake Out': ['Faint Attack', 'Explosion', 'Sucker Punch', 'X-Scissor'],
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
                            ['Protect', 'Dive'],
                        {
                            'Protect': ['Hydro Pump', 'Crunch', 'Night Slash'],
                            'Hydro Pump': ['Dark Pulse', 'Ice Beam', 'Aqua Jet', 'Hidden Power [Grass]', 'Ancient Power'],
                            'Crunch': ['Waterfall', 'Taunt', 'Aqua Jet', 'Substitute'],
                            'Taunt': ['Earthquake', 'Ice Fang'],
                            'Substitute': ['Zen Headbutt'],
                            'Dive': ['Crunch', 'Double-Edge', 'Night Slash'],
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
                    ), baseStats=(120, 120, 120, 120, 120, 120), genders=('',), images=('493.gif', 'arceus-dark.png', 'arceus-dark (1).png')
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
                    ), baseStats=(120, 120, 120, 120, 120, 120), genders=('',), images=('493.gif', 'arceus-fire.png', 'arceus-fire (1).png')
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
                    ), baseStats=(1, 90, 45, 30, 30, 40), genders=('',), images=('292.gif', '292.png', '292 (1).png')
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
                    ), baseStats=(120, 120, 120, 120, 120, 120), genders=('',), images=('493.gif', 'arceus-ghost.png', 'arceus-ghost (1).png')
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
                                'Thunder': ['Thunderbolt', 'Mirror Move', 'Light Screen', 'Reflect'],
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
                    ), baseStats=(120, 120, 120, 120, 120, 120), genders=('',), images=('493.gif', 'arceus-steel.png', 'arceus-steel (1).png')
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
                    ), baseStats=(35, 55, 30, 50, 40, 90), genders=('M', 'F'), images=('025.gif', '025-m.png', '025-m (1).png')
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
                                'Protect': ['Helping Hand', 'Mud-Slap', 'Thunderbolt', 'Fake Tears'],
                                'Mud-Slap': ['Light Screen', 'Thunderbolt'],
                                'Helping Hand': ['Light Screen', 'Thunderbolt'],
                                'Thunderbolt': ['Charge Beam', 'Discharge', 'Hidden Power [Ice]', 'Hidden Power [Water]', 'Hyper Beam', 'Hidden Power [Grass]', 'Shadow Ball', 'Shock Wave', 'Signal Beam', 'Swift', 'Trump Card', 'Yawn', 'Rain Dance', 'Thunder']
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
                    sets=(), baseStats=(90, 75, 75, 115, 90, 55), genders=('M', 'F')
                )
            if 'Raikou':
                root.pokesets['Raikou'] = pokemon_ddl.PokemonSet(
                    name='Raikou', species='Raikou', abilities=('Pressure',), pkTypes=('Electric',),
                    sets=(), baseStats=(90, 85, 75, 115, 100, 115), genders=('',)
                )
            if 'Manectric':
                root.pokesets['Manectric'] = pokemon_ddl.PokemonSet(
                    name='Manectric', species='Manectric', abilities=('Static', 'Lightning Rod'), pkTypes=('Electric',),
                    sets=(), baseStats=(70, 75, 60, 105, 60, 105), genders=('M', 'F')
                )
            if 'Plusle':
                root.pokesets['Plusle'] = pokemon_ddl.PokemonSet(
                    name='Plusle', species='Plusle', abilities=('Plus',), pkTypes=('Electric',),
                    sets=(), baseStats=(60, 50, 40, 85, 75, 95), genders=('M', 'F')
                )
            if 'Minun':
                root.pokesets['Minun'] = pokemon_ddl.PokemonSet(
                    name='Minun', species='Minun', abilities=('Minus',), pkTypes=('Electric',),
                    sets=(), baseStats=(60, 40, 50, 75, 85, 95), genders=('M', 'F')
                )
            if 'Luxray':
                root.pokesets['Luxray'] = pokemon_ddl.PokemonSet(
                    name='Luxray', species='Luxray', abilities=('Rivalry', 'Intimidate'), pkTypes=('Electric',),
                    sets=(), baseStats=(80, 120, 79, 95, 79, 70), genders=('M', 'F')
                )
            if 'Pachirisu':
                root.pokesets['Pachirisu'] = pokemon_ddl.PokemonSet(
                    name='Pachirisu', species='Pachirisu', abilities=('Run Away', 'Pick Up'), pkTypes=('Electric',),
                    sets=(), baseStats=(60, 45, 70, 45, 90, 95), genders=('M', 'F')
                )
            if 'Electivire':
                root.pokesets['Electivire'] = pokemon_ddl.PokemonSet(
                    name='Electivire', species='Electivire', abilities=('Motor Drive',), pkTypes=('Electric',),
                    sets=(), baseStats=(75, 123, 67, 95, 85, 95), genders=('M', 'F')
                )
            if 'Arceus-Electric':
                root.pokesets['Arceus-Electric'] = pokemon_ddl.PokemonSet(
                    name='Arceus-Electric', species='Arceus', abilities=('Multitype',), pkTypes=('Electric',),
                    sets=(), baseStats=(120, 120, 120, 120, 120, 120), genders=('',)
                )

        # Rock type pokemon
        if 'Rock':
            if 'Golem':
                root.pokesets['Golem'] = pokemon_ddl.PokemonSet(
                    name='Golem', species='Golem', abilities=('Rock Head', 'Sturdy'), pkTypes=('Rock', 'Ground'),
                    sets=(), baseStats=(80, 110, 130, 55, 65, 45), genders=('M', 'F')
                )
            if 'Omastar':
                root.pokesets['Omastar'] = pokemon_ddl.PokemonSet(
                    name='Omastar', species='Omastar', abilities=('Swift Swim', 'Shell Armor'),
                    pkTypes=('Rock', 'Water'),
                    sets=(), baseStats=(70, 60, 125, 115, 70, 55), genders=('M', 'F')
                )
            if 'Kabutops':
                root.pokesets['Kabutops'] = pokemon_ddl.PokemonSet(
                    name='Kabutops', species='Kabutops', abilities=('Swift Swim', 'Battle Armor'),
                    pkTypes=('Rock', 'Water'),
                    sets=(), baseStats=(60, 115, 105, 65, 70, 80), genders=('M', 'F')
                )
            if 'Aerodactyl':
                root.pokesets['Aerodactyl'] = pokemon_ddl.PokemonSet(
                    name='Aerodactyl', species='Aerodactyl', abilities=('Rock Head', 'Pressure'),
                    pkTypes=('Rock', 'Flying'),
                    sets=(), baseStats=(80, 105, 65, 60, 75, 130), genders=('M', 'F')
                )
            if 'Sudowoodo':
                root.pokesets['Sudowoodo'] = pokemon_ddl.PokemonSet(
                    name='Sudowoodo', species='Sudowoodo', abilities=('Sturdy', 'Rock Head'), pkTypes=('Rock',),
                    sets=(), baseStats=(70, 100, 115, 30, 65, 30), genders=('M', 'F')
                )
            if 'Shuckle':
                root.pokesets['Shuckle'] = pokemon_ddl.PokemonSet(
                    name='Shuckle', species='Shuckle', abilities=('Sturdy', 'Gluttony'), pkTypes=('Bug', 'Rock'),
                    sets=(), baseStats=(20, 10, 230, 10, 230, 5), genders=('M', 'F')
                )
            if 'Corsola':
                root.pokesets['Corsola'] = pokemon_ddl.PokemonSet(
                    name='Corsola', species='Corsola', abilities=('Hustle', 'Natural Cure'), pkTypes=('Water', 'Rock'),
                    sets=(), baseStats=(55, 55, 85, 65, 85, 35), genders=('M', 'F')
                )
            if 'Lunatone':
                root.pokesets['Lunatone'] = pokemon_ddl.PokemonSet(
                    name='Lunatone', species='Lunatone', abilities=('Levitate',), pkTypes=('Rock', 'Psychic'),
                    sets=(), baseStats=(70, 55, 65, 95, 85, 70), genders=('',)
                )
            if 'Solrock':
                root.pokesets['Solrock'] = pokemon_ddl.PokemonSet(
                    name='Solrock', species='Solrock', abilities=('Levitate',), pkTypes=('Rock', 'Psychic'),
                    sets=(), baseStats=(70, 95, 85, 55, 65, 70), genders=('',)
                )
            if 'Cradily':
                root.pokesets['Cradily'] = pokemon_ddl.PokemonSet(
                    name='Cradily', species='Cradily', abilities=('Suction Cups',), pkTypes=('Rock', 'Grass'),
                    sets=(), baseStats=(86, 81, 97, 81, 107, 43), genders=('M', 'F')
                )
            if 'Armaldo':
                root.pokesets['Armaldo'] = pokemon_ddl.PokemonSet(
                    name='Armaldo', species='Armaldo', abilities=('Battle Armor',), pkTypes=('Rock', 'Bug'),
                    sets=(), baseStats=(75, 125, 100, 70, 80, 45), genders=('M', 'F')
                )
            if 'Relicanth':
                root.pokesets['Relicanth'] = pokemon_ddl.PokemonSet(
                    name='Relicanth', species='Relicanth', abilities=('Swift Swim', 'Rock Head'),
                    pkTypes=('Water', 'Rock'),
                    sets=(), baseStats=(100, 90, 130, 45, 65, 55), genders=('M', 'F')
                )
            if 'Regirock':
                root.pokesets['Regirock'] = pokemon_ddl.PokemonSet(
                    name='Regirock', species='Regirock', abilities=('Clear Body',), pkTypes=('Rock',),
                    sets=(), baseStats=(80, 100, 200, 50, 100, 50), genders=('',)
                )
            if 'Rampardos':
                root.pokesets['Rampardos'] = pokemon_ddl.PokemonSet(
                    name='Rampardos', species='Rampardos', abilities=('Mold Breaker',), pkTypes=('Rock',),
                    sets=(), baseStats=(97, 165, 60, 65, 50, 58), genders=('M', 'F')
                )
            if 'Rhyperior':
                root.pokesets['Rhyperior'] = pokemon_ddl.PokemonSet(
                    name='Rhyperior', species='Rhyperior', abilities=('Lightning Rod', 'Solid Rock'),
                    pkTypes=('Rock', 'Ground'),
                    sets=(), baseStats=(115, 140, 130, 55, 55, 40), genders=('M', 'F')
                )
            if 'Arceus-Rock':
                root.pokesets['Arceus-Rock'] = pokemon_ddl.PokemonSet(
                    name='Arceus-Rock', species='Arceus', abilities=('Multitype',), pkTypes=('Rock',),
                    sets=(), baseStats=(120, 120, 120, 120, 120, 120), genders=('',)
                )

        # Poison type pokemon
        if 'Poison':
            if 'Venusaur':
                root.pokesets['Venusaur'] = pokemon_ddl.PokemonSet(
                    name='Venusaur', species='Venusaur', abilities=('Overgrow',), pkTypes=('Grass', 'Poison'),
                    sets=(), baseStats=(80, 82, 83, 100, 100, 80), genders=('M', 'F')
                )
            if 'Beedrill':
                root.pokesets['Beedrill'] = pokemon_ddl.PokemonSet(
                    name='Beedrill', species='Beedrill', abilities=('Swarm',), pkTypes=('Bug', 'Poison'),
                    sets=(), baseStats=(65, 80, 40, 45, 80, 75), genders=('M', 'F')
                )
            if 'Arbok':
                root.pokesets['Arbok'] = pokemon_ddl.PokemonSet(
                    name='Arbok', species='Arbok', abilities=('Intimidate', 'Shed Skin'), pkTypes=('Poison',),
                    sets=(), baseStats=(60, 85, 69, 65, 79, 80), genders=('M', 'F')
                )
            if 'Nidoqueen':
                root.pokesets['Nidoqueen'] = pokemon_ddl.PokemonSet(
                    name='Nidoqueen', species='Nidoqueen', abilities=('Poison Point', 'Rivalry'),
                    pkTypes=('Poison', 'Ground'),
                    sets=(), baseStats=(90, 82, 87, 75, 85, 76), genders=('F',)
                )
            if 'Nidoking':
                root.pokesets['Nidoking'] = pokemon_ddl.PokemonSet(
                    name='Nidoking', species='Nidoking', abilities=('Poison Point', 'Rivalry'),
                    pkTypes=('Poison', 'Ground'),
                    sets=(), baseStats=(81, 92, 77, 85, 75, 85), genders=('M',)
                )
            if 'Vileplume':
                root.pokesets['Vileplume'] = pokemon_ddl.PokemonSet(
                    name='Vileplume', species='Vileplume', abilities=('Chlorophyll',), pkTypes=('Grass', 'Poison'),
                    sets=(), baseStats=(75, 80, 85, 100, 90, 50), genders=('M', 'F')
                )
            if 'Venomoth':
                root.pokesets['Venomoth'] = pokemon_ddl.PokemonSet(
                    name='Venomoth', species='Venomoth', abilities=('Shield Dust', 'Tinted Lens'),
                    pkTypes=('Bug', 'Poison'),
                    sets=(), baseStats=(70, 65, 60, 90, 75, 90), genders=('M', 'F')
                )
            if 'Victreebel':
                root.pokesets['Victreebel'] = pokemon_ddl.PokemonSet(
                    name='Victreebel', species='Victreebel', abilities=('Chlorophyll',), pkTypes=('Grass', 'Poison'),
                    sets=(), baseStats=(80, 105, 65, 100, 60, 70), genders=('M', 'F')
                )
            if 'Tentacruel':
                root.pokesets['Tentacruel'] = pokemon_ddl.PokemonSet(
                    name='Tentacruel', species='Tentacruel', abilities=('Clear Body', 'Liquid Ooze'),
                    pkTypes=('Water', 'Poison'),
                    sets=(), baseStats=(80, 70, 65, 80, 120, 100), genders=('M', 'F')
                )
            if 'Muk':
                root.pokesets['Muk'] = pokemon_ddl.PokemonSet(
                    name='Muk', species='Muk', abilities=('Stench', 'Sticky Hold'), pkTypes=('Poison',),
                    sets=(), baseStats=(105, 105, 75, 65, 100, 50), genders=('M', 'F')
                )
            if 'Weezing':
                root.pokesets['Weezing'] = pokemon_ddl.PokemonSet(
                    name='Weezing', species='Weezing', abilities=('Levitate',), pkTypes=('Poison',),
                    sets=(), baseStats=(65, 90, 120, 85, 70, 60), genders=('M', 'F')
                )
            if 'Ariados':
                root.pokesets['Ariados'] = pokemon_ddl.PokemonSet(
                    name='Ariados', species='Ariados', abilities=('Swarm', 'Insomnia'), pkTypes=('Bug', 'Poison'),
                    sets=(), baseStats=(70, 90, 70, 60, 60, 40), genders=('M', 'F')
                )
            if 'Crobat':
                root.pokesets['Crobat'] = pokemon_ddl.PokemonSet(
                    name='Crobat', species='Crobat', abilities=('Inner Focus',), pkTypes=('Poison', 'Flying'),
                    sets=(), baseStats=(85, 90, 80, 70, 80, 130), genders=('M', 'F')
                )
            if 'Dustox':
                root.pokesets['Dustox'] = pokemon_ddl.PokemonSet(
                    name='Dustox', species='Dustox', abilities=('Shield Dust',), pkTypes=('Bug', 'Poison'),
                    sets=(), baseStats=(60, 50, 70, 50, 90, 65), genders=('M', 'F')
                )
            if 'Swalot':
                root.pokesets['Swalot'] = pokemon_ddl.PokemonSet(
                    name='Swalot', species='Swalot', abilities=('Liquid Ooze', 'Sticky Hold'), pkTypes=('Poison',),
                    sets=(), baseStats=(100, 73, 83, 73, 83, 55), genders=('M', 'F')
                )
            if 'Seviper':
                root.pokesets['Seviper'] = pokemon_ddl.PokemonSet(
                    name='Seviper', species='Seviper', abilities=('Shed Skin',), pkTypes=('Poison',),
                    sets=(), baseStats=(73, 100, 60, 100, 60, 65), genders=('M', 'F')
                )
            if 'Roserade':
                root.pokesets['Roserade'] = pokemon_ddl.PokemonSet(
                    name='Roserade', species='Roserade', abilities=('Natural Cure', 'Poison Point'),
                    pkTypes=('Grass', 'Poison'),
                    sets=(), baseStats=(60, 70, 55, 125, 105, 90), genders=('M', 'F')
                )
            if 'Arceus-Poison':
                root.pokesets['Arceus-Poison'] = pokemon_ddl.PokemonSet(
                    name='Arceus-Poison', species='Arceus', abilities=('Multitype',), pkTypes=('Poison',),
                    sets=(), baseStats=(120, 120, 120, 120, 120, 120), genders=('',)
                )

        # Ground type pokemon
        if 'Ground':
            if 'Sandslash':
                root.pokesets['Sandslash'] = pokemon_ddl.PokemonSet(
                    name='Sandslash', species='Sandslash', abilities=('Sand Veil',), pkTypes=('Ground',),
                    sets=(), baseStats=(75, 100, 110, 45, 55, 65), genders=('M', 'F')
                )
            if 'Dugtrio':
                root.pokesets['Dugtrio'] = pokemon_ddl.PokemonSet(
                    name='Dugtrio', species='Dugtrio', abilities=('Sand Veil', 'Arena Trap'), pkTypes=('Ground',),
                    sets=(), baseStats=(35, 80, 50, 50, 70, 120), genders=('M', 'F')
                )
            if 'Marowak':
                root.pokesets['Marowak'] = pokemon_ddl.PokemonSet(
                    name='Marowak', species='Marowak', abilities=('Rock Head', 'Lightning Rod'), pkTypes=('Ground',),
                    sets=(), baseStats=(60, 80, 110, 50, 80, 45), genders=('M', 'F')
                )
            if 'Quagsire':
                root.pokesets['Quagsire'] = pokemon_ddl.PokemonSet(
                    name='Quagsire', species='Quagsire', abilities=('Damp', 'Water Absorb'),
                    pkTypes=('Water', 'Ground'),
                    sets=(), baseStats=(95, 85, 85, 65, 65, 35), genders=('M', 'F')
                )
            if 'Donphan':
                root.pokesets['Donphan'] = pokemon_ddl.PokemonSet(
                    name='Donphan', species='Donphan', abilities=('Sturdy',), pkTypes=('Ground',),
                    sets=(), baseStats=(90, 120, 120, 60, 60, 50), genders=('M', 'F')
                )
            if 'Swampert':
                root.pokesets['Swampert'] = pokemon_ddl.PokemonSet(
                    name='Swampert', species='Swampert', abilities=('Torrent',), pkTypes=('Water', 'Ground'),
                    sets=(), baseStats=(100, 110, 90, 85, 90, 60), genders=('M', 'F')
                )
            if 'Whiscash':
                root.pokesets['Whiscash'] = pokemon_ddl.PokemonSet(
                    name='Whiscash', species='Whiscash', abilities=('Oblivious', 'Anticipation'),
                    pkTypes=('Water', 'Ground'),
                    sets=(), baseStats=(110, 78, 73, 76, 71, 60), genders=('M', 'F')
                )
            if 'Claydol':
                root.pokesets['Claydol'] = pokemon_ddl.PokemonSet(
                    name='Claydol', species='Claydol', abilities=('Levitate',), pkTypes=('Ground', 'Psychic'),
                    sets=(), baseStats=(60, 70, 105, 70, 120, 75), genders=('',)
                )
            if 'Groudon':
                root.pokesets['Groudon'] = pokemon_ddl.PokemonSet(
                    name='Groudon', species='Groudon', abilities=('Drought',), pkTypes=('Ground',),
                    sets=(), baseStats=(100, 150, 140, 100, 90, 90), genders=('',)
                )
            if 'Torterra':
                root.pokesets['Torterra'] = pokemon_ddl.PokemonSet(
                    name='Torterra', species='Torterra', abilities=('Overgrow',), pkTypes=('Grass', 'Ground'),
                    sets=(), baseStats=(95, 109, 105, 75, 85, 56), genders=('M', 'F')
                )
            if 'Wormadam-Sandy':
                root.pokesets['Wormadam-Sandy'] = pokemon_ddl.PokemonSet(
                    name='Wormadam-Sandy', species='Wormadam', abilities=('Anticipation',), pkTypes=('Bug', 'Ground'),
                    sets=(), baseStats=(60, 79, 105, 59, 85, 36), genders=('F',)
                )
            if 'Gastrodon':
                root.pokesets['Gastrodon'] = pokemon_ddl.PokemonSet(
                    name='Gastrodon', species='Gastrodon', abilities=('Sticky Hold', 'Storm Drain'),
                    pkTypes=('Water', 'Ground'),
                    sets=(), baseStats=(111, 83, 68, 92, 82, 39), genders=('M', 'F')
                )
            if 'Gastrodon-East':
                root.pokesets['Gastrodon-East'] = pokemon_ddl.PokemonSet(
                    name='Gastrodon-East', species='Gastrodon', abilities=('Sticky Hold', 'Storm Drain'),
                    pkTypes=('Water', 'Ground'),
                    sets=(), baseStats=(111, 83, 68, 92, 82, 39), genders=('M', 'F')
                )
            if 'Garchomp':
                root.pokesets['Garchomp'] = pokemon_ddl.PokemonSet(
                    name='Garchomp', species='Garchomp', abilities=('Sand Veil',), pkTypes=('Dragon', 'Ground'),
                    sets=(), baseStats=(108, 130, 95, 80, 85, 102), genders=('M', 'F')
                )
            if 'Hippowdon':
                root.pokesets['Hippowdon'] = pokemon_ddl.PokemonSet(
                    name='Hippowdon', species='Hippowdon', abilities=('Sand Stream',), pkTypes=('Ground',),
                    sets=(), baseStats=(108, 112, 118, 68, 72, 47), genders=('M', 'F')
                )
            if 'Gliscor':
                root.pokesets['Gliscor'] = pokemon_ddl.PokemonSet(
                    name='Gliscor', species='Gliscor', abilities=('Hyper Cutter', 'Sand Veil'),
                    pkTypes=('Ground', 'Flying'),
                    sets=(), baseStats=(75, 95, 125, 45, 75, 95), genders=('M', 'F')
                )
            if 'Arceus-Ground':
                root.pokesets['Arceus-Ground'] = pokemon_ddl.PokemonSet(
                    name='Arceus-Ground', species='Arceus', abilities=('Multitype',), pkTypes=('Ground',),
                    sets=(), baseStats=(120, 120, 120, 120, 120, 120), genders=('',)
                )

        # Bug type pokemon
        if 'Bug':
            if 'Butterfree':
                root.pokesets['Butterfree'] = pokemon_ddl.PokemonSet(
                    name='Butterfree', species='Butterfree', abilities=('Compound Eyes',), pkTypes=('Bug', 'Flying'),
                    sets=(), baseStats=(60, 45, 50, 80, 80, 70), genders=('M', 'F')
                )
            if 'Parasect':
                root.pokesets['Parasect'] = pokemon_ddl.PokemonSet(
                    name='Parasect', species='Parasect', abilities=('Effect Spore', 'Dry Skin'),
                    pkTypes=('Bug', 'Grass'),
                    sets=(), baseStats=(60, 95, 80, 60, 80, 30), genders=('M', 'F')
                )
            if 'Pinsir':
                root.pokesets['Pinsir'] = pokemon_ddl.PokemonSet(
                    name='Pinsir', species='Pinsir', abilities=('Hyper Cutter', 'Mold Breaker'), pkTypes=('Bug',),
                    sets=(), baseStats=(65, 125, 100, 55, 70, 85), genders=('M', 'F')
                )
            if 'Ledian':
                root.pokesets['Ledian'] = pokemon_ddl.PokemonSet(
                    name='Ledian', species='Ledian', abilities=('Swarm', 'Early Bird'), pkTypes=('Bug', 'Flying'),
                    sets=(), baseStats=(55, 35, 50, 55, 110, 85), genders=('M', 'F')
                )
            if 'Beautifly':
                root.pokesets['Beautifly'] = pokemon_ddl.PokemonSet(
                    name='Beautifly', species='Beautifly', abilities=('Swarm',), pkTypes=('Bug', 'Flying'),
                    sets=(), baseStats=(60, 70, 50, 90, 50, 65), genders=('M', 'F')
                )
            if 'Masquerain':
                root.pokesets['Masquerain'] = pokemon_ddl.PokemonSet(
                    name='Masquerain', species='Masquerain', abilities=('Intimidate',), pkTypes=('Bug', 'Flying'),
                    sets=(), baseStats=(70, 60, 62, 80, 82, 60), genders=('M', 'F')
                )
            if 'Ninjask':
                root.pokesets['Ninjask'] = pokemon_ddl.PokemonSet(
                    name='Ninjask', species='Ninjask', abilities=('Speed Boost',), pkTypes=('Bug', 'Flying'),
                    sets=(), baseStats=(61, 90, 45, 50, 50, 160), genders=('M', 'F')
                )
            if 'Volbeat':
                root.pokesets['Volbeat'] = pokemon_ddl.PokemonSet(
                    name='Volbeat', species='Volbeat', abilities=('Illuminate', 'Swarm'), pkTypes=('Bug',),
                    sets=(), baseStats=(65, 73, 55, 47, 75, 85), genders=('M',)
                )
            if 'Illumise':
                root.pokesets['Illumise'] = pokemon_ddl.PokemonSet(
                    name='Illumise', species='Illumise', abilities=('Oblivious', 'Tinted Lens'), pkTypes=('Bug',),
                    sets=(), baseStats=(65, 47, 55, 73, 75, 85), genders=('F',)
                )
            if 'Kricketune':
                root.pokesets['Kricketune'] = pokemon_ddl.PokemonSet(
                    name='Kricketune', species='Kricketune', abilities=('Swarm',), pkTypes=('Bug',),
                    sets=(), baseStats=(77, 85, 51, 55, 51, 65), genders=('M', 'F')
                )
            if 'Wormadam':
                root.pokesets['Wormadam'] = pokemon_ddl.PokemonSet(
                    name='Wormadam', species='Wormadam', abilities=('Anticipation',), pkTypes=('Bug', 'Grass'),
                    sets=(), baseStats=(60, 59, 85, 79, 105, 36), genders=('F',)
                )
            if 'Mothim':
                root.pokesets['Mothim'] = pokemon_ddl.PokemonSet(
                    name='Mothim', species='Mothim', abilities=('Swarm',), pkTypes=('Bug', 'Flying'),
                    sets=(), baseStats=(70, 94, 50, 94, 50, 66), genders=('M',)
                )
            if 'Vespiquen':
                root.pokesets['Vespiquen'] = pokemon_ddl.PokemonSet(
                    name='Vespiquen', species='Vespiquen', abilities=('Pressure',), pkTypes=('Bug', 'Flying'),
                    sets=(), baseStats=(70, 80, 102, 80, 102, 40), genders=('F',)
                )
            if 'Yanmega':
                root.pokesets['Yanmega'] = pokemon_ddl.PokemonSet(
                    name='Yanmega', species='Yanmega', abilities=('Speed Boost', 'Tinted Lens'),
                    pkTypes=('Bug', 'Flying'),
                    sets=(), baseStats=(86, 76, 86, 116, 56, 95), genders=('M', 'F')
                )
            if 'Arceus-Bug':
                root.pokesets['Arceus-Bug'] = pokemon_ddl.PokemonSet(
                    name='Arceus-Bug', species='Arceus', abilities=('Multitype',), pkTypes=('Bug',),
                    sets=(), baseStats=(120, 120, 120, 120, 120, 120), genders=('',)
                )

        # Grass type pokemon
        if 'Grass':
            if 'Exeggutor':
                root.pokesets['Exeggutor'] = pokemon_ddl.PokemonSet(
                    name='Exeggutor', species='Exeggutor', abilities=('Chlorophyll',), pkTypes=('Grass', 'Psychic'),
                    sets=(), baseStats=(95, 95, 85, 125, 65, 55), genders=('M', 'F')
                )
            if 'Meganium':
                root.pokesets['Meganium'] = pokemon_ddl.PokemonSet(
                    name='Meganium', species='Meganium', abilities=('Overgrow',), pkTypes=('Grass',),
                    sets=(), baseStats=(80, 82, 100, 83, 100, 80), genders=('M', 'F')
                )
            if 'Bellossom':
                root.pokesets['Bellossom'] = pokemon_ddl.PokemonSet(
                    name='Bellossom', species='Bellossom', abilities=('Chlorophyll',), pkTypes=('Grass',),
                    sets=(), baseStats=(75, 80, 85, 90, 100, 50), genders=('M', 'F')
                )
            if 'Jumpluff':
                root.pokesets['Jumpluff'] = pokemon_ddl.PokemonSet(
                    name='Jumpluff', species='Jumpluff', abilities=('Chlorophyll', 'Leaf Guard'),
                    pkTypes=('Grass', 'Flying'),
                    sets=(), baseStats=(75, 55, 70, 55, 85, 110), genders=('M', 'F')
                )
            if 'Sunflora':
                root.pokesets['Sunflora'] = pokemon_ddl.PokemonSet(
                    name='Sunflora', species='Sunflora', abilities=('Chlorophyll', 'Solar Power'), pkTypes=('Grass',),
                    sets=(), baseStats=(75, 75, 55, 105, 85, 30), genders=('M', 'F')
                )
            if 'Celebi':
                root.pokesets['Celebi'] = pokemon_ddl.PokemonSet(
                    name='Celebi', species='Celebi', abilities=('Natural Cure',), pkTypes=('Psychic', 'Grass'),
                    sets=(), baseStats=(100, 100, 100, 100, 100, 100), genders=('',)
                )
            if 'Sceptile':
                root.pokesets['Sceptile'] = pokemon_ddl.PokemonSet(
                    name='Sceptile', species='Sceptile', abilities=('Overgrow',), pkTypes=('Grass',),
                    sets=(), baseStats=(70, 85, 65, 105, 85, 120), genders=('M', 'F')
                )
            if 'Ludicolo':
                root.pokesets['Ludicolo'] = pokemon_ddl.PokemonSet(
                    name='Ludicolo', species='Ludicolo', abilities=('Swift Swim', 'Rain Dish'),
                    pkTypes=('Water', 'Grass'),
                    sets=(), baseStats=(80, 70, 70, 90, 100, 70), genders=('M', 'F')
                )
            if 'Tropius':
                root.pokesets['Tropius'] = pokemon_ddl.PokemonSet(
                    name='Tropius', species='Tropius', abilities=('Chlorophyll', 'Solar Power'),
                    pkTypes=('Grass', 'Flying'),
                    sets=(), baseStats=(99, 68, 83, 72, 87, 51), genders=('M', 'F')
                )
            if 'Cherrim':
                root.pokesets['Cherrim'] = pokemon_ddl.PokemonSet(
                    name='Cherrim', species='Cherrim', abilities=('Flower Gift',), pkTypes=('Grass',),
                    sets=(), baseStats=(70, 60, 70, 87, 78, 85), genders=('M', 'F')
                )
            if 'Carnivine':
                root.pokesets['Carnivine'] = pokemon_ddl.PokemonSet(
                    name='Carnivine', species='Carnivine', abilities=('Levitate',), pkTypes=('Grass',),
                    sets=(), baseStats=(74, 100, 72, 90, 72, 46), genders=('M', 'F')
                )
            if 'Tangrowth':
                root.pokesets['Tangrowth'] = pokemon_ddl.PokemonSet(
                    name='Tangrowth', species='Tangrowth', abilities=('Chlorophyll', 'Leaf Guard'), pkTypes=('Grass',),
                    sets=(), baseStats=(100, 100, 125, 110, 50, 50), genders=('M', 'F')
                )
            if 'Leafeon':
                root.pokesets['Leafeon'] = pokemon_ddl.PokemonSet(
                    name='Leafeon', species='Leafeon', abilities=('Leaf Guard',), pkTypes=('Grass',),
                    sets=(), baseStats=(65, 110, 130, 60, 65, 95), genders=('M', 'F')
                )
            if 'Shaymin':
                root.pokesets['Shaymin'] = pokemon_ddl.PokemonSet(
                    name='Shaymin', species='Shaymin', abilities=('Natural Cure',), pkTypes=('Grass',),
                    sets=(), baseStats=(100, 100, 100, 100, 100, 100), genders=('',)
                )
            if 'Arceus-Grass':
                root.pokesets['Arceus-Grass'] = pokemon_ddl.PokemonSet(
                    name='Arceus-Grass', species='Arceus', abilities=('Multitype',), pkTypes=('Grass',),
                    sets=(), baseStats=(120, 120, 120, 120, 120, 120), genders=('',)
                )

        # Psychic type pokemon
        if 'Psychic':
            if 'Alakazam':
                root.pokesets['Alakazam'] = pokemon_ddl.PokemonSet(
                    name='Alakazam', species='Alakazam', abilities=('Synchronize', 'Inner Focus'), pkTypes=('Psychic',),
                    sets=(), baseStats=(55, 50, 45, 135, 85, 120), genders=('M', 'F')
                )
            if 'Slowbro':
                root.pokesets['Slowbro'] = pokemon_ddl.PokemonSet(
                    name='Slowbro', species='Slowbro', abilities=('Oblivious', 'Own Tempo'),
                    pkTypes=('Water', 'Psychic'),
                    sets=(), baseStats=(95, 75, 110, 100, 80, 30), genders=('M', 'F')
                )
            if 'Hypno':
                root.pokesets['Hypno'] = pokemon_ddl.PokemonSet(
                    name='Hypno', species='Hypno', abilities=('Insomnia', 'Forewarn'), pkTypes=('Psychic',),
                    sets=(), baseStats=(85, 73, 70, 73, 115, 67), genders=('M', 'F')
                )
            if 'Starmie':
                root.pokesets['Starmie'] = pokemon_ddl.PokemonSet(
                    name='Starmie', species='Starmie', abilities=('Illuminate', 'Natural Cure'),
                    pkTypes=('Water', 'Psychic'),
                    sets=(), baseStats=(60, 75, 85, 100, 85, 115), genders=('',)
                )
            if 'Mr. Mime':
                root.pokesets['Mr. Mime'] = pokemon_ddl.PokemonSet(
                    name='Mr. Mime', species='Mr. Mime', abilities=('Soundproof', 'Filter'), pkTypes=('Psychic',),
                    sets=(), baseStats=(40, 45, 65, 100, 120, 90), genders=('M', 'F')
                )
            if 'Mewtwo':
                root.pokesets['Mewtwo'] = pokemon_ddl.PokemonSet(
                    name='Mewtwo', species='Mewtwo', abilities=('Pressure',), pkTypes=('Psychic',),
                    sets=(), baseStats=(106, 110, 90, 154, 90, 130), genders=('',)
                )
            if 'Mew':
                root.pokesets['Mew'] = pokemon_ddl.PokemonSet(
                    name='Mew', species='Mew', abilities=('Synchronize',), pkTypes=('Psychic',),
                    sets=(), baseStats=(100, 100, 100, 100, 100, 100), genders=('',)
                )
            if 'Xatu':
                root.pokesets['Xatu'] = pokemon_ddl.PokemonSet(
                    name='Xatu', species='Xatu', abilities=('Synchronize', 'Early Bird'), pkTypes=('Psychic', 'Flying'),
                    sets=(), baseStats=(65, 75, 70, 95, 70, 95), genders=('M', 'F')
                )
            if 'Espeon':
                root.pokesets['Espeon'] = pokemon_ddl.PokemonSet(
                    name='Espeon', species='Espeon', abilities=('Synchronize',), pkTypes=('Psychic',),
                    sets=(), baseStats=(65, 65, 60, 130, 95, 110), genders=('M', 'F')
                )
            if 'Slowking':
                root.pokesets['Slowking'] = pokemon_ddl.PokemonSet(
                    name='Slowking', species='Slowking', abilities=('Oblivious', 'Own Tempo'),
                    pkTypes=('Water', 'Psychic'),
                    sets=(), baseStats=(95, 75, 80, 100, 110, 30), genders=('M', 'F')
                )
            if 'Unown':
                root.pokesets['Unown'] = pokemon_ddl.PokemonSet(
                    name='Unown', species='Unown', abilities=('Levitate',), pkTypes=('Psychic',),
                    sets=(), baseStats=(48, 72, 48, 72, 48, 48), genders=('',)
                )
            if 'Wobbuffet':
                root.pokesets['Wobbuffet'] = pokemon_ddl.PokemonSet(
                    name='Wobbuffet', species='Wobbuffet', abilities=('Shadow Tag',), pkTypes=('Psychic',),
                    sets=(), baseStats=(190, 33, 58, 33, 58, 33), genders=('M', 'F')
                )
            if 'Girafarig':
                root.pokesets['Girafarig'] = pokemon_ddl.PokemonSet(
                    name='Girafarig', species='Girafarig', abilities=('Inner Focus', 'Early Bird'),
                    pkTypes=('Normal', 'Psychic'),
                    sets=(), baseStats=(70, 80, 65, 90, 65, 85), genders=('M', 'F')
                )
            if 'Lugia':
                root.pokesets['Lugia'] = pokemon_ddl.PokemonSet(
                    name='Lugia', species='Lugia', abilities=('Pressure',), pkTypes=('Psychic', 'Flying'),
                    sets=(), baseStats=(106, 90, 130, 90, 154, 110), genders=('',)
                )
            if 'Gardevoir':
                root.pokesets['Gardevoir'] = pokemon_ddl.PokemonSet(
                    name='Gardevoir', species='Gardevoir', abilities=('Synchronize', 'Trace'), pkTypes=('Psychic',),
                    sets=(), baseStats=(68, 65, 65, 125, 115, 80), genders=('M', 'F')
                )
            if 'Grumpig':
                root.pokesets['Grumpig'] = pokemon_ddl.PokemonSet(
                    name='Grumpig', species='Grumpig', abilities=('Thick Fat', 'Own Tempo'), pkTypes=('Psychic',),
                    sets=(), baseStats=(80, 45, 65, 90, 110, 80), genders=('M', 'F')
                )
            if 'Chimecho':
                root.pokesets['Chimecho'] = pokemon_ddl.PokemonSet(
                    name='Chimecho', species='Chimecho', abilities=('Levitate',), pkTypes=('Psychic',),
                    sets=(), baseStats=(65, 50, 70, 95, 80, 65), genders=('M', 'F')
                )
            if 'Deoxys':
                root.pokesets['Deoxys'] = pokemon_ddl.PokemonSet(
                    name='Deoxys', species='Deoxys', abilities=('Pressure',), pkTypes=('Psychic',),
                    sets=(), baseStats=(50, 150, 50, 150, 50, 150), genders=('',)
                )
            if 'Deoxys-Attack':
                root.pokesets['Deoxys-Attack'] = pokemon_ddl.PokemonSet(
                    name='Deoxys-Attack', species='Deoxys', abilities=('Pressure',), pkTypes=('Psychic',),
                    sets=(), baseStats=(50, 180, 20, 180, 20, 150), genders=('',)
                )
            if 'Deoxys-Defense':
                root.pokesets['Deoxys-Defense'] = pokemon_ddl.PokemonSet(
                    name='Deoxys-Defense', species='Deoxys', abilities=('Pressure',), pkTypes=('Psychic',),
                    sets=(), baseStats=(50, 70, 160, 70, 160, 90), genders=('',)
                )
            if 'Deoxys-Speed':
                root.pokesets['Deoxys-Speed'] = pokemon_ddl.PokemonSet(
                    name='Deoxys-Speed', species='Deoxys', abilities=('Pressure',), pkTypes=('Psychic',),
                    sets=(), baseStats=(50, 95, 90, 95, 90, 180), genders=('',)
                )
            if 'Uxie':
                root.pokesets['Uxie'] = pokemon_ddl.PokemonSet(
                    name='Uxie', species='Uxie', abilities=('Levitate',), pkTypes=('Psychic',),
                    sets=(), baseStats=(75, 75, 130, 75, 130, 95), genders=('',)
                )
            if 'Mesprit':
                root.pokesets['Mesprit'] = pokemon_ddl.PokemonSet(
                    name='Mesprit', species='Mesprit', abilities=('Levitate',), pkTypes=('Psychic',),
                    sets=(), baseStats=(80, 105, 105, 105, 105, 80), genders=('',)
                )
            if 'Azelf':
                root.pokesets['Azelf'] = pokemon_ddl.PokemonSet(
                    name='Azelf', species='Azelf', abilities=('Levitate',), pkTypes=('Psychic',),
                    sets=(), baseStats=(75, 125, 70, 125, 70, 115), genders=('',)
                )
            if 'Cresselia':
                root.pokesets['Cresselia'] = pokemon_ddl.PokemonSet(
                    name='Cresselia', species='Cresselia', abilities=('Levitate',), pkTypes=('Psychic',),
                    sets=(), baseStats=(120, 70, 120, 75, 130, 85), genders=('F',)
                )
            if 'Arceus-Psychic':
                root.pokesets['Arceus-Psychic'] = pokemon_ddl.PokemonSet(
                    name='Arceus-Psychic', species='Arceus', abilities=('Multitype',), pkTypes=('Psychic',),
                    sets=(), baseStats=(120, 120, 120, 120, 120, 120), genders=('',)
                )

        # Flying type pokemon
        if 'Flying':
            if 'Pidgeot':
                root.pokesets['Pidgeot'] = pokemon_ddl.PokemonSet(
                    name='Pidgeot', species='Pidgeot', abilities=('Keen Eye', 'Tangled Feet'),
                    pkTypes=('Normal', 'Flying'),
                    sets=(), baseStats=(83, 80, 75, 70, 70, 91), genders=('M', 'F')
                )
            if 'Fearow':
                root.pokesets['Fearow'] = pokemon_ddl.PokemonSet(
                    name='Fearow', species='Fearow', abilities=('Keen Eye',), pkTypes=('Normal', 'Flying'),
                    sets=(), baseStats=(65, 90, 65, 61, 61, 100), genders=('M', 'F')
                )
            if "Farfetch'd":
                root.pokesets["Farfetch'd"] = pokemon_ddl.PokemonSet(
                    name="Farfetch'd", species="Farfetch'd", abilities=('Keen Eye', 'Inner Focus'),
                    pkTypes=('Normal', 'Flying'),
                    sets=(), baseStats=(52, 65, 55, 58, 62, 60), genders=('M', 'F')
                )
            if 'Dodrio':
                root.pokesets['Dodrio'] = pokemon_ddl.PokemonSet(
                    name='Dodrio', species='Dodrio', abilities=('Run Away', 'Early Bird'), pkTypes=('Normal', 'Flying'),
                    sets=(), baseStats=(60, 110, 70, 60, 60, 100), genders=('M', 'F')
                )
            if 'Gyarados':
                root.pokesets['Gyarados'] = pokemon_ddl.PokemonSet(
                    name='Gyarados', species='Gyarados', abilities=('Intimidate',), pkTypes=('Water', 'Flying'),
                    sets=(), baseStats=(95, 125, 79, 60, 100, 81), genders=('M', 'F')
                )
            if 'Noctowl':
                root.pokesets['Noctowl'] = pokemon_ddl.PokemonSet(
                    name='Noctowl', species='Noctowl', abilities=('Insomnia', 'Keen Eye'), pkTypes=('Normal', 'Flying'),
                    sets=(), baseStats=(100, 50, 50, 76, 96, 70), genders=('M', 'F')
                )
            if 'Mantine':
                root.pokesets['Mantine'] = pokemon_ddl.PokemonSet(
                    name='Mantine', species='Mantine', abilities=('Swift Swim', 'Water Absorb'),
                    pkTypes=('Water', 'Flying'),
                    sets=(), baseStats=(65, 40, 70, 80, 140, 70), genders=('M', 'F')
                )
            if 'Swellow':
                root.pokesets['Swellow'] = pokemon_ddl.PokemonSet(
                    name='Swellow', species='Swellow', abilities=('Guts',), pkTypes=('Normal', 'Flying'),
                    sets=(), baseStats=(60, 85, 60, 50, 50, 125), genders=('M', 'F')
                )
            if 'Pelipper':
                root.pokesets['Pelipper'] = pokemon_ddl.PokemonSet(
                    name='Pelipper', species='Pelipper', abilities=('Keen Eye',), pkTypes=('Water', 'Flying'),
                    sets=(), baseStats=(60, 50, 100, 85, 70, 65), genders=('M', 'F')
                )
            if 'Altaria':
                root.pokesets['Altaria'] = pokemon_ddl.PokemonSet(
                    name='Altaria', species='Altaria', abilities=('Natural Cure',), pkTypes=('Dragon', 'Flying'),
                    sets=(), baseStats=(75, 70, 90, 70, 105, 80), genders=('M', 'F')
                )
            if 'Staraptor':
                root.pokesets['Staraptor'] = pokemon_ddl.PokemonSet(
                    name='Staraptor', species='Staraptor', abilities=('Intimidate',), pkTypes=('Normal', 'Flying'),
                    sets=(), baseStats=(85, 120, 70, 50, 50, 100), genders=('M', 'F')
                )
            if 'Chatot':
                root.pokesets['Chatot'] = pokemon_ddl.PokemonSet(
                    name='Chatot', species='Chatot', abilities=('Keen Eye', 'Tangled Feet'),
                    pkTypes=('Normal', 'Flying'),
                    sets=(), baseStats=(76, 65, 45, 92, 42, 91), genders=('M', 'F')
                )
            if 'Togekiss':
                root.pokesets['Togekiss'] = pokemon_ddl.PokemonSet(
                    name='Togekiss', species='Togekiss', abilities=('Hustle', 'Serene Grace'),
                    pkTypes=('Normal', 'Flying'),
                    sets=(), baseStats=(85, 50, 95, 120, 115, 80), genders=('M', 'F')
                )
            if 'Arceus-Flying':
                root.pokesets['Arceus-Flying'] = pokemon_ddl.PokemonSet(
                    name='Arceus-Flying', species='Arceus', abilities=('Multitype',), pkTypes=('Flying',),
                    sets=(), baseStats=(120, 120, 120, 120, 120, 120), genders=('',)
                )

        # Normal type pokemon
        if 'Normal':
            if 'Raticate':
                root.pokesets['Raticate'] = pokemon_ddl.PokemonSet(
                    name='Raticate', species='Raticate', abilities=('Run Away', 'Guts'), pkTypes=('Normal',),
                    sets=(), baseStats=(55, 81, 60, 50, 70, 97), genders=('M', 'F')
                )
            if 'Clefable':
                root.pokesets['Clefable'] = pokemon_ddl.PokemonSet(
                    name='Clefable', species='Clefable', abilities=('Cute Charm', 'Magic Guard'), pkTypes=('Normal',),
                    sets=(), baseStats=(95, 70, 73, 85, 90, 60), genders=('M', 'F')
                )
            if 'Wigglytuff':
                root.pokesets['Wigglytuff'] = pokemon_ddl.PokemonSet(
                    name='Wigglytuff', species='Wigglytuff', abilities=('Cute Charm', 'Competitive'),
                    pkTypes=('Normal',),
                    sets=(), baseStats=(140, 70, 45, 75, 50, 45), genders=('M', 'F')
                )
            if 'Persian':
                root.pokesets['Persian'] = pokemon_ddl.PokemonSet(
                    name='Persian', species='Persian', abilities=('Limber', 'Technician'), pkTypes=('Normal',),
                    sets=(), baseStats=(65, 70, 60, 65, 65, 115), genders=('M', 'F')
                )
            if 'Kangaskhan':
                root.pokesets['Kangaskhan'] = pokemon_ddl.PokemonSet(
                    name='Kangaskhan', species='Kangaskhan', abilities=('Early Bird', 'Scrappy'), pkTypes=('Normal',),
                    sets=(), baseStats=(105, 95, 80, 40, 80, 90), genders=('F',)
                )
            if 'Ditto':
                root.pokesets['Ditto'] = pokemon_ddl.PokemonSet(
                    name='Ditto', species='Ditto', abilities=('Limber',), pkTypes=('Normal',),
                    sets=(), baseStats=(48, 48, 48, 48, 48, 48), genders=('',)
                )
            if 'Tauros':
                root.pokesets['Tauros'] = pokemon_ddl.PokemonSet(
                    name='Tauros', species='Tauros', abilities=('Intimidate', 'Anger Point'), pkTypes=('Normal',),
                    sets=(), baseStats=(75, 100, 95, 40, 70, 110), genders=('M',)
                )
            if 'Snorlax':
                root.pokesets['Snorlax'] = pokemon_ddl.PokemonSet(
                    name='Snorlax', species='Snorlax', abilities=('Immunity', 'Thick Fat'), pkTypes=('Normal',),
                    sets=(), baseStats=(160, 110, 65, 65, 110, 30), genders=('M', 'F')
                )
            if 'Furret':
                root.pokesets['Furret'] = pokemon_ddl.PokemonSet(
                    name='Furret', species='Furret', abilities=('Run Away', 'Keen Eye'), pkTypes=('Normal',),
                    sets=(), baseStats=(85, 76, 64, 45, 55, 90), genders=('M', 'F')
                )
            if 'Dunsparce':
                root.pokesets['Dunsparce'] = pokemon_ddl.PokemonSet(
                    name='Dunsparce', species='Dunsparce', abilities=('Serene Grace', 'Run Away'), pkTypes=('Normal',),
                    sets=(), baseStats=(100, 70, 70, 65, 65, 45), genders=('M', 'F')
                )
            if 'Granbull':
                root.pokesets['Granbull'] = pokemon_ddl.PokemonSet(
                    name='Granbull', species='Granbull', abilities=('Intimidate', 'Quick Feet'), pkTypes=('Normal',),
                    sets=(), baseStats=(90, 120, 75, 60, 60, 45), genders=('M', 'F')
                )
            if 'Ursaring':
                root.pokesets['Ursaring'] = pokemon_ddl.PokemonSet(
                    name='Ursaring', species='Ursaring', abilities=('Guts', 'Quick Feet'), pkTypes=('Normal',),
                    sets=(), baseStats=(90, 130, 75, 75, 75, 55), genders=('M', 'F')
                )
            if 'Porygon2':
                root.pokesets['Porygon2'] = pokemon_ddl.PokemonSet(
                    name='Porygon2', species='Porygon2', abilities=('Trace', 'Download'), pkTypes=('Normal',),
                    sets=(), baseStats=(85, 80, 90, 105, 95, 60), genders=('',)
                )
            if 'Stantler':
                root.pokesets['Stantler'] = pokemon_ddl.PokemonSet(
                    name='Stantler', species='Stantler', abilities=('Intimidate', 'Frisk'), pkTypes=('Normal',),
                    sets=(), baseStats=(73, 95, 62, 85, 65, 85), genders=('M', 'F')
                )
            if 'Smeargle':
                root.pokesets['Smeargle'] = pokemon_ddl.PokemonSet(
                    name='Smeargle', species='Smeargle', abilities=('Own Tempo', 'Technician'), pkTypes=('Normal',),
                    sets=(), baseStats=(55, 20, 35, 20, 45, 75), genders=('M', 'F')
                )
            if 'Miltank':
                root.pokesets['Miltank'] = pokemon_ddl.PokemonSet(
                    name='Miltank', species='Miltank', abilities=('Thick Fat', 'Scrappy'), pkTypes=('Normal',),
                    sets=(), baseStats=(95, 80, 105, 40, 70, 100), genders=('F',)
                )
            if 'Blissey':
                root.pokesets['Blissey'] = pokemon_ddl.PokemonSet(
                    name='Blissey', species='Blissey', abilities=('Natural Cure', 'Serene Grace'), pkTypes=('Normal',),
                    sets=(), baseStats=(255, 10, 10, 75, 135, 55), genders=('F',)
                )
            if 'Linoone':
                root.pokesets['Linoone'] = pokemon_ddl.PokemonSet(
                    name='Linoone', species='Linoone', abilities=('Pickup', 'Gluttony'), pkTypes=('Normal',),
                    sets=(), baseStats=(78, 70, 61, 50, 61, 100), genders=('M', 'F')
                )
            if 'Slaking':
                root.pokesets['Slaking'] = pokemon_ddl.PokemonSet(
                    name='Slaking', species='Slaking', abilities=('Truant',), pkTypes=('Normal',),
                    sets=(), baseStats=(150, 160, 100, 95, 65, 100), genders=('M', 'F')
                )
            if 'Exploud':
                root.pokesets['Exploud'] = pokemon_ddl.PokemonSet(
                    name='Exploud', species='Exploud', abilities=('Soundproof',), pkTypes=('Normal',),
                    sets=(), baseStats=(104, 91, 63, 91, 63, 68), genders=('M', 'F')
                )
            if 'Delcatty':
                root.pokesets['Delcatty'] = pokemon_ddl.PokemonSet(
                    name='Delcatty', species='Delcatty', abilities=('Cute Charm', 'Normalize'), pkTypes=('Normal',),
                    sets=(), baseStats=(70, 65, 65, 55, 55, 70), genders=('M', 'F')
                )
            if 'Spinda':
                root.pokesets['Spinda'] = pokemon_ddl.PokemonSet(
                    name='Spinda', species='Spinda', abilities=('Own Tempo', 'Tangled Feet'), pkTypes=('Normal',),
                    sets=(), baseStats=(60, 60, 60, 60, 60, 60), genders=('M', 'F')
                )
            if 'Zangoose':
                root.pokesets['Zangoose'] = pokemon_ddl.PokemonSet(
                    name='Zangoose', species='Zangoose', abilities=('Immunity',), pkTypes=('Normal',),
                    sets=(), baseStats=(73, 115, 60, 60, 60, 90), genders=('M', 'F')
                )
            if 'Kecleon':
                root.pokesets['Kecleon'] = pokemon_ddl.PokemonSet(
                    name='Kecleon', species='Kecleon', abilities=('Color Change',), pkTypes=('Normal',),
                    sets=(), baseStats=(60, 90, 70, 60, 120, 40), genders=('M', 'F')
                )
            if 'Bibarel':
                root.pokesets['Bibarel'] = pokemon_ddl.PokemonSet(
                    name='Bibarel', species='Bibarel', abilities=('Simple', 'Unaware'), pkTypes=('Normal', 'Water'),
                    sets=(), baseStats=(79, 85, 60, 55, 60, 71), genders=('M', 'F')
                )
            if 'Ambipom':
                root.pokesets['Ambipom'] = pokemon_ddl.PokemonSet(
                    name='Ambipom', species='Ambipom', abilities=('Technician', 'Pickup'), pkTypes=('Normal',),
                    sets=(), baseStats=(75, 100, 66, 60, 66, 115), genders=('M', 'F')
                )
            if 'Lopunny':
                root.pokesets['Lopunny'] = pokemon_ddl.PokemonSet(
                    name='Lopunny', species='Lopunny', abilities=('Cute Charm', 'Klutz'), pkTypes=('Normal',),
                    sets=(), baseStats=(65, 76, 84, 54, 96, 105), genders=('M', 'F')
                )
            if 'Purugly':
                root.pokesets['Purugly'] = pokemon_ddl.PokemonSet(
                    name='Purugly', species='Purugly', abilities=('Thick Fat', 'Own Tempo'), pkTypes=('Normal',),
                    sets=(), baseStats=(71, 82, 64, 64, 59, 112), genders=('M', 'F')
                )
            if 'Lickilicky':
                root.pokesets['Lickilicky'] = pokemon_ddl.PokemonSet(
                    name='Lickilicky', species='Lickilicky', abilities=('Own Tempo', 'Oblivious'), pkTypes=('Normal',),
                    sets=(), baseStats=(110, 85, 95, 80, 95, 50), genders=('M', 'F')
                )
            if 'Porygon-Z':
                root.pokesets['Porygon-Z'] = pokemon_ddl.PokemonSet(
                    name='Porygon-Z', species='Porygon-Z', abilities=('Adaptability', 'Download'), pkTypes=('Normal',),
                    sets=(), baseStats=(85, 80, 70, 135, 75, 90), genders=('',)
                )
            if 'Regigigas':
                root.pokesets['Regigigas'] = pokemon_ddl.PokemonSet(
                    name='Regigigas', species='Regigigas', abilities=('Slow Start',), pkTypes=('Normal',),
                    sets=(), baseStats=(110, 160, 110, 80, 110, 100), genders=('',)
                )
            if 'Arceus':
                root.pokesets['Arceus'] = pokemon_ddl.PokemonSet(
                    name='Arceus', species='Arceus', abilities=('Multitype',), pkTypes=('Normal',),
                    sets=(), baseStats=(120, 120, 120, 120, 120, 120), genders=('',)
                )

        # Water type pokemon
        if 'Water':
            if 'Blastoise':
                root.pokesets['Blastoise'] = pokemon_ddl.PokemonSet(
                    name='Blastoise', species='Blastoise', abilities=('Torrent',), pkTypes=('Water',),
                    sets=(), baseStats=(79, 83, 100, 85, 105, 78), genders=('M', 'F')
                )
            if 'Golduck':
                root.pokesets['Golduck'] = pokemon_ddl.PokemonSet(
                    name='Golduck', species='Golduck', abilities=('Damp', 'Cloud Nine'), pkTypes=('Water',),
                    sets=(), baseStats=(80, 82, 78, 95, 80, 85), genders=('M', 'F')
                )
            if 'Kingler':
                root.pokesets['Kingler'] = pokemon_ddl.PokemonSet(
                    name='Kingler', species='Kingler', abilities=('Hyper Cutter', 'Shell Armor'), pkTypes=('Water',),
                    sets=(), baseStats=(55, 130, 115, 50, 50, 75), genders=('M', 'F')
                )
            if 'Seaking':
                root.pokesets['Seaking'] = pokemon_ddl.PokemonSet(
                    name='Seaking', species='Seaking', abilities=('Swift Swim', 'Water Veil'), pkTypes=('Water',),
                    sets=(), baseStats=(80, 92, 65, 65, 80, 68), genders=('M', 'F')
                )
            if 'Vaporeon':
                root.pokesets['Vaporeon'] = pokemon_ddl.PokemonSet(
                    name='Vaporeon', species='Vaporeon', abilities=('Water Absorb',), pkTypes=('Water',),
                    sets=(), baseStats=(130, 65, 60, 110, 95, 65), genders=('M', 'F')
                )
            if 'Feraligatr':
                root.pokesets['Feraligatr'] = pokemon_ddl.PokemonSet(
                    name='Feraligatr', species='Feraligatr', abilities=('Torrent',), pkTypes=('Water',),
                    sets=(), baseStats=(85, 105, 100, 79, 83, 78), genders=('M', 'F')
                )
            if 'Azumarill':
                root.pokesets['Azumarill'] = pokemon_ddl.PokemonSet(
                    name='Azumarill', species='Azumarill', abilities=('Thick Fat', 'Huge Power'), pkTypes=('Water',),
                    sets=(), baseStats=(100, 50, 80, 50, 80, 50), genders=('M', 'F')
                )
            if 'Politoed':
                root.pokesets['Politoed'] = pokemon_ddl.PokemonSet(
                    name='Politoed', species='Politoed', abilities=('Water Absorb', 'Damp'), pkTypes=('Water',),
                    sets=(), baseStats=(90, 75, 75, 90, 100, 70), genders=('M', 'F')
                )
            if 'Qwilfish':
                root.pokesets['Qwilfish'] = pokemon_ddl.PokemonSet(
                    name='Qwilfish', species='Qwilfish', abilities=('Poison Point', 'Swift Swim'),
                    pkTypes=('Water', 'Poison'),
                    sets=(), baseStats=(65, 95, 75, 55, 55, 85), genders=('M', 'F')
                )
            if 'Octillery':
                root.pokesets['Octillery'] = pokemon_ddl.PokemonSet(
                    name='Octillery', species='Octillery', abilities=('Suction Cups', 'Sniper'), pkTypes=('Water',),
                    sets=(), baseStats=(75, 105, 75, 105, 75, 45), genders=('M', 'F')
                )
            if 'Suicune':
                root.pokesets['Suicune'] = pokemon_ddl.PokemonSet(
                    name='Suicune', species='Suicune', abilities=('Pressure',), pkTypes=('Water',),
                    sets=(), baseStats=(100, 75, 115, 90, 115, 85), genders=('',)
                )
            if 'Wailord':
                root.pokesets['Wailord'] = pokemon_ddl.PokemonSet(
                    name='Wailord', species='Wailord', abilities=('Water Veil', 'Oblivious'), pkTypes=('Water',),
                    sets=(), baseStats=(170, 90, 45, 90, 45, 60), genders=('M', 'F')
                )
            if 'Milotic':
                root.pokesets['Milotic'] = pokemon_ddl.PokemonSet(
                    name='Milotic', species='Milotic', abilities=('Marvel Scale',), pkTypes=('Water',),
                    sets=(), baseStats=(95, 60, 79, 100, 125, 81), genders=('M', 'F')
                )
            if 'Huntail':
                root.pokesets['Huntail'] = pokemon_ddl.PokemonSet(
                    name='Huntail', species='Huntail', abilities=('Swift Swim',), pkTypes=('Water',),
                    sets=(), baseStats=(55, 104, 105, 94, 75, 52), genders=('M', 'F')
                )
            if 'Gorebyss':
                root.pokesets['Gorebyss'] = pokemon_ddl.PokemonSet(
                    name='Gorebyss', species='Gorebyss', abilities=('Swift Swim',), pkTypes=('Water',),
                    sets=(), baseStats=(55, 84, 105, 114, 75, 52), genders=('M', 'F')
                )
            if 'Luvdisc':
                root.pokesets['Luvdisc'] = pokemon_ddl.PokemonSet(
                    name='Luvdisc', species='Luvdisc', abilities=('Swift Swim',), pkTypes=('Water',),
                    sets=(), baseStats=(43, 30, 55, 40, 65, 97), genders=('M', 'F')
                )
            if 'Kyogre':
                root.pokesets['Kyogre'] = pokemon_ddl.PokemonSet(
                    name='Kyogre', species='Kyogre', abilities=('Drizzle',), pkTypes=('Water',),
                    sets=(), baseStats=(100, 100, 90, 150, 140, 90), genders=('',)
                )
            if 'Floatzel':
                root.pokesets['Floatzel'] = pokemon_ddl.PokemonSet(
                    name='Floatzel', species='Floatzel', abilities=('Swift Swim',), pkTypes=('Water',),
                    sets=(), baseStats=(85, 105, 55, 85, 50, 115), genders=('M', 'F')
                )
            if 'Lumineon':
                root.pokesets['Lumineon'] = pokemon_ddl.PokemonSet(
                    name='Lumineon', species='Lumineon', abilities=('Swift Swim', 'Storm Drain'), pkTypes=('Water',),
                    sets=(), baseStats=(69, 69, 76, 69, 86, 91), genders=('M', 'F')
                )
            if 'Phione':
                root.pokesets['Phione'] = pokemon_ddl.PokemonSet(
                    name='Phione', species='Phione', abilities=('Hydration',), pkTypes=('Water',),
                    sets=(), baseStats=(80, 80, 80, 80, 80, 80), genders=('',)
                )
            if 'Manaphy':
                root.pokesets['Manaphy'] = pokemon_ddl.PokemonSet(
                    name='Manaphy', species='Manaphy', abilities=('Hydration',), pkTypes=('Water',),
                    sets=(), baseStats=(100, 100, 100, 100, 100, 100), genders=('',)
                )
            if 'Arceus-Water':
                root.pokesets['Arceus-Water'] = pokemon_ddl.PokemonSet(
                    name='Arceus-Water', species='Arceus', abilities=('Multitype',), pkTypes=('Water',),
                    sets=(), baseStats=(120, 120, 120, 120, 120, 120), genders=('',)
                )

    if 'Pokemon Probabilities':
        pokemon_weights = {
            # Dragon
            'Dragonite': 2.0, 'Kingdra': 2.2, 'Flygon': 2.2, 'Salamence': 2.0, 'Latias': 0.5, 'Latios': 0.5,
            'Rayquaza': 0.2,
            'Dialga': 0.2, 'Palkia': 0.25, 'Giratina': 0.2, 'Arceus-Dragon': 0.015,

            # Ice
            'Dewgong': 1.5, 'Cloyster': 2.0, 'Jynx': 1.2, 'Lapras': 2.0, 'Articuno': 2.0, 'Delibird': 0.1,
            'Glalie': 2.0,
            'Walrein': 2.0, 'Regice': 2.0, 'Abomasnow': 3.0, 'Weavile': 2.0, 'Glaceon': 2.0, 'Mamoswine': 2.0,
            'Froslass': 2.0,
            'Arceus-Ice': 0.015,

            # Fighting
            'Primape': 1.0, 'Poliwrath': 2.0, 'Machamp': 2.0, 'Hitmonlee': 1.6, 'Hitmonchan': 1.6, 'Heracross': 2.0,
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
            'Gengar': 2.0, 'Shedinja': 1.8, 'Banette': 1.1, 'Drifblim': 1.5, 'Mismagius': 1.0, 'Dusknoir': 2.0,
            'Rotom': 0.25,
            'Rotom-Fan': 0.6, 'Rotom-Frost': 0.6, 'Rotom-Heat': 0.6, 'Rotom-Mow': 0.6, 'Rotom-Wash': 0.6,
            'Arceus-Ghost': 0.015,

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
            'Garchomp': 2.0, 'Hippowdon': 2.2, 'Gliscor': 2.0, 'Arceus-Ground': 0.015,

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
            'Swellow': 2.0, 'Pelipper': 1.0, 'Altaria': 2.1, 'Staraptor': 2.0, 'Chatot': 0.5, 'Togekiss': 2.0,
            'Arceus-Flying': 0.015,

            # Normal
            'Raticate': 0.8, 'Clefable': 2.0, 'Wigglytuff': 1.0, 'Persian': 2.0, 'Kangaskhan': 2.0, 'Ditto': 1.2,
            'Tauros': 2.0,
            'Snorlax': 2.0, 'Furret': 1.0, 'Dunsparce': 1.0, 'Granbull': 1.0, 'Ursaring': 2.0, 'Porygon2': 2.0,
            'Stantler': 1.0,
            'Smeargle': 2.0, 'Miltank': 2.0, 'Blissey': 2.0, 'Linoone': 1.0, 'Slaking': 1.4, 'Exploud': 2.0,
            'Delcatty': 0.5,
            'Spinda': 0.5, 'Zangoose': 2.0, 'Kecleon': 1.0, 'Bibarel': 1.0, 'Ambipom': 2.0, 'Lopunny': 2.0,
            'Purugly': 1.0,
            'Lickilicky': 2.0, 'Porygon-Z': 2.0, 'Regigigas': 2.0, 'Arceus': 0.015,

            # Water
            'Blastoise': 2.0, 'Golduck': 1.0, 'Kingler': 2.0, 'Seaking': 1.0, 'Vaporeon': 2.0, 'Feraligatr': 2.0,
            'Azumarill': 2.0, 'Politoed': 1.2, 'Qwilfish': 1.1, 'Octillery': 1.3, 'Suicune': 1.5, 'Wailord': 2.0,
            'Milotic': 2.0,
            'Huntail': 0.8, 'Gorebyss': 0.8,
            'Luvdisc': 0.1, 'Kyogre': 0.25, 'Floatzel': 2.0, 'Lumineon': 1.0, 'Phione': 1.0, 'Manaphy': 0.5,
            'Arceus-Water': 0.015,
        }
        pokemon_to_types_map = {
            'Pikachu': ['Electric'],
            'Quagsire': ['Water', 'Ground'], 'Tangrowth': ['Grass'], 'Wailord': ['Water'],
            'Sharpedo': ['Water', 'Dark'], 'Drapion': ['Dark', 'Poison'], 'Rampardos': ['Rock'],
            'Venusaur': ['Grass', 'Poison'], 'Charizard': ['Fire', 'Flying'], 'Blastoise': ['Water'],
            'Butterfree': ['Bug', 'Flying'], 'Beedrill': ['Bug', 'Poison'], 'Pidgeot': ['Normal', 'Flying'],
            'Raticate': ['Normal'], 'Fearow': ['Normal', 'Flying'], 'Arbok': ['Poison'], 'Raichu': ['Electric'],
            'Sandslash': ['Ground'], 'Nidoqueen': ['Poison', 'Ground'], 'Nidoking': ['Poison', 'Ground'],
            'Clefable': ['Normal'], 'Ninetales': ['Fire'], 'Wigglytuff': ['Normal'], 'Vileplume': ['Grass', 'Poison'],
            'Parasect': ['Bug', 'Grass'], 'Venomoth': ['Bug', 'Poison'], 'Dugtrio': ['Ground'], 'Persian': ['Normal'],
            'Golduck': ['Water'], 'Primape': ['Fighting'], 'Arcanine': ['Fire'], 'Poliwrath': ['Water', 'Fighting'],
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
        smoothing = 0.67

        raw_type_totals = {name: 0.0 for name in type_names}
        for pokemon, weight in pokemon_weights.items():
            num_types = len(pokemon_to_types_map[pokemon])
            for p_type in pokemon_to_types_map[pokemon]:
                raw_type_totals[p_type] += 1 / num_types

        smoothed_type_totals = {k: (float(np.mean(list(raw_type_totals.values()))) - v) * smoothing + v for k, v in
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

    if 'Physical Moves':
        # Normal-type moves
        root.moves['Barrage'] = pokemon_ddl.Move('Barrage', 15, 0.85, 'Phys', 'Normal')
        root.moves['Bide'] = pokemon_ddl.Move('Bide', 0, 1.0, 'Phys', 'Normal')
        root.moves['Body Slam'] = pokemon_ddl.Move('Body Slam', 85, 1.0, 'Phys', 'Normal')
        root.moves['Comet Punch'] = pokemon_ddl.Move('Comet Punch', 18, .85, 'Phys', 'Normal')
        root.moves['Constrict'] = pokemon_ddl.Move('Constrict', 10, 1.0, 'Phys', 'Normal')
        root.moves['Covet'] = pokemon_ddl.Move('Covet', 40, 1.0, 'Phys', 'Normal')
        root.moves['Crush Claw'] = pokemon_ddl.Move('Crush Claw', 75, .95, 'Phys', 'Normal')
        root.moves['Crush Grip'] = pokemon_ddl.Move('Crush Grip', 0, 1.0, 'Phys', 'Normal')
        root.moves['Cut'] = pokemon_ddl.Move('Cut', 50, 0.95, 'Phys', 'Normal')
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
        root.moves['Selfdestruct'] = pokemon_ddl.Move('Selfdestruct', 200, 1.0, 'Phys', 'Normal')
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
        root.moves['Dizzy Punch'] = pokemon_ddl.Move('Dizzy Punch', 70, 1.0, 'Phys', 'Psychic')
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
        root.moves['Faint Attack'] = pokemon_ddl.Move('Faint Attack', 60, 1.0, 'Phys', 'Dark')
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
        root.moves['Hidden Power [Fire]'] = pokemon_ddl.Move('Hidden Power [Fire]', 60, 1.0, 'Spec', 'Normal')
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
        root.moves['BubbleBeam'] = pokemon_ddl.Move('BubbleBeam', 65, 1.0, 'Spec', 'Water')
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
        root.moves['Zap Cannon'] = pokemon_ddl.Move('Zap Cannon', 100, 0.5, 'Spec', 'Electric')

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
        root.moves['Softboiled'] = pokemon_ddl.Move('Softboiled', 0, 1.0, 'Stat', 'Normal')
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
        root.moves['Grasswhistle'] = pokemon_ddl.Move('Grasswhistle', 0, 0.55, 'Stat', 'Grass')
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
        root.moves['Sand-attack'] = pokemon_ddl.Move('Sand-attack', 0, 1.0, 'Stat', 'Ground')
        root.moves['Spikes'] = pokemon_ddl.Move('Spikes', 0, 1.0, 'Stat', 'Ground')

        # Rock-type moves
        root.moves['Rock Polish'] = pokemon_ddl.Move('Rock Polish', 0, 1.0, 'Stat', 'Rock')
        root.moves['Sandstorm'] = pokemon_ddl.Move('Sandstorm', 0, 1.0, 'Stat', 'Rock')
        root.moves['Stealth Rock'] = pokemon_ddl.Move('Stealth Rock', 0, 1.0, 'Stat', 'Rock')

        # Fire-type moves
        root.moves['Sunny Day'] = pokemon_ddl.Move('Sunny Day', 0, 1.0, 'Stat', 'Fire')
        root.moves['Will-O-Wisp'] = pokemon_ddl.Move('Will-O-Wisp', 0, 0.75, 'Stat', 'Fire')
    transaction.commit()

    print(root.pokesets['Dragonite'].toString())


if __name__ == '__main__':
    runDML()
