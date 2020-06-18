# Roland's working file
from time import sleep
import sys
from tabulate import tabulate
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_inventory():
    headers = ['Name', 'Amount']
    print(tabulate(sorted([(k, v)
                           for k, v in inventory.items()]), headers=headers))


def write_message(speaker, message):
    print(speaker+': ', end='')
    for letter in message:
        sys.stdout.write(letter)
        sys.stdout.flush()
        if letter == '!' or letter == '.' or letter == '?':
            sleep(0.5)
        else:
            sleep(0.1)


def story_telling():
    write_message("Stranger", "Hey! You! You're finally awake.")
    input('Press ENTER to continue...')
    write_message('You', "W-what? Who are you? Where am I?")
    input('Press ENTER to continue...')
    write_message(
        'Stranger', "I am... I was a fellow student like you... We are in the basement of Codecool.")
    input('Press ENTER to continue...')
    write_message('You', 'In where?!?! How did I get here? Last time I remember... It was 3rd day of TW week. I was about to leave.\nThen I got hit in the back of my head...')
    input('Press ENTER to continue...')
    write_message(
        'Student', 'Everyone who doesn\'t study ends up here... This is why there are news about students who suddenly disappear.')
    write_message('You', 'No! That can\'t be!! I HAVE TO GET OUT OF HERE!!!!')
    input('Press ENTER to continue...')
    write_message('Student', 'There is a way... The basement holds creatures, unknown to us. Nobody who passed the first room ever returned.\n You have to defeat what\'s to come, to leave the basement.')
    input('Press ENTER to continue...')
    write_message('You', 'I have to try!')
    input('Press ENTER to continue...')
    write_message(
        'Student', 'Then I\'ll wish you the best of luck... But before you go, I have a few questions...')


def combat_display(creature1, creature2):
    print("""               {}
           HP:  {}
        damage: {}
        armor:  {}
        """.format(creature1['name'], creature1['HP'], creature1['damage'], creature1['armor']))
    print("""               {}
           HP:  {}
        damage: {}
        armor:  {}
        """.format(creature2['name'], creature2['HP'], creature2['damage'], creature2['armor']))


def combat_event(dealer, target):
    clear()
    combat_display(dealer, target)
    sleep(3)
    if target['armor'] > 0:
        print(
            f"{dealer['name']} dealt {dealer['damage']} damage to {target['name']}\'s armor.")
        if target['armor'] - dealer['damage'] >= 0:
            target['armor'] -= dealer['damage']
        else:
            target['armor'] = 0
    else:
        print(
            f"{dealer['name']} dealt {dealer['damage']} damage to {target['name']}\'s health.")
        if target['armor'] - dealer['damage'] >= 0:
            target['HP'] -= dealer['damage']
        else:
            target['HP'] = 0
    sleep(3)
    clear()
    combat_display(player, mob)
    sleep(3)
    return dealer, target


def in_combat(player, mob):
    is_running = True
    while is_running:
        player, mob = combat_event(player, mob)
        if player['HP'] > 0 and mob['HP'] > 0:
            mob, player = combat_event(mob, player)
        else:
            is_running = False
    if player['HP'] > 0 and mob['HP'] <= 0:
        print(f"{player['name']}won the fight!")
        sleep(1)
        input("Press ENTER to continue...")
        clear()
    return player


weapons = {
    'Beginner\'s Wrath': {'damage': 1},
    'Adapt\'s Bravery': {'damage': 2},
    'Expert\'s Edge': {'damage': 5},
    'The CEO\'s Ban Hammer': {'damage': 10}
}
armors = {
    'Python shirt': {'armor': 1},
    'Javascript bib shorts': {'armor': 2},
    'Java jacket': {'armor': 5},
    'Mentorbot costume': {'armor': 10}
}
food = {
    'Rushed breakfast': {'HP restore': 10},
    'Avarage lunch': {"HP restore": 15},
    'McDonald\'s Happy Meal menu': {'HP restore': 35},
    'Grandma\'s family sized dinner': {'HP restore': 75}
}

inventory = [['Python shirt', 1, 1], ["Rushed breakfast", 1, 1]]
inventory = {'Python shirt': 1, 'Grandma\'s family sized dinner': 2}
headers = ["Item", "Amount"]
# print(tabulate([k + str(v) for k, v in inventory.items()], headers=headers))

# flip the code and name and sort
# data = sorted([(k, v) for k, v in inventory.items()])
player = {'name': 'WailGree', 'HP': 10, 'damage': 10, 'armor': 5}
mob = {'name': 'goat', 'HP': 5, 'damage': 1, 'armor': 5}
in_combat(player, mob)
