# Number of cells per width/height
GRID_WIDTH = 50
GRID_HEIGHT =50

# Cell size in px
CELL_SIZE = 10

# Canvas size in px
CANVAS_WIDTH = GRID_WIDTH * CELL_SIZE
CANVAS_HEIGHT = GRID_HEIGHT * CELL_SIZE

ODOUR_FACTOR = 0.002

COLOR_BLUE = '#0b4cb5'
COLOR_RED = '#e30e0e'
COLOR_ANT = '#f6ff3d'



def odour_to_hex(odour):
    grey = int(odour * 2.55)
    return '#{:02x}{:02x}{:02x}'.format(grey, grey, grey)
