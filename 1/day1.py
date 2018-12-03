freq = 0

with open('input.txt', 'r') as file:
    for freq_change in file:
        if freq_change[0] == '+':
            freq += int(freq_change[1:])
        else:
            freq -= int(freq_change[1:])
    
print(freq)
