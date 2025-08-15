import random
from typing import List, Tuple
import ZODB, ZODB.FileStorage
import pokemon_ddl  # Assuming this is the name of your ddl file


def getFullPokemon_corrected(num: int, root) -> Tuple[list, list]:
    """
    Selects a team of `num` Pokémon with better type and species diversity.
    This approach builds a dynamic pool of valid candidates for each selection.
    """
    # Load the master probability lists and type map once
    all_pokemon_names = root.pokeprobability['pokemon'][0]
    all_pokemon_probs = root.pokeprobability['pokemon'][1]
    pokemon_to_types_map = root.pokeprobability['pokemon_to_types_map']

    # Create a dictionary for faster lookups of a pokemon's base probability
    base_probabilities = dict(zip(all_pokemon_names, all_pokemon_probs))

    # These will store the final team
    chosen_objects = []

    # This keeps track of which pokemon are still available to be picked
    remaining_pokemon = all_pokemon_names[:]

    # This keeps track of how many of each type are on the team
    local_type_counts = {type_name: 0 for type_name in root.pokeprobability['type_names']}

    # Define your caps for types and species
    # No more than 2 of any given type on a team of 6.
    TYPE_CAP = max(num // 3, 2)

    for i in range(num):
        # At the start of picking each new team member, build a fresh list of valid candidates
        candidates = []
        candidate_weights = []

        # Get the species of Pokémon already on the team to prevent duplicates
        chosen_species = {p.species for p in chosen_objects}

        # Iterate through all pokemon that haven't been picked yet
        for name in remaining_pokemon:
            species_obj = root.pokesets[name]

            # --- Validation Step ---
            # 1. Check for species duplicates (e.g., no two Wormadam forms)
            if species_obj.species in chosen_species:
                continue  # Skip this pokemon, it's a dupe

            # 2. Check the type cap
            is_valid_by_type = True
            types = pokemon_to_types_map[name]
            for p_type in types:
                if local_type_counts[p_type] >= TYPE_CAP:
                    is_valid_by_type = False
                    break  # This pokemon would violate the type cap

            if not is_valid_by_type:
                continue  # Skip this pokemon

            # If the pokemon is valid, add it to our candidate pool for this round
            candidates.append(name)
            candidate_weights.append(base_probabilities[name])

        # If there are valid candidates, choose one based on their relative weights
        if candidates:
            # This is a fair lottery among all currently valid options
            selected_name = random.choices(candidates, weights=candidate_weights, k=1)[0]
            selected_species_obj = root.pokesets[selected_name]

            # --- Update State for the Next Round ---
            chosen_objects.append(selected_species_obj)
            remaining_pokemon.remove(selected_name)

            # Update the counts for the types of the pokemon we just added
            for p_type in pokemon_to_types_map[selected_name]:
                local_type_counts[p_type] += 1

    # Extract just the names for the return value to match the original function signature
    chosen_names = [p.name for p in chosen_objects]

    return chosen_names, chosen_objects


if __name__ == '__main__':
    storage = ZODB.FileStorage.FileStorage('../data/PokeData.fs')
    db = ZODB.DB(storage)
    connection = db.open()
    root = connection.root

    counts = {type_name: 0 for type_name in root.pokeprobability['type_names']}

    # Run the simulation with the CORRECTED function
    for i in range(1000):  # Increased iterations for a smoother distribution
        chosen_names, chosen_objects = getFullPokemon_corrected(6, root)
        for pokemon in chosen_objects:
            for p_type in pokemon.pkTypes:
                counts[p_type] += 1

    print("--- Corrected Distribution ---")
    # Sort the results for easier reading
    sorted_counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))
    print(sorted_counts)