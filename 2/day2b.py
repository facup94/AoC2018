def close(a, b):
    cant = 0

    for i in range(len(a)):
        if a[i] != b[i]:
            cant += 1

            if cant > 1:
                break


    if cant == 1:
        return True
    else: 
        return False


all_ids = []
with open("input.txt", 'r') as file:
    for id in file:
        all_ids.append(id)


for i in range(len(all_ids)-1):
    for j in range(i+1, len(all_ids)):
        if close(all_ids[i], all_ids[j]):

            for x in range(len(all_ids[i])):
                if all_ids[i][x] == all_ids[j][x]:
                    print(all_ids[i][x], end="")


