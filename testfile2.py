import numpy as np
import matplotlib.pyplot as plt

# --- Your data remains unchanged ---
pokemon_weights = {
    # Dragon
    'Dragonite': 2.0, 'Kingdra': 2.2, 'Flygon': 2.2, 'Salamence': 2.0, 'Latias': 0.5, 'Latios': 0.5, 'Rayquaza': 0.2,
    'Dialga': 0.2, 'Palkia': 0.25, 'Giratina': 0.2, 'Arceus-Dragon': 0.015,

    # Ice
    'Dewgong': 1.5, 'Cloyster': 2.0, 'Jynx': 1.2, 'Lapras': 2.0, 'Articuno': 2.0, 'Delibird': 0.1, 'Glalie': 2.0,
    'Walrein': 2.0, 'Regice': 2.0, 'Abomasnow': 3.0, 'Weavile': 2.0, 'Glaceon': 2.0, 'Mamoswine': 2.0, 'Froslass': 2.0,
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
    'Typhlosion': 2.0, 'Magcargo': 0.5, 'Entei': 1.5, 'Ho-oh': 0.2, 'Camerupt': 1.5, 'Torkoal': 0.5, 'Magmortar': 2.0,
    'Heatran': 1.6, 'Arceus-Fire': 0.015,

    # Ghost
    'Gengar': 2.0, 'Shedinja': 1.3, 'Banette': 1.1, 'Drifblim': 1.5, 'Mismagius': 1.0, 'Dusknoir': 2.0,
    'Rotom': 0.3,
    'Rotom-Fan': 0.7, 'Rotom-Frost': 0.7, 'Rotom-Heat': 0.7, 'Rotom-Mow': 0.7, 'Rotom-Wash': 0.7,
    # Forms weighted individually
    'Arceus-Ghost': 0.015,

    # Steel
    'Forretress': 2.0, 'Steelix': 2.0, 'Scizor': 2.0, 'Skarmory': 2.0, 'Mawile': 1.0, 'Aggron': 2.0, 'Metagross': 2.0,
    'Registeel': 1.0, 'Jirachi': 0.5, 'Empoleon': 2.0, 'Bastiodon': 1.0,
    'Wormadam-Trash': 0.2,
    'Bronzong': 2.0, 'Magnezone': 2.0, 'Probopass': 1.2, 'Arceus-Steel': 0.015,

    # Electric
    'Raichu': 2.0, 'Electrode': 2.0, 'Jolteon': 2.0, 'Zapdos': 2.0, 'Lanturn': 1.5, 'Ampharos': 2.0, 'Raikou': 1.5,
    'Manectric': 2.0,
    'Plusle': 0.25, 'Minun': 0.25,  # Set with total value of 1 -> 0.5 each
    'Luxray': 2.0, 'Pachirisu': 1.0, 'Electivire': 2.0, 'Arceus-Electric': 0.015,

    # Rock
    'Golem': 2.0, 'Omastar': 2.0, 'Kabutops': 2.0, 'Aerodactyl': 2.0, 'Sudowoodo': 1.0, 'Shuckle': 1.0, 'Corsola': 0.1,
    'Lunatone': 0.3, 'Solrock': 0.3,  # Paired set -> 1.0 each
    'Cradily': 2.0, 'Armaldo': 2.0, 'Relicanth': 2.0, 'Regirock': 2.0, 'Rampardos': 2.0, 'Rhyperior': 2.0,
    'Arceus-Rock': 0.015,

    # Poison
    'Venusaur': 2.0, 'Beedrill': 1.0, 'Arbok': 1.1, 'Nidoqueen': 2.0, 'Nidoking': 2.0, 'Vileplume': 2.0,
    'Venomoth': 1.0, 'Victreebel': 2.0, 'Tentacruel': 2.0, 'Muk': 2.0, 'Weezing': 2.0, 'Ariados': 0.6, 'Crobat': 2.0,
    'Dustox': 0.5, 'Swalot': 1.0, 'Seviper': 1.5, 'Roserade': 2.0, 'Arceus-Poison': 0.015,

    # Ground
    'Sandslash': 2.0, 'Dugtrio': 1.5, 'Marowak': 2.0, 'Quagsire': 2.0, 'Donphan': 2.0, 'Swampert': 2.0, 'Whiscash': 1.5,
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
    'Pidgeot': 1.3, 'Fearow': 1.3, 'Farfetch\'d': 0.5, 'Dodrio': 2.0, 'Gyarados': 2.0, 'Noctowl': 1.0, 'Mantine': 1.5,
    'Swellow': 2.0, 'Pelipper': 1.0, 'Altaria': 2.1, 'Staraptor': 2.0, 'Chatot': 0.5, 'Togekiss': 2.0,
    'Arceus-Flying': 0.015,

    # Normal
    'Raticate': 0.8, 'Clefable': 2.0, 'Wigglytuff': 1.0, 'Persian': 2.0, 'Kangaskhan': 2.0, 'Ditto': 1.2, 'Tauros': 2.0,
    'Snorlax': 2.0, 'Furret': 1.0, 'Dunsparce': 1.0, 'Granbull': 1.0, 'Ursaring': 2.0, 'Porygon2': 2.0, 'Stantler': 1.0,
    'Smeargle': 2.0, 'Miltank': 2.0, 'Blissey': 2.0, 'Linoone': 1.0, 'Slaking': 2.0, 'Exploud': 2.0, 'Delcatty': 0.5,
    'Spinda': 0.5, 'Zangoose': 2.0, 'Kecleon': 1.0, 'Bibarel': 1.0, 'Ambipom': 2.0, 'Lopunny': 2.0, 'Purugly': 1.0,
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
    'Starmie': ['Water', 'Psychic'], 'Mr. Mime': ['Psychic'], 'Scizor': ['Bug', 'Steel'], 'Jynx': ['Ice', 'Psychic'],
    'Pinsir': ['Bug'], 'Tauros': ['Normal'], 'Gyarados': ['Water', 'Flying'], 'Lapras': ['Water', 'Ice'],
    'Ditto': ['Normal'], 'Vaporeon': ['Water'], 'Jolteon': ['Electric'], 'Flareon': ['Fire'], 'Porygon2': ['Normal'],
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
    'Sneasel': ['Dark', 'Ice'], 'Ursaring': ['Normal'], 'Magcargo': ['Fire', 'Rock'], 'Swinub': ['Ice', 'Ground'],
    'Corsola': ['Water', 'Rock'], 'Octillery': ['Water'], 'Delibird': ['Ice', 'Flying'], 'Mantine': ['Water', 'Flying'],
    'Skarmory': ['Steel', 'Flying'], 'Houndoom': ['Dark', 'Fire'], 'Kingdra': ['Water', 'Dragon'],
    'Donphan': ['Ground'], 'Porygon-Z': ['Normal'], 'Stantler': ['Normal'], 'Smeargle': ['Normal'],
    'Hitmontop': ['Fighting'], 'Miltank': ['Normal'], 'Blissey': ['Normal'], 'Raikou': ['Electric'], 'Entei': ['Fire'],
    'Suicune': ['Water'], 'Tyranitar': ['Rock', 'Dark'], 'Lugia': ['Psychic', 'Flying'], 'Ho-oh': ['Fire', 'Flying'],
    'Celebi': ['Psychic', 'Grass'], 'Sceptile': ['Grass'], 'Blaziken': ['Fire', 'Fighting'],
    'Swampert': ['Water', 'Ground'], 'Mightyena': ['Dark'], 'Linoone': ['Normal'], 'Beautifly': ['Bug', 'Flying'],
    'Dustox': ['Bug', 'Poison'], 'Ludicolo': ['Water', 'Grass'], 'Shiftry': ['Grass', 'Dark'],
    'Swellow': ['Normal', 'Flying'], 'Pelipper': ['Water', 'Flying'], 'Gardevoir': ['Psychic'],
    'Masquerain': ['Bug', 'Flying'], 'Breloom': ['Grass', 'Fighting'], 'Slaking': ['Normal'],
    'Ninjask': ['Bug', 'Flying'], 'Shedinja': ['Bug', 'Ghost'], 'Exploud': ['Normal'], 'Hariyama': ['Fighting'],
    'Delcatty': ['Normal'], 'Sableye': ['Dark', 'Ghost'], 'Mawile': ['Steel'], 'Aggron': ['Steel', 'Rock'],
    'Medicham': ['Fighting', 'Psychic'], 'Manectric': ['Electric'], 'Plusle': ['Electric'], 'Minun': ['Electric'],
    'Volbeat': ['Bug'], 'Illumise': ['Bug'], 'Roserade': ['Grass', 'Poison'], 'Swalot': ['Poison'],
    'Camerupt': ['Fire', 'Ground'], 'Torkoal': ['Fire'], 'Grumpig': ['Psychic'], 'Spinda': ['Normal'],
    'Flygon': ['Ground', 'Dragon'], 'Cacturne': ['Grass', 'Dark'], 'Altaria': ['Dragon', 'Flying'],
    'Zangoose': ['Normal'], 'Seviper': ['Poison'], 'Lunatone': ['Rock', 'Psychic'], 'Solrock': ['Rock', 'Psychic'],
    'Whiscash': ['Water', 'Ground'], 'Crawdaunt': ['Water', 'Dark'], 'Claydol': ['Ground', 'Psychic'],
    'Cradily': ['Rock', 'Grass'], 'Armaldo': ['Rock', 'Bug'], 'Milotic': ['Water'], 'Kecleon': ['Normal'],
    'Banette': ['Ghost'], 'Tropius': ['Grass', 'Flying'], 'Chimecho': ['Psychic'], 'Absol': ['Dark'], 'Glalie': ['Ice'],
    'Walrein': ['Ice', 'Water'], 'Huntail': ['Water'], 'Gorebyss': ['Water'], 'Relicanth': ['Water', 'Rock'],
    'Luvdisc': ['Water'], 'Salamence': ['Dragon', 'Flying'], 'Metagross': ['Steel', 'Psychic'], 'Regirock': ['Rock'],
    'Regice': ['Ice'], 'Registeel': ['Steel'], 'Latias': ['Dragon', 'Psychic'], 'Latios': ['Dragon', 'Psychic'],
    'Kyogre': ['Water'], 'Groudon': ['Ground'], 'Rayquaza': ['Dragon', 'Flying'], 'Jirachi': ['Steel', 'Psychic'],
    'Deoxys': ['Psychic'], 'Deoxys-Attack': ['Psychic'], 'Deoxys-Defense': ['Psychic'], 'Deoxys-Speed': ['Psychic'],
    'Torterra': ['Grass', 'Ground'], 'Infernape': ['Fire', 'Fighting'], 'Empoleon': ['Water', 'Steel'],
    'Staraptor': ['Normal', 'Flying'], 'Bibarel': ['Normal', 'Water'], 'Kricketune': ['Bug'], 'Luxray': ['Electric'],
    'Bastiodon': ['Rock', 'Steel'], 'Wormadam': ['Bug', 'Grass'], 'Wormadam-Sandy': ['Bug', 'Ground'],
    'Wormadam-Trash': ['Bug', 'Steel'], 'Mothim': ['Bug', 'Flying'], 'Vespiquen': ['Bug', 'Flying'],
    'Pachirisu': ['Electric'], 'Floatzel': ['Water'], 'Cherrim': ['Grass'], 'Gastrodon': ['Water', 'Ground'],
    'Gastrodon-East': ['Water', 'Ground'], 'Ambipom': ['Normal'], 'Drifblim': ['Ghost', 'Flying'],
    'Lopunny': ['Normal'], 'Mismagius': ['Ghost'], 'Honchkrow': ['Dark', 'Flying'], 'Purugly': ['Normal'],
    'Skuntank': ['Poison', 'Dark'], 'Bronzong': ['Steel', 'Psychic'], 'Chatot': ['Normal', 'Flying'],
    'Spiritomb': ['Ghost', 'Dark'], 'Garchomp': ['Dragon', 'Ground'], 'Lucario': ['Fighting', 'Steel'],
    'Hippowdon': ['Ground'], 'Toxicroak': ['Poison', 'Fighting'], 'Carnivine': ['Grass'], 'Lumineon': ['Water'],
    'Abomasnow': ['Grass', 'Ice'], 'Weavile': ['Dark', 'Ice'], 'Magnezone': ['Electric', 'Steel'],
    'Electivire': ['Electric'], 'Magmortar': ['Fire'], 'Togekiss': ['Normal', 'Flying'], 'Yanmega': ['Bug', 'Flying'],
    'Leafeon': ['Grass'], 'Glaceon': ['Ice'], 'Gliscor': ['Ground', 'Flying'], 'Mamoswine': ['Ice', 'Ground'],
    'Gallade': ['Psychic', 'Fighting'], 'Probopass': ['Rock', 'Steel'], 'Dusknoir': ['Ghost'],
    'Froslass': ['Ice', 'Ghost'], 'Rotom': ['Electric', 'Ghost'], 'Rotom-Heat': ['Electric', 'Fire'],
    'Rotom-Wash': ['Electric', 'Water'], 'Rotom-Frost': ['Electric', 'Ice'], 'Rotom-Mow': ['Electric', 'Grass'],
    'Rotom-Fan': ['Electric', 'Flying'], 'Uxie': ['Psychic'], 'Mesprit': ['Psychic'], 'Azelf': ['Psychic'],
    'Dialga': ['Steel', 'Dragon'], 'Palkia': ['Water', 'Dragon'], 'Heatran': ['Fire', 'Steel'], 'Regigigas': ['Normal'],
    'Giratina': ['Ghost', 'Dragon'], 'Cresselia': ['Psychic'], 'Phione': ['Water'], 'Manaphy': ['Water'],
    'Darkrai': ['Dark'], 'Shaymin': ['Grass'], 'Arceus': ['Normal'], 'Arceus-Fighting': ['Fighting'],
    'Arceus-Flying': ['Flying'], 'Arceus-Poison': ['Poison'], 'Arceus-Ground': ['Ground'], 'Arceus-Rock': ['Rock'],
    'Arceus-Bug': ['Bug'], 'Arceus-Ghost': ['Ghost'], 'Arceus-Steel': ['Steel'], 'Arceus-Fire': ['Fire'],
    'Arceus-Water': ['Water'], 'Arceus-Grass': ['Grass'], 'Arceus-Electric': ['Electric'],
    'Arceus-Psychic': ['Psychic'], 'Arceus-Ice': ['Ice'], 'Arceus-Dragon': ['Dragon'], 'Arceus-Dark': ['Dark']
}

