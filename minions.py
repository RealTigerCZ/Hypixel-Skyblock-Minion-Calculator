
class Minion():
    def __init__(self, id, name, minion_type, products, items_per_actions, time_between_actions_for_every_tier, max_tier, xp_per_item, NPC_prize, use_autosmelt):
        self.__id = id
        self.__name = name
        self.__type = minion_type

        self.__time_between_actions = time_between_actions_for_every_tier
        self.__max_tier = max_tier

        self.__items_per_actions = items_per_actions
        self.__xp_per_item = xp_per_item
        self.__NPC_prize = NPC_prize

        self.__use_autosmelt = use_autosmelt

        if type(products) == str:
            self.__has_only_one_product = True
            self.__product = products

        else:
            self.__has_only_one_product = False
            self.__products = products

    def __repr__(self):
        to_print = "Name: " + self.__name + "\n"
        to_print += "Id: " + str(self.__id)  + "\n"
        to_print += "Type: " + self.__type  + "\n"

        if self.__has_only_one_product:
            to_print += "Product: " + self.__product + "\n"
        else:
            to_print += "Products: "
            if self.__use_autosmelt:
                to_print  += f"Without autosmelt upgrade: {self.__products[0]}, WITH autosmelt upgrade: {self.__products[1]}\n"
            else:
                for product in self.__products:
                    to_print += product + ", "
                to_print = to_print[:-2] + "\n"

        if self.__has_only_one_product:
            to_print += "Items per action: " + self.__items_per_actions + "\n"
        else:
            to_print += "Items per action: "
            for i in range(len(self.__products)):
                to_print += str(self.__items_per_actions[i]) + " x " + self.__products[i] + ", "
            to_print = to_print[:-2] + "\n"

        if self.__has_only_one_product:
            to_print += "XP per item: " + self.__xp_per_item + "\n"
        else:
            to_print += "XP per item: "
            for i in range(len(self.__products)):
                to_print += str(self.__xp_per_item[i]) + "XP for " + self.__products[i] + ", "
            to_print = to_print[:-2] + "\n"

        if self.__has_only_one_product:
            to_print += "NPC prize, coins per item: " + self.__NPC_prize + "\n"
        else:
            to_print += "NPC prize, coins per item: "
            for i in range(len(self.__products)):
                to_print += str(self.__NPC_prize[i]) + " coin for " + self.__products[i] + ", "
            to_print = to_print[:-2] + "\n"


        to_print += "Time between actions for every tier: \n"
        for i in range(len(self.__time_between_actions)):
            to_print += f"Tier {i+1} -> {self.__time_between_actions[i]}s\n"

        return to_print


    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_time_between_actions(self, tier):
        return self.__time_between_actions[tier-1]

    def get_max_tier(self):
        return self.__max_tier

    def get_items_per_actions(self):
        return self.__items_per_actions

    def get_xp_per_item(self):
        return self.__xp_per_item

    def get_products(self):
        if self.__has_only_one_product:
            return self.__product
        else:
            return self.__products

    def get_npc_prize(self):
        return self.__NPC_prize

    def has_only_one_product(self):
        return self.__has_only_one_product

    def use_autosmelt(self):
        return self.__use_autosmelt

class Minions():
    def __init__(self):
        self.__max_id = 0
        self.__minion_list = []

    def add_minion(self, name, minion_type, products, items_per_actions, time_between_actions_for_every_tier, max_tier, xp_per_item, NPC_prize, use_autosmelt = False):
        self.__max_id += 1
        self.__minion_list.append(Minion(self.__max_id, name, minion_type, products, items_per_actions, time_between_actions_for_every_tier, max_tier, xp_per_item, NPC_prize, use_autosmelt))

    def search_by_name(self, name):
        for minion in self.__minion_list:
            if minion.get_name() == name:
                return minion

    def search_by_id(self, id):
        for minion in self.__minion_list:
            if minion.get_id() == id:
                return minion

minions = Minions()

#                   name        type       products     item per action  time between actions      max tier  XP      NPC prize
minions.add_minion("wheat", "farming", ["wheat","seeds"], [1,1.5], [15,15,13,13,11,11,10,10,9,9,8,7], 12, [0.4,0.1], [-1,0.5])
minions.add_minion("carrot", "farming", "carrot", 3, [20,20,18,18,16,16,14,14,12,12,10,8], 12, 0.1, -1)
minions.add_minion("potato", "farming", "potato", 3, [20,20,18,18,16,16,14,14,12,12,10,8], 12, 0.1, -1)
minions.add_minion("pumpkin", "farming", "pumpkin", 1, [32,32,30,30,27,27,24,24,20,20,16,12], 12, 0.3, -1)
minions.add_minion("melon", "farming", "melon slice", 5, [24,24,22.5,22.5,21,21,18.5,18.5,16,16,13,10], 12, 0.1, -1)
minions.add_minion("mushroom", "farming", ["red mushroom","brown mushroom"], [0.5,0.5], [30,30,28,28,26,26,23,23,20,20,16,12], 12, [0.5,0.5], [-1,-1])
minions.add_minion("cocoa beans", "farming", "cocoa beans", 3, [27,27,25,25,23,23,21,21,18,18,15,12], 12, 0.2, -1)
minions.add_minion("cactus", "farming", ["cactus","cactus green"], 3, [27,27,25,25,23,23,21,21,18,18,15,12], 12, [0.2,0.2], [-1,-1], use_autosmelt = True)





"""
TO TEST:
 - recalcucalte profit
 - check autosmelt
"""



if __name__ == "__main__":
    print(minions.search_by_name("wheat"))
