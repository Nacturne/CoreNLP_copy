from Core import TreeClass as tc
import pandas as pd

file_original = open('input/test.txt', 'r')
file_predicted = open('input/full_hid25_re0-0007-test.txt', 'r')

original_temp = []
predicted_temp = []


for line in file_original:
    original_tree = tc.ScoreTree(line)

    for node in original_tree.allNodes():
        if not node.isLeaf():
            data_entry = [] # will be populated with ['score', 'l_child_score', 'r_child_score', 'phrase_length']
            data_entry.append(int(node.label))
            data_entry.append(int(node.children[0].label))
            data_entry.append(int(node.children[1].label))
            data_entry.append(node.num_phrases())
            original_temp.append(data_entry)



for line in file_predicted:
    predicted_tree = tc.ScoreTree(line)

    for node in predicted_tree.allNodes():
        if not node.isLeaf():
            data_entry = [] # will be populated with ['pred_score', 'pred_phrase_length']
            data_entry.append(int(node.label))
            data_entry.append(node.num_phrases())
            predicted_temp.append(data_entry)


original_frame = pd.DataFrame(original_temp, columns=['score', 'l_child_score', 'r_child_score', 'phrase_length'])
predicted_frame = pd.DataFrame(predicted_temp, columns=['pred_score', 'pred_phrase_length'])

result = pd.concat([original_frame, predicted_frame], axis=1)
result.to_csv('output/stats.txt',sep='\t')




file_original.close()
file_predicted.close()