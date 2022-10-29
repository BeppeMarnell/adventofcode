class BCard:
    def __init__(self, rows):
        self.row_score = [0 for _ in rows]
        self.rows = rows
        self.numbers_got = []
        self.list = [item for sublist in rows for item in sublist]


    def tickNumber(self, number):
        for idx, v in enumerate(self.rows):
            if number in v:
                self.row_score[idx] += 1
                self.numbers_got.append(number)

        if 5 in self.row_score:
            # calculate the sum
            fl = [x for x in self.list if x not in self.numbers_got]
            return sum(fl)
        else:
            return -99

data = ""
with open('input.txt', 'r') as file:
    data = file.read().split('\n')

data = [d for d in data]

# get the extracted numbers
numbers = [int(num) for num in data[0].split(',')]

# create the bingo cards (these are composed by 5 rows of numbers)
bingo_cards = []
tmp_card = []
for i in range(2, len(data)):
    if data[i] == '':
        continue

    # split the string into a list of numbers
    numbs = [int(numb) for numb in data[i].split(' ') if numb != '']
    tmp_card.append(numbs)
    print(numbs)

    if len(tmp_card) == 5:
        bingo_cards.append(BCard(tmp_card))
        print(len(bingo_cards))
        tmp_card = []

## part 1 -----
winning_boards = []
log_boards = []

for n in numbers:
    for k, card in enumerate(bingo_cards):
        # skip the ones that have already won
        if k in log_boards:
            continue

        # tick the number on the board
        b_value = card.tickNumber(n)
        if b_value > 0:
            winning_boards.append((k, n, b_value))
            log_boards.append(k)


print('\n')

print(len(winning_boards))

print('First winning board is', winning_boards[0][0], 'with value', winning_boards[0][1]*winning_boards[0][2])

## part 2 -----
print('Last winning board is', winning_boards[-1][0], 'with value', winning_boards[-1][1]*winning_boards[-1][2])
