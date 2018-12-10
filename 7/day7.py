steps = {}
with open('input.txt', 'r') as input:
  for line in input:
    before = line[5]
    step = line[36]

    if step not in steps:
      steps[step] = {'prev':[], 'post':[]}
    if before not in steps:
      steps[before] = {'prev':[], 'post':[]}
    
    steps[step]['prev'].append(before)
    steps[before]['post'].append(step)

# for step, data in steps.items():
#   print(step, data)

for 

