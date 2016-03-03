# scp -P 130 run.py xliang@ambiguity.cs.stonybrook.edu:/home/xliang/CoreNLP_copy/python_tools/model_select/run.py

from tools import model_select
import os
import subprocess as sb


# parameters:
parent_folder = 'simp/'
eval_type = 'root'
goal_path = 'myData/simplify/simp_dev.txt'
test_path = 'myData/simplify/simp_test.txt'






ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))) + '/'
list_out = sb.check_output(['ls'],cwd=ROOT+'myModels/'+parent_folder)
list_out = list_out.split('\n')[:-1]
list_out = [parent_folder+x+'/' for x in list_out]

print('-----------------------------------------')
print('Folder List:')
for i in list_out:
	print(i)
print('-----------------------------------------\n')


MODEL_FOLDER_LIST = list_out
for model in MODEL_FOLDER_LIST:
    result = model_select(MODEL_FOLDER = model,
                            TYPE = eval_type,
                            GOAL_PATH = goal_path,
                            TEST_PATH = test_path)

    print('\n--------------------------------------------------------------------------')
    print('Best model for-----{0}-----on-----{1}-----of-----{2}:'.format(result['MODEL_FOLDER'],result['GOAL_PATH'], result['TYPE']))
    print('index: {0}-------------accuracy : {1}'.format(result['best_model'], result['best_model_accuracy']))

    print('{0}-----accuracy on-----{1}: {2}'.format(result['TYPE'], result['TEST_PATH'], result['test_accuracy']))
    print('---------------------------------------------------------------------------\n\n')
