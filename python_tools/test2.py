from Core import TreeClass as tc

file_in = open('input/original/dev.txt', 'r')
file_out = open('output/non_neutral_dev.txt','w')

for line in file_in:
    if not line[1] == '2':
        file_out.write(line)

file_out.close()
file_in.close()

