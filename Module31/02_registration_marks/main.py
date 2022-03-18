import re

car_numbers = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'
print()
print("Результат:")
civilian_cars = re.findall(r"\b\w\d{3}\w{2}\d{2,3}",car_numbers)
print("Список номеров частных автомобилей: ",civilian_cars)
taxi_cars = re.findall(r"\b\w{2}\d{3}\d{2,3}",car_numbers)
print("Список номеров такси:",taxi_cars)


