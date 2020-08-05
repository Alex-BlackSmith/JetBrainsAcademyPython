class CoffeeMachine():
    num_of_machines = 0
    coffee_machine_supplies = {'water': 400,
                               'milk':540,
                               'coffee beans': 120,
                               'disposable cups':9,
                               'money': 550
    }

    coffee_table = {1: {'water': 250, 'milk': 0,'coffee beans': 16, 'money': -4},
                    2: {'water': 350, 'milk': 75, 'coffee beans': 20, 'money': -7},
                    3: {'water': 200, 'milk': 100, 'coffee beans': 12, 'money': -6}
    }

    def __new__(cls):
        if cls.num_of_machines == 0:
            cls.num_of_machines += 1
            return object.__new__(cls)
        return None

    def __init__(self):
        self.action = ""
        self.state = True

    def remaining(self):
        print('The coffee machine has:')
        for supply in self.coffee_machine_supplies:
            if supply == 'money':
                print('$', end='')
            print(self.coffee_machine_supplies[supply], 'of', supply)
        print()

    def take(self):
        money = self.coffee_machine_supplies['money']
        print('I gave you ${}'.format(money))
        print()
        self.coffee_machine_supplies['money'] = 0

    def fill_machine(self):
        print('Write how many ml of water do you want to add:')
        self.coffee_machine_supplies['water'] += int(input())
        print('Write how many ml of milk do you want to add:')
        self.coffee_machine_supplies['milk'] += int(input())
        print('Write how many grams of coffee beans do you want to add:')
        self.coffee_machine_supplies['coffee beans'] += int(input())
        print('Write how many disposable cups of coffee do you want to add:')
        self.coffee_machine_supplies['disposable cups'] += int(input())

    def Check_supplies(self, type):
        for supply, amount in self.coffee_table[type].items():
            if amount > self.coffee_machine_supplies[supply]:
                print('Sorry, not enough {}!'.format(supply))
                return False
        print('I have enough resources, making you a coffee!')
        return True

    def Make_coffee(self, type):
        if self.Check_supplies(type):
            for supply, amount in self.coffee_table[type].items():
                self.coffee_machine_supplies[supply] -= self.coffee_table[type][supply]
            self.coffee_machine_supplies['disposable cups'] -= 1
        #return supplies

    def input_process(self):
        print('Write action (buy, fill, take, remaining, exit):')
        self.action = input()
        if self.action == 'buy':
            print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
            coffee_type = input()
            if coffee_type == 'back':
                return True
            self.Make_coffee(int(coffee_type))
        elif self.action == 'fill':
            self.fill_machine()
        elif self.action == 'take':
            self.take()
        elif self.action == 'remaining':
            self.remaining()
        elif self.action == 'exit':
            self.state = False
        return self.state

coffee_machine = CoffeeMachine()

while True:
    if coffee_machine.input_process():
        continue
    else:
        break


