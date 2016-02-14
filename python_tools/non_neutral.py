file_in = open("input/simplify/simp_dev.txt", 'r')
file_out = open("input/non_neutral/non_neutral_dev.txt", 'w')

count = 0

for line in file_in:
    if line[1] != '2':
        file_out.write(line)
        count += 1

file_in.close()
file_out.close()

print(count)