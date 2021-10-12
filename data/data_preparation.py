import os
file_path =  os.path.dirname(os.path.realpath(__file__))

#API from:
link = "https://sky.shiiyu.moe/api/v2/bazaar"
npc_price_data_path = file_path + "/NPC prices.txt"
missing_item_path = file_path + "/missing_npc_price_items_added_to_bazaar.txt"



def prepare_data(debug_comment = False):
    import requests
    response = requests.get(link)
    raw_bazaar_data = response.json()
    raw_npc_price_data = prepare_npc_price_data()

    missing = open(missing_item_path, "w")
    missing_items_count = 0

    data = {}
    for item in raw_bazaar_data:
        name = raw_bazaar_data[item]["name"]
        try:
            data[item] = {"id": item, "name": name, "npc_price": raw_npc_price_data[name], "bazaar_price": raw_bazaar_data[item]["price"]}
        except KeyError as e:
            missing_items_count += 1
            missing.write(str(e)[1:][:-1] + "\n")
            if debug_comment:
                print("Warning: Missing npc price for: " + str(e))

    missing.close()

    if missing_items_count:
        print(f"Warning: There is/are {missing_items_count} missing npc price(s), writed to: {missing_item_path}\n")


    return data

def prepare_npc_price_data():
    data = {}
    missing_price_count = 0
    file = open(npc_price_data_path, "r")
    for line in file.readlines():
        if not line.startswith("#") and len(line) != 1: #commenting whole lines and ignoring empty lines
            line = line.split()
            if len(line) == 2:
                key = line[0]
            else:
                key = ""
                for i in line[:-1]:
                    key += i + " "
                key = key[:-1]
            data[key] = line[-1]

            if line[-1] == "-1":
                missing_price_count += 1

    if missing_price_count:
        print(f"Warning: There is/are {missing_price_count} missing npc price(s)\n")

    npc_price_check(data)
    return data

def npc_price_check(data):
    for i in data.values():
        try:
            i = float(i)
        except ValueError:
            assert i == "/", f"invalid price: {i}"


if __name__ == "__main__":
    #testing
    print(prepare_npc_price_data())
    #print(prepare_data(False))
