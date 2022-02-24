import os
from typing import  Any


class File:
    """ Класс контекст-менеджер """


    def __init__(self,path:str,row:int) -> None:
        """ Фенкция приёма пути и  имени файла + порядковый номер операции
        :param path:
        :param row:
        """
        self.path = path
        self.row = row
        self.code = "a"

    def __enter__(self) -> Any:
        """ Функция созания файла и записи """

        self.file = open(self.path,self.code)
        self.file.write(f"{row + 1} Hello World!!!!!\n")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        """ Функция закрытия файла и обработки ошибок """

        self.file.close()
        return True


for row in range(14):
    with File(os.path.abspath("TEST_2.txt"),row) as TEST:
        print("Done")
