violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
my_list = []
number = int(input("Сколько песен выбрать: "))
time_sum = 0
for i in range(number):
    print("Название", i + 1,"песни:", end = " ")
    song_name = input()
    for songs in violator_songs:
        if songs[0] == song_name:
            time_sum += songs[1]
    else:
        print("Такой песни нет")

print("Общее время звучания песен:", round(time_sum,2),"минут")


