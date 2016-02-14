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

'''
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    root_original['score'].replace([0,4],[1,3],inplace=True)
    root_predicted['score'].replace([0,4],[1,3],inplace=True)
'''

print("The global F1 score on root is:")
print(metrics.accuracy_score(root_original['score'], root_predicted['score']))