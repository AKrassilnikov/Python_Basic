def years(start_year,stop_year):
    count_1 = 0
    count_2 = 0
    for year in range(start_year,stop_year + 1):
        for same_num in str(year):
            if same_num == str(year)[0]:
                count_1 += 1
                if count_1 == 3:
                    year_list.append(year)
            elif same_num == str(year)[1]:
                count_2 += 1
                if count_2 == 3:
                    year_list.append(year)
        count_2 = 0
        count_1 = 0
    print(year_list)


year_list = []

start_year = int(input("Введите первый год: "))
stop_year = int(input("Введите второй год: "))
years(start_year,stop_year)
