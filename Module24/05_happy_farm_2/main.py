class Potato:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зелёная', 3: 'Зрелая'}
    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print('Картошка {} сейчас {}'.format(self.index, Potato.states[self.state]))

class PotatoGarden:

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка проростает!')
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):
        for i_potato in self.potatoes:
            if not i_potato.is_ripe():
                print('Картошка ещё не созрела!\n')
                break
            else:
                print('Вся картошка созрела! Можно собирать!\n', end="")

class Gardener:
    gardener_name = input('Введите имя садовника: ')
    gardener_bed = input('Грядка с растением за которым ухаживает садовник: ')
    states_of_care = { 0: 'Поливает', 1: 'Окучивает', 2: 'Подкармливает', 3: 'Обрабатывает' }
    state = 1
    def print_state_of_care(self):
        key = gartner.state
        print('Садовник {} сейчас {} картошку\n'.format(Gardener.gardener_name,Gardener.states_of_care[key]))

my_garden = PotatoGarden(5)
my_garden.are_all_ripe()
gartner  = Gardener()
for _ in range(3):
    my_garden.grow_all()
    print()
    my_garden.are_all_ripe()
    gartner.print_state_of_care()
    gartner.state += 1
