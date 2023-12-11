import os


def get_path_from_root(path_to_file):
    root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    return f"{root_path}/{path_to_file}"


assets_library = {
    'backgrounds': {
        'start': 'assets/backgrounds/start.jpg',
        'game_over': 'assets/backgrounds/game_over.png',
        'main_background': 'assets/backgrounds/background.jpg',
        'win': 'assets/backgrounds/fireworks_win.jpg',
        'level_up': 'assets/backgrounds/level_up.png',
        'registration_page': 'assets/backgrounds/registration.png',
        'credits': 'assets/backgrounds/credits.jpg'
    },
    'fonts': {
        'kiddy_play': 'assets/fonts/Kiddy Play.ttf',
        'fuku_catch': 'assets/fonts/FukuCatch.otf'
    },
    'sounds': {
        'soundtrack': 'assets/sounds/soundtrack.mp3',
        'bonus': 'assets/sounds/bonus_points_2.wav',
        'intro': 'assets/sounds/intro.wav',
        'level': 'assets/sounds/level_complete.wav',
        'damage': 'assets/sounds/small_damage.wav',
        'win': 'assets/sounds/win.mp3',
        'game_over': 'assets/sounds/game_over.wav'
    },
    'sprites': {
        'bug': {
            'bug1': 'assets/sprites/bug1.png',
            'bug2': 'assets/sprites/bug2.png',
            'bug3': 'assets/sprites/bug3.png',
            'bug4': 'assets/sprites/bug4.png',
            'bug5': 'assets/sprites/bug5.png',
            'bug6': 'assets/sprites/bug6.png',
            'bug7': 'assets/sprites/bug7.png',
            'bug8': 'assets/sprites/bug8.png',
        },
        'duck': {
            'duck1': 'assets/sprites/duck1.png',
            'duck2': 'assets/sprites/duck2.png',
            'duck3': 'assets/sprites/duck3.png',
            'duck4': 'assets/sprites/duck4.png',
            'duck5': 'assets/sprites/duck5.png',
            'duck6': 'assets/sprites/duck6.png',
        },
        'error': 'assets/sprites/error.png',
        'heart': {
            'heart1': 'assets/sprites/heart_full.png',
            'heart2': 'assets/sprites/heart_almost_full.png',
            'heart3': 'assets/sprites/heart_medium2.png',
            'heart4': 'assets/sprites/heart_medium1.png',
            'heart5': 'assets/sprites/heart_low.png',
            'heart6': 'assets/sprites/heart_empty.png',
        },
        'level': {
            'level1': 'assets/sprites/level1.png',
            'level2': 'assets/sprites/level2.png',
            'level3': 'assets/sprites/level3.png',
        },
        'player': {
            'player_left': {
                'player_left1': 'assets/sprites/player_idle_left.png',
                'player_left2': 'assets/sprites/player9.png',
                'player_left3': 'assets/sprites/player10.png',
                'player_left4': 'assets/sprites/player11.png',
                'player_left5': 'assets/sprites/player12.png',
                'player_left6': 'assets/sprites/player13.png',
                'player_left7': 'assets/sprites/player14.png',
                'player_left8': 'assets/sprites/player15.png',
                'player_left9': 'assets/sprites/player16.png',
            },
            'player_right': {
                'player_right1': 'assets/sprites/player_idle.png',
                'player_right2': 'assets/sprites/player1.png',
                'player_right3': 'assets/sprites/player2.png',
                'player_right4': 'assets/sprites/player3.png',
                'player_right5': 'assets/sprites/player4.png',
                'player_right6': 'assets/sprites/player5.png',
                'player_right7': 'assets/sprites/player6.png',
                'player_right8': 'assets/sprites/player7.png',
                'player_right9': 'assets/sprites/player8.png',
            }
        },
        'python': {
            'python1': 'assets/sprites/python1.png',
            'python2': 'assets/sprites/python2.png',
            'python3': 'assets/sprites/python3.png',
        },
        'tick': 'assets/sprites/tick.png',
        'warning': 'assets/sprites/warning.png'
    }
}
