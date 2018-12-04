side_size = 1000
whole_piece = [[0]*side_size for _ in range(side_size)]

with open("input.txt", "r") as file:
  for linea in file:
    p1, p2 = linea.split(" ")[2:4]
    x, y = p1[:-1].split(",")
    w, h = p2[:-1].split("x")

    x, y, w, h = int(x), int(y), int(w), int(h)
    
    for i in range(x, x+w):
      for j in range(y, y+h):
        whole_piece[i][j] += 1

cantidad = 0
for i in range(1000):
  for j in range(1000):
    if whole_piece[i][j] > 1:
      cantidad += 1

print(cantidad)
