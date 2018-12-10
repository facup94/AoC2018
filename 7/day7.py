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

event_list = []
steps_copy = steps.copy()

while True:
  # Add steps that have all previous tasks ready
  for step_id, data in steps.copy().items():
    if len(data['prev']) == 0:
      event_list.append(step_id)
      # Remove them to not add them twice
      steps.pop(step_id)

  if len(event_list) == 0:
    break

  # Order and pop first
  event_list.sort()
  next_step = event_list.pop(0)
  
  # Remove step from "previous" tasks
  for post_step in steps_copy[next_step]['post']:
    if post_step in steps:
      steps[post_step]['prev'].remove(next_step)

  print(next_step, end='')


