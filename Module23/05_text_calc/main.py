
def def_calc(calculate):
    first = int(calculate[0])
    second = int(calculate[2])
    action_list = ['+','-','/','*','**']
    action = 0
    for calc in range(len(action_list)):
        if calculate[1] == action_list[calc]:
            action = calc + 1
    if action == 1:
      return first + second
    elif action == 2:
        return first - second
    elif action == 3:
        return first / second
    elif action == 4:
        return first * second
    elif action == 5:
        return first ** second
    elif action == 0:
        return "Action is not dedicated"

with open("calc.txt",'r') as calc_file:
    for line in calc_file.readlines():
        print("Result =", def_calc(line.split()))
