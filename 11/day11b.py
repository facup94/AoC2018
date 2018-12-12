grid_serial_number = 6042

grid = [[0]*300 for _ in range(300)]

for y in range(300):
  for x in range(300):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += grid_serial_number
    power_level *= rack_id
    power_level = int(str(power_level)[-3])
    power_level -= 5
    grid[y][x] = power_level

for row in grid[:10]:
  print(row[:10])

pre_processed_grid = [[0]*300 for _ in range(300)]
for y_original_grid in range(300):
  print('\rFilling pre-processed grid - ROW:', y_original_grid, '/ 300', end='')
  for x_original_grid in range(300):
    for y in range(y_original_grid, 300):
      for x in range(x_original_grid, 300):
        pre_processed_grid[y][x] += grid[y_original_grid][x_original_grid]

print('')

for row in pre_processed_grid[:10]:
  print(row[:10])

print('cortar')

largest_power_sum = 0
largest_power_sum_x = 0
largest_power_sum_y = 0
largest_power_sum_size = 0

for side_size in range(1, 301):
  print('Testing size ', side_size, ' (', str(side_size*100/300)[:4], '%)', sep='')
  for y_start in range(301 - side_size):
    for x_start in range(301 - side_size):
      power_sum = sum([grid[y][x] for y in range(y_start, y_start + side_size) for x in range(x_start, x_start + side_size)])
      
      if power_sum > largest_power_sum:
        largest_power_sum = power_sum
        largest_power_sum_x = x
        largest_power_sum_y = y
        largest_power_sum_size = side_size

print(largest_power_sum_x, largest_power_sum_y, side_size, sep=',')