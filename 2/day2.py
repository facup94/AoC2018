def count(id):
    letters = {}
    has_2 = False
    has_3 = False
    for letter in id:
        if letter not in letters:
            letters[letter] = 0
        
        letters[letter] += 1
    
    for a in letters.values():
        if a == 2:
            has_2 = True
        if a == 3:
            has_3 = True

    return has_2, has_3


count_2 = 0
count_3 = 0
with open("input.txt", 'r') as file:
    for id in file:
        res = count(id)
        if res[0]:
            count_2 += 1
        if res[1]:
            count_3 += 1

print(str(count_2 * count_3))
