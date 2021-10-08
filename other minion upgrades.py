class Upgrade():
    def __init__(self, id, name, affects_speed, adds_outputs, one_per_profile = False, one_per_minion = False, speed_mult = None, outputs = None, special_case = None):
        self.__id = id
        self.__name = name
        self.__affects_speed = affects_speed
        self.__adds_outputs = adds_outputs
        self.__special_case = special_case

        self.__one_per_profile = one_per_profile
        self.__one_per_minion = one_per_minion
        self.__speed_mult = speed_mult
        self.__outputs = outputs
        self.__special_case = special_case

    def __repr__(self):
        toPrint = self.__name
        toPrint += f"\nID: {self.__id}\n"
        toPrint += f"Affects speed: {self.__affects_speed}\n"
        if self.__affects_speed:
            toPrint += f"Speed multiplier: {self.__speed_mult}\n"

        toPrint += f"Adds outputs: {self.__adds_outputs}\n"
        if self.__adds_outputs:
            toPrint += f"Outputs: {self.__outputs}\n"

        toPrint += f"One per profile: {self.__one_per_profile}\n"
        toPrint += f"One per minion: {self.__one_per_minion}\n"
        return toPrint

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_speed_mult(self, minion):
        if special_case == "better soulflow":
            if minion.get_name() == "voidling":
                return 1 + 0.03 * minion.get_tier()
        return self.__speed_mult

    def get_outputs(self):
        return outputs

    def calc_outputs(self, time, time_between_actions, items_per_actions):
        if special_case == "dia spread":
            return 0.1 * items_per_actions * (time/time_between_actions)

        elif special_case == "potato spread":
            #NOT CONFIRMED
            return 0.1 * items_per_actions * (time/time_between_actions)

        elif special_case == "krapmus helm":
            return -1

        elif "soulflow" in special_case:
            return time/180

    def one_per_profile(self):
        return self.__one_per_profile

    def one_per_minion(self):
        return self.__one_per_minion

    def affects_speed(self):
        return self.__affect_speed

    def adds_outputs(self):
        return self.__adds_outputs

class Upgrades():
    def __init__(self):
        self.__max_id = 0
        self.__upgrades_list = []

    def add_upgrade(self,  name, affects_speed, adds_outputs, one_per_profile = False, one_per_minion = False, speed_mult = None, outputs = None, special_case = None):
        self.__max_id += 1
        self.__upgrades_list.append(Upgrade(self.__max_id,  name, affects_speed, adds_outputs, one_per_profile, one_per_minion, speed_mult, outputs, special_case))

    def search_by_name(self, name):
        for upgrade in self.__upgrades_list:
            if upgrade.get_name() == name:
                return upgrade

    def search_by_id(self, id):
        for upgrade in self.__upgrades_list:
            if upgrade.get_id() == id:
                return upgrade

    def print_short_info(self):
        for upgrade in self.__upgrades_list:
            print("{:2d}".format(upgrade.get_id()) + " " + upgrade.get_name())

upgrades = Upgrades()

upgrades.add_upgrade("auto smelter or dwarven super compactor", False, False, one_per_minion = True)
upgrades.add_upgrade("diamond spreading", False, True, outputs = "diamond", special_case = "dia spread")
upgrades.add_upgrade("potato spreading", False, True, outputs = "potato", special_case = "potato spread")
upgrades.add_upgrade("krampus helmet", False, True, outputs = "red gift", special_case = "krampus helm")
upgrades.add_upgrade("minion expander", True, False, speed_mult = 1.05)
upgrades.add_upgrade("flycatcher", True, False, speed_mult = 1.2)
upgrades.add_upgrade("enchanted egg", False, False)
upgrades.add_upgrade("flint shovel", False, False)
upgrades.add_upgrade("lesser soulflow engine", True, True, speed_mult = 0.5, outputs = "raw soulfow", special_case = "lesser slouflow")
upgrades.add_upgrade("soulflow engine", True, True, speed_mult = 0.5, outputs = "raw soulfow", special_case = "better slouflow")

if __name__ == "__main__":
    #testing
    print(upgrades.search_by_name("flycatcher"))
    upgrades.print_short_info()
