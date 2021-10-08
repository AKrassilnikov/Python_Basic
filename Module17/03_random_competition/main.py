import random

team_1 = [round(random.uniform(1, 10),2) for _ in range(20)]
team_2 = [round(random.uniform(1, 10),2) for _ in range(20)]
team_winners = [(team_1[score] if team_1[score] > team_2[score]
                   else team_2[score]) for score in range(20)]
print("Первая команда: ",team_1)
print("Вторая команда: ",team_2)

print("Победители тура: ",team_winners)
