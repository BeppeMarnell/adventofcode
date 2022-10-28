data = ""
with open('input.txt', 'r') as file:
    data = file.read().split('\n')

data = [d for d in data if d != '']

# part 1 -----
count_byte = [0 for _ in data[0]]

for byte in data:
    for k, v in enumerate(byte):
        if int(v) == 1:
            count_byte[k] += 1

count_byte_g = ''.join([str(int(val/len(data) > 0.5)) for val in count_byte])
count_byte_e = ''.join([str(int(val/len(data) <= 0.5)) for val in count_byte])

g_rate = int(count_byte_g, 2)
e_rate = int(count_byte_e, 2)

print(g_rate*e_rate)

# part 2 -----

