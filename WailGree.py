# Roland's working file
from time import sleep
import sys
from tabulate import tabulate
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_inventory(inventory):
    headers = ['Name', 'Amount']
    print(tabulate(sorted([(k, v)
                           for k, v in inventory.items()]), headers=headers))


def write_message(speaker, message, delay=0.1, mark_delay=0.5):
    print(speaker+': ', end='')
    for letter in message:
        sys.stdout.write(letter)
        sys.stdout.flush()
        if letter == '!' or letter == '.' or letter == '?':
            sleep(mark_delay)
        else:
            sleep(delay)


def story_telling():
    write_message("Stranger", "Hey! You! You're finally awake.")
    input('\nPress ENTER to continue...')
    write_message('You', "W-what? Who are you? Where am I?")
    input('\nPress ENTER to continue...')
    write_message(
        'Stranger', "I am... I was a fellow student like you... We are in the basement of Codecool.")
    input('\nPress ENTER to continue...')
    write_message('You', 'In where?!?! How did I get here? Last time I remember... It was 3rd day of TW week. I was about to leave.\nThen I got hit in the back of my head...')
    input('\nPress ENTER to continue...')
    write_message(
        'Student', 'Everyone who doesn\'t study ends up here... This is why there are news about students who suddenly disappear.')
    input('\nPress ENTER to continue...')
    write_message('You', 'No! That can\'t be!! I HAVE TO GET OUT OF HERE!!!!')
    input('\nPress ENTER to continue...')
    write_message('Student', 'There is a way... The basement holds creatures, unknown to us. Nobody who passed the first room ever returned.\n You have to defeat what\'s to come, to leave the basement.')
    input('\nPress ENTER to continue...')
    write_message('You', 'I have to try!')
    input('\nPress ENTER to continue...')
    write_message(
        'Student', 'Then I\'ll wish you the best of luck... But before you go, I have a few questions...')
    input('\nPress ENTER to continue...')


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
    sleep(1)
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
    combat_display(dealer, target)
    sleep(1)
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
        print(f"{player['name']} won the fight!")
        sleep(1)
        input("Press ENTER to continue...")
        clear()
    elif player['HP'] == 0:
        return player
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
