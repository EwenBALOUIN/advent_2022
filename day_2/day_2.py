opp_rock = "A"
opp_paper = "B"
opp_scissors = "C" 
you_rock = "X"
you_paper = "Y"
you_scissors = "Z"
rock=1
paper=2
scissors=3
total_score = 0
score = 0

def get_result(opponent, you):
    value = get_move_value(you)
    print("move : {0}".format(value))
    opp = get_move_value_opp(opponent)
    if opp == value:
        print("Draw")
        value += 3
    elif opp == rock and value == paper:
        print("Win")
        value +=  6
    elif opp == paper and value == scissors:
        print("Win")
        value +=  6
    elif opp == scissors and value == rock:
        print("Win")
        value +=  6
    else:
        print("Lose")
        value +=  0
    return value

def get_move_value(move):
    if move == you_rock:
        return 1
    elif move == you_paper:
        return 2
    elif move == you_scissors:
        return 3
    else:
        return 0

def get_move_value_opp(move):
    if move == opp_rock:
        return 1
    elif move == opp_paper:
        return 2
    elif move == opp_scissors:
        return 3
    else:
        return 0

with open('day_2\input_2.txt') as f:
    lines = f.readlines()
    for line in lines:
        match= line.split()
        opponent = match[0]
        you = match[1]
        print("opp : {0}, you : {1}".format(opponent, you))
        score = get_result(opponent, you)
        total_score += score
        print("score : {0}".format(score))
        print("total_score : {0}".format(total_score))
        score = 0
print("total_score : {0}".format(total_score))