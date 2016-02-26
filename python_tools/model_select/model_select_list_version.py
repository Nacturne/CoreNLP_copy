# scp -P 130 model_select_list_version.py xliang@ambiguity.cs.stonybrook.edu:/home/xliang/CoreNLP_copy/python_tools/model_select_list_version.py

import os
import subprocess as sb

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))) + '/'


MODEL_FOLDER_LIST = ['random_sample/random_20_percent_re/random_20_percent_re0/']
TYPE = 'global'
GOAL_PATH = 'myData/original/train.txt'
TEST_PATH = 'myData/original/train.txt'


EVAL_PATH = 'edu.stanford.nlp.sentiment.Evaluate_accuracy'



MODEL_PATH = ROOT + 'myModels/'

CLASS_PATH = 'jre/lib/jfxswt.jar:jre/lib/jce.jar:jre/lib/rt.jar:jre/lib/jsse.jar:jre/lib/javaws.jar:jre/lib/management-agent.jar:jre/lib/jfr.jar:jre/lib/resources.jar:jre/lib/plugin.jar:jre/lib/charsets.jar:jre/lib/deploy.jar:jre/lib/ext/sunec.jar:jre/lib/ext/nashorn.jar:jre/lib/ext/localedata.jar:jre/lib/ext/cldrdata.jar:jre/lib/ext/jfxrt.jar:jre/lib/ext/sunpkcs11.jar:jre/lib/ext/sunjce_provider.jar:jre/lib/ext/dnsns.jar:jre/lib/ext/jaccess.jar:jre/lib/ext/zipfs.jar:build/classes/main:build/resources/main:lib/lucene-core-4.10.3.jar:lib/slf4j-api.jar:lib/ant-contrib-1.0b3.jar:lib/ejml-0.23.jar:lib/lucene-analyzers-common-4.10.3.jar:lib/joda-time.jar:lib/xom-1.2.10.jar:lib/commons-logging.jar:lib/jollyday-0.4.7.jar:lib/AppleJavaExtensions.jar:lib/javax.json.jar:lib/protobuf.jar:lib/jflex-1.5.1.jar:lib/lucene-queryparser-4.10.3.jar:lib/lucene-demo-4.10.3.jar:lib/jgrapht-core-0.9.1.jar:lib/lucene-queries-4.10.3.jar:lib/appbundler-1.0.jar:lib/junit.jar:lib/log4j-1.2.16.jar:lib/javax.servlet.jar:lib/javacc.jar:lib/slf4j-simple.jar:lib/commons-lang3-3.1.jar'

for MODEL_FOLDER in MODEL_FOLDER_LIST:

    models = sb.check_output(['ls',MODEL_PATH + MODEL_FOLDER])
    models = models.split('\n')[:-1]

    eval_dict = {}

    for index, model in enumerate(models):
        result = sb.check_output(['java', '-classpath',CLASS_PATH, EVAL_PATH, '-model', MODEL_PATH + MODEL_FOLDER + model, '-treebank', ROOT + GOAL_PATH],cwd=ROOT)
        result = result.split('\n')[:-1]
        #result = ['global accuracy:', number, 'root accuracy:', number]

        if TYPE == 'root':
            eval_dict[model] = float(result[3])
        elif TYPE == 'global':
            eval_dict[model] = float(result[1])
        else:
            raise Exception('TYPE variable can not be recognized')

	print('{0}\t{1}'.format(model,eval_dict[model]))    

    max_model = max(eval_dict, key=eval_dict.get)

    print('--------------------------------------------------------------------------')
    print('Best model for-----{0}-----on-----{1}-----of-----{2}:'.format(MODEL_FOLDER, GOAL_PATH, TYPE))
    print('index: {0}-------------accuracy : {1}'.format(max_model, eval_dict[max_model]))



    test_result = sb.check_output(['java', '-classpath',CLASS_PATH, EVAL_PATH, '-model', MODEL_PATH + MODEL_FOLDER + max_model, '-treebank', ROOT + TEST_PATH],cwd=ROOT)
    test_result = test_result.split('\n')[:-1]

    if TYPE == 'root':
        test_accuracy = float(test_result[3])
    elif TYPE == 'global':
        test_accuracy = float(test_result[1])

    print('{0}-----accuracy on-----{1}: {2}'.format(TYPE, TEST_PATH, test_accuracy))

    print('---------------------------------------------------------------------------\n\n')




