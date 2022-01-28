
class MyDict:
    my_dict = {'ab':'ba','aa':'aa','bb':'bb','ba':'ab'}

    def get_value(self,key):
        return MyDict.my_dict.get(key,0)


value = input("Input key: ")
result = MyDict()
print("Return: ",result.get_value(value))
