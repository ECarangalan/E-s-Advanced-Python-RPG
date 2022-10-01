import sys, time

my_hero = {
    "name" : 'Pogi',
    "level" : 1,
    "health" : 100,
    "equipment" : {'Invisible infinity pouch', 'Collar of the Gods', "Protector's Orb",},
    "attacks" : (("sonic bark", 55), ("death stare", 30), 
                ("pogi push", 25), ("love scratch", 50), ("pogi charge", 45), ('defend', 10)),
    "coins" : {
        "copper" : 50,
        "silver" : 0,
        "gold" : 0,
    }
}

enemy_one ={
    "name" : 'Fevmes, God of Fate',
    "level" : 5,
    "health" : 100,
    "equipment" : {'Sling', 'Warped Seal',},
    "attacks" : (('forsee', 20), ('lash', 25), ('firesling', 30)),
    "coins" : {
        "copper" : 5,
        "silver" : 15,
        "gold" : 2
    }
}

enemy_two = {
    "name" : 'Inagen, God of Life & Death',
    "level" : 5,
    "health" : 100, 
    "equipment" : { 'Talisman of the Daywalker', 'Lifebinder', 'Ashes',},
    "attacks" : (('mirror', 25), ('soultap', 50), ('decay', 40)),
    "coins" : {
        "copper" : 5,
        "silver" : 15,
        "gold" : 2
    }
}

enemy_three = {
    "name" : 'Phaztin, God of The Afterlife',
    "level" : 5,
    "health" : 100, 
    "equipment" : {'Lantern of Whispers', 'Soulkeeper', 
                    "Instrument of Hell's Games", },
    "attacks" : (('dreamkiss', 20), ('nightkiss', 50), ('overwhelm', 25)),
    "coins" : {
        "copper" : 5,
        "silver" : 15,
        "gold" : 2
    }
}

def slow_print(string_to_print):
    for letter in string_to_print:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)
    print(" ")



def Pogi_Tales_RPG():
    print("-------------------")
    slow_print("Pogi wakes up and the room is dark...")

Pogi_Tales_RPG()






























