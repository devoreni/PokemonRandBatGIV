import pickle
from sklearn import tree
import os
import csv

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

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(train, answer)
    packed = {'model': clf, 'keys': num_to_item}
    print(store_model(packed))
    return

if __name__ == '__main__':
    train_decision_tree()