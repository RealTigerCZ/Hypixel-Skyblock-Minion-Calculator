class Minion():
    def __init__(self, id, name, minion_type, products, items_per_actions, time_between_actions_for_every_tier, max_tier, xp_per_item, use_autosmelt, use_chicken_egg, use_flint_shovel, special_type, can_be_affected_by_crystal, special_minion_case):
        self.__id = id
        self.__name = name
        self.__type = minion_type

        self.__time_between_actions = time_between_actions_for_every_tier
        self.__max_tier = max_tier

        self.__items_per_actions = items_per_actions
        self.__xp_per_item = xp_per_item
        self.__NPC_prize = None

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
        """
        TEPORARY DISABLED!
        if special_minion_case != "flower":
            self.__check()
        """
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
            to_print += f"Items per action: {self.__items_per_actions}\n"
        else:
            to_print += "Items per action: "
            for i in range(len(self.__products)):
                to_print += str(self.__items_per_actions[i]) + " x " + self.__products[i] + ", "
            to_print = to_print[:-2] + "\n"

        if self.__has_only_one_product:
            to_print += f"XP per item:  {self.__xp_per_item}\n"
        else:
            to_print += "XP per item: "
            for i in range(len(self.__products)):
                to_print += str(self.__xp_per_item[i]) + "XP for " + self.__products[i] + ", "
            to_print = to_print[:-2] + "\n"

        if self.__has_only_one_product:
            to_print += f"NPC prize, coins per item:  {self.__NPC_prize}\n"
        else:
            to_print += "NPC prize, coins per item: "
            for i in range(len(self.__products)):
                to_print += str(self.__NPC_prize[i]) + " coin for " + self.__products[i] + ", "
            to_print = to_print[:-2] + "\n"


        to_print += "Time between actions for every tier: \n"
        for i in range(len(self.__time_between_actions)):
            to_print += f"Tier {i+1} -> {self.__time_between_actions[i]}s\n"

        return to_print

    def __check(self):
        def helper(values, types):
            if type(values) == list:
                for x in values:
                    if type(x) not in types:
                        return True

        def value_check(errors_num, errors, value, value_name ,value_type, lenght = None, msg = None, negative = False, zero = False, in_list_values = None):
            def int_check(errors_num, errors, value, value_name, negative, zero):
                if value == -1:
                    errors_num += 1
                    errors += f"E{errors_num}: Invalid {value_name} -> NOT YET FINISHED! -> {value}\n"
                elif value < 0 and not negative:
                    errors_num += 1
                    errors += f"E{errors_num}: Invalid {value_name} -> Can't be negative -> {value}\n"
                elif value == 0 and not zero:
                    errors_num += 1
                    errors += f"E{errors_num}: Invalid {value_name} -> Can't be zero -> {value}\n"
                return errors_num, errors

            if value == None:
                errors_num += 1
                errors += f"E{errors_num}: Invalid {value_name} -> is not defined  -> {value}\n"
            elif value_type == str:
                if type(value) != value_type:
                    errors_num += 1
                    errors += f"E{errors_num}: Invalid {value_name} -> not a string  -> {value}\n"
            elif value_type == list:
                if type(value) != value_type:
                    errors_num += 1
                    errors += f"E{errors_num}: Invalid {value_name} -> not a list  -> {value}\n"
                elif len(value) != lenght:
                    errors_num += 1
                    errors += f"E{errors_num}: Invalid lenght of {value_name} -> expected {lenght} -> and its {value}\n"
                else:
                    correct_type = True
                    correct_value = True
                    not_finished = False
                    if in_list_values == "int":
                        for item in value:
                            if type(item) not in [int, float]:
                                correct_type = False
                            elif item < 0:
                                if item == -1:
                                    not_finished = True
                                else:
                                    correct_value = False
                            elif not zero and item == 0:
                                correct_value = False
                        if not correct_type:
                            errors_num += 1
                            errors += f"E{errors_num}: Invalid value in {value_name} -> some value is not a number -> {value}\n"
                        if not correct_value:
                            errors_num += 1
                            errors += f"E{errors_num}: Invalid value in {value_name} -> some value is zero or negative -> {value}\n"
                        if not_finished:
                            errors_num += 1
                            errors += f"E{errors_num}: Invalid value in {value_name} -> some value is NOT FINISHED (-1) -> {value}\n"

                    elif in_list_values == "str":
                        for item in value:
                            if type(item) != str:
                                correct_type != False
                        if not correct_type:
                            errors_num += 1
                            errors += f"E{errors_num}: Invalid value in {value_name} -> some value is not a string -> {value}\n"

            elif value_type == [int, float] or value_type == [float, int]:
                if type(value) not in value_type:
                    errors_num += 1
                    errors += f"E{errors_num}: Invalid {value_name} -> not a number -> {value}\n"
                else:
                    errors_num, errors = int_check(errors_num, errors, value, value_name, negative, zero)

            elif value_type == int:
                if type(value) != value_type:
                    errors_num += 1
                    errors += f"E{errors_num}: Invalid {value_name} -> not an integer -> {value}\n"
                else:
                    errors_num, errors = int_check(errors_num, errors, value, value_name, negative, zero)


            elif type(value_type) == list:
                if type(value) not in value_type:
                    errors_num += 1
                    errors += f"E{errors_num}: Invalid {value_name} -> {msg} -> {value}\n"
            return errors_num, errors

        errors_num = 0
        errors = ""

        errors_num, errors = value_check(errors_num, errors, self.__id, "ID", int, zero = True)
        errors_num, errors = value_check(errors_num, errors, self.__name, "name", str)
        errors_num, errors = value_check(errors_num, errors, self.__type, "type", str)

        if self.__type not in ["mining", "farming", "slayer", "foraging", "fishing", "combat"]:
            errors_num += 1
            errors += f"E{errors_num}: Invalid minion type -> {self.__type}\n"

        errors_num, errors = value_check(errors_num, errors, self.__time_between_actions, "time between actions", list, lenght = self.__max_tier, in_list_values = "int")
        errors_num, errors = value_check(errors_num, errors, self.__max_tier, "max tier", int)
        errors_num, errors = value_check(errors_num, errors, self.__max_tier, "max tier", int)
        errors_num, errors = value_check(errors_num, errors, self.__max_tier, "max tier", int)

        if self.__has_only_one_product:
            errors_num, errors = value_check(errors_num, errors, self.__product, "product", str)
            errors_num, errors = value_check(errors_num, errors, self.__items_per_actions, "items per actions", [int, float])
            errors_num, errors = value_check(errors_num, errors, self.__xp_per_item, "XP per item", [int, float], zero = True)
            errors_num, errors = value_check(errors_num, errors, self.__NPC_prize, "NPC prize", [int, float])
        else:
            errors_num, errors = value_check(errors_num, errors, self.__products, "product", list, lenght = len(self.__products), in_list_values = "str")
            errors_num, errors = value_check(errors_num, errors, self.__items_per_actions, "items per actions", list, lenght = len(self.__products), in_list_values = "int")
            errors_num, errors = value_check(errors_num, errors, self.__xp_per_item, "XP per item", list, lenght = len(self.__products), in_list_values = "int", zero = True)
            errors_num, errors = value_check(errors_num, errors, self.__NPC_prize, "NPC prize", list, lenght = len(self.__products), in_list_values = "int")

        if errors_num:
            print(f"\n{self.__name} minion checking finished with {errors_num} error(s)\n{errors}")
        else:
            print(f"{self.__name} minion checking finished with {errors_num} errors")

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

    def add_minion(self, name, minion_type, products, items_per_actions, time_between_actions_for_every_tier, max_tier, xp_per_item, use_autosmelt = False, use_chicken_egg = False, use_flint_shovel = False, special_type = None, can_be_affected_by_crystal = True, special_minion_case = None):
        self.__max_id += 1
        self.__minion_list.append(Minion(self.__max_id, name, minion_type, products, items_per_actions, time_between_actions_for_every_tier, max_tier, xp_per_item, use_autosmelt, use_chicken_egg, use_flint_shovel, special_type, can_be_affected_by_crystal, special_minion_case))

    def search_by_name(self, name):
        for minion in self.__minion_list:
            if minion.get_name() == name:
                return minion

    def search_by_id(self, id):
        return self.__minion_list[id-1]

    def print_short_info(self):
        for minion in self.__minion_list:
            print("{:2d}".format(minion.get_id()) + " " + minion.get_name())



