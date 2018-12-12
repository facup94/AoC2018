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

largest_power_sum = 0
largest_power_sum_x = 0
largest_power_sum_y = 0

for y in range(298):
  for x in range(298):
    power_sum =  grid[y  ][x] + grid[y  ][x+1] + grid[y  ][x+2]
    power_sum += grid[y+1][x] + grid[y+1][x+1] + grid[y+1][x+2]
    power_sum += grid[y+2][x] + grid[y+2][x+1] + grid[y+2][x+2]

    if power_sum > largest_power_sum:
      largest_power_sum = power_sum
      largest_power_sum_x = x
      largest_power_sum_y = y

print(largest_power_sum_x, largest_power_sum_y)