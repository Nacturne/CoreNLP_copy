from Core import TreeClass as tc

sign = '3_1_2'

file_in = open('output/correct_example/row_sentences/' + sign + '.txt', 'r')

sentence_list = file_in.readlines()

for i in range(10):
    original_tree = tc.ScoreTree(sentence_list[2*i])
    predicted_tree = tc.ScoreTree(sentence_list[2*i+1])

    file_out = open('output/correct_example/' + sign + '/original_' + str(i+1) + '.dot', 'w')
    file_out.write(original_tree.toGraphInput())
    file_out.close()

    file_out = open('output/correct_example/' + sign + '/predicted_' + str(i+1) + '.dot', 'w')
    file_out.write(predicted_tree.toGraphInput())
    file_out.close()




file_in.close()