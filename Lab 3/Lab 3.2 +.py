#RPG YO! HYPE
import random
player = {"name": "Arthas Menethil",
          "health": 100,
          "mana": 100,
          "experience": 0,
          "alive": True,
          "inventory": []}

player["inventory"].append("Frostmourne")

def print_player(plyr):
    print("Player stats:")
    for key in plyr:
        print("Your " + key + " is " + str(plyr[key]))

print_player(player)

def compute_experience(damage):
    return random.randrange(0, damage*2)

def take_damage(player, damage):
    player["health"] -= damage
    player["experience"] += compute_experience(damage)
    if player["health"] <= 0:
        player["alive"] = False
    return player

while player["alive"] == True:
    take_damage(player, random.randrange(1,10))
    print_player(player)