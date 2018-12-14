def generate_recipes(current_recipes, i1, i2):
  digits_sum = [int(x) for x in str(current_recipes[i1] + current_recipes[i2])]
  current_recipes.extend(digits_sum)

recipes = [3, 7]
elve_1 = 0
elve_2 = 1

while recipes[-6:] != [2, 0, 9, 2, 3, 1] and recipes[-7:-1] != [2, 0, 9, 2, 3, 1]:
  generate_recipes(recipes, elve_1, elve_2)
  
  elve_1 += recipes[elve_1] + 1
  while elve_1 >= len(recipes):
    elve_1 -= len(recipes)

  elve_2 += recipes[elve_2] + 1
  while elve_2 >= len(recipes):
    elve_2 -= len(recipes)

if recipes[-6:] == [2, 0, 9, 2, 3, 1]:
  print(len(recipes)-6)
else:
  print(len(recipes)-7)
