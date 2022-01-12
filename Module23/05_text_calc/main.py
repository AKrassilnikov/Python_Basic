
def def_calc(calculate):
    first = float(calculate[0])
    second = float(calculate[2])
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
        return "Action is not defined"
calc_summ = 0
with open("calc.txt",'r') as calc_file:
    for line in calc_file.readlines():
        result_calc = def_calc(line.split())
        print(result_calc)
        if not isinstance(result_calc,str):
            calc_summ += result_calc
print("Result =",calc_summ)
