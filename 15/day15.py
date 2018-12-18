class Unit:
  def __init__(self, tipo, posX, posY):
    self.tipo = tipo
    self.posX = posX
    self.posY = posY

  def __lt__(self, other):
    if self.posY < other.posY:
      return True
    elif self.posY == other.posY:
      return self.posX < other.posX
    else:
      return False

  def __repr__(self):
    return self.tipo + ' (' + str(self.posX) + ', ' + str(self.posY) + ')' 


def can_reach(mapa, start, end):
  if end in mapa[start]:
    return True
  else:
    return any([can_reach(mapa, x, end) for x in mapa[start]])

def reachable_spaces(mapa, start, spaces: set):
  spaces.add(start)
  for n in mapa[start]:
    if n not in spaces:
      reachable_spaces(mapa, n, spaces)



import copy
import sys

units = []
mapa = []

# Read input
with open('input.txt', 'r') as input_file:
  y = 0
  for line in input_file:
    line = line.strip()
    
    map_row = []
    x = 0
    for ch in line:
      if ch == 'G' or ch == 'E':
        map_row.append('.')
        units.append(Unit(ch, x, y))
      else:
        map_row.append(ch)
      
      x += 1
    
    mapa.append(map_row)
    y += 1

units.sort()
goblins = [x for x in units if x.tipo == 'G']
elves = [x for x in units if x.tipo == 'E']

while len(goblins) > 0 and len(elves) > 0:
  for unit in units:
    # Posible targets
    targets = goblins if unit.tipo == 'E' else elves
    # Get posible target positions
    open_squares_adjacent_target = []
    for target in targets:
      if target.posY-1 >= 0 and mapa[target.posY-1][target.posX] == "." and sum([1 for x in units if x.posY == target.posY-1 and x.posX == target.posX]) == 0:
        open_squares_adjacent_target.append((target.posX, target.posY-1))
      if target.posY+1 < len(mapa) and mapa[target.posY+1][target.posX] == "." and sum([1 for x in units if x.posY == target.posY+1 and x.posX == target.posX]) == 0:
        open_squares_adjacent_target.append((target.posX, target.posY+1))
      if target.posX-1 >= 0 and mapa[target.posY][target.posX-1] == "." and sum([1 for x in units if x.posY == target.posY and x.posX == target.posX-1]) == 0:
        open_squares_adjacent_target.append((target.posX-1, target.posY))
      if target.posX+1 < len(mapa[0]) and mapa[target.posY][target.posX+1] == "." and sum([1 for x in units if x.posY == target.posY and x.posX == target.posX+1]) == 0:
        open_squares_adjacent_target.append((target.posX+1, target.posY))
    
    # Check for paths to targets
    # 1-Build yes/no map
    occupied_spaces_map = copy.deepcopy(mapa)
    for u in units:
      occupied_spaces_map[u.posY][u.posX] = '#'
    
    # 2-Check for each space wich neighbors can reach
    accessbile_spaces_dict = {}
    for y in range(len(occupied_spaces_map)):
      for x in range(len(occupied_spaces_map[y])):
        if occupied_spaces_map[y][x] == '#':
          continue
        
        if (x, y) not in accessbile_spaces_dict:
          accessbile_spaces_dict[(x,y)] = []
          
        if y-1 >= 0 and occupied_spaces_map[y-1][x] == ".":
          accessbile_spaces_dict[(x,y)].append((x,y-1))
        if y+1 < len(occupied_spaces_map) and occupied_spaces_map[y+1][x] == ".":
          accessbile_spaces_dict[(x,y)].append((x,y+1))
        if x-1 >= 0 and occupied_spaces_map[y][x-1] == ".":
          accessbile_spaces_dict[(x,y)].append((x-1,y))
        if x+1 < len(occupied_spaces_map[y]) and occupied_spaces_map[y][x+1] == ".":
          accessbile_spaces_dict[(x,y)].append((x+1,y))

    
    map_copy = copy.deepcopy(mapa)
    for u in units:
      map_copy[u.posY][u.posX] = u.tipo
    for row in map_copy:
      print(''.join(row))
    

    s = (25, 22)
    print(accessbile_spaces_dict[s])
    w = set()
    reachable_spaces(accessbile_spaces_dict, s, w)
    print(w)
    sys.exit()

    reachable_positions = []
    for space in open_squares_adjacent_target:
      if can_reach(accessbile_spaces_dict, (unit.posX, unit.posY), space):
        pass
    



    

  
  goblins = [x for x in units if x.tipo == 'G']
  elves = [x for x in units if x.tipo == 'E']
  units.sort()
