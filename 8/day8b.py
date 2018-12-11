class Node:
  def __init__(self):
    self.childs = []
    self.metadata = []
    self.value = 0
  
  def add_child(self, child):
    self.childs.append(child)

  def add_metadata(self, meta):
    self.metadata.append(meta)
    if len(self.childs) == 0:
      self.value += meta
    elif meta-1 < len(self.childs):
        self.value += self.childs[meta-1].value

def get_node(input):
  num_sons = input.pop(0)
  num_meta = input.pop(0)

  node = Node()
  for _ in range(num_sons):
    node.add_child(get_node(input))
  
  for _ in range(num_meta):    
    node.add_metadata(input.pop(0))

  return node


with open('input.txt', 'r') as input:
  tree_original = [int(x) for x in input.readline().split(' ')]

root = get_node(tree_original[:])
print(root.value)
