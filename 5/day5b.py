with open('input.txt', 'r') as input:
  data = input.read().replace('\n', '')

data_original = data

types = {}
for unit in data:
  if unit.lower() not in types:
    types[unit.lower()] = 0

for unit_type in types.keys():
  data = data_original.replace(unit_type,'')
  data = data.replace(unit_type.upper(),'')

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
  
  types[unit_type] = len(data)
  print(unit_type, len(data))

minimizin_unit = ''
minium_length = 0
for unit_type, size in types.items():
  if size < minium_length or minium_length == 0:
    minium_length = size
    minimizin_unit = unit_type + '/' + unit_type.upper()

print(minimizin_unit, minium_length)
