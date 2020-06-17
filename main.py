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


def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    WailGree.write_message('Student', 'Please tell me your name:')
    name = input()
    WailGree.write_message('Student', """Please choose a race (by number)
    1 Dwarf (ProgBasics)
    2 Human (Web)
    3 Elf   (OOP)\n""")
    race = input()
    if race == '1':
        race = 'Dwarf'
    elif race == '2':
        race = 'Human'
    elif race == '3':
        race = 'Elf'
    WailGree.write_message('Student', 'Please choose gender(m/f):')
    gender = input()
    player = {'name': name, 'race': race, 'gender': gender.upper()}
    if race == 'Dwarf':
        if gender.upper() == 'M' or gender.upper() == 'F':
            player.update({'icon': '🙇'})
    elif race == 'Human':
        if gender.upper() == 'M' or gender.upper() == 'F':
            player.update({'icon': '👨'})
    elif race == 'Elf':
        if gender.upper() == 'M' or gender.upper() == 'F':
            player.update({'icon': '🧝'})
    return player


def game(map_number, player):
    BOARD_WIDTH, BOARD_HEIGHT, PLAYER_START_X, PLAYER_START_Y = mateszathmari.map_details(
        map_number)
    board = mateszathmari.generate_stuffs(
        engine.create_board(BOARD_WIDTH, BOARD_HEIGHT), map_number)
    util.clear_screen()
    is_running = True
    while is_running:   # loop in loops in loops in loops
        engine.put_player_on_board(
            board, player, PLAYER_START_X, PLAYER_START_Y)
        ui.display_board(board)

        key = util.key_pressed()
        if key == 'q':
            is_running = False
        else:
            board2, PLAYER_START_X2, PLAYER_START_Y2, map_number = mateszathmari.move_player(
                key, board, player, map_number)
            valid, board = ai.mob_move(board, '💀')
            if board2 != 0:
                board = board2
                PLAYER_START_X = PLAYER_START_X2
                PLAYER_START_Y = PLAYER_START_Y2
        util.clear_screen()


def main():
    # choice = input("Do you want to watch the story? (y/n)").upper()
    # if choice == 'Y':
    #     WailGree.story_telling()
    # player = create_player()
    # if choice == 'Y':
    #     WailGree.write_message(player['name'], '')
    player = {'gender': 'M', 'icon': '🙇', 'name': 'sdfsdf', 'race': 'Dwarf'} # for test only
    map_number = 1
    game(map_number, player['icon'])


if __name__ == '__main__':
    main()
