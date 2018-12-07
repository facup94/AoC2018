def get_areas_by_range(pos, grid, search_range):
  pos_x, pos_y = pos
  area_found = 'x'
  for x in range(max(pos_x-search_range, 0), min(pos_x+search_range+1, len(grid))):
    for y in range(max(pos_y-(search_range-abs(pos_x-x)), 0), min(pos_y+(search_range-abs(pos_x-x)+1, len(grid[pos_x]))):
      if pos == (1, 3) and search_range == 2:
        print(x, y, grid[x][y])
      if grid[x][y] != "x":
        if area_found == 'x':
          area_found = grid[x][y].lower()
        else:
          return '.'
  return area_found

def print_grid(grid):
  for row in grid:
    print(''.join(row))
  print('--------------------')


#Creo la grilla y su copia
original_grid = [['x']*10 for i in range(10)]
grid = [['x']*10 for i in range(10)]

# Completo la grilla con la entrada
with open('input2.txt','r') as input:
  area_id = 64
  for pair in input:
    y, x = map(lambda x: int(x), pair[:-1].split(', '))
    area_id += 1
    original_grid[x][y] = chr(area_id)
    grid[x][y] = chr(area_id)

for row in range(len(grid)):
  for col in range(len(grid[row])):
    if grid[row][col] == 'x':
      search_range = 1
      in_area = get_areas_by_range((row, col), original_grid, search_range)
      while in_area == 'x':
        search_range += 1
        in_area = get_areas_by_range((row, col), original_grid, search_range)
      
      grid[row][col] = in_area

print_grid(grid)

# for row in original_grid:
#   print(''.join([str(x).replace('-1','.') for x in row]))
# print('--------------------')
# for row in grid:
#   print(''.join([str(x) for x in row]))