TYPE_NAMES = ['Dragon', 'Ice', 'Fighting', 'Dark', 'Fire', 'Ghost', 'Steel', 'Electric', 'Rock', 'Poison', 'Ground',
              'Bug', 'Grass', 'Psychic', 'Flying', 'Normal', 'Water']


def calculate_probabilities(smoothing_factor: float) -> dict:
    """Calculates the final, normalized probabilities for each Pokémon."""
    # Step 1: Calculate raw type totals based on normalized contribution
    raw_type_totals = {name: 0.0 for name in TYPE_NAMES}
    for pokemon, weight in pokemon_weights.items():
        types = pokemon_to_types_map.get(pokemon)
        if not types: continue
        contribution_per_type = 1.0 / len(types)
        for p_type in types:
            raw_type_totals[p_type] += contribution_per_type

    # Step 2: Smooth the raw totals
    raw_totals_list = list(raw_type_totals.values())
    average_total = np.mean(raw_totals_list)
    smoothed_type_totals = {
        k: (average_total - v) * smoothing_factor + v
        for k, v in raw_type_totals.items()
    }

    # Step 3: Calculate the final scaled weight for each Pokémon
    pokemon_scaled_weights = {}
    total_scaled_weights = 0
    for name, weight in pokemon_weights.items():
        types = pokemon_to_types_map.get(name)
        if not types: continue

        scaler = sum(smoothed_type_totals[p_type] for p_type in types) / len(types)
        scaled_weight = scaler * weight
        pokemon_scaled_weights[name] = scaled_weight
        total_scaled_weights += scaled_weight

    # Step 4: Normalize to get final probabilities that sum to 1.0
    return {k: v / total_scaled_weights for k, v in pokemon_scaled_weights.items()}


