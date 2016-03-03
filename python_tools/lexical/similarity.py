from Core import TreeClass as tc
import numpy as np

file_original = open('input/test.txt', 'r')
file_predicted = open('input/full_hid25_re0-0007-test.txt','r')

gram_5_list_original = []
gram_5_node_list_original = []

gram_5_node_list_predicted = []


for line in file_original:
    tree = tc.ScoreTree(line)
    for node in tree.allNodes():
        if node.num_phrases() == 5:
            gram_5_node_list_original.append(node)

            word_list = [x.word for x in node.wordNodes()]
            gram_5_list_original.append(word_list)


for line in file_predicted:
    tree = tc.ScoreTree(line)
    for node in tree.allNodes():
        if node.num_phrases() == 5:
            gram_5_node_list_predicted.append(node)





for i in range(len(gram_5_list_original)):
    current = gram_5_list_original[i]
    current_words = np.array(current)
    for j in range(i, len(gram_5_list_original)):
        j_words = np.array(gram_5_list_original[j])
        if sum(current_words == j_words) == 4:
            print(gram_5_node_list_original[i].toPTB())
            print(gram_5_node_list_predicted[i].toPTB())
            print(gram_5_node_list_original[j].toPTB())
            print(gram_5_node_list_predicted[j].toPTB())


file_original.close()
file_predicted.close()