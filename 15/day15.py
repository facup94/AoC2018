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


units = []
mapa = []

a = '##.##..##..G........G.........##'

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

goblins = [x for x in units if x.tipo == 'G']
elves = [x for x in units if x.tipo == 'E']

while len(goblins) > 0 and len(elves) > 0:
  for unit in units:
    targets = goblins if unit.tipo == 'E' else elves
    
    open_squares_adjacent_target = []
    for target in targets:
      if target.posY-1 >= 0:
                    open_squares_adjacent_target.append((x,y))
    


    

  
  goblins = [x for x in units if x.tipo == 'G']
  elves = [x for x in units if x.tipo == 'E']
  units.sort()
