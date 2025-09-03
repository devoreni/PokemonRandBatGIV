import sys
import os
import ZODB, ZODB.FileStorage
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pokemon_ddl

DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'PokeData.fs'))

@pytest.fixture(scope='module')
def db_root():
    storage = ZODB.FileStorage.FileStorage(DB_PATH)
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root
    yield root
    connection.close()


class TestAllOutPhysicalSweeper:
    def test_gallade(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Gallade', species='Gallade', abilities=(), pkTypes=(), sets=(),
                            baseStats=(68, 125, 65, 65, 115, 80), genders=('M',))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Close Combat', 'Psycho Cut', 'Night Slash', 'Protect']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs == '252 Atk / 252 Spe'
        assert result.nature in {'Jolly', 'Adamant'}

    def test_gallade_2(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Gallade', species='Gallade', abilities=(), pkTypes=(), sets=(),
                            baseStats=(68, 125, 65, 65, 115, 80), genders=('M',))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Close Combat', 'Psycho Cut', 'Swords Dance', 'Protect']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs == '252 Atk / 252 Spe'
        assert result.nature in {'Jolly', 'Adamant'}

    def test_staraptor(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Staraptor', species='Staraptor', abilities=(), pkTypes=(), sets=(),
                            baseStats=(85, 120, 70, 50, 50, 100), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Brave Bird', 'Close Combat', 'U-turn', 'Protect']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs == '252 Atk / 252 Spe'
        assert result.nature in {'Jolly', 'Adamant'}

    def test_weavile(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Weavile', species='Weavile', abilities=(), pkTypes=(), sets=(),
                            baseStats=(70, 120, 65, 45, 85, 125), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Ice Shard', 'Night Slash', 'Screech', 'Protect']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs == '252 Atk / 252 Spe'
        assert result.nature in {'Jolly', 'Adamant'}


class TestAllOutSpecialSweeper:
    def test_gengar(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Gengar', species='Gengar', abilities=(), pkTypes=(), sets=(),
                            baseStats=(60, 65, 60, 130, 75, 110), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Shadow Ball', 'Sludge Bomb', 'Focus Blast', 'Protect']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs == '252 SpA / 252 Spe'
        assert result.nature in {'Timid', 'Modest'}

    def test_alakazam(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Alakazam', species='Alakazam', abilities=(), pkTypes=(), sets=(),
                            baseStats=(55, 50, 45, 135, 85, 120), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Psychic', 'Signal Beam', 'Calm Mind', 'Protect']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs == '252 SpA / 252 Spe'
        assert result.nature in {'Timid', 'Modest'}

    def test_jolteon(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Jolteon', species='Jolteon', abilities=(), pkTypes=(), sets=(),
                            baseStats=(65, 65, 60, 110, 95, 130), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Thunderbolt', 'Shadow Ball', 'Hidden Power [Ice]', 'Signal Beam']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs == '252 SpA / 252 Spe'
        assert result.nature in {'Timid', 'Modest'}


class TestAllOutMixedSweeper:
    def test_infernape(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Infernape', species='Infernape', abilities=(), pkTypes=(), sets=(),
                            baseStats=(76, 104, 71, 104, 71, 108), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Close Combat', 'Flare Blitz', 'Grass Knot', 'Protect']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs == '252 Atk / 252 Spe'
        assert result.nature in ('Hasty', 'Naive', 'Naughty', 'Lonely', 'Mild', 'Rash')

    def test_salamence(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Salamence', species='Salamence', abilities=(), pkTypes=(), sets=(),
                            baseStats=(95, 135, 80, 110, 80, 100), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Draco Meteor', 'Fire Blast', 'Earthquake', 'Dragon Claw']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs in ('252 Atk / 252 Spe', '252 SpA / 252 Spe')
        assert result.nature in ('Hasty', 'Naive')

    def test_salamence_2(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Salamence', species='Salamence', abilities=(), pkTypes=(), sets=(),
                            baseStats=(95, 135, 80, 110, 80, 100), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Draco Meteor', 'Protect', 'Earthquake', 'Dragon Claw']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs in ('252 Atk / 252 Spe', '252 SpA / 252 Spe')
        assert result.nature in ('Hasty', 'Naive', 'Adamant', 'Jolly', 'Naughty', 'Lonely')

    def test_pikachu(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Pikachu', species='Pikachu', abilities=(), pkTypes=(), sets=(),
                            baseStats=(35, 55, 30, 50, 40, 90), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Protect', 'Surf', 'Volt Tackle', 'Endeavor']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs in ('252 Atk / 252 Spe', '252 SpA / 252 Spe')
        assert result.nature in ('Hasty', 'Naive')

    def test_lucario(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Lucario', species='Lucario', abilities=(), pkTypes=(), sets=(),
                            baseStats=(70, 110, 70, 115, 70, 90), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Close Combat', 'Extreme Speed', 'Aura Sphere', 'Dark Pulse']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs in ('252 Atk / 252 Spe', '252 SpA / 252 Spe')
        assert result.nature in ('Hasty', 'Naive')

    def test_lucario_2(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Lucario', species='Lucario', abilities=(), pkTypes=(), sets=(),
                            baseStats=(70, 110, 70, 115, 70, 90), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Follow Me', 'Me First', 'Force Palm', 'Protect']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs in ('252 HP / 252 Spe',)
        assert result.nature in ('Jolly',)


class TestBulkyPhysicalAttacker:
    def test_rhyperior(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Rhyperior', species='Rhyperior', abilities=(), pkTypes=(), sets=(),
                            baseStats=(115, 140, 130, 55, 55, 40), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Rock Slide', 'Earthquake', 'Megahorn', 'Protect']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs == '252 HP / 252 Atk'
        assert result.nature in ('Brave', 'Adamant')

    def test_machamp(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Machamp', species='Machamp', abilities=(), pkTypes=(), sets=(),
                            baseStats=(90, 130, 80, 65, 85, 55), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Dynamic Punch', 'Bullet Punch', 'Stone Edge', 'Protect']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs == '252 HP / 252 Atk'
        assert result.nature == 'Adamant'

    def test_swampert(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Swampert', species='Swampert', abilities=(), pkTypes=(), sets=(),
                            baseStats=(100, 110, 90, 85, 90, 60), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Rest', 'Sleep Talk', 'Earthquake', 'Curse']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs in ('252 HP / 252 Atk', '252 HP / 252 Def', '252 HP / 252 SpD')
        assert result.nature in ('Brave', 'Adamant', 'Impish', 'Careful')

    def test_curse_snorlax(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Snorlax', species='Snorlax', abilities=(), pkTypes=(), sets=(),
                                        baseStats=(160, 110, 65, 65, 110, 30), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Curse', 'Rest', 'Body Slam', 'Earthquake']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs == '252 HP / 252 Def'
        assert result.nature == 'Impish', 'Adamant'


class TestBulkySpecialAttacker:
    def test_lanturn(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Lanturn', species='Lanturn', abilities=(), pkTypes=(), sets=(),
                            baseStats=(125, 58, 58, 76, 76, 67), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Surf', 'Discharge', 'Signal Beam', 'Protect']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs in ('252 HP / 252 SpA', '252 HP / 252 Def', '252 HP / 252 SpD')
        assert result.nature in ('Modest', 'Calm', 'Bold')

    def test_lanturn_2(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Lanturn', species='Lanturn', abilities=(), pkTypes=(), sets=(),
                            baseStats=(125, 58, 58, 76, 76, 67), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Surf', 'Discharge', 'Bounce', 'Protect']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs in ('252 HP / 252 SpA', '252 HP / 252 Def', '252 HP / 252 SpD')
        assert result.nature in ('Sassy', 'Relaxed', 'Quiet')

    def test_magnezone(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Magnezone', species='Magnezone', abilities=(), pkTypes=(), sets=(),
                            baseStats=(70, 70, 115, 130, 90, 60), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Thunderbolt', 'Flash Cannon', 'Hidden Power [Ice]', 'Protect']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs in ('252 HP / 252 SpA', '252 SpA / 252 Spe')
        assert result.nature in ('Modest', 'Timid')

    def test_vaporeon(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Vaporeon', species='Vaporeon', abilities=(), pkTypes=(), sets=(),
                            baseStats=(130, 65, 60, 110, 95, 65), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Surf', 'Ice Beam', 'Wish', 'Protect']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs == '252 HP / 252 SpA'
        assert result.nature == 'Modest'

class TestBulkyMixedAttacker:
    def test_camerupt(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Camerupt', species='Camerupt', abilities=(), pkTypes=(), sets=(),
                                        baseStats=(70, 100, 70, 105, 75, 40), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Protect', 'Eruption', 'Earthquake', 'Slack Off']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs in ('252 HP / 252 Atk', '252 Atk / 252 SpA', '252 HP / 252 SpA')
        assert result.nature in ('Brave', 'Quiet')

    def test_swalot(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Swalot', species='Swalot', abilities=(), pkTypes=(), sets=(),
                                        baseStats=(100, 73, 83, 73, 83, 55), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Strength', 'Sludge Bomb', 'Bullet Seed', 'Protect']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs in ('252 HP / 252 Atk', '252 Atk / 252 SpA', '252 HP / 252 SpA')
        assert result.nature in ('Brave', 'Quiet')

    def test_cacturne(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Cacturne', species='Cacturne', abilities=(), pkTypes=(), sets=(),
                                        baseStats=(70, 115, 60, 115, 60, 55), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Protect', 'Dynamic Punch', 'Mud-Slap', 'Dark Pulse']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs in ('252 HP / 252 Atk', '252 Atk / 252 SpA', '252 HP / 252 SpA')
        assert result.nature in ('Brave', 'Quiet')


class TestFastSupport:
    def test_crobat(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Crobat', species='Crobat', abilities=(), pkTypes=(), sets=(),
                            baseStats=(85, 90, 80, 70, 80, 130), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Taunt', 'Tailwind', 'U-turn', 'Roost']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs in ('252 HP / 252 Spe', '252 HP / 252 Def', '252 HP / 252 SpD')
        assert result.nature in ('Jolly', 'Impish', 'Careful')

    def test_raichu(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Raichu', species='Raichu', abilities=(), pkTypes=(), sets=(),
                            baseStats=(60, 90, 55, 90, 80, 100), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Protect', 'Fake Out', 'Encore', 'Grass Knot']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs == '252 HP / 252 Spe'
        assert result.nature == 'Timid'

    def test_jumpluff(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Jumpluff', species='Jumpluff', abilities=(), pkTypes=(), sets=(),
                            baseStats=(75, 55, 70, 55, 85, 110), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Sleep Powder', 'Leech Seed', 'Protect', 'Energy Ball']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs == '252 HP / 252 Spe'
        assert result.nature == 'Timid'


class TestPhysicalWall:
    def test_skarmory(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Skarmory', species='Skarmory', abilities=(), pkTypes=(), sets=(),
                            baseStats=(65, 80, 140, 40, 70, 70), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Spikes', 'Roost', 'Whirlwind', 'Protect']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs in ('252 HP / 252 Def', '252 HP / 252 SpD')
        assert result.nature in ('Impish', 'Careful', 'Bold', 'Calm')

    def test_skarmory_2(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Skarmory', species='Skarmory', abilities=(), pkTypes=(), sets=(),
                            baseStats=(65, 80, 140, 40, 70, 70), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Spikes', 'Roost', 'Whirlwind', 'Counter']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs in ('252 HP / 252 Def', '252 HP / 252 SpD')
        assert result.nature in ('Impish', 'Careful', 'Bold', 'Calm')

    def test_weezing(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Weezing', species='Weezing', abilities=(), pkTypes=(), sets=(),
                            baseStats=(65, 90, 120, 85, 70, 60), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Will-O-Wisp', 'Pain Split', 'Toxic', 'Protect']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs == '252 HP / 252 Def'
        assert result.nature == 'Bold'

    def test_forretress(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Forretress', species='Forretress', abilities=(), pkTypes=(), sets=(),
                            baseStats=(75, 90, 140, 60, 60, 40), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Spikes', 'Toxic Spikes', 'Rapid Spin', 'Protect']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs == '252 HP / 252 Def'
        assert result.nature == 'Impish'

    def test_omastar(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Omastar', species='Omastar', abilities=(), pkTypes=(), sets=(),
                            baseStats=(70, 60, 125, 115, 70, 55), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Surf', 'Stealth Rock', 'Ice Beam', 'Protect']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs == '252 HP / 252 SpA'
        assert result.nature == 'Modest'

class TestDualWall:
    def test_shuckle(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Shuckle', species='Shuckle', abilities=(), pkTypes=(), sets=(),
                            baseStats=(20, 10, 230, 10, 230, 5), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Toxic', 'Encore', 'Rest', 'Knock Off']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs in ('252 HP / 252 Def', '252 HP / 252 SpD')
        assert result.nature in ('Bold', 'Calm', 'Impish', 'Careful', 'Sassy', 'Relaxed')

class TestSpecialWall:
    def test_blissey(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Blissey', species='Blissey', abilities=(), pkTypes=(), sets=(),
                            baseStats=(255, 10, 10, 75, 135, 55), genders=('F',))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Wish', 'Protect', 'Seismic Toss', 'Toxic']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs in ('252 Def / 252 SpD', '252 HP / 252 Def', '252 HP / 252 SpD')
        assert result.nature in ('Calm', 'Bold')

    def test_blissey_2(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Blissey', species='Blissey', abilities=(), pkTypes=(), sets=(),
                            baseStats=(255, 10, 10, 75, 135, 55), genders=('F',))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Hyper Beam', 'Shadow Ball', 'Wish', 'Protect']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs in ('252 HP / 252 SpA', '252 SpA / 252 Spe', '252 HP / 252 Def', '252 HP / 252 SpD')
        assert result.nature in ('Timid', 'Modest', 'Bold', 'Calm')

    def test_cresselia(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Cresselia', species='Cresselia', abilities=(), pkTypes=(), sets=(),
                            baseStats=(120, 70, 120, 75, 130, 85), genders=('F',))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Moonlight', 'Psychic', 'Icy Wind', 'Thunder Wave']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs in ('252 Def / 252 SpD', '252 HP / 252 Def', '252 HP / 252 SpD')
        assert result.nature in ('Calm', 'Bold')

    def test_mantine(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Mantine', species='Mantine', abilities=(), pkTypes=(), sets=(),
                            baseStats=(65, 40, 70, 80, 140, 70), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Roost', 'Haze', 'Protect', 'Air Slash']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs == '252 HP / 252 SpD'
        assert result.nature == 'Calm'


class TestUtility:
    def test_dewgong(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Dewgong', species='Dewgong', abilities=(), pkTypes=(), sets=(),
                            baseStats=(90, 70, 80, 70, 95, 70), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Perish Song', 'Whirlpool', 'Protect', 'Rest']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs in ('252 HP / 252 SpD', '252 HP / 252 Def')
        assert result.nature in ('Calm', 'Bold')

    def test_walrein(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Walrein', species='Walrein', abilities=(), pkTypes=(), sets=(),
                            baseStats=(110, 80, 90, 95, 90, 65), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Fissure', 'Sheer Cold', 'Sleep Talk', 'Rest']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs in ('252 HP / 252 SpD', '252 HP / 252 Def')
        assert result.nature in ('Calm', 'Bold')

    def test_dusclops(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Dusclops', species='Dusclops', abilities=(), pkTypes=(), sets=(),
                                        baseStats=(40, 70, 130, 60, 130, 25), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Will-O-Wisp', 'Pain Split', 'Trick Room', 'Confuse Ray']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs in ('252 HP / 252 Def', '252 HP / 252 SpD')
        assert result.nature in ('Relaxed', 'Sassy')

    def test_gastrodon(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Gastrodon', species='Gastrodon', abilities=(), pkTypes=(), sets=(),
                                        baseStats=(111, 83, 68, 92, 82, 39), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Will-O-Wisp', 'Recover', 'Icy Wind', 'Muddy Water']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs in ('252 HP / 252 Def', '252 HP / 252 SpD')
        assert result.nature in ('Relaxed', 'Sassy', 'Calm', 'Bold')

class TestWallbreaker:
    def test_marowak(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Marowak', species='Marowak', abilities=(), pkTypes=(), sets=(),
                                    baseStats=(60, 80, 110, 50, 80, 45), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Swords Dance', 'Earthquake', 'Stone Edge', 'Protect']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs == '252 HP / 252 Atk'
        assert result.nature == 'Adamant'

class TestEdgeCases:
    def test_belly_drum_linoone(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Linoone', species='Linoone', abilities=(), pkTypes=(), sets=(),
                                        baseStats=(78, 70, 61, 50, 61, 100), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Belly Drum', 'Extreme Speed', 'Shadow Claw', 'Protect']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs == '252 Atk / 252 Spe'
        assert result.nature == 'Jolly'

    def test_counter_forretress(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Forretress', species='Forretress', abilities=(), pkTypes=(), sets=(),
                                        baseStats=(75, 90, 140, 60, 60, 40), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Spikes', 'Stealth Rock', 'Counter', 'Payback']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs == '252 HP / 252 Def'
        assert result.nature == 'Impish'

    def test_explosion_gengar(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Gengar', species='Gengar', abilities=(), pkTypes=(), sets=(),
                                        baseStats=(60, 65, 60, 130, 75, 110), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Shadow Ball', 'Focus Blast', 'Thunderbolt', 'Explosion']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs == '252 SpA / 252 Spe'
        assert result.nature in ('Timid', 'Modest')

class TestChallenge:
    def test_seismic_toss_chansey(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Chansey', species='Chansey', abilities=(), pkTypes=(), sets=(),
                                        baseStats=(250, 5, 5, 35, 105, 50), genders=('F',))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Seismic Toss', 'Toxic', 'Soft-Boiled', 'Aromatherapy']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs == '252 HP / 252 Def'
        assert result.nature == 'Bold'

    def test_swords_dance_lucario(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Lucario', species='Lucario', abilities=(), pkTypes=(), sets=(),
                                        baseStats=(70, 110, 70, 115, 70, 90), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Swords Dance', 'Extreme Speed', 'Copycat', 'Protect']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs == '252 HP / 252 Atk'
        assert result.nature == 'Adamant'

    def test_willowisp_dusknoir(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Dusknoir', species='Dusknoir', abilities=(), pkTypes=(), sets=(),
                                        baseStats=(45, 100, 135, 65, 135, 45), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Will-O-Wisp', 'Pain Split', 'Shadow Sneak', 'Ice Punch']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs == '252 HP / 252 SpD'
        assert result.nature == 'Careful'

    def test_ninjask(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Ninjask', species='Ninjask', abilities=(), pkTypes=(), sets=(),
                                        baseStats=(61, 90, 45, 50, 50, 160), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Protect', 'Substitute', 'Baton Pass', 'Swords Dance']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs in ('252 HP / 252 SpD', '252 HP / 252 Def')
        assert result.nature in ('Calm', 'Bold')

    def test_ninjask_2(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Ninjask', species='Ninjask', abilities=(), pkTypes=(), sets=(),
                                        baseStats=(61, 90, 45, 50, 50, 160), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Dig', 'Substitute', 'Baton Pass', 'Swords Dance']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs in ('252 HP / 252 Atk', '252 HP / 252 Def', '252 HP / 252 SpD')
        assert result.nature in ('Adamant', 'Careful', 'Impish')

    def test_mothim(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Mothim', species='Mothim', abilities=(), pkTypes=(), sets=(),
                                        baseStats=(70, 94, 50, 94, 50, 66), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Protect', 'Skill Swap', 'Safeguard', 'U-turn']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs in ('252 HP / 252 Atk', '252 HP / 252 Def', '252 HP / 252 SpD')
        assert result.nature in ('Adamant', 'Careful', 'Impish')

    def test_vespiquen(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Vespiquen', species='Vespiquen', abilities=(), pkTypes=(), sets=(),
                                        baseStats=(70, 80, 102, 80, 102, 40), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Protect', 'Defend Order', 'Attack Order', 'Air Cutter']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs in ('252 HP / 252 Atk', '252 HP / 252 Def', '252 HP / 252 SpD')
        assert result.nature in ('Brave', 'Sassy', 'Relaxed')

class TestVariety:
    def test_empoleon_calm(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Empoleon', species='Empoleon', abilities=(), pkTypes=(), sets=(),
                            baseStats=(84, 86, 88, 111, 101, 60), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Protect', 'Stealth Rock', 'Roar', 'Surf']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs in '252 HP / 252 SpD'
        assert result.nature == 'Calm'

    def test_empoleon_modest(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Empoleon', species='Empoleon', abilities=(), pkTypes=(), sets=(),
                            baseStats=(84, 86, 88, 111, 101, 60), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Protect', 'Feather Dance', 'Hydro Cannon', 'Flash Cannon']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs in '252 HP / 252 SpA'
        assert result.nature == 'Modest'

    def test_empoleon_modest_or_timid(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Empoleon', species='Empoleon', abilities=(), pkTypes=(), sets=(),
                            baseStats=(84, 86, 88, 111, 101, 60), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Protect', 'Agility', 'Hydro Cannon', 'Flash Cannon']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs in ('252 HP / 252 SpA', '252 SpA / 252 Spe')
        assert result.nature in ('Modest', 'Timid')

    def test_empoleon_adamant(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Empoleon', species='Empoleon', abilities=(), pkTypes=(), sets=(),
                            baseStats=(84, 86, 88, 111, 101, 60), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Protect', 'Knock Off', 'Drill Peck', 'Aqua Jet']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs in '252 HP / 252 Atk'
        assert result.nature == 'Adamant'

    def test_empoleon_adamant_or_jolly(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Empoleon', species='Empoleon', abilities=(), pkTypes=(), sets=(),
                            baseStats=(84, 86, 88, 111, 101, 60), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Protect', 'Agility', 'Drill Peck', 'Waterfall']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs in ('252 HP / 252 Atk', '252 Atk / 252 Spe')
        assert result.nature in ('Adamant', 'Jolly')

    def test_empoleon_careful(self, db_root):
        pk_set = pokemon_ddl.PokemonSet(name='Empoleon', species='Empoleon', abilities=(), pkTypes=(), sets=(),
                            baseStats=(84, 86, 88, 111, 101, 60), genders=('M', 'F'))
        pk_indiv = pokemon_ddl.PokemonIndiv()
        pk_indiv.moves = ['Protect', 'Knock Off', 'Stealth Rock', 'Roar']
        result = pk_set.chooseEVsAndNature(pk_indiv, db_root, debug=True)
        assert result.EVs in '252 HP / 252 SpD'
        assert result.nature == 'Careful'