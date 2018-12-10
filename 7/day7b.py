steps_remaining, steps_done, steps_currently  = {}, {}, {}
with open('input.txt', 'r') as input:
  for line in input:
    before = line[5]
    step = line[36]

    if step not in steps_remaining:
      steps_remaining[step] = {'prev':[], 'post':[], 'start_time':-1, 'end_time':-1, 'duration':60+(ord(step)-64)}
    if before not in steps_remaining:
      steps_remaining[before] = {'prev':[], 'post':[], 'start_time':-1, 'end_time':-1, 'duration':60+(ord(before)-64)}
    
    steps_remaining[step]['prev'].append(before)
    steps_remaining[before]['post'].append(step)

event_list = []
time = -1

while len(steps_remaining) + len(steps_currently) > 0:
  time += 1

  finished_steps = sorted([step_id for step_id, data in steps_currently.items() if data['end_time']==time])
  while len(finished_steps) > 0:
    finishing_step_id = finished_steps.pop(0)
    # Remove step from running steps
    finishing_step = steps_currently.pop(finishing_step_id)
    # Add step to finished steps
    steps_done[finishing_step_id] = finishing_step
    # Remove finished step from remaining steps requirements
    for next_step_id in finishing_step['post']:
      if next_step_id in steps_remaining:
        steps_remaining[next_step_id]['prev'].remove(finishing_step_id)

  ready_steps = sorted([x for x, data in steps_remaining.items() if len(data['prev'])==0])
  while len(steps_currently) < 5 and len(ready_steps) > 0:
    starting_step_id = ready_steps.pop(0)
    
    # Remove step from remaining
    starting_step = steps_remaining.pop(starting_step_id)
    # Set times
    starting_step['start_time'] = time
    starting_step['end_time'] = starting_step['start_time'] + starting_step['duration']
    # Add step to running steps
    steps_currently[starting_step_id] = starting_step

print(time)