class Car:
  def __init__(self, x, y, direction):
    self.x = x
    self.y = y
    self.direction = direction
    self.rotation = 'L'
  
  def get_rotation(self):
    b = self.rotation
    if self.rotation == 'L':
      self.rotation = 'S'
    elif self.rotation == 'S':
      self.rotation = 'R'
    else:
      self.rotation = 'L'
    
    return b
  
  def __lt__(self, other):
    if self.y == other.y:
      return self.x < other.x
    return self.y < other.y
  
  def __eq__(self, other):
    return self.x == other.x and self.y == other.y
  
  def __repr__(self):
    return self.direction + ' (' + str(self.x) + ', ' + str(self.y) + ')'
    

def car_in_position(list, x, y):
  for c in list:
    if c.x == x and c.y == y:
      return True
  return False

def print_current_status(tracks, cars):
  print(''.join(['-' for i in range(50)]))
  for y in range(len(tracks)):
    for x in range(len(tracks[y])):
      for car in cars:
        if car.x == x and car.y == y:
          print(car.direction, end='')
          break
      else:
        print(tracks[y][x], end='')
    print('')

track_map = []
car_list = []

with open('input.txt', 'r') as input_file:
  y = 0
  for line in input_file:
    line = line[:-1]
    x = 0
    l_map = []
    for c in line:
      if c in ['<', '>']:
        l_map.append('-')
        car_list.append(Car(x, y, c))
      elif c in ['^', 'v']:
        l_map.append('|')
        car_list.append(Car(x, y, c))
      else:
        l_map.append(c)
      
      x += 1
    
    track_map.append(l_map)
    y += 1


for l in track_map:
  print(''.join(l))


crashed = False
while not crashed:
  car_list.sort()
  for car in car_list:
    # print_current_status(track_map, car_list)
    # Car is going right to left
    if car.direction == '<':
      if car_in_position(car_list, car.x-1, car.y):
        for i in range(5):
          print('CRASH CRASH  ', car.x-1, car.y)
        crashed = True
        break
      else:
        car.x -= 1
      
      if track_map[car.y][car.x] == '\\':
        car.direction = '^'
      elif track_map[car.y][car.x] == '/':
        car.direction = 'v'
      elif track_map[car.y][car.x] == '+':
        rotation = car.get_rotation()
        if rotation == 'L':
          car.direction = 'v'
        elif rotation == 'R':
          car.direction = '^'

    # Car is going left to right
    elif car.direction == '>':
      if car_in_position(car_list, car.x+1, car.y):
        for i in range(5):
          print('CRASH CRASH  ', car.x+1, car.y)
        crashed = True
        break
      else:
        car.x += 1

      if track_map[car.y][car.x] == '/':
        car.direction = '^'
      elif track_map[car.y][car.x] == '\\':
        car.direction = 'v'
      elif track_map[car.y][car.x] == '+':
        rotation = car.get_rotation()
        if rotation == 'L':
          car.direction = '^'
        elif rotation == 'R':
          car.direction = 'v'
    
    # Car is going upward
    elif car.direction == '^':
      if car_in_position(car_list, car.x, car.y-1):
        for i in range(5):
          print('CRASH CRASH  ', car.x, car.y-1)
        crashed = True
        break
      else:
        car.y -= 1

      if track_map[car.y][car.x] == '/':
        car.direction = '>'
      elif track_map[car.y][car.x] == '\\':
        car.direction = '<'
      elif track_map[car.y][car.x] == '+':
        rotation = car.get_rotation()
        if rotation == 'L':
          car.direction = '<'
        elif rotation == 'R':
          car.direction = '>'

    # Car is going downward
    else:
      if car_in_position(car_list, car.x, car.y+1):
        for i in range(5):
          print('CRASH CRASH  ', car.x, car.y+1)
        crashed = True
        break
      else:
        car.y += 1

      if track_map[car.y][car.x] == '/':
        car.direction = '<'
      elif track_map[car.y][car.x] == '\\':
        car.direction = '>'
      elif track_map[car.y][car.x] == '+':
        rotation = car.get_rotation()
        if rotation == 'L':
          car.direction = '>'
        elif rotation == 'R':
          car.direction = '<'
    
    if crashed:
      break
      
      