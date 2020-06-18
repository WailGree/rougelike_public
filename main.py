import util
import engine
import ui
import WailGree
import mateszathmari
import ai

# Characters: 🗝️ 💀 🤕 🐲 💊 🗡️ 🔪 🛡️
# Races: Human, elf, dwarf
#        👨 👩 🧝‍♂️ 🧝‍♀️ 👨 👩
PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20

backpack = {}
visited_rooms = 0


def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    WailGree.write_message('Student', 'Please tell me your name:', 0.01, 0.01)
    name = input()
    WailGree.write_message('Student', """Please choose a race (by number)
    1 Dwarf (ProgBasics) [10 HP, 5 damage, 3 armor]
    2 Human (Web)        [15 HP, 3 damage, 5 armor]
    3 Elf   (OOP)        [20 HP, 1 damage, 7 armor]\n""", 0.01, 0.01)
    race = input()
    if race == '1':
        race = 'Dwarf'
    elif race == '2':
        race = 'Human'
    elif race == '3':
        race = 'Elf'
    WailGree.write_message('Student', 'Please choose gender(m/f):', 0.01, 0.01)
    gender = input()
    player = {'name': name, 'race': race}
    if race == 'Dwarf':
        if gender.upper() == 'M' or gender.upper() == 'F':
            player.update({'HP': 10, 'damage': 5, 'armor': 3, 'icon': '🙇'})
    elif race == 'Human':
        if gender.upper() == 'M' or gender.upper() == 'F':
            player.update({'HP': 15, 'damage': 3, 'armor': 5, 'icon': '👨'})
    elif race == 'Elf':
        if gender.upper() == 'M' or gender.upper() == 'F':
            player.update({'HP': 20, 'damage': 1, 'armor': 7, 'icon': '🧝'})
    return player


def generate_mob(map_number):
    mob = {}
    if map_number == 1:
        mob.update({'name': 'skeleton', 'HP': 10,
                    'damage': 5, 'armor': 3, 'icon': '💀'})
    elif map_number == 2:
        mob.update({'name': 'alien', 'HP': 15,
                    'damage': 3, 'armor': 5, 'icon': '👽'})
    elif map_number == 3:
        mob.update({'name': 'devil', 'HP': 10,
                    'damage': 15, 'armor': 0, 'icon': '👺'})
    elif map_number == 4:
        mob.update({'name': 'mentor guardian', 'HP': 20,
                    'damage': 15, 'armor': 0, 'icon': '👿'})
    return mob


def game(map_number, player):
    BOARD_WIDTH, BOARD_HEIGHT, PLAYER_START_X, PLAYER_START_Y = mateszathmari.map_details(
        map_number)
    mob = generate_mob(map_number)
    board = mateszathmari.generate_stuffs(
        engine.create_board(BOARD_WIDTH, BOARD_HEIGHT), map_number, mob)
    util.clear_screen()
    backpack = {}
    is_running = True
    show_inventory = False
    while is_running:   # loop in loops in loops in loops
        engine.put_player_on_board(
            board, player, PLAYER_START_X, PLAYER_START_Y)
        ui.display_board(board)
        if show_inventory:
            WailGree.display_inventory(player)

        key = util.key_pressed()
        if key == 'q':
            is_running = False
        else:
            if key == 'w' or key == 'a' or key == 's' or key == 'd':
                mob = generate_mob(map_number)
                board2, PLAYER_START_X2, PLAYER_START_Y2, map_number, backpack = mateszathmari.move_player(
                    key, board, player, map_number, mob)
                valid, board = ai.mob_move(board, mob['icon'], player, mob)
                if board2 != 0:
                    board = board2
                    PLAYER_START_X = PLAYER_START_X2
                    PLAYER_START_Y = PLAYER_START_Y2
            elif key == 'i':
                if show_inventory:
                    show_inventory = False
                else:
                    show_inventory = True
        util.clear_screen()


def main():
    choice = input("Do you want to watch the story? (y/n)").upper()
    if choice == 'Y':
        WailGree.story_telling()
    player = create_player()
    if choice == 'Y':
        WailGree.write_message(player['name'], '')
    # player = {'gender': 'M', 'icon': '🙇',
    #           'name': 'sdfsdf', 'race': 'Dwarf', 'HP': 20, 'damage': 1, 'armor': 7, 'icon': '🧝'}  # for test only
    map_number = 1
    game(map_number, player)


if __name__ == '__main__':
    main()
