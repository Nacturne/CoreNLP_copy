import pandas as pd


def stats(data, score, l_child_score, r_child_score, total_nodes_num):
    selected = data[(data['score'] == score) & (data['l_child_score'] == l_child_score) & (data['r_child_score'] == r_child_score)]
    sub_total = selected.shape[0]
    correct = selected[selected['pred_score'] == score].shape[0]

    if total_nodes_num != 0:
        portion = sub_total/float(total_nodes_num)
    else:
        portion = None

    if sub_total != 0:
        accuracy = correct/float(sub_total)
    else:
        accuracy = None

    result_list = [l_child_score, r_child_score, score, correct, sub_total, portion, accuracy]
    return result_list

    #print('{0}\t{1}\t{2}\t{3}\t{4}\t{5:.2f}\t{6:.4f}'.format(l_child_score, r_child_score, score, correct, sub_total, sub_total/float(total_nodes_num),correct/float(sub_total)))





data = pd.read_csv('output/stats.txt', sep='\t', index_col=0)

data['score'].replace([0,4],[1,3],inplace=True)
data['l_child_score'].replace([0,4],[1,3],inplace=True)
data['r_child_score'].replace([0,4],[1,3],inplace=True)
data['pred_score'].replace([0,4],[1,3],inplace=True)


writer = pd.ExcelWriter('layer_wise_stats.xlsx',engine='xlsxwriter')

for phrase_length in range(1,31):
    temp = []
    local_data = data[data['phrase_length'] == phrase_length]
    #print('l_child_score\tr_child_score\tscore\tcorrect\tsub_total\tsub_portion\taccuracy')
    for i in [1,2,3]:
        for j in [1,2,3]:
            for k in [1,2,3]:
                temp.append(stats(local_data, l_child_score=i, r_child_score=j, score=k, total_nodes_num=local_data.shape[0]))
    frame = pd.DataFrame(temp, columns=['l_child_score','r_child_score','score','correct','sub_total','sub_portion','accuracy'])
    frame.to_excel(writer,sheet_name='phrase_length_' + str(phrase_length), index=False)


writer.save()




'''
print('left_child_score\tright_child_score\tscore\tcorrect\ttotal\tprotion\taccuracy')
for i in [1,2,3]:
    for j in [1,2,3]:
        for k in [1,2,3]:
            stats(data, l_child_score=i, r_child_score=j, score=k, total_nodes_num=40195)
'''