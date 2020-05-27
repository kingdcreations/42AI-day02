import time
import getpass
from random import randint


def log(func):

    def wrapper(*args, **kwargs):
        f = open('machine.log', 'a')
        name = func.__name__.replace("_", " ").title()
        t = time.time()
        func(*args, **kwargs)
        texec = time.time() - t
        txt = f"({getpass.getuser()}) Running: {name}"
        print(txt.ljust(30 + len(getpass.getuser()), " "), file=f, end="")
        ttxt = "[ exec-time = "
        if (texec < 1):
            ttxt += '{:.3f}'.format(texec * 1000)
            ttxt += " ms ]"
        else:
            ttxt += '{:.3f}'.format(texec)
            ttxt += " s  ]"
        print(ttxt, file=f)
        f.close()
        return func(*args, **kwargs)
    return wrapper


class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    open("machine.log", "w")
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
        machine.make_coffee()
        machine.add_water(70)
