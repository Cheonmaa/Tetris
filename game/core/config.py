# ========================================================================================
#                                   GAME CONFIGURATION
# ========================================================================================



# ----------------------------------------------------------------------------------------
#                                   Global Variables
# ----------------------------------------------------------------------------------------

#Overall Game Settings
game_title = "Game Title"
game_version = "0.1"
game_fps = 60

#Window dimensions
window_width = 800
window_height = 600
block_size = 30

# Grid settings
grid_rows = 20
grid_cols = 10

#Gameplay zone
game_zone_width = block_size * grid_rows
game_zone_height = block_size * grid_cols

#Speed settings
fall_speed = 1
fall_speeds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Coordinates left top corner of the game zone
game_zone_x = (window_width - game_zone_width) // 2
game_zone_y = (window_height - game_zone_height) // 2

#Colors
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
COLORS = [RED, GREEN, BLUE]

#Tetris Shapes
SHAPES = [
    [
        ['.....',
         '.....',
         '.....',
         'OOOO.',
         '.....'],
        ['.....',
         '..O..',
         '..O..',
         '..O..',
         '..O..']
    ],
    [
        ['.....',
         '.....',
         '..O..',
         '.OOO.',
         '.....'],
        ['.....',
         '..O..',
         '.OO..',
         '..O..',
         '.....'],
        ['.....',
         '.....',
         '.OOO.',
         '..O..',
         '.....'],
        ['.....',
         '..O..',
         '..OO.',
         '..O..',
         '.....']
    ],
    [
        [
         '.....',
         '.....',
         '..OO.',
         '.OO..',
         '.....'],
        ['.....',
         '.....',
         '.OO..',
         '..OO.',
         '.....'],
        ['.....',
         '.O...',
         '.OO..',
         '..O..',
         '.....'],
        ['.....',
         '..O..',
         '.OO..',
         '.O...',
         '.....']
    ],
    [
        ['.....',
         '..O..',
         '..O.',
         '..OO.',
         '.....'],
        ['.....',
         '...O.',
         '.OOO.',
         '.....',
         '.....'],
        ['.....',
         '.OO..',
         '..O..',
         '..O..',
         '.....'],
        ['.....',
         '.....',
         '.OOO.',
         '.O...',
         '.....']
    ],
]

#Game Score
score = 0

#Game Condition
gameover = False

