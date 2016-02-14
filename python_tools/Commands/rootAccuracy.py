import config
import argparse
import pandas as pd
import warnings
from Core import TreeClass
from sklearn import metrics



parser = argparse.ArgumentParser()
parser.add_argument('Original', metavar='original_file', type=str, help="The path of the original file")
parser.add_argument('Predicted', metavar='predicted_file', type=str, help="The path of the file predicted by model")
args = parser.parse_args()

file_in = open(config.ROOT_DIR + '/' + args.Original, 'r')
temp = []
for s in file_in:
    if s[0] == '(':
        tree = TreeClass.ScoreTree(s)
        for node in tree.allNodes():
            temp.append([int(node.label), node.num_phrases(), int(node.isRoot())])
file_in.close()
stats_original = pd.DataFrame(temp, columns=['score', 'num_phrases', 'is_root'])

file_in = open(config.ROOT_DIR + '/' + args.Predicted, 'r')
temp = []
for s in file_in:
    if s[0] == '(':
        tree = TreeClass.ScoreTree(s)
        for node in tree.allNodes():
            temp.append([int(node.label), node.num_phrases(),  int(node.isRoot())])
file_in.close()
stats_predicted = pd.DataFrame(temp, columns=['score', 'num_phrases', 'is_root'])

root_original = stats_original[stats_original['is_root'] == 1]
root_predicted = stats_predicted[stats_predicted['is_root'] == 1]


with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    root_original['score'].replace([0,4],[1,3],inplace=True)
    root_predicted['score'].replace([0,4],[1,3],inplace=True)

original_1 = root_original[root_original['score'] == 1]
predicted_1 = root_predicted[root_original['score'] == 1]

original_2 = root_original[root_original['score'] == 2]
predicted_2 = root_predicted[root_original['score'] == 2]

original_3 = root_original[root_original['score'] == 3]
predicted_3 = root_predicted[root_original['score'] == 3]

accuracy_1 = metrics.accuracy_score(original_1['score'],predicted_1['score'])
accuracy_2 = metrics.accuracy_score(original_2['score'],predicted_2['score'])
accuracy_3 = metrics.accuracy_score(original_3['score'],predicted_3['score'])


print("---------------------------------------------------------")
print("{0:8}\t{1:8}\t{2:8}\t{3:8}".format('    ','neg','neutral', 'pos'))
print("---------------------------------------------------------")
print('{0:8}\t{1:8.5f}\t{2:8.5f}\t{3:8.5f}'.format('Root',accuracy_1,accuracy_2,accuracy_3))
print("---------------------------------------------------------")
