import copy

collection_area = []
with open('input.txt', 'r') as input_file:
  for line in input_file:
    collection_area.append([x for x in line.strip()])

for minute in range(10):
  col_area = copy.deepcopy(collection_area)
  for y_start in range(len(col_area)):
    for x_start in range(len(col_area[y_start])):
      num_trees = 0
      num_lumberyards = 0

      # Count adjacent
      for y in range(max(y_start-1, 0), min(y_start+2, len(col_area))):
        for x in range(max(x_start-1, 0), min(x_start+2, len(col_area[y]))):
          if y == y_start and x == x_start:
            continue
          
          if collection_area[y][x] == '|':
            num_trees += 1
          elif collection_area[y][x] == '#':
            num_lumberyards += 1
      
      if collection_area[y_start][x_start] == '.' and num_trees >= 3:
        col_area[y_start][x_start] = '|'
      elif collection_area[y_start][x_start] == '|' and num_lumberyards >= 3:
        col_area[y_start][x_start] = '#'
      elif collection_area[y_start][x_start] == '#':
        if num_lumberyards == 0 or num_trees == 0:
          col_area[y_start][x_start] = '.'
  
  collection_area = col_area
  
num_trees = 0
num_lumberyards = 0
for row in collection_area:
  for space in row:
    if space == '|':
      num_trees += 1
    if space == '#':
      num_lumberyards += 1

print(num_trees * num_lumberyards)


