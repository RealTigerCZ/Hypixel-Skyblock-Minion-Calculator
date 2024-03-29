class MinionFuel():
    def __init__(self, id, item, fuel_time, boost, multiplicative = False, special_case = None):
        self.__id = id
        self.__item = item
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
        if self.has_item_on_bazaar():
            toPrint += self.__item.get_name() + "\n"
        else:
            toPrint += self.__item + "\n"

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

    def has_item_on_bazaar(self):
        return type(self.__item) != "str"

    def get_item(self):
        return self.__item

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

    def add_fuel(self, item, fuel_time, boost, multiplicative = False, special_case = None):
        self.__max_id += 1
        self.__fuel_list.append(MinionFuel(self.__max_id, item, fuel_time, boost, multiplicative, special_case))

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


class Crystal():
    def __init__(self, id, name, boost, affecting, radius):
        self.__id = id
        self.__name = name
        self.__boost = boost
        self.__affecting = affecting
        self.__radius = radius

    def __repr__(self):
        toPrint = ""
        toPrint += self.__name + "\n"
        toPrint += f"ID: {self.__id}\n"
        toPrint += f"Boost: {self.__boost}\n"
        toPrint += f"affecting: {self.__affecting}\n"
        toPrint += f"radius: {self.__radius}\n"

        return toPrint

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_boost(self):
        return self.__boost

    def get_radius(self):
        return self.__radius

    def is_affecting(self, who):
        return self.__affecting == who


class Other():
    def __init__(self, id, name, boost):
        self.__id = id
        self.__name = name
        self.__boost = boost

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_boost(self):
        return self.__boost

class Other_bonuses():
    def __init__(self):
        self.__max_id = 0
        self.__all_list = []
        self.__crystal_list = []


    def add_crystal(self, name, boost, affecting, radius):
        self.__max_id += 1
        self.__crystal_list.append(Crystal(self.__max_id, name, boost, affecting, radius))
        self.__all_list.append(Crystal(self.__max_id, name, boost, affecting, radius))


    def search_all_by_name(self, name):
        for boost in self.__all_list:
            if boost.get_name() == name:
                return boost

    def search_crystals_by_name(self, name):
        for c in self.__crystal_list:
            if c.get_name() == name:
                return c

    def search_crystals_by_affecting(self, minion_type):
        for c in self.__crystal_list:
            if c.is_affecting(minion_type):
                return c

    def print_short_info(self):
        print("Crystals:")
        for crystal in self.__crystal_list:
            print("{:2d}".format(crystal.get_id()) + " " + crystal.get_name())
        print("\nOther:")



def create_fuels(items):
    fuels = Fuels()

    fuels.add_fuel(items.search_by_name("Coal"), 0.5, 5)
    fuels.add_fuel("Block of Coal", 5, 5)
    fuels.add_fuel(items.search_by_name("Enchanted Bread"), 12, 5)
    fuels.add_fuel(items.search_by_name("Enchanted Coal"), 24, 10)
    fuels.add_fuel(items.search_by_name("Enchanted Charcoal"), 36, 20)
    fuels.add_fuel(items.search_by_name("Solar Panel"), -1, 25, special_case = "solar panel")
    fuels.add_fuel(items.search_by_name("Enchanted Lava Bucket"), -1, 25)
    fuels.add_fuel(items.search_by_name("Magma Bucket"), -1, 30)
    fuels.add_fuel(items.search_by_name("Plasma Bucket"), -1, 35)
    fuels.add_fuel(items.search_by_name("Hamster Wheel"), 24, 50)
    fuels.add_fuel(items.search_by_name("Foul Flesh"), 5, 90)
    fuels.add_fuel("Tasty Cheese", 1, 2, multiplicative = True)
    fuels.add_fuel(items.search_by_name("Catalyst"), 3, 3, multiplicative = True)
    fuels.add_fuel(items.search_by_name("Hyper Catalyst"), 6, 4, multiplicative = True)

    return fuels

def create_bonuses():
    bonuses = Other_bonuses()

    bonuses.add_crystal("farm crystal", 10, "farming", 8)
    bonuses.add_crystal("woodcutting crystal", 10, "foraging", 12)
    bonuses.add_crystal("mithril crystal", 10, "mining", 40)

    return bonuses
