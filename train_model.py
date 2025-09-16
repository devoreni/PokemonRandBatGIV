import matplotlib
matplotlib.use('TkAgg')
import pickle
from sklearn import tree
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

    clf = tree.DecisionTreeClassifier(max_depth=15)
    clf = clf.fit(train, answer)
    packed = {'model': clf, 'keys': num_to_item}
    print(store_model(packed))

    '''class_names = [num_to_item[i] for i in range(len(num_to_item))]
    plt.figure(figsize=(20, 9))
    tree.plot_tree(clf,
                   max_depth=5,
                   feature_names=feature_names,
                   class_names=class_names,
                   filled=True,
                   fontsize=10)
    plt.savefig('decision_tree_overview.png', dpi=300)
    plt.show()'''
    return

if __name__ == '__main__':
    train_decision_tree()