file_in = open('input/original/test.txt', 'r')

total = 0
neutral = 0
for line in file_in:
    if line[0] == '(':
        total += 1
        if line[1] == '2':
            neutral += 1

print('total: {0}'.format(total))
print('neutral: {0}'.format(neutral))
print('portion: {0}'.format(neutral/float(total)))
file_in.close()