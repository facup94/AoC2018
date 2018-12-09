def print_grid(grid, bool_print=False):
  grid_string = ''
  for row in grid:
    grid_string += ' '.join(str(x).rjust(3, '0') for x in row) + '\n'
  grid_string += '--------------------'

  if bool_print:
    print(grid_string)
  return grid_string


# Creating grids
grid_side_size = 400
distance_grid = [[{'areas':[], 'distance':grid_side_size*3} for _ in range(grid_side_size)] for i in range(grid_side_size)]
area_size = {}
area_centers = {}

with open('input.txt','r') as input:
  area_id = 0
  for pair in input:
    y, x = map(lambda x: int(x), pair[:-1].split(', '))
    area_id += 1
    area_centers[area_id] = (x, y)
    area_size[area_id] = 0

for x in range(grid_side_size):
  for y in range(grid_side_size):
    
    for area_id, area_center in area_centers.items():
      distance = abs(x-area_center[0]) + abs(y-area_center[1])
      
      if distance < distance_grid[y][x]['distance']:
        distance_grid[y][x]['areas'] = [area_id]
        distance_grid[y][x]['distance'] = distance

      elif distance == distance_grid[y][x]['distance']:
        distance_grid[y][x]['areas'].append(area_id)
    
for row in range(grid_side_size):
  for column in range(grid_side_size):
    
    if len(distance_grid[row][column]['areas']) == 1:

      if row==0 or column==0 or row==grid_side_size-1 or column==grid_side_size-1:
        if distance_grid[row][column]['areas'][0] in area_size:
          area_size.pop(distance_grid[row][column]['areas'][0])
      
      elif distance_grid[row][column]['areas'][0] in area_size:
        area_size[distance_grid[row][column]['areas'][0]] += 1

print(max(area_size.values()))