import sys
import os
import ZODB, ZODB.FileStorage
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pokemon_ddl

def get_PokemonSets_from_db():
    storage = ZODB.FileStorage.FileStorage('../data/PokeData.fs')
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root
    pokemon = list(root.pokesets.keys())
    connection.close()
    return pokemon

@pytest.fixture(scope='module')
def db_root():
    storage = ZODB.FileStorage.FileStorage('../data/PokeData.fs')
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root
    yield root
    connection.close()


@pytest.mark.parametrize("name", get_PokemonSets_from_db())
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
