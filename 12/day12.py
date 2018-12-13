pots = []
rules = {}

with open('input.txt', 'r') as file_input:
  pots = list(file_input.readline())[15:-1]
  pots = list('....................') + pots + list('....................')

  file_input.readline()

  for line in file_input:
    rules[line[:5]] = line[9]

for generation in range(1, 20+1):
  old_pots = pots.copy()

  for pot_index in range(2, len(pots)-3):
    index_from = pot_index-2
    index_to = pot_index+3
    
    pots[pot_index] = rules[''.join(old_pots[index_from:index_to])]

total = 0
for pot_number, status in enumerate(pots):
  if status == '#':
    total += pot_number - 20
print(total)