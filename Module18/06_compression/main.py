string = input("Введите данные:")
cnt = 0
shifr = ''
for i in range(len(string)):
    sim = string[i]
    cnt += 1
    if i == len(string) - 1:
        shifr = shifr + string[i] + str(cnt)
        break
    if string[i] != string[i+1]:
        shifr = shifr + string[i] + str(cnt)
        cnt = 0
print (shifr)

