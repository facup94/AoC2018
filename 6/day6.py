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
distance_grids = {}
area_size = {}

# Completing grids with input
with open('input.txt','r') as input:
  area_id = 0
  for pair in input:
    y, x = map(lambda x: int(x), pair[:-1].split(', '))
    area_id += 1
    distance_grids[area_id] = [[0]*grid_side_size for i in range(grid_side_size)]
    area_size[area_id] = 0

    for row in range(grid_side_size):
      for column in range(grid_side_size):
        distance = abs(row-y) + abs(column-x)
        distance_grids[area_id][row][column] = distance

for row in range(grid_side_size):
  for column in range(grid_side_size):
    closest_area = 0
    closest_area_distance = grid_side_size*2+1
    two_same_distance = False
    for area_id, distance_grid in distance_grids.items():
      if distance_grid[row][column] < closest_area_distance:
        closest_area_distance = distance_grid[row][column]
        closest_area = area_id
        two_same_distance = False
      elif distance_grid[row][column] == closest_area_distance:
        two_same_distance = True
    
    if row == 0 or column==0 or row==grid_side_size-1 or column==grid_side_size-1:
      if closest_area in area_size:
        area_size.pop(closest_area)

    if not two_same_distance and closest_area in area_size:
      area_size[closest_area] += 1

print(max(area_size.values()))
