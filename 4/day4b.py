class Record:
  def __init__(self, day, month, year, hour, minute, action, id):
    self.day = day
    self.month = month
    self.year = year
    self.hour = hour
    self.minute = minute
    self.action = action
    self.id = id
  
  def __str__(self):
    out = str(self.day) + '/' + str(self.month) + '/' + str(self.year) + ' ' + str(self.hour) + ':' + str(self.minute) + ' ' + self.action
    if self.id is not None:
      out += ' > ' + str(self.id)
    return out

  def ord(self):
    num = self.year * 100000000
    num += self.month * 1000000
    num += self.day * 10000
    num += self.hour * 100
    num += self.minute
    return num
    

actions = []
with open('input.txt', 'r') as input:
  for row in input:
    row = row[:-1]
    id = int(row.split(' ')[3][1:]) if row[19]=='G' else None
    rec = Record(int(row[9:11]), int(row[6:8]), int(row[1:5]), int(row[12:14]), int(row[15:17]), row[19].lower(), id)

    actions.append(rec)

actions.sort(key=lambda x : x.ord())

guards = {}
guard_id = 0
fall_time = 0
wake_time = 0

for row in actions:
  if row.action == 'g':
    guard_id = row.id

    if guard_id not in guards:
      guards[guard_id] = [0] * 61

  elif row.action == 'f':
    fall_time = row.minute

  else:
    wake_time = row.minute
    for i in range(fall_time, wake_time):
      guards[guard_id][i] += 1
    guards[guard_id][60] += wake_time - fall_time


max_time_in_minute = 0
minute_with_most_time = 0
guard_id_with_most_time_in_one_minute = 0
for guard_id, sleep_times in guards.items():
  for i in range(len(sleep_times[:60])):
    time = sleep_times[i]
    if time > max_time_in_minute:
      max_time_in_minute = time
      minute_with_most_time = i
      guard_id_with_most_time_in_one_minute = guard_id

print('Guard', guard_id_with_most_time_in_one_minute, 'slept', max_time_in_minute, 'in minute', minute_with_most_time)
print('Output', guard_id_with_most_time_in_one_minute * minute_with_most_time)