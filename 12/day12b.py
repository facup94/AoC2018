pots = []
rules = {}
pots_history = []


with open('input.txt', 'r') as file_input:
  pots = list(file_input.readline())[15:-1]
  pots = list('....................') + pots + ['.'] * 10000
  
  file_input.readline()

  for line in file_input:
    rules[line[:5]] = line[9]

# for generation in range(1, 50000000000+1):
for generation in range(1, 2000+1):
  old_pots = pots.copy()

  for pot_index in range(2, len(pots)-3):
    index_from = pot_index-2
    index_to = pot_index+3
    
    pots[pot_index] = rules[''.join(old_pots[index_from:index_to])]
  
  if generation % 200 == 0:
    pots_history.append([i for i in range(len(pots)) if pots[i]=='#'])

with open('output.txt', 'w') as output_file:
  for i, pot_gen in enumerate(pots_history):
    output_file.write(str((i+1)*200))
    output_file.write(' ')
    output_file.write(' '.join([str(x) for x in pot_gen]))
    output_file.write(' ')
    output_file.write(str(sum(pot_gen)-20*len(pot_gen)))
    output_file.write('\n')