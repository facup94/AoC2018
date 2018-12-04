side_size = 1000
whole_piece_ids = []
for i in range(side_size):
  temp = []
  for j in range(side_size):
    temp.append([])
  whole_piece_ids.append(temp)
no_overlap_ids = {}

with open("input.txt", "r") as file:
  for linea in file:
    id, _, p1, p2 = linea.split(" ")

    x, y = p1[:-1].split(",")
    w, h = p2[:-1].split("x")

    x, y, w, h = int(x), int(y), int(w), int(h)
    
    no_overlap_ids[id] = True

    for i in range(x, x+w):
      for j in range(y, y+h):
        whole_piece_ids[i][j].append(id)

for i in range(1000):
  for j in range(1000):

    if len(whole_piece_ids[i][j]) > 1:
      for id in whole_piece_ids[i][j]:
        no_overlap_ids[id] = False

for id, no_overlaped in no_overlap_ids.items():
  if no_overlaped:
    print(id[1:], no_overlaped)
