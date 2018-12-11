class Point:
  def __init__(self, x , y, vel_horizontal, vel_vertical):
    self.x = x
    self.y = y
    self.vel_horizontal = vel_horizontal
    self.vel_vertical = vel_vertical
  
  def move(self):
    self.x = self.x + self.vel_horizontal
    self.y = self.y + self.vel_vertical
  
import copy

original_points = []
with open('input.txt') as file_input:
  for line in file_input:
    pos_x = int(line[10:16])
    pos_y = int(line[18:24])
    vel_h = int(line[36:38])
    vel_v = int(line[40:42])

    original_points.append(Point(pos_x, pos_y, vel_h, vel_v))

points = copy.deepcopy(original_points)

min_height = -1
seconds_minsize = 0
seconds = 0
while seconds < 20000:
  height = max([point.y for point in points]) - min([point.y for point in points]) + 1
  if min_height == -1 or height < min_height:
    min_height = height
    seconds_minsize = seconds
  for point in points:
    point.move()
  
  seconds += 1

seconds = 0
points = original_points[:]
while seconds < seconds_minsize:
  for point in points:
    point.move()
  seconds += 1

min_x = min([point.x for point in points])
min_y = min([point.y for point in points])
width = max([point.x for point in points]) - min_x + 1
height = max([point.y for point in points]) - min_y + 1

with open('output.txt', 'w') as output_file:
  for row in range(height):
    print
    line = [' ']*width

    for point in points:
      if row == point.y-min_y:
        line[point.x-min_x] = '#'
    
    output_file.write(''.join(line))
    output_file.write('\n')
