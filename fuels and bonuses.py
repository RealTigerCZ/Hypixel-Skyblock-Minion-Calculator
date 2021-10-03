class MinionFuel():
    def __init__(self, id, name, fuel_time, boost, multiplicative = False, special_case = None):
        self.__id = id
        self.__name = name
        self.__fuel_time = fuel_time
        self.__boost = boost
        self.__multiplicative = multiplicative
        self.__special_case = special_case

        if self.__fuel_time == -1:
            self.__infinite = True
        else:
            self.__infinite = False

    def __repr__(self):
        toPrint = ""
        toPrint += self.__name + "\n"
        toPrint += f"ID: {self.__id}\n"

        if self.__infinite:
            toPrint += f"Fuel time: infinite\n"
        else:
            toPrint += f"Fuel time: {self.__fuel_time} hour(s)\n"

        if self.__multiplicative:
            toPrint += f"Boost: {self.__boost} times\n"
        else:
            toPrint += f"Boost: {self.__boost}%\n"

        return toPrint

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_fuel_time(self):
        return self.__fuel_time

    def get_boost(self):
        return self.__boost

    def is_multiplicative(self):
        return self.__multiplicative

    def is_infinite(self):
        return self.__infinite

class Fuels():
    def __init__(self):
        self.__max_id = 0
        self.__fuel_list = []

    def add_fuel(self, name, fuel_time, boost, multiplicative = False, special_case = None):
        self.__max_id += 1
        self.__fuel_list.append(MinionFuel(self.__max_id, name, fuel_time, boost, multiplicative, special_case))

    def search_by_name(self, name):
        for fuel in self.__fuel_list:
            if fuel.get_name() == name:
                return fuel

    def search_by_id(self, id):
        for fuel in self.__fuel_list:
            if fuel.get_id() == id:
                return fuel

    def print_short_info(self):
        for fuel in self.__fuel_list:
            print("{:2d}".format(fuel.get_id()) + " " + fuel.get_name())


fuels = Fuels()

fuels.add_fuel("coal", 0.5, 5)
fuels.add_fuel("block of coal", 5, 5)
fuels.add_fuel("enchanted bread", 12, 5)
fuels.add_fuel("enchanted coal", 24, 10)
fuels.add_fuel("enchanted charcoal", 36, 20)
fuels.add_fuel("solar panel", -1, 25, special_case = "solar panel")
fuels.add_fuel("enchanted lava bucket", -1, 25)
fuels.add_fuel("magma bucket", -1, 30)
fuels.add_fuel("plasma bucket", -1, 35)
fuels.add_fuel("hamster wheel", 24, 50)
fuels.add_fuel("foul flesh", 5, 90)
fuels.add_fuel("tasty cheese", 1, 2, multiplicative = True)
fuels.add_fuel("catalyst", 3, 3, multiplicative = True)
fuels.add_fuel("hyper catalyst", 6, 4, multiplicative = True)



class Other_bonuses():
    def __init__(self, id):
        pass



if __name__ == "__main__":
    #testing
    print(fuels.search_by_name("coal"))
    print(fuels.search_by_name("enchanted lava bucket"))
    print(fuels.search_by_name("catalyst"))
    fuels.print_short_info()
