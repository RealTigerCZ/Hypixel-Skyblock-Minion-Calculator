
class Minion():
    def __init__(self, id, name, minion_type, products, items_per_actions, time_between_actions_for_every_tier, max_tier, xp_per_item, NPC_prize, use_autosmelt, use_chicken_egg, use_flint_shovel, special_type, can_be_affected_by_crystal, special_minion_case):
        self.__id = id
        self.__name = name
        self.__type = minion_type

        self.__time_between_actions = time_between_actions_for_every_tier
        self.__max_tier = max_tier

        self.__items_per_actions = items_per_actions
        self.__xp_per_item = xp_per_item
        self.__NPC_prize = NPC_prize

        self.__use_autosmelt = use_autosmelt
        self.__use_chicken_egg = use_chicken_egg
        self.__use_flint_shovel = use_flint_shovel
        self.__special_type = special_type
        self.__affected_by_crystal = can_be_affected_by_crystal

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

            elif self.__use_chicken_egg:
                to_print  += f"{self.__products[0]}, {self.__products[1]} + with chicken egg upgrade: {self.__products[2]}\n"

            elif self.__use_flint_shovel:
                to_print  += f"Without flint shovel upgrade: {self.__products[0]}, WITH flint shovel upgrade: {self.__products[1]}\n"


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

    def get_primary_type(self):
        return self.__minion_type

    def get_boost_type(self):
        if self.__affected_by_crystal:
            if self.__special_type:
                return self.__special_type
            else:
                return self.__minion_type

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

    def use_chicken_egg(self):
        return self.__use_chicken_egg

    def use_flint_shovel(self):
        return self.__use_flint_shovel

class Minions():
    def __init__(self):
        self.__max_id = 0
        self.__minion_list = []

    def add_minion(self, name, minion_type, products, items_per_actions, time_between_actions_for_every_tier, max_tier, xp_per_item, NPC_prize, use_autosmelt = False, use_chicken_egg = False, use_flint_shovel = False, special_type = None, can_be_affected_by_crystal = True, special_minion_case = None):
        self.__max_id += 1
        self.__minion_list.append(Minion(self.__max_id, name, minion_type, products, items_per_actions, time_between_actions_for_every_tier, max_tier, xp_per_item, NPC_prize, use_autosmelt, use_chicken_egg, use_flint_shovel, special_type, can_be_affected_by_crystal, special_minion_case))

    def search_by_name(self, name):
        for minion in self.__minion_list:
            if minion.get_name() == name:
                return minion

    def search_by_id(self, id):
        for minion in self.__minion_list:
            if minion.get_id() == id:
                return minion

    def print_short_info(self):
        for minion in self.__minion_list:
            print("{:2d}".format(minion.get_id()) + " " + minion.get_name())

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
minions.add_minion("sugar cane", "farming", "sugar cane", 3, [22,22,20,20,18,18,16,16,14.5,14.5,12,9], 12, 0.1, -1)
minions.add_minion("cow", "farming", ["raw beef", "leather"], [1,1], [26,26,24,24,22,22,20,20,17,17,13,10], 12, [0.1,0.2], [-1,-1])
minions.add_minion("pig", "farming", "raw porkchop", 1, [26,26,24,24,22,22,20,20,17,17,13,10], 12, 0.2, -1)
minions.add_minion("chicken", "farming", ["raw chicken", "feather", "egg"], [1,1,1], [26,26,24,24,22,22,20,20,18,18,15,12], 12, [0.1,0.2,0.2], [-1,-1,-1], use_chicken_egg = True)
minions.add_minion("sheep", "farming", ["mutton","white wool"], [1,1], [24,24,22,22,20,20,18,18,16,16,12,9], 12, [0.1,0.1], [-1,-1])
minions.add_minion("rabbit", "farming", ["raw rabbit","rabbit's foot", "rabbit hide"], [1,0.35,0.35], [26,26,24,24,22,22,20,20,17,17,13,10], 12, [0.1,0.2,0.2], [-1,-1,-1])
minions.add_minion("nether wart", "farming", "nether wart", 3, [50,50,47,47,44,44,41,41,38,38,32,27], 12, 0.2, 3)

