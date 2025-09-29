import sys
import os
import ZODB, ZODB.FileStorage
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pokemon_ddl

DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'PokeData.fs'))

def get_all_pokemon_names_from_db():
    storage = ZODB.FileStorage.FileStorage(DB_PATH)
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root
    pokemon = list(root.pokesets.keys())
    moves = list(root.moves.keys())
    connection.close()
    return pokemon, moves

ALL_POKEMON_NAMES, ALL_MOVE_NAMES = get_all_pokemon_names_from_db()

@pytest.fixture(scope='module')
def db_root():
    storage = ZODB.FileStorage.FileStorage(DB_PATH)
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root
    yield root
    connection.close()


@pytest.mark.parametrize("name", ALL_POKEMON_NAMES)
def test_PokemonSet_object_MoveSets(name, db_root):
    pk_set = db_root.pokesets[name]
    assert isinstance(pk_set, pokemon_ddl.PokemonSet), f"Object for '{name}' is not a valid PokemonSet."

    # Skip this test for Pokémon that legitimately have no defined movesets yet.
    # This prevents the test from failing unnecessarily on incomplete data.
    if not pk_set.sets:
        pytest.skip(f"Skipping moveset validation for '{name}' because no sets are defined.")

    master_move_list = db_root.moves  # For cleaner access

    for i, move_set in enumerate(pk_set.sets):
        assert isinstance(move_set, pokemon_ddl.MoveSet), \
            f"For '{name}', item {i} in .sets is not a valid MoveSet object."

        # 1. Test the starting moves
        for start_move in move_set.starting:
            # Use 'in' for a clear membership test.
            # The custom message will print only on failure.
            assert start_move in master_move_list, \
                f"Validation failed for Pokémon '{name}' in MoveSet #{i + 1}:\n" \
                f"  > Starting move '{start_move}' does not exist in the master moves database."

        # 2. Test the childrenMatrix nodes and edges
        for parent_move, child_moves in move_set.childrenMatrix.items():
            # Test the parent move (the dictionary key)
            assert parent_move in master_move_list, \
                f"Validation failed for Pokémon '{name}' in MoveSet #{i + 1}:\n" \
                f"  > Parent move '{parent_move}' does not exist in the master moves database."

            # Test each child move in the list of children
            for child_move in child_moves:
                assert child_move in master_move_list, \
                    f"Validation failed for Pokémon '{name}' in MoveSet #{i + 1}:\n" \
                    f"  > Child move '{child_move}' (linked from parent '{parent_move}') does not exist in the master moves database."

@pytest.mark.parametrize('name', ALL_POKEMON_NAMES)
def test_PokemonSet_object_Images(name, db_root):
    pk = db_root.pokesets[name]
    assets = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'assets', 'PokemonSprites'))
    assert os.path.exists(f'{assets}/{pk.images[0]}'), \
        f'For {name}: {pk.images[0]} does not exist in assets'
    assert os.path.exists(f'{assets}/{pk.images[1]}'), \
        f'For {name}: {pk.images[1]} does not exist in assets'
    assert os.path.exists(f'{assets}/{pk.images[2]}'), \
        f'For {name}: {pk.images[2]} does not exist in assets'

@pytest.mark.parametrize('name', ALL_POKEMON_NAMES)
def test_PokemonSet_object_Abilities(name, db_root):
    pk = db_root.pokesets[name]
    assert len(pk.abilities) == len(pk.ability_weights)

@pytest.mark.parametrize('move', ALL_MOVE_NAMES)
def test_Move_object_attributes(move, db_root):
    mv = db_root.moves[move]
    assert type(mv.power) is int
    assert 0 <= mv.accuracy <= 1
    assert mv.category in {'Phys', 'Spec', 'Stat'}
    assert mv.moveType in {'Dragon', 'Ice', 'Fighting', 'Dark', 'Fire', 'Ghost', 'Steel', 'Electric',
              'Rock', 'Poison', 'Ground',
              'Bug', 'Grass', 'Psychic', 'Flying', 'Normal', 'Water'}
    assert mv.name == move
    assert mv.pp > 0

@pytest.mark.parametrize('name', ALL_POKEMON_NAMES)
def test_pokemon_has_type_map(name, db_root):
    assert name in set(db_root.pokeprobability['pokemon_to_types_map'].keys())