def create_minions(items):
    minions = Minions()
    #import ignore.babla as babla #DEBUGGING TOOL

    def foo(name):
        item = items.search_by_name(name)
        if not item:
            print(f"Warning: item '{name}' not found!")
            #print(babla.search(name)) #DEBUGGING TOOL
        return item

    #                   name        type       products     item per action  time between actions      max tier  XP      NPC prize
    minions.add_minion("wheat", "farming", [foo("Wheat"), foo("Seeds")], [1,1.5], [15,15,13,13,11,11,10,10,9,9,8,7], 12, [0.4,0.1])
    minions.add_minion("carrot", "farming", foo("Carrot"), 3, [20,20,18,18,16,16,14,14,12,12,10,8], 12, 0.1)
    minions.add_minion("potato", "farming", foo("Potato"), 3, [20,20,18,18,16,16,14,14,12,12,10,8], 12, 0.1)
    minions.add_minion("pumpkin", "farming", foo("Pumpkin"), 1, [32,32,30,30,27,27,24,24,20,20,16,12], 12, 0.3)
    minions.add_minion("melon", "farming", foo("Melon"), 5, [24,24,22.5,22.5,21,21,18.5,18.5,16,16,13,10], 12, 0.1)
    minions.add_minion("mushroom", "farming", [foo("Red Mushroom"), foo("Brown Mushroom")], [0.5,0.5], [30,30,28,28,26,26,23,23,20,20,16,12], 12, [0.5,0.5])
    minions.add_minion("cocoa beans", "farming", foo("Cocoa Beans"), 3, [27,27,25,25,23,23,21,21,18,18,15,12], 12, 0.2)
    minions.add_minion("cactus", "farming", [foo("Cactus"), foo("Cactus Green")], [3,3], [27,27,25,25,23,23,21,21,18,18,15,12], 12, [0.2,0.2], use_autosmelt = True)
    minions.add_minion("sugar cane", "farming", foo("Sugar Cane"), 3, [22,22,20,20,18,18,16,16,14.5,14.5,12,9], 12, 0.1)
    minions.add_minion("cow", "farming", [foo("Raw Beef"), foo("Leather")], [1,1], [26,26,24,24,22,22,20,20,17,17,13,10], 12, [0.1,0.2], can_be_affected_by_crystal = False)
    minions.add_minion("pig", "farming", foo("Raw Porkchop"), 1, [26,26,24,24,22,22,20,20,17,17,13,10], 12, 0.2, can_be_affected_by_crystal = False)
    minions.add_minion("chicken", "farming", [foo("Raw Chicken"), foo("Feather"), foo("Egg")], [1,1,1], [26,26,24,24,22,22,20,20,18,18,15,12], 12, [0.1,0.2,0.2], use_chicken_egg = True, can_be_affected_by_crystal = False)
    minions.add_minion("sheep", "farming", [foo("Mutton"),foo("White Wool")], [1,1], [24,24,22,22,20,20,18,18,16,16,12,9], 12, [0.1,0.1], can_be_affected_by_crystal = False)
    minions.add_minion("rabbit", "farming", [foo("Raw Rabbit"),foo("Rabbit's Foot"), foo("Rabbit Hide")], [1,0.35,0.35], [26,26,24,24,22,22,20,20,17,17,13,10], 12, [0.1,0.2,0.2], can_be_affected_by_crystal = False)
    minions.add_minion("nether wart", "farming", foo("Nether Wart"), 3, [50,50,47,47,44,44,41,41,38,38,32,27], 12, 0.2)

    minions.add_minion("cobblestone", "mining", foo("Cobblestone"), 1, [14,14,12,12,10,10,9,9,8,8,7,6], 12, 0.1, can_be_affected_by_crystal = False)
    minions.add_minion("coal", "mining", foo("Coal"), 1, [15,15,13,13,12,12,10,10,9,9,7,6], 12, 0.3)
    minions.add_minion("iron", "mining", [foo("Iron Ore"), foo("Iron Ingot")], [1,1], [17,17,15,15,14,14,12,12,10,10,8,7], 12, [0.3,0.3], use_autosmelt = True)
    minions.add_minion("gold", "mining", [foo("Gold Ore"), foo("Gold Ingot")], [1,1], [22,22,20,20,18,18,16,16,14,14,11,9], 12, [0.4,0.4], use_autosmelt = True)
    minions.add_minion("diamond", "mining", foo("Diamond"), 1, [29,29,27,27,25,25,22,22,19,19,15,12], 12, 0.4)
    minions.add_minion("lapis", "mining", foo("Lapis Lazuli"), 6, [29,29,27,27,25,25,23,23,21,21,18,16], 12, 0.1)
    minions.add_minion("emerald", "mining", foo("Emerald"), 1, [28,28,26,26,24,24,21,21,18,18,14,12], 12, 0.4)
    minions.add_minion("redstone", "mining", foo("Redstone"), 4.5, [29,29,27,27,25,25,23,23,21,21,18,16], 12, 0.2)
    minions.add_minion("quartz", "mining", foo("Nether Quartz"), 1, [22.5,22.5,21,21,19,19,17,17,14.5,14.5,11.5], 11, 0.3)
    minions.add_minion("obsidian", "mining", foo("Obsidian"), 1, [45,45,42,42,39,39,35,35,30,30,24,21], 12, 0.4, can_be_affected_by_crystal = False)
    minions.add_minion("glowstone", "mining", foo("Glowstone Dust"), 3, [25,25,23,23,21,21,19,19,16,16,13], 11, 0.2, can_be_affected_by_crystal = False)
    minions.add_minion("gravel", "mining", [foo("Gravel"), foo("Flint")], [1,1], [26,26,24,24,22,22,19,19,16,16,13], 11, [0.2,0.2], use_flint_shovel = True)
    minions.add_minion("ice", "mining", foo("Ice"), 1, [14,14,12,12,10,10,9,9,8,8,7], 11, 0.5, can_be_affected_by_crystal = False)
    minions.add_minion("sand", "mining", foo("Sand"), 1, [26,26,24,24,22,22,19,19,16,16,13], 11, 0.2, can_be_affected_by_crystal = False)
    minions.add_minion("endstone", "mining", foo("End Stone"), 1, [26,26,24,24,22,22,19,19,16,16,13], 11, 0.4, can_be_affected_by_crystal = False)
    minions.add_minion("mithril", "mining", foo("Mithril"), 2, [80,80,75,75,70,70,65,65,60,60,55,50], 12, 0.4)

    minions.add_minion("zombie", "combat", [foo("Rotten Flesh"), foo("Poisonous Potato"), foo("Potato"), foo("Carrot")], [1,0.05,0.01,0.01], [26,26,24,24,22,22,20,20,17,17,13], 11, [0.3,0,0.1,0.1])
    minions.add_minion("skeleton", "combat", foo("Bone"), 1, [26,26,24,24,22,22,20,20,17,17,13], 11, 0.2)
    minions.add_minion("spider", "combat", [foo("String"), foo("Spider Eye")], [1,0.5], [26,26,24,24,22,22,20,20,17,17,13], 11, [0.2,0.3])
    minions.add_minion("cave spider", "combat", [foo("Spider Eye"), foo("String")], [1,0.5], [26,26,24,24,22,22,20,20,17,17,13], 11, [0.3,0.2])
    minions.add_minion("creeper", "combat", foo("Gunpowder"), 1, [27,27,25,25,23,23,21,21,18,18,14], 11, 0.3)
    minions.add_minion("enderman", "combat", foo("Ender Pearl"), 1, [32,32,30,30,28,28,25,25,22,22,18], 11, 0.3)
    minions.add_minion("ghast", "combat", foo("Ghast Tear"), 1, [50,50,47,47,44,44,41,41,38,38,32], 11, 0.5)
    minions.add_minion("slime", "combat", foo("Slimeball"), 1.8, [26,26,24,24,22,22,19,19,16,16,12], 11, 0.2)
    minions.add_minion("blaze", "combat", foo("Blaze Rod"), 1, [33,33,31,31,28.5,28.5,25,25,21,21,16.5], 11, 0.3)
    minions.add_minion("magma cube", "combat", foo("Magma Cream"), 1.8, [32,32,30,30,28,28,25,25,22,22,18], 11, 0.2)

    minions.add_minion("revenant", "slayer", [foo("Rotten Flesh"), foo("Diamond")], [3,0.2], [29,29,26,26,23,23,19,19,14.5,14.5,10,8], 12, [0.3,0.4], special_minion_case = "revenant")
    minions.add_minion("tarantula", "slayer", [foo("String"), foo("Spider Eye"), foo("Iron Ingot")], [3.16,1, 0.2], [29,29,26,26,23,23,19,19,14.5,14.5,10], 11, [0.2,0.3,0.3], special_minion_case = "tarantula")
    minions.add_minion("voidling", "slayer", [foo("Block of Quartz"), foo("Obsidian")], [0.4,2.42], [45,45,42,42,39,39,35,35,30,30,24], 11, [-1,-1], special_minion_case = "voidling")

    minions.add_minion("oak", "foraging", foo("Oak Wood"), 4, [48,48,45,45,42,42,38,38,33,33,27], 11, 0.1)
    minions.add_minion("birch", "foraging", foo("Birch Wood"), 4, [48,48,45,45,42,42,38,38,33,33,27], 11, 0.1)
    minions.add_minion("spruce", "foraging", foo("Spruce Wood"), 4, [48,48,45,45,42,42,38,38,33,33,27], 11, 0.1)
    minions.add_minion("dark oak", "foraging", foo("Dark Oak Wood"), 4, [48,48,45,45,42,42,38,38,33,33,27], 11, 0.1)
    minions.add_minion("acacia", "foraging", foo("Acacia Wood"), 4, [48,48,45,45,42,42,38,38,33,33,27], 11, 0.1)
    minions.add_minion("jungle", "foraging", foo("Jungle Wood"), 4, [48,48,45,45,42,42,38,38,33,33,27], 11, 0.1)

    #other
    minions.add_minion("flower", "foraging", "Allium, Azure Bluet, Blue Orchid, Dandelion, Poppy, Peony, Oxeye Daisy, Rose Bush, Lilac, Red Tulip, Sunflower, White Tulip, Pink Tulip, Orange Tulips flower randomly: The two-high flowers can be turned into their specific dyes and sold for two coins instead of 1", 0, [30,29,28,27,26,25,24,23,22,20,18], 11, -1, 1, special_type = "other", special_minion_case = "flower")
    minions.add_minion("snow", "mining", foo("Snowball"), 4, [13,13,12,12,11,11,9.5,9.5,8,8,6.5], 11, 0.1, special_type = "other")

    minions.add_minion("clay", "fishing", foo("Clay"), 4, [32,32,30,30,27.5,27.5,24,24,20,20,16], 11, 0.1, can_be_affected_by_crystal = False, special_type = "mining")
    minions.add_minion("fishing", "fishing", [foo("Raw Fish"), foo("Raw Salmon"), foo("Pufferfish"), foo("Clownfish"), foo("Prismarine Crystals"), foo("Prismarine Shard"), foo("Sponge")], [1, 0.5, 0.24, 0.08, 0.06, 0.06, 0.06], [78,75,72,72,68,68,62.5,62.5,53,53,35], 11, [0.5, 0.7, 1, 2, 0.25, 0.25, 0.5])

    return minions