minions.add_minion("cobblestone", "mining", "cobblestone", 1, [14,14,12,12,10,10,9,9,8,8,7,6], 12, 0.1, -1, can_be_affected_by_crystal = False)
minions.add_minion("coal", "mining", "coal", 1, [15,15,13,13,12,12,10,10,9,9,7,6], 12, 0.3, -1)
minions.add_minion("iron", "mining", ["iron ore", "iron ingot"], 1, [17,17,15,15,14,14,12,12,10,10,8,7], 12, [0.3,0.3], [-1,-1], use_autosmelt = True)
minions.add_minion("gold", "mining", ["gold ore", "gold ingot"], 1, [22,22,20,20,18,18,16,16,14,14,11,9], 12, [0.4,0.4], [-1,-1], use_autosmelt = True)
minions.add_minion("diamond", "mining", "diamond", 1, [29,29,27,27,25,25,22,22,19,19,15,12], 12, 0.4, -1)
minions.add_minion("lapis", "mining", "lapis lazuli", 6, [29,29,27,27,25,25,23,23,21,21,18,16], 12, 0.1, -1)
minions.add_minion("emerald", "mining", "emerald", 1, [28,28,26,26,24,24,21,21,18,18,14,12], 12, 0.4, -1)
minions.add_minion("redstone", "mining", "redstone", 4.5, [29,29,27,27,25,25,23,23,21,21,18,16], 12, 0.2, -1)
minions.add_minion("quartz", "mining", "nether quartz", 1, [22.5,22.5,21,21,19,19,17,17,14.5,14.5,11.5], 11, 0.3, -1)
minions.add_minion("obsidian", "mining", "obsidian", 1, [45,45,42,42,39,39,35,35,30,30,24,21], 12, 0.4, -1, can_be_affected_by_crystal = False)
minions.add_minion("glowstone", "mining", "glowstone", 3, [25,25,23,23,21,21,19,19,16,16,13], 11, 0.2, -1, can_be_affected_by_crystal = False)
minions.add_minion("gravel", "mining", ["gravel", "flint"], 1, [26,26,24,24,22,22,19,19,16,16,13], 11, [0.2,0.2], [-1,-1], use_flint_shovel = True)
minions.add_minion("ice", "mining", "ice", 1, [14,14,12,12,10,10,9,9,8,8,7], 11, 0.5, -1, can_be_affected_by_crystal = False)
minions.add_minion("sand", "mining", "sand", 1, [26,26,24,24,22,22,19,19,16,16,13], 11, 0.2, -1, can_be_affected_by_crystal = False)
minions.add_minion("endstone", "mining", "endstone", 1, [26,26,24,24,22,22,19,19,16,16,13], 11, 0.4, -1, can_be_affected_by_crystal = False)
minions.add_minion("mithril", "mining", "mithril", 2, [80,80,75,75,70,70,65,65,60,60,55,50], 12, 0.4, -1)

minions.add_minion("zombie", "combat", ["rotten flesh", "poisonous potato", "potato", "carrot"], [1,0.05,0.01,0.01], [26,26,24,24,22,22,20,20,17,17,13], 11, [0.3,0,0.1,0.1], [-1,-1,-1,-1])
minions.add_minion("skeleton", "combat", "bone", 1, [26,26,24,24,22,22,20,20,17,17,13], 11, 0.2, -1)
minions.add_minion("skeleton", "combat", "bone", 1, [26,26,24,24,22,22,20,20,17,17,13], 11, 0.2, -1)
minions.add_minion("spider", "combat", ["string","spider eye"], [1,0.5], [26,26,24,24,22,22,20,20,17,17,13], 11, [0.2,0.3], [-1,-1])
minions.add_minion("cave spider", "combat", ["spider eye", "string"], [1,0.5], [26,26,24,24,22,22,20,20,17,17,13], 11, [0.3,0.2], [-1,-1])
minions.add_minion("creeper", "combat", "gun powder", 1, [27,27,25,25,23,23,21,21,18,18,14], 11, 0.3, -1)
minions.add_minion("enderman", "combat", "ender pearl", 1, [32,32,30,30,28,28,25,25,22,22,18], 11, 0.3, -1)
minions.add_minion("ghast", "combat", "ghast tear", 1, [50,50,47,47,44,44,41,41,38,38,32], 11, 0.5, -1)
minions.add_minion("slime", "combat", "slime ball", 1.8, [26,26,24,24,22,22,19,19,16,16,12], 11, 0.2, -1)
minions.add_minion("blaze", "combat", "blaze rod", 1, [33,33,31,31,28.5,28.5,25,25,21,21,16.5], 11, 0.3, -1)
minions.add_minion("magma cube", "combat", "magma cream", 1.8, [32,32,30,30,28,28,25,25,22,22,18], 11, 0.2, -1)

