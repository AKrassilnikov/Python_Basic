
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
def my_songs(song_name):
    for songs in violator_songs:
        if songs[0] == song_name:
            my_list.append(song_name)
            return songs[1]
    else:
        print("Такой песни нет")
        return 0

my_list = []
number = int(input("Сколько песен выбрать: "))
time_sum = 0
for i in range(number):
    print("Название", i + 1,"песни:", end = " ")
    song_name = input()
    if my_list.count(song_name) == True:
        print("Эта песня уже добавлена")
        continue
    else:
        time = my_songs(song_name)
        time_sum += time

print("Общее время звучания песен:", round(time_sum,2),"минут")


