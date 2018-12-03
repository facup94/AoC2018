freq = 0
frequencies_reached = {}
repeat = True

with open('input.txt', 'r') as file:
    while repeat:
        for freq_change in file:
            if freq_change[0] == '+':
                freq += int(freq_change[1:])
            else:
                freq -= int(freq_change[1:])
        
            if freq not in frequencies_reached:
                frequencies_reached[freq] = True
            else:
                repeat = False
                print(freq)
                break

        file.seek(0)
