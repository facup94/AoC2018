with open('input.txt', 'r') as input:
  data = input.read().replace('\n', '')

i = 0
while i < len(data)-1:
  unit_a = data[i]
  unit_b = data[i+1]

  if unit_a != unit_b and unit_a.lower() == unit_b.lower():
    data = data[:i] + data[i+2:]
    i -= 2    
  
  i += 1
  while i < 0:
    i += 1

print(len(data))