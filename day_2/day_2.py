
data = ""
with open('input.txt', 'r') as file:
    data = file.read().split('\n')

data = [d for d in data if d != '']

# part 1 -----

depth = 0
h_pos = 0

for command in data:
    if 'forward' in command:
        h_pos += int(command[-1])
    elif 'down' in command:
        depth += int(command[-1])
    elif 'up' in command:
        depth -= int(command[-1])

print(depth * h_pos)

# part 2 -----

aim = 0
depth = 0
h_pos = 0

for command in data:
    if 'forward' in command:
        value = int(command[-1])
        h_pos += value
        depth += aim * value

    elif 'down' in command:
        aim += int(command[-1])
    elif 'up' in command:
        aim -= int(command[-1])

print(depth * h_pos)