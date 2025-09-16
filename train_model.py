import matplotlib
matplotlib.use('TkAgg')
import pickle
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
import os
import csv
import matplotlib.pyplot as plt

def store_model(bundle):
    try:
        loader = open('./pickle_model', 'wb')
        pickle.dump(bundle, loader)
        loader.close()
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def train_decision_tree():
    num_to_item = {}
    train, answer = [], []

    feature_names = []

    first_file = os.listdir('./item_files')[0]
    with open(os.path.join('./item_files', first_file), 'r') as f:
        reader = csv.reader(f)
        feature_names = next(reader)
    for i, file in enumerate(os.listdir('./item_files')):
        filepath = os.path.join('./item_files', file)
        with open(filepath, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            num_to_item[i] = file[:-4]
            for row in reader:
                numeric_row = [float(item) for item in row]
                train.append(numeric_row)
                answer.append(i)

    clf = tree.DecisionTreeClassifier(min_samples_leaf=1)
    clf = clf.fit(train, answer)
    packed = {'model': clf, 'keys': num_to_item}
    print(store_model(packed))
    return

def train_random_forrest():
    num_to_item = {}
    train, answer = [], []

    feature_names = []
    if not os.path.exists('./item_files') or not os.listdir('./item_files'):
        print("Error: 'item_files' directory is empty or does not exist.")
        return
    first_file = os.listdir('./item_files')[0]
    with open(os.path.join('./item_files', first_file), 'r') as f:
        reader = csv.reader(f)
        feature_names = next(reader)

    for i, file in enumerate(os.listdir('./item_files')):
        filepath = os.path.join('./item_files', file)
        with open(filepath, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            num_to_item[i] = file[:-4]
            for row in reader:
                numeric_row = [float(item) for item in row]
                train.append(numeric_row)
                answer.append(i)

    clf = RandomForestClassifier(n_estimators=100, min_samples_leaf=1, random_state=42)

    clf = clf.fit(train, answer)
    packed = {'model': clf, 'keys': num_to_item}
    print(store_model(packed))

    return

if __name__ == '__main__':
    # train_decision_tree()
    train_random_forrest()