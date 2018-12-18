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

class Graph:
  def __init__(self):
    self.nodes = set()
    self.edges = defaultdict(list)
    self.distances = {}

  def add_node(self, value):
    self.nodes.add(value)

  def add_edge(self, from_node, to_node, distance):
    if to_node not in self.edges[from_node]:
      self.edges[from_node].append(to_node)
    if from_node not in self.edges[to_node]:
      self.edges[to_node].append(from_node)
    if (from_node, to_node) not in self.distances:
      self.distances[(from_node, to_node)] = distance
    if (to_node, from_node) not in self.distances:
      self.distances[(to_node, from_node)] = distance


def dijsktra(graph, initial):
  visited = {initial: 0}
  path = {}

  nodes = set(graph.nodes)

  while nodes: 
    min_node = None
    for node in nodes:
      if node in visited:
        if min_node is None:
          min_node = node
        elif visited[node] < visited[min_node]:
          min_node = node

    if min_node is None:
      break

    nodes.remove(min_node)
    current_weight = visited[min_node]

    for edge in graph.edges[min_node]:
      weight = current_weight + graph.distances[(min_node, edge)]
      if edge not in visited or weight < visited[edge]:
        visited[edge] = weight
        path[edge] = min_node

  return visited, path



import copy
import sys
from collections import defaultdict

units = []
mapa = []

# Read input
with open('c:\\Users\\nbcorar399\\Desktop\\advent_of_code_2018\\15\\input.txt', 'r') as input_file:
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
    
    # Graph
    graph = Graph()
    # Add nodes
    for y in range(len(occupied_spaces_map)):
      for x in range(len(occupied_spaces_map[y])):
        if occupied_spaces_map[y][x] == '.':
          graph.add_node((x, y))
    # Add edges
    for y in range(len(occupied_spaces_map)):
      for x in range(len(occupied_spaces_map[y])):
        if occupied_spaces_map[y][x] == '.':
          for n in accessbile_spaces_dict[(x,y)]:
            graph.add_edge((x,y), n, 1)
    # Add starting node and edges from there
    graph.add_node((unit.posX, unit.posY))
    if unit.posY-1 >= 0 and occupied_spaces_map[unit.posY-1][unit.posX] == '.':
      graph.add_edge((unit.posX, unit.posY), (unit.posX, unit.posY-1), 1)
    if unit.posY+1 < len(occupied_spaces_map) and occupied_spaces_map[unit.posY+1][unit.posX] == '.':
      graph.add_edge((unit.posX, unit.posY), (unit.posX, unit.posY+1), 1)
    if unit.posX-1 >= 0 and occupied_spaces_map[unit.posY][unit.posX-1] == '.':
      graph.add_edge((unit.posX, unit.posY), (unit.posX-1, unit.posY), 1)
    if unit.posX+1 < len(occupied_spaces_map[unit.posY]) and occupied_spaces_map[unit.posY][unit.posX+1] == '.':
      graph.add_edge((unit.posX, unit.posY), (unit.posX+1, unit.posY), 1)

    # Apply Dijsktra
    accessible_targets, accessible_targets_paths = dijsktra(graph, (unit.posX,unit.posY))
    
    while len(accessible_targets) > 0:
      print(accessible_targets)
      closest_target = min(accessible_targets, key=accessible_targets.get)
      print(closest_target)
      print(min(accessible_targets))
      sys.exit()
      if closest_target not in open_squares_adjacent_target:
        accessible_targets.pop(closest_target)
        continue

      sys.exit()
    

    sys.exit()


    

  
  goblins = [x for x in units if x.tipo == 'G']
  elves = [x for x in units if x.tipo == 'E']
  units.sort()
