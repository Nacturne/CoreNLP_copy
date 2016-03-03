from Core import TreeClass as tc

file_original = open('input/test.txt', 'r')
file_predicted = open('input/full_hid25_re0-0007-test.txt', 'r')

sign = '3_1_2'

file_out = open('output/correct_example/row_sentences/' + sign + '.txt', 'w')

counter = 0

original_list = file_original.readlines()
predicted_list = file_predicted.readlines()





#(l_child, r_child, parent) = (2, 2, 1)
for i in range(len(original_list)):
    original_tree = tc.ScoreTree(original_list[i])
    predicted_tree = tc.ScoreTree(predicted_list[i])
    original_node_list = original_tree.allNodes()
    predicted_node_list = predicted_tree.allNodes()

    for j in range(len(original_node_list)):
        original_node = original_node_list[j]
        predicted_node = predicted_node_list[j]

        if not original_node.isLeaf():
            if (original_node.children[0].label in ['3','4']) and \
                    (original_node.children[1].label in ['0','1']) and \
                    (original_node.label in ['2']) and \
                    (predicted_node.label in ['2']) and \
                    (counter < 10):
                file_out.write(original_node.toPTB() + '\n')
                file_out.write(predicted_node.toPTB() + '\n')
                counter += 1


file_original.close()
file_predicted.close()
file_out.close()

'''
for i in range(len(predicted_list)):
    predicted_tree = tc.ScoreTree(predicted_list[i])
    node_list = predicted_tree.allNodes()
'''