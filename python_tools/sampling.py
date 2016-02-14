import random as rdm


file_in = open('input/original/train.txt', 'r')
file_out = open('output/random_80_percent_train.txt', 'w')

population = file_in.readlines()
sample_num = int(len(population)*0.8)

rdm.seed(1)
samples = rdm.sample(population,sample_num)

for line in samples:
    file_out.write(line)


file_in.close()
file_out.close()

'''
from Core import TreeClass as tc

file_in_population = open('input/original/train.txt', 'r')
file_in_sample = open('output/random_80_percent_train.txt', 'r')

counter_population = 0
counter_sample = 0

for line in file_in_population:
    tree = tc.ScoreTree(line)
    counter_population += len(tree.allNodes())

for line in file_in_sample:
    tree = tc.ScoreTree(line)
    counter_sample += len(tree.allNodes())

file_in_population.close()
file_in_sample.close()

print(counter_population)
print(counter_sample)

print(counter_sample/float(counter_population))
'''