minions.add_minion("revenant", "slayer", ["rotten flesh","diamond"], [3,0.2], [29,29,26,26,23,23,19,19,14.5,14.5,10,8], 12, [0.3,0.4], [-1,-1], special_minion_case = "revenant")
minions.add_minion("tarantula", "slayer", ["string","spider eye", "iron ingot", ], [3.16,1, 0.2], [29,29,26,26,23,23,19,19,14.5,14.5,10], 11, [0.2,0.3,0.3], [-1,-1,-1], special_minion_case = "tarantula")
minions.add_minion("voidling", "slayer", ["quartz","obsidian"], [0.4,2.42], [45,45,42,42,39,39,35,35,30,30,24], 11, [-1.-1], [-1,-1], special_minion_case = "voidling")

minions.add_minion("oak", "foraging", "oak wood", 4, [48,48,45,45,42,42,38,38,33,33,27], 11, 0.1, -1)
minions.add_minion("birch", "foraging", "birch wood", 4, [48,48,45,45,42,42,38,38,33,33,27], 11, 0.1, -1)
minions.add_minion("spruce", "foraging", "spruce wood", 4, [48,48,45,45,42,42,38,38,33,33,27], 11, 0.1, -1)
minions.add_minion("dark oak", "foraging", "dark oak wood", 4, [48,48,45,45,42,42,38,38,33,33,27], 11, 0.1, -1)
minions.add_minion("acacia", "foraging", "acacia wood", 4, [48,48,45,45,42,42,38,38,33,33,27], 11, 0.1, -1)
minions.add_minion("jungle", "foraging", "jungle wood", 4, [48,48,45,45,42,42,38,38,33,33,27], 11, 0.1, -1)

#other
minions.add_minion("flower", "foraging", "Allium, Azure Bluet, Blue Orchid, Dandelion, Poppy, Peony, Oxeye Daisy, Rose Bush, Lilac, Red Tulip, Sunflower, White Tulip, Pink Tulip, Orange Tulips flower randomly: The two-high flowers can be turned into their specific dyes and sold for two coins instead of 1", 0, [30,29,28,27,26,25,24,23,22,20,18], 11, -1, 1, special_type = "other", special_minion_case = "flower")
minions.add_minion("snow", "mining", "snow ball", 4, [13,13,12,12,11,11,9.5,9.5,8,8,6.5], 11, 0.1, -1, special_type = "other")

minions.add_minion("clay", "fishing", "clay", 4, [32,32,30,30,27.5,27.5,24,24,20,20,16], 11, 0.1, -1, can_be_affected_by_crystal = False, special_type = "mining")
minions.add_minion("fishing", "fishing", ["raw fish", "raw salmon", "pufferfish", "clownfish", "prismarine crystals", "prismarine shard", "sponge"], [1, 0.5, 0.24, 0.08, 0.06, 0.06, 0.06], [78,75,72,72,68,68,62.5,62.5,53,53,35], 11, [0.5, 0.7, 1, 2, 0.25, 0.25, 0.5], [-1,-1,-1,-1,-1,-1,-1])





if __name__ == "__main__":
    #testing
    print(minions.search_by_name("wheat"))
    minions.print_short_info()
