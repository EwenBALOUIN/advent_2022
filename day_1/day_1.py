with open('day_1\input_1.txt') as f:
    lines = f.readlines()
    best_sum = 0
    sum_calories = 0
    elf = 0
    list_best= []
    for line in lines:
        if line == "\n":
            elf += 1
            print("Elf number {0}. Have {1} calories.".format(elf, sum_calories))
            list_best.append(int(sum_calories))
            best_sum = sum_calories if sum_calories > best_sum else best_sum
            sum_calories = 0
        else:
            sum_calories += int(line)
    print(best_sum)
    print(sum(sorted(list_best, reverse=True)[:3]))