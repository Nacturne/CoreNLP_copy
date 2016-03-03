from Core import TreeClass as tc

file_in = open('output/gram_5_2_diff.txt','r')
lines = file_in.readlines()
for i in range(len(lines)/4):
    tree = tc.ScoreTree(lines[i*4])
    file_out = open('output/gram_5_2_diff/pair_{0}_a_original.dot'.format(i+1), 'w')
    file_out.write(tree.toGraphInput())
    file_out.close()

    tree = tc.ScoreTree(lines[i*4+1])
    file_out = open('output/gram_5_2_diff/pair_{0}_a_predicted.dot'.format(i+1), 'w')
    file_out.write(tree.toGraphInput())
    file_out.close()

    tree = tc.ScoreTree(lines[i*4+2])
    file_out = open('output/gram_5_2_diff/pair_{0}_b_original.dot'.format(i+1), 'w')
    file_out.write(tree.toGraphInput())
    file_out.close()

    tree = tc.ScoreTree(lines[i*4+3])
    file_out = open('output/gram_5_2_diff/pair_{0}_b_predicted.dot'.format(i+1), 'w')
    file_out.write(tree.toGraphInput())
    file_out.close()





file_in.close()