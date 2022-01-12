def def_calc(data):
    action_list = ['+','-','/','*','**']
    action = 0
    for calc in range(len(action_list)):
        if data[1] == action_list[calc]:
            action = calc + 1
    return action

def def_action(action,line):
    first = float(line[0])
    second = float(line[2])
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
        result = def_calc(line.split())
        if result == 0:
            print('Error in line:', line[:-1], "change? yes or no",end=" ")
            change = input('> ')
            if change == 'yes':
                line_change = line.split()
                line_change[1] = input("Enter action: ")
                result = def_calc(line_change)
                result = def_action(result, line.split())
                calc_summ += result
                print("Result =", result)
            if change == 'no':
                print("Result =", def_action(result, line.split()))
        else:
            result = def_action(result, line.split())
            calc_summ += result
            print("Result =",result)
print('Summ results = ',calc_summ)
