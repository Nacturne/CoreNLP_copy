from tools import model_select

MODEL_FOLDER_LIST = ['learningRate/learning_rate_full/learning_rate_002/']
for model in MODEL_FOLDER_LIST:
    result = model_select(MODEL_FOLDER = model,
                            TYPE = 'global',
                            GOAL_PATH = 'myData/original/dev.txt',
                            TEST_PATH = 'myData/original/test.txt')

    print('\n--------------------------------------------------------------------------')
    print('Best model for-----{0}-----on-----{1}-----of-----{2}:'.format(result['MODEL_FOLDER'],result['GOAL_PATH'], result['TYPE']))
    print('index: {0}-------------accuracy : {1}'.format(result['best_model'], result['best_model_accuracy']))

    print('{0}-----accuracy on-----{1}: {2}'.format(result['TYPE'], result['TEST_PATH'], result['test_accuracy']))
    print('---------------------------------------------------------------------------\n\n')