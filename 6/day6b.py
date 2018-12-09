def print_grid(grid, number_width=3, bool_print=False):
  grid_string = ''
  for row in grid:
    grid_string += ' '.join(str(x).rjust(number_width, '0') for x in row) + '\n'
  grid_string += '--------------------'

  if bool_print:
    print(grid_string)
  return grid_string


# Creating grids
grid_side_size = 400
distance_grids = {}
area_size = {}
total_distance_grid = [[0]*grid_side_size for i in range(grid_side_size)]
MAX_DISTANCE = 10000

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

        total_distance_grid[column][row] += distance

special_region_size = 0
for row in total_distance_grid:
  for element in row:
    if element < MAX_DISTANCE:
      special_region_size += 1

print(special_region_size)