import ZODB, ZODB.FileStorage
import functions
import csv
import os

STORAGE = ZODB.FileStorage.FileStorage('./data/PokeData.fs')
DB = ZODB.DB(STORAGE)
CONNECTION = DB.open()
DB_ROOT = CONNECTION.root

def main():

    pk_name, chosen_pk = functions.getPokemonTeam(1, DB_ROOT)
    indiv_in_list = functions.createIndivPokemon(chosen_pk, DB_ROOT)
    indiv = indiv_in_list[0]
    print(indiv.toString())
    print(indiv.hpStat, indiv.atkStat, indiv.defStat, indiv.spaStat, indiv.spdStat, indiv.speStat)

    while (chosen_item := input('Item: ')) not in DB_ROOT.items['items']:
        print('Item not found')

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



        if not_exists:
            writer.writerow(header_row)
        writer.writerow(input_layer)

if __name__ == '__main__':
    main()