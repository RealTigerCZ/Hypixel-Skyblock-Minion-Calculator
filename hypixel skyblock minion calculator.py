import colorama
colorama.init(convert=True)
colorama.init(autoreset=True)
BLUE = colorama.Style.BRIGHT + colorama.Fore.BLUE
GREEN = colorama.Style.BRIGHT + colorama.Fore.GREEN
RED = colorama.Style.BRIGHT + colorama.Fore.RED
WHITE = colorama.Style.BRIGHT + colorama.Fore.WHITE
YELLOW = colorama.Style.BRIGHT +  colorama.Fore.YELLOW 

def main():
    print("Welcome to Hypixel Skyblock Minion Calculator.\n")
    print("Idea from ThirtyVirus: https://www.youtube.com/watch?v=MoE-5p5IYtY\n")
    print("This software is free to use, but it's not as great as software which was developed by ThirtyVirus\n")
    input("Press ENTER to continue: ")

    vycisti_obrazovku()

    calculate()

    input("Press ENTER to exit: ")

def vycisti_obrazovku(): #it cleans the window
  import sys as _sys
  import subprocess as _subprocess
  if _sys.platform.startswith("win"):
    _subprocess.call(["cmd.exe", "/C", "cls"])
  else:
    _subprocess.call(["clear"])

def calculate():
    time_between_actions = zadej(GREEN + "time between actions: ","float")
    items_per_actions = zadej(GREEN + "items per action: ","float")
    unit_price = zadej(GREEN + "unit price: ","float")
    fuel = zadej(GREEN + "fuel or other bonuses " + WHITE + " in % (if you don't have fuel or other bonuses like pets, leave it blank or type 0): ","fuel")
    upgrade1,name_upgrade1 = has_upgrade("first")
    upgrade2,name_upgrade2 = has_upgrade("second")
    pocet_minionu = zadej("how many " +  GREEN + "minions" + WHITE + " do you have: ","int")

    bonuses = 0
    
    if fuel:
        bonuses += fuel
    if upgrade1 and upgrade1 != "dia_spread":
        bonuses += upgrade1
    if upgrade2 and upgrade2 != "dia_spread":
        bonuses += upgrade2
    if bonuses:
        bonuses /= 100 #because is was in %
        time_between_actions = time_between_actions*(1-(bonuses/(1+bonuses))) #bonus speed

    earnings_from_dia_spread = 0
    if upgrade1 == "dia_spread" or upgrade2 == "dia_spread":
        earnings_from_dia_spread = 5760/time_between_actions
        if upgrade1 == upgrade2:
            earnings_from_dia_spread *= 2
    
    earnings = 3600/time_between_actions*items_per_actions*unit_price + earnings_from_dia_spread #earning per hour
    earnings = round(earnings)

    vycisti_obrazovku()
    print("Your minion setup:")
    print(GREEN + "Minion Action Interval: " + BLUE + str(round(time_between_actions,2)))
    print(GREEN + "Items Per Action: " + BLUE + str(items_per_actions))
    print(GREEN + "Fuel And Other Bonuses: " + BLUE + f"{fuel}",end=" ") 
    if fuel: print(BLUE + "%") 
    else: print()
    print(GREEN + "First Upgrade Slot: " + BLUE + f"{name_upgrade1}")
    print(GREEN + "First Upgrade Slot: " + BLUE + f"{name_upgrade2}")
    print(GREEN + "Minions Quantity: " + BLUE + str(pocet_minionu))
    print("-------------------------------------------------------------------------")
    print(BLUE  + "For 1 minion:")
    print(WHITE + "1 hour: ",YELLOW+ str(earnings) + " coins")
    print(WHITE + "1 day:  ",YELLOW+ str(earnings*24) + " coins")
    print(WHITE + "1 week: ",YELLOW+ str(earnings*24*7) + " coins")
    if pocet_minionu > 1:
        earnings *= pocet_minionu
        print("-------------------------------------------------------------------------")
        print(BLUE  + f"For {pocet_minionu} minions:")
        print(WHITE + "1 hour: ",YELLOW+ str(earnings) + " coins")
        print(WHITE + "1 day:  ",YELLOW+ str(earnings*24) + " coins")
        print(WHITE + "1 week: ",YELLOW+ str(earnings*24*7) + " coins")
    
    


def zadej(mess,typ = "str"):
    value = input(WHITE + "Please enter " + mess + BLUE)
    if typ == "int":
        try:
            value = int(value)
        except ValueError:
            print(RED + "Incorrect integer, please try again!")
            vycisti_obrazovku()
            value = zadej(mess,typ)
        if value <= 0:
            print(RED + "Incorrect number, please try again!")
            value = zadej(mess,typ)

    elif typ == "float":
        try:
            value = float(value)
        except ValueError:
            vycisti_obrazovku()
            print(RED + "Incorrect number, please try again!")
            value = zadej(mess,typ)
        if value <= 0:
            vycisti_obrazovku()
            print(RED + "This can not be 0 or lower than 0, please try again!")
            value = zadej(mess,typ)
    elif typ == "fuel":
        if value == "" or value == "0" or value.lower() == "none" :
            return None
        else:
            try:
                value = float(value)
            except ValueError:
                print(RED + "I can't understand :(\n" + WHITE + """Please write a value in % (if it is a catalyst, that has 3x bonus write "300") or if you do not have fuel or other bonuses, do not write anything or write "0" """)
                value = zadej(mess,typ)
            if value < 0:
                vycisti_obrazovku()
                print(RED + "This can not be lower than zero, please try it again!")
                value = zadej(mess,typ)

    return value

def has_upgrade(order): #returns what upgrade have minion in upgrade slot
    print("\n" +YELLOW + f"What do you have in {order} upgrade slot?")
    print("Type:")
    print(RED + "1",WHITE + " - ", GREEN + "Flycatcher")
    print(RED + "2",WHITE + " - ", GREEN + "Minion Expander")
    print(RED + "3",WHITE + " - ", GREEN + "Diamond Spreading")
    print(RED + "0",WHITE + " - ", GREEN + "none of the above")
    value = input()
    try:
        value = int(value)
    except ValueError:
        vycisti_obrazovku()
        print(RED + "Invalid number, please try it again.")
        value = has_upgrade(order)
    if value == 0:
        return None,None
    elif value == 1:
        return 20,"Flycatcher"
    elif value == 2:
        return 5.125,"Minion Expander"
    elif value == 3:
        return "dia_spread","Diamnod Spreading"
    else:
        vycisti_obrazovku()
        print(RED + "Incorrect number, please enter selection number.")
        value = has_upgrade(order)
        return value 

if __name__ == "__main__":
    main()
