class Date:
    def __init__(self,string) -> None:
        """ Функция класса принимает на вход дату ввиде строки
        :param string
        """
        self.string = string

    @classmethod
    def date_is_valid(cls,string) -> bool:
        """ Функция класса принимает на вход строку и проверяет на корректность даты
        :param string
        """
        s = string.split("-")
        return False if int(s[0]) > 31 or int(s[1]) > 12 or len(s) != 3 else True

    def __str__(self):
        """ Функция вывода даты """
        s = self.string.split("-")
        return 'День: ' + s[0] + ' Месяц: ' + s[1] + ' Год: ' + s[2]

date = Date('10-12-2022')
print(date)
print(Date.date_is_valid('10-15-2022'))