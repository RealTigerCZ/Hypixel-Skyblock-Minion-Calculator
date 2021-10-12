class Item():
    def __init__(self, data):
        self.__id = data["id"]
        self.__name = data["name"]
        self.__bazaar_price = data["bazaar_price"]
        self.__npc_price = data["npc_price"]

        if self.__bazaar_price == "/":
            self.__bazaar_price == None
        else:
            self.__bazaar_price = float(self.__bazaar_price)

        if self.__npc_price == "/":
            self.__npc_price == None
        else:
            self.__npc_price = float(self.__npc_price)
            if int(self.__npc_price) == self.__npc_price:
                self.__npc_price = int(self.__npc_price)

    def __repr__(self):
        toPrint = f"item: {self.__name}\n"
        toPrint += f"ID: {self.__id}\n"
        toPrint += f"bazaar price: {self.__bazaar_price}\n"
        toPrint += f"NPC price: {self.__npc_price}\n"

        return toPrint

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_bazaar_price(self):
        return self.__bazaar_price

    def get_npc_price(self):
        return self.__npc_price

class Items():
    def __init__(self):
        self.__item_list = []

    def add_item(self, item_data):
        self.__item_list.append(Item(item_data))

    def search_by_name(self, name):
        for item in self.__item_list:
            if item.get_name() == name:
                return item

    def search_by_id(self, id):
        for item in self.__item_list:
            if item.get_id() == id:
                return item

    def print_short_info(self):
        for item in self.__item_list:
            print(item.get_id(), item.get_name())

def create_items(data):
    items = Items()

    for item in data:
        items.add_item(data[item])

    for item in not_bazaar_items:
        items.add_item(item)

    return items

not_bazaar_items = [
{'material': 'INK_SACK', 'durability': 2, 'name': 'Cactus Green', 'npc_price': 1, 'id': 'INK_SACK:2', 'bazaar_price': "/"},
{'material': 'EGG', 'name': 'Egg', 'npc_price': 3, 'id': 'EGG', 'bazaar_price': "/"},
{'material': 'WOOL', 'name': 'White Wool', 'npc_price': 2, 'id': 'WOOL', 'bazaar_price': "/"},
{'material': 'IRON_ORE', 'name': 'Iron Ore', 'npc_price': 3, 'id': 'IRON_ORE', 'bazaar_price': "/"},
{'material': 'GOLD_ORE', 'name': 'Gold Ore', 'npc_price': 3, 'id': 'GOLD_ORE', 'bazaar_price': "/"},
{'material': 'POISONOUS_POTATO', 'name': 'Poisonous Potato', 'npc_price': 10, 'id': 'POISONOUS_POTATO', 'bazaar_price': "/"},
{'material': 'QUARTZ_BLOCK', 'name': 'Block of Quartz', 'npc_price': 16, 'id': 'QUARTZ_BLOCK', 'bazaar_price': "/"}]