if __name__ == '__main__':
    # --- Analysis Setup ---
    smoothing_factors = np.linspace(0, 1, 21)  # Test factors from 0.0 to 1.0
    results = []

    # Calculate the baseline probabilities (at smoothing=0)
    baseline_probs = calculate_probabilities(smoothing_factor=0.0)
    baseline_probs_array = np.array(list(baseline_probs.values()))

    print("Running analysis for different smoothing factors...")
    for factor in smoothing_factors:
        print(f"  Testing factor: {factor:.2f}")

        current_probs = calculate_probabilities(factor)

        # --- METRIC CALCULATION ---
        # Metric 1: Type Evenness (lower is better)
        type_final_probs = {name: 0.0 for name in TYPE_NAMES}
        for name, prob in current_probs.items():
            types = pokemon_to_types_map.get(name)
            if not types: continue
            for p_type in types:
                type_final_probs[p_type] += prob / len(types)
        type_evenness = np.std(list(type_final_probs.values()))

        # Metric 2: Deviation from Base (higher is worse)
        current_probs_array = np.array(list(current_probs.values()))
        deviation_from_base = np.sum((current_probs_array - baseline_probs_array) ** 2)

        results.append({
            "factor": factor,
            "type_evenness": type_evenness,
            "deviation": deviation_from_base,
        })
    print("Analysis complete.")

    # --- Data Preparation for Plotting ---
    type_evenness_data = np.array([r['type_evenness'] for r in results])
    deviation_data = np.array([r['deviation'] for r in results])

    # Normalize both metrics to a 0-1 scale to find the intersection
    norm_evenness = (type_evenness_data - type_evenness_data.min()) / (
                type_evenness_data.max() - type_evenness_data.min())
    norm_deviation = (deviation_data - deviation_data.min()) / (deviation_data.max() - deviation_data.min())

    # Find the intersection point
    diff = np.abs(norm_evenness - norm_deviation)
    intersect_idx = np.argmin(diff)
    optimal_factor = smoothing_factors[intersect_idx]

    # --- Plotting the results ---
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(12, 8))

    ax.plot(smoothing_factors, norm_evenness, 'o-', color='royalblue', label='Type Imbalance (0 = Most Even)')
    ax.plot(smoothing_factors, norm_deviation, 'x-', color='firebrick', label='Deviation from Base Weights (0 = None)')

    # Highlight the intersection point
    ax.axvline(optimal_factor, color='gray', linestyle='--', label=f'Optimal Factor = {optimal_factor:.2f}')
    ax.plot(optimal_factor, norm_evenness[intersect_idx], 'ko', markersize=10, zorder=5)

    ax.set_xlabel('Smoothing Factor (0 = Type Popularity Matters, 1 = All Types Equal)')
    ax.set_ylabel('Normalized Score (0 = Best, 1 = Worst)')
    ax.set_title('Finding the Optimal Balance Between Type Evenness and Weight Faithfulness')
    ax.legend()

    plt.show()

    print(f"\nAnalysis complete.")
    print(
        f"The optimal smoothing factor where the two metrics are most balanced is approximately: {optimal_factor:.2f}")