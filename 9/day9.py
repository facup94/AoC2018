class CircleElement:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next


with open('input.txt', 'r') as input:
  line = input.readline().split(' ')
  num_players = int(line[0])  
  last_marble = int(line[6])


scores = {}
for i in range(1, num_players+1):
  scores[i] = 0

first_marble = CircleElement(0)
first_marble.prev = first_marble
first_marble.next = first_marble
current_marble = first_marble

current_player = 1

for i in range(1, last_marble+1):
  if i % 23 != 0:
    marble_1 = current_marble.next
    marble_2 = marble_1.next
    
    new_marble = CircleElement(i, marble_1, marble_2)

    marble_1.next = new_marble
    marble_2.prev = new_marble

    current_marble = new_marble
  
  else:
    removed_marble = current_marble.prev.prev.prev.prev.prev.prev.prev
    removed_marble.prev.next = removed_marble.next
    removed_marble.next.prev = removed_marble.prev

    scores[current_player] += i
    scores[current_player] += removed_marble.value

    current_marble = removed_marble.next

    
  current_player += 1
  if current_player > num_players:
    current_player = 1


print(max(scores.values()))