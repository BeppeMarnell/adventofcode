data = ""

with open('day_1.txt', 'r') as file:
    data = file.read().split('\n')

data = [int(d) for d in data if d != '']

n = 0

for k, v in enumerate(data):
    if k == 0: # skip the first one
        continue

    if v > data[k-1]:
        n += 1

print(n)
