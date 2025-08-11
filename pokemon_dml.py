from BTrees.OOBTree import OOBTree
import ZODB, ZODB.FileStorage
import persistent
import pokemon_ddl
import transaction
import numpy as np
import random
import pprint


def runDML():
    storage = ZODB.FileStorage.FileStorage('PokeData.fs')
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
        if 'Dragonite':
            root.pokesets['Dragonite'] = pokemon_ddl.PokemonSet(
                name='Dragonite', species='Dragonite', abilities=('Inner Focus',), pkTypes=('Dragon', 'Flying'),
                sets=(), legalMoves=set(), baseStats=(91, 134, 95, 100, 100, 80), genders=('M', 'F')
            )
        if 'Kingdra':
            root.pokesets['Kingdra'] = pokemon_ddl.PokemonSet(
                name='Kingdra', species='Kingdra', abilities=('Swift Swim', 'Sniper'), pkTypes=('Water', 'Dragon'),
                sets=(), legalMoves=set(), baseStats=(75, 95, 95, 95, 95, 85), genders=('M', 'F')
            )
        if 'Flygon':
            root.pokesets['Flygon'] = pokemon_ddl.PokemonSet(
                name='Flygon', species='Flygon', abilities=('Levitate',), pkTypes=('Ground', 'Dragon'),
                sets=(), legalMoves=set(), baseStats=(80, 100, 80, 80, 80, 100), genders=('M', 'F')
            )
        if 'Salamence':
            root.pokesets['Salamence'] = pokemon_ddl.PokemonSet(
                name='Salamence', species='Salamence', abilities=('Intimidate',), pkTypes=('Dragon', 'Flying'),
                sets=(), legalMoves=set(), baseStats=(95, 135, 80, 110, 80, 100), genders=('M', 'F')
            )
        if 'Latias':
            root.pokesets['Latias'] = pokemon_ddl.PokemonSet(
                name='Latias', species='Latias', abilities=('Levitate',), pkTypes=('Dragon', 'Psychic'),
                sets=(), legalMoves=set(), baseStats=(80, 80, 90, 110, 130, 110), genders=('F',)
            )
        if 'Latios':
            root.pokesets['Latios'] = pokemon_ddl.PokemonSet(
                name='Latios', species='Latios', abilities=('Levitate',), pkTypes=('Dragon', 'Psychic'),
                sets=(), legalMoves=set(), baseStats=(80, 90, 80, 130, 110, 110), genders=('M',)
            )
        if 'Rayquaza':
            root.pokesets['Rayquaza'] = pokemon_ddl.PokemonSet(
                name='Rayquaza', species='Rayquaza', abilities=('Air Lock',), pkTypes=('Dragon', 'Flying'),
                sets=(), legalMoves=set(), baseStats=(105, 150, 90, 150, 90, 95), genders=('',)
            )
        if 'Dialga':
            root.pokesets['Dialga'] = pokemon_ddl.PokemonSet(
                name='Dialga', species='Dialga', abilities=('Pressure',), pkTypes=('Steel', 'Dragon'),
                sets=(), legalMoves=set(), baseStats=(100, 120, 120, 150, 100, 90), genders=('',)
            )
        if 'Palkia':
            root.pokesets['Palkia'] = pokemon_ddl.PokemonSet(
                name='Palkia', species='Palkia', abilities=('Pressure',), pkTypes=('Water', 'Dragon'),
                sets=(), legalMoves=set(), baseStats=(90, 120, 100, 150, 120, 100), genders=('',)
            )
        if 'Giratina':
            root.pokesets['Giratina'] = pokemon_ddl.PokemonSet(
                name='Giratina', species='Giratina', abilities=('Pressure',), pkTypes=('Ghost', 'Dragon'),
                sets=(), legalMoves=set(), baseStats=(150, 100, 120, 100, 120, 90), genders=('',)
            )
        if 'Arceus-Dragon':
            root.pokesets['Arceus-Dragon'] = pokemon_ddl.PokemonSet(
                name='Arceus-Dragon', species='Arceus', abilities=('Multitype',), pkTypes=('Dragon',),
                sets=(), legalMoves=set(), baseStats=(120, 120, 120, 120, 120, 120), genders=('',)
            )

        # Ice type pokemon
        if 'Ice Type Pokemon':
            if 'Dewgong':
                root.pokesets['Dewgong'] = pokemon_ddl.PokemonSet(
                    name='Dewgong', species='Dewgong', abilities=('Thick Fat', 'Hydration'), pkTypes=('Water', 'Ice'),
                    sets=(), legalMoves=set(), baseStats=(90, 70, 80, 70, 95, 70), genders=('M', 'F')
                )
            if 'Cloyster':
                root.pokesets['Cloyster'] = pokemon_ddl.PokemonSet(
                    name='Cloyster', species='Cloyster', abilities=('Shell Armor', 'Skill Link'), pkTypes=('Water', 'Ice'),
                    sets=(), legalMoves=set(), baseStats=(50, 95, 180, 85, 45, 70), genders=('M', 'F')
                )
            if 'Jynx':
                root.pokesets['Jynx'] = pokemon_ddl.PokemonSet(
                    name='Jynx', species='Jynx', abilities=('Oblivious', 'Forewarn'), pkTypes=('Ice', 'Psychic'),
                    sets=(), legalMoves=set(), baseStats=(65, 50, 35, 115, 95, 95), genders=('F',)
                )
            if 'Lapras':
                root.pokesets['Lapras'] = pokemon_ddl.PokemonSet(
                    name='Lapras', species='Lapras', abilities=('Water Absorb', 'Shell Armor'), pkTypes=('Water', 'Ice'),
                    sets=(), legalMoves=set(), baseStats=(130, 85, 80, 85, 95, 60), genders=('M', 'F')
                )
            if 'Articuno':
                root.pokesets['Articuno'] = pokemon_ddl.PokemonSet(
                    name='Articuno', species='Articuno', abilities=('Pressure',), pkTypes=('Ice', 'Flying'),
                    sets=(), legalMoves=set(), baseStats=(90, 85, 100, 95, 125, 85), genders=('',)
                )
            if 'Delibird':
                root.pokesets['Delibird'] = pokemon_ddl.PokemonSet(
                    name='Delibird', species='Delibird', abilities=('Vital Spirit', 'Hustle'), pkTypes=('Ice', 'Flying'),
                    sets=(), legalMoves=set(), baseStats=(45, 55, 45, 65, 45, 75), genders=('M', 'F')
                )
            if 'Glalie':
                root.pokesets['Glalie'] = pokemon_ddl.PokemonSet(
                    name='Glalie', species='Glalie', abilities=('Inner Focus', 'Ice Body'), pkTypes=('Ice',),
                    sets=(), legalMoves=set(), baseStats=(80, 80, 80, 80, 80, 80), genders=('M', 'F')
                )
            if 'Walrein':
                root.pokesets['Walrein'] = pokemon_ddl.PokemonSet(
                    name='Walrein', species='Walrein', abilities=('Thick Fat', 'Ice Body'), pkTypes=('Ice', 'Water'),
                    sets=(), legalMoves=set(), baseStats=(110, 80, 90, 95, 90, 65), genders=('M', 'F')
                )
            if 'Regice':
                root.pokesets['Regice'] = pokemon_ddl.PokemonSet(
                    name='Regice', species='Regice', abilities=('Clear Body',), pkTypes=('Ice',),
                    sets=(), legalMoves=set(), baseStats=(80, 50, 100, 100, 200, 50), genders=('',)
                )
            if 'Abomasnow':
                root.pokesets['Abomasnow'] = pokemon_ddl.PokemonSet(
                    name='Abomasnow', species='Abomasnow', abilities=('Snow Warning',), pkTypes=('Grass', 'Ice'),
                    sets=(), legalMoves=set(), baseStats=(90, 92, 75, 92, 85, 60), genders=('M', 'F')
                )
            if 'Weavile':
                root.pokesets['Weavile'] = pokemon_ddl.PokemonSet(
                    name='Weavile', species='Weavile', abilities=('Pressure',), pkTypes=('Dark', 'Ice'),
                    sets=(), legalMoves=set(), baseStats=(70, 120, 65, 45, 85, 125), genders=('M', 'F')
                )
            if 'Glaceon':
                root.pokesets['Glaceon'] = pokemon_ddl.PokemonSet(
                    name='Glaceon', species='Glaceon', abilities=('Snow Cloak',), pkTypes=('Ice',),
                    sets=(), legalMoves=set(), baseStats=(65, 60, 110, 130, 95, 65), genders=('M', 'F')
                )
            if 'Mamoswine':
                root.pokesets['Mamoswine'] = pokemon_ddl.PokemonSet(
                    name='Mamoswine', species='Mamoswine', abilities=('Oblivious', 'Snow Cloak'), pkTypes=('Ice', 'Ground'),
                    sets=(), legalMoves=set(), baseStats=(110, 130, 80, 70, 60, 80), genders=('M', 'F')
                )
            if 'Froslass':
                root.pokesets['Froslass'] = pokemon_ddl.PokemonSet(
                    name='Froslass', species='Froslass', abilities=('Snow Cloak',), pkTypes=('Ice', 'Ghost'),
                    sets=(), legalMoves=set(), baseStats=(70, 80, 70, 80, 70, 110), genders=('F',)
                )
            if 'Arceus-Ice':
                root.pokesets['Arceus-Ice'] = pokemon_ddl.PokemonSet(
                    name='Arceus-Ice', species='Arceus', abilities=('Multitype',), pkTypes=('Ice',),
                    sets=(), legalMoves=set(), baseStats=(120, 120, 120, 120, 120, 120), genders=('',)
                )

        #Fighting type pokemon
        if 'Fighting':
            if 'Primape':
                root.pokesets['Primape'] = pokemon_ddl.PokemonSet(
                    name='Primape', species='Primape', abilities=('Vital Spirit', 'Anger Point'), pkTypes=('Fighting',),
                    sets=(), legalMoves=set(), baseStats=(65, 105, 60, 60, 70, 95), genders=('M', 'F')
                )
            if 'Poliwrath':
                root.pokesets['Poliwrath'] = pokemon_ddl.PokemonSet(
                    name='Poliwrath', species='Poliwrath', abilities=('Water Absorb', 'Damp'),
                    pkTypes=('Water', 'Fighting'),
                    sets=(), legalMoves=set(), baseStats=(90, 85, 95, 70, 90, 70), genders=('M', 'F')
                )
            if 'Machamp':
                root.pokesets['Machamp'] = pokemon_ddl.PokemonSet(
                    name='Machamp', species='Machamp', abilities=('Guts', 'No Guard'), pkTypes=('Fighting',),
                    sets=(), legalMoves=set(), baseStats=(90, 130, 80, 65, 85, 55), genders=('M', 'F')
                )
            if 'Hitmonlee':
                root.pokesets['Hitmonlee'] = pokemon_ddl.PokemonSet(
                    name='Hitmonlee', species='Hitmonlee', abilities=('Limber', 'Reckless'), pkTypes=('Fighting',),
                    sets=(), legalMoves=set(), baseStats=(50, 120, 53, 35, 110, 87), genders=('M',)
                )
            if 'Hitmonchan':
                root.pokesets['Hitmonchan'] = pokemon_ddl.PokemonSet(
                    name='Hitmonchan', species='Hitmonchan', abilities=('Keen Eye', 'Iron Fist'), pkTypes=('Fighting',),
                    sets=(), legalMoves=set(), baseStats=(50, 105, 79, 35, 110, 76), genders=('M',)
                )
            if 'Heracross':
                root.pokesets['Heracross'] = pokemon_ddl.PokemonSet(
                    name='Heracross', species='Heracross', abilities=('Swarm', 'Guts'), pkTypes=('Bug', 'Fighting'),
                    sets=(), legalMoves=set(), baseStats=(80, 125, 75, 40, 95, 85), genders=('M', 'F')
                )
            if 'Hitmontop':
                root.pokesets['Hitmontop'] = pokemon_ddl.PokemonSet(
                    name='Hitmontop', species='Hitmontop', abilities=('Intimidate', 'Technician'),
                    pkTypes=('Fighting',),
                    sets=(), legalMoves=set(), baseStats=(50, 95, 95, 35, 110, 70), genders=('M',)
                )
            if 'Blaziken':
                root.pokesets['Blaziken'] = pokemon_ddl.PokemonSet(
                    name='Blaziken', species='Blaziken', abilities=('Blaze',), pkTypes=('Fire', 'Fighting'),
                    sets=(), legalMoves=set(), baseStats=(80, 120, 70, 110, 70, 80), genders=('M', 'F')
                )
            if 'Breloom':
                root.pokesets['Breloom'] = pokemon_ddl.PokemonSet(
                    name='Breloom', species='Breloom', abilities=('Effect Spore', 'Poison Heal'),
                    pkTypes=('Grass', 'Fighting'),
                    sets=(), legalMoves=set(), baseStats=(60, 130, 80, 60, 60, 70), genders=('M', 'F')
                )
            if 'Hariyama':
                root.pokesets['Hariyama'] = pokemon_ddl.PokemonSet(
                    name='Hariyama', species='Hariyama', abilities=('Thick Fat', 'Guts'), pkTypes=('Fighting',),
                    sets=(), legalMoves=set(), baseStats=(144, 120, 60, 40, 60, 50), genders=('M', 'F')
                )
            if 'Medicham':
                root.pokesets['Medicham'] = pokemon_ddl.PokemonSet(
                    name='Medicham', species='Medicham', abilities=('Pure Power',), pkTypes=('Fighting', 'Psychic'),
                    sets=(), legalMoves=set(), baseStats=(60, 60, 75, 60, 75, 80), genders=('M', 'F')
                )
            if 'Infernape':
                root.pokesets['Infernape'] = pokemon_ddl.PokemonSet(
                    name='Infernape', species='Infernape', abilities=('Blaze',), pkTypes=('Fire', 'Fighting'),
                    sets=(), legalMoves=set(), baseStats=(76, 104, 71, 104, 71, 108), genders=('M', 'F')
                )
            if 'Lucario':
                root.pokesets['Lucario'] = pokemon_ddl.PokemonSet(
                    name='Lucario', species='Lucario', abilities=('Steadfast', 'Inner Focus'),
                    pkTypes=('Fighting', 'Steel'),
                    sets=(), legalMoves=set(), baseStats=(70, 110, 70, 115, 70, 90), genders=('M', 'F')
                )
            if 'Toxicroak':
                root.pokesets['Toxicroak'] = pokemon_ddl.PokemonSet(
                    name='Toxicroak', species='Toxicroak', abilities=('Anticipation', 'Dry Skin'),
                    pkTypes=('Poison', 'Fighting'),
                    sets=(), legalMoves=set(), baseStats=(83, 106, 65, 86, 65, 85), genders=('M', 'F')
                )
            if 'Gallade':
                root.pokesets['Gallade'] = pokemon_ddl.PokemonSet(
                    name='Gallade', species='Gallade', abilities=('Steadfast',), pkTypes=('Psychic', 'Fighting'),
                    sets=(), legalMoves=set(), baseStats=(68, 125, 65, 65, 115, 80), genders=('M',)
                )
            if 'Arceus-Fighting':
                root.pokesets['Arceus-Fighting'] = pokemon_ddl.PokemonSet(
                    name='Arceus-Fighting', species='Arceus', abilities=('Multitype',), pkTypes=('Fighting',),
                    sets=(), legalMoves=set(), baseStats=(120, 120, 120, 120, 120, 120), genders=('',)
                )

        # Dark type pokemon
        if 'Dark':
            if 'Umbreon':
                root.pokesets['Umbreon'] = pokemon_ddl.PokemonSet(
                    name='Umbreon', species='Umbreon', abilities=('Synchronize',), pkTypes=('Dark',),
                    sets=(), legalMoves=set(), baseStats=(95, 65, 110, 60, 130, 65), genders=('M', 'F')
                )
            if 'Houndoom':
                root.pokesets['Houndoom'] = pokemon_ddl.PokemonSet(
                    name='Houndoom', species='Houndoom', abilities=('Early Bird', 'Flash Fire'),
                    pkTypes=('Dark', 'Fire'),
                    sets=(), legalMoves=set(), baseStats=(75, 90, 50, 110, 80, 95), genders=('M', 'F')
                )
            if 'Tyranitar':
                root.pokesets['Tyranitar'] = pokemon_ddl.PokemonSet(
                    name='Tyranitar', species='Tyranitar', abilities=('Sand Stream',), pkTypes=('Rock', 'Dark'),
                    sets=(), legalMoves=set(), baseStats=(100, 134, 110, 95, 100, 61), genders=('M', 'F')
                )
            if 'Mightyena':
                root.pokesets['Mightyena'] = pokemon_ddl.PokemonSet(
                    name='Mightyena', species='Mightyena', abilities=('Intimidate', 'Quick Feet'),
                    pkTypes=('Dark',),
                    sets=(), legalMoves=set(), baseStats=(70, 90, 70, 60, 60, 70), genders=('M', 'F')
                )
            if 'Shiftry':
                root.pokesets['Shiftry'] = pokemon_ddl.PokemonSet(
                    name='Shiftry', species='Shiftry', abilities=('Chlorophyll', 'Early Bird'),
                    pkTypes=('Grass', 'Dark'),
                    sets=(), legalMoves=set(), baseStats=(90, 100, 60, 90, 60, 80), genders=('M', 'F')
                )
            if 'Sableye':
                root.pokesets['Sableye'] = pokemon_ddl.PokemonSet(
                    name='Sableye', species='Sableye', abilities=('Keen Eye', 'Stall'), pkTypes=('Dark', 'Ghost'),
                    sets=(), legalMoves=set(), baseStats=(50, 75, 75, 65, 65, 50), genders=('M', 'F')
                )
            if 'Sharpedo':
                root.pokesets['Sharpedo'] = pokemon_ddl.PokemonSet(
                    name='Sharpedo', species='Sharpedo', abilities=('Rough Skin',), pkTypes=('Water', 'Dark'),
                    sets=(), legalMoves=set(), baseStats=(70, 120, 40, 95, 40, 95), genders=('M', 'F')
                )
            if 'Cacturne':
                root.pokesets['Cacturne'] = pokemon_ddl.PokemonSet(
                    name='Cacturne', species='Cacturne', abilities=('Sand Veil',), pkTypes=('Grass', 'Dark'),
                    sets=(), legalMoves=set(), baseStats=(70, 115, 60, 115, 60, 55), genders=('M', 'F')
                )
            if 'Crawdaunt':
                root.pokesets['Crawdaunt'] = pokemon_ddl.PokemonSet(
                    name='Crawdaunt', species='Crawdaunt', abilities=('Hyper Cutter', 'Shell Armor'),
                    pkTypes=('Water', 'Dark'),
                    sets=(), legalMoves=set(), baseStats=(63, 120, 85, 90, 55, 55), genders=('M', 'F')
                )
            if 'Absol':
                root.pokesets['Absol'] = pokemon_ddl.PokemonSet(
                    name='Absol', species='Absol', abilities=('Pressure', 'Super Luck'), pkTypes=('Dark',),
                    sets=(), legalMoves=set(), baseStats=(65, 130, 60, 75, 60, 75), genders=('M', 'F')
                )
            if 'Honchkrow':
                root.pokesets['Honchkrow'] = pokemon_ddl.PokemonSet(
                    name='Honchkrow', species='Honchkrow', abilities=('Insomnia', 'Super Luck'),
                    pkTypes=('Dark', 'Flying'),
                    sets=(), legalMoves=set(), baseStats=(100, 125, 52, 105, 52, 71), genders=('M', 'F')
                )
            if 'Skuntank':
                root.pokesets['Skuntank'] = pokemon_ddl.PokemonSet(
                    name='Skuntank', species='Skuntank', abilities=('Stench', 'Aftermath'),
                    pkTypes=('Poison', 'Dark'),
                    sets=(), legalMoves=set(), baseStats=(103, 93, 67, 71, 61, 84), genders=('M', 'F')
                )
            if 'Spiritomb':
                root.pokesets['Spiritomb'] = pokemon_ddl.PokemonSet(
                    name='Spiritomb', species='Spiritomb', abilities=('Pressure',), pkTypes=('Ghost', 'Dark'),
                    sets=(), legalMoves=set(), baseStats=(50, 92, 108, 92, 108, 35), genders=('',)
                )
            if 'Drapion':
                root.pokesets['Drapion'] = pokemon_ddl.PokemonSet(
                    name='Drapion', species='Drapion', abilities=('Battle Armor', 'Sniper'),
                    pkTypes=('Poison', 'Dark'),
                    sets=(), legalMoves=set(), baseStats=(70, 90, 110, 60, 75, 95), genders=('M', 'F')
                )
            if 'Darkrai':
                root.pokesets['Darkrai'] = pokemon_ddl.PokemonSet(
                    name='Darkrai', species='Darkrai', abilities=('Bad Dreams',), pkTypes=('Dark',),
                    sets=(), legalMoves=set(), baseStats=(70, 90, 90, 135, 90, 125), genders=('',)
                )
            if 'Arceus-Dark':
                root.pokesets['Arceus-Dark'] = pokemon_ddl.PokemonSet(
                    name='Arceus-Dark', species='Arceus', abilities=('Multitype',), pkTypes=('Dark',),
                    sets=(), legalMoves=set(), baseStats=(120, 120, 120, 120, 120, 120), genders=('',)
                )

        # Fire type pokemon
        if 'Fire':
            if 'Charizard':
                root.pokesets['Charizard'] = pokemon_ddl.PokemonSet(
                    name='Charizard', species='Charizard', abilities=('Blaze',), pkTypes=('Fire', 'Flying'),
                    sets=(), legalMoves=set(), baseStats=(78, 84, 78, 109, 85, 100), genders=('M', 'F')
                )
            if 'Ninetales':
                root.pokesets['Ninetales'] = pokemon_ddl.PokemonSet(
                    name='Ninetales', species='Ninetales', abilities=('Flash Fire',), pkTypes=('Fire',),
                    sets=(), legalMoves=set(), baseStats=(73, 76, 75, 81, 100, 100), genders=('M', 'F')
                )
            if 'Arcanine':
                root.pokesets['Arcanine'] = pokemon_ddl.PokemonSet(
                    name='Arcanine', species='Arcanine', abilities=('Intimidate', 'Flash Fire'), pkTypes=('Fire',),
                    sets=(), legalMoves=set(), baseStats=(90, 110, 80, 100, 80, 95), genders=('M', 'F')
                )
            if 'Rapidash':
                root.pokesets['Rapidash'] = pokemon_ddl.PokemonSet(
                    name='Rapidash', species='Rapidash', abilities=('Run Away', 'Flash Fire'), pkTypes=('Fire',),
                    sets=(), legalMoves=set(), baseStats=(65, 100, 70, 80, 80, 105), genders=('M', 'F')
                )
            if 'Flareon':
                root.pokesets['Flareon'] = pokemon_ddl.PokemonSet(
                    name='Flareon', species='Flareon', abilities=('Flash Fire',), pkTypes=('Fire',),
                    sets=(), legalMoves=set(), baseStats=(65, 130, 60, 95, 110, 65), genders=('M', 'F')
                )
            if 'Moltres':
                root.pokesets['Moltres'] = pokemon_ddl.PokemonSet(
                    name='Moltres', species='Moltres', abilities=('Pressure',), pkTypes=('Fire', 'Flying'),
                    sets=(), legalMoves=set(), baseStats=(90, 100, 90, 125, 85, 90), genders=('',)
                )
            if 'Typhlosion':
                root.pokesets['Typhlosion'] = pokemon_ddl.PokemonSet(
                    name='Typhlosion', species='Typhlosion', abilities=('Blaze',), pkTypes=('Fire',),
                    sets=(), legalMoves=set(), baseStats=(78, 84, 78, 109, 85, 100), genders=('M', 'F')
                )
            if 'Magcargo':
                root.pokesets['Magcargo'] = pokemon_ddl.PokemonSet(
                    name='Magcargo', species='Magcargo', abilities=('Magma Armor', 'Flame Body'),
                    pkTypes=('Fire', 'Rock'),
                    sets=(), legalMoves=set(), baseStats=(50, 50, 120, 80, 80, 30), genders=('M', 'F')
                )
            if 'Entei':
                root.pokesets['Entei'] = pokemon_ddl.PokemonSet(
                    name='Entei', species='Entei', abilities=('Pressure',), pkTypes=('Fire',),
                    sets=(), legalMoves=set(), baseStats=(115, 115, 85, 90, 75, 100), genders=('',)
                )
            if 'Ho-oh':
                root.pokesets['Ho-oh'] = pokemon_ddl.PokemonSet(
                    name='Ho-oh', species='Ho-oh', abilities=('Pressure',), pkTypes=('Fire', 'Flying'),
                    sets=(), legalMoves=set(), baseStats=(106, 130, 90, 110, 154, 90), genders=('',)
                )
            if 'Camerupt':
                root.pokesets['Camerupt'] = pokemon_ddl.PokemonSet(
                    name='Camerupt', species='Camerupt', abilities=('Magma Armor', 'Solid Rock'),
                    pkTypes=('Fire', 'Ground'),
                    sets=(), legalMoves=set(), baseStats=(70, 100, 70, 105, 75, 40), genders=('M', 'F')
                )
            if 'Torkoal':
                root.pokesets['Torkoal'] = pokemon_ddl.PokemonSet(
                    name='Torkoal', species='Torkoal', abilities=('White Smoke',), pkTypes=('Fire',),
                    sets=(), legalMoves=set(), baseStats=(70, 85, 140, 85, 70, 20), genders=('M', 'F')
                )
            if 'Magmortar':
                root.pokesets['Magmortar'] = pokemon_ddl.PokemonSet(
                    name='Magmortar', species='Magmortar', abilities=('Flame Body',), pkTypes=('Fire',),
                    sets=(), legalMoves=set(), baseStats=(75, 95, 67, 125, 95, 83), genders=('M', 'F')
                )
            if 'Heatran':
                root.pokesets['Heatran'] = pokemon_ddl.PokemonSet(
                    name='Heatran', species='Heatran', abilities=('Flash Fire',), pkTypes=('Fire', 'Steel'),
                    sets=(), legalMoves=set(), baseStats=(91, 90, 106, 130, 106, 77), genders=('M', 'F')
                )
            if 'Arceus-Fire':
                root.pokesets['Arceus-Fire'] = pokemon_ddl.PokemonSet(
                    name='Arceus-Fire', species='Arceus', abilities=('Multitype',), pkTypes=('Fire',),
                    sets=(), legalMoves=set(), baseStats=(120, 120, 120, 120, 120, 120), genders=('',)
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
            'Gengar': 2.0, 'Shedinja': 1.3, 'Banette': 1.1, 'Drifblim': 1.5, 'Mismagius': 1.0, 'Dusknoir': 2.0,
            'Rotom': 0.25,
            'Rotom-Fan': 0.6, 'Rotom-Frost': 0.6, 'Rotom-Heat': 0.6, 'Rotom-Mow': 0.6, 'Rotom-Wash': 0.6,
            # Forms weighted individually
            'Arceus-Ghost': 0.015,

            # Steel
            'Forretress': 2.0, 'Steelix': 2.0, 'Scizor': 2.0, 'Skarmory': 2.0, 'Mawile': 1.0, 'Aggron': 2.0,
            'Metagross': 2.0,
            'Registeel': 1.0, 'Jirachi': 0.5, 'Empoleon': 2.0, 'Bastiodon': 1.0,
            'Wormadam-Trash': 0.2,
            'Bronzong': 2.0, 'Magnezone': 2.0, 'Probopass': 1.2, 'Arceus-Steel': 0.015,

            # Electric
            'Raichu': 2.0, 'Electrode': 2.0, 'Jolteon': 2.0, 'Zapdos': 2.0, 'Lanturn': 1.5, 'Ampharos': 2.0,
            'Raikou': 1.5,
            'Manectric': 2.0,
            'Plusle': 0.25, 'Minun': 0.25,  # Set with total value of 1 -> 0.5 each
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
            'Wormadam-Sandy': 0.2,  # Detrimental -> 0.1
            'Gastrodon': 1.0, 'Gastrodon-East': 1.0,  # Set value 2 -> 1 each
            'Garchomp': 2.0, 'Hippowdon': 2.2, 'Gliscor': 2.0, 'Arceus-Ground': 0.015,

            # Bug
            'Butterfree': 1.0, 'Parasect': 0.5, 'Pinsir': 2.0, 'Ledian': 0.1, 'Beautifly': 1.0, 'Masquerain': 1.0,
            'Ninjask': 2.0, 'Volbeat': 0.5, 'Illumise': 0.5, 'Kricketune': 0.5,
            'Wormadam': 0.2,  # Base form of detrimental set -> 0.1
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

        TYPE_NAMES = ['Dragon', 'Ice', 'Fighting', 'Dark', 'Fire', 'Ghost', 'Steel', 'Electric', 'Rock', 'Poison',
                      'Ground',
                      'Bug', 'Grass', 'Psychic', 'Flying', 'Normal', 'Water']
        smoothing = 0.675

        raw_type_totals = {name: 0.0 for name in TYPE_NAMES}
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
        root.moves['Double-edge'] = pokemon_ddl.Move('Double-edge', 120, 1.0, 'Phys', 'Normal')
        root.moves['Double Hit'] = pokemon_ddl.Move('Double Hit', 35, 0.9, 'Phys', 'Normal')
        root.moves['Doubleslap'] = pokemon_ddl.Move('Doubleslap', 15, 0.85, 'Phys', 'Normal')
        root.moves['Egg Bomb'] = pokemon_ddl.Move('Egg Bomb', 100, 0.75, 'Phys', 'Normal')
        root.moves['Endeavor'] = pokemon_ddl.Move('Endeavor', 0, 1.0, 'Phys', 'Normal')
        root.moves['Explosion'] = pokemon_ddl.Move('Explosion', 250, 1.0, 'Phys', 'Normal')
        root.moves['ExtremeSpeed'] = pokemon_ddl.Move('ExtremeSpeed', 80, 1.0, 'Phys', 'Normal')
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
        root.moves['Smellingsalt'] = pokemon_ddl.Move('Smellingsalt', 60, 1, 'Phys', 'Normal')
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
        root.moves['DynamicPunch'] = pokemon_ddl.Move('DynamicPunch', 100, 0.5, 'Phys', 'Fighting')
        root.moves['Focus Punch'] = pokemon_ddl.Move('Focus Punch', 150, 1.0, 'Phys', 'Fighting')
        root.moves['Force Palm'] = pokemon_ddl.Move('Force Palm', 60, 1.0, 'Phys', 'Fighting')
        root.moves['Hammer Arm'] = pokemon_ddl.Move('Hammer Arm', 100, 0.9, 'Phys', 'Fighting')
        root.moves['Hi Jump Kick'] = pokemon_ddl.Move('Hi Jump Kick', 100, 0.9, 'Phys', 'Fighting')
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
        root.moves['Wake-up Slap'] = pokemon_ddl.Move('Wake-up Slap', 60, 1.0, 'Phys', 'Fighting')

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
        root.moves['ThunderPunch'] = pokemon_ddl.Move('ThunderPunch', 75, 1.0, 'Phys', 'Electric')
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
        root.moves['SolarBeam'] = pokemon_ddl.Move('SolarBeam', 120, 1.0, 'Spec', 'Grass')

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
        root.moves['AncientPower'] = pokemon_ddl.Move('AncientPower', 60, 1.0, 'Spec', 'Rock')
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
        root.moves['Dragonbreath'] = pokemon_ddl.Move('Dragonbreath', 60, 1.0, 'Spec', 'Dragon')
        root.moves['Roar of Time'] = pokemon_ddl.Move('Roar of Time', 150, 0.9, 'Spec', 'Dragon')
        root.moves['Spacial Rend'] = pokemon_ddl.Move('Spacial Rend', 100, 0.95, 'Spec', 'Dragon')
        root.moves['Twister'] = pokemon_ddl.Move('Twister', 40, 1.0, 'Spec', 'Dragon')

        # Ground-type moves
        root.moves['Earth Power'] = pokemon_ddl.Move('Earth Power', 90, 1.0, 'Spec', 'Ground')
        root.moves['Mud Bomb'] = pokemon_ddl.Move('Mud Bomb', 65, 0.85, 'Spec', 'Ground')
        root.moves['Mud Shot'] = pokemon_ddl.Move('Mud Shot', 55, 0.95, 'Spec', 'Ground')
        root.moves['Mud-slap'] = pokemon_ddl.Move('Mud-slap', 20, 1.0, 'Spec', 'Ground')

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
        root.moves['Hidden Power'] = pokemon_ddl.Move('Hidden Power', 0, 1.0, 'Spec', 'Normal')
        root.moves['Hyper Beam'] = pokemon_ddl.Move('Hyper Beam', 150, 0.9, 'Spec', 'Normal')
        root.moves['Hyper Voice'] = pokemon_ddl.Move('Hyper Voice', 90, 1.0, 'Spec', 'Normal')
        root.moves['Judgment'] = pokemon_ddl.Move('Judgment', 100, 1.0, 'Spec', 'Normal')
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
        root.moves['Endure'] = pokemon_ddl.Move('Endure', 0, 1.0, 'Stat', 'Normal', (('Reversal', 0.3), ('Flail', 0.3)))
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
        root.moves['Lock-on'] = pokemon_ddl.Move('Lock-on', 0, 1.0, 'Stat', 'Normal')
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
        root.moves['Stockpile'] = pokemon_ddl.Move('Stockpile', 0, 1.0, 'Stat', 'Normal', (('Spit Up', .5), ('Swallow', .5)))
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
        root.moves['Rain Dance'] = pokemon_ddl.Move('Rain Dance', 0, 1.0, 'Stat', 'Water', (('Thunder', 0.3), ('Weather Ball', 0.2)))
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
        root.moves['Featherdance'] = pokemon_ddl.Move('Featherdance', 0, 1.0, 'Stat', 'Flying')
        root.moves['Mirror Move'] = pokemon_ddl.Move('Mirror Move', 0, 1.0, 'Stat', 'Flying')
        root.moves['Roost'] = pokemon_ddl.Move('Roost', 0, 1.0, 'Stat', 'Flying')
        root.moves['Tailwind'] = pokemon_ddl.Move('Tailwind', 0, 1.0, 'Stat', 'Flying')

        # Dragon-type moves
        root.moves['Dragon Dance'] = pokemon_ddl.Move('Dragon Dance', 0, 1.0, 'Stat', 'Dragon')

        # Ice-type moves
        root.moves['Hail'] = pokemon_ddl.Move('Hail', 0, 1.0, 'Stat', 'Ice', (('Blizzard', 0.3), ('Weather Ball', 0.2)))
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
        root.moves['Sunny Day'] = pokemon_ddl.Move('Sunny Day', 0, 1.0, 'Stat', 'Fire', (('SolarBeam', 0.1), ('Weather Ball', 0.2)))
        root.moves['Will-o-wisp'] = pokemon_ddl.Move('Will-o-wisp', 0, 0.75, 'Stat', 'Fire')
    transaction.commit()

    print(root.pokesets['Venusaur'].toString())


if __name__ == '__main__':
    runDML()
