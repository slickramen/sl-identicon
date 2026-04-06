# Imports
from PIL import Image, ImageDraw
import hashlib
import sys
from math import floor

# Consts
GRID_SIZE = 24
GRID_W = 5
GRID_H = 5
PADDING = 12

BG_COL = 250

input_str = "sample"

if len(sys.argv) > 1:
    input_str = sys.argv[1]

input_str = input_str.lower()

# Hash digest
digest = hashlib.md5(input_str.encode()).digest()

# Colour output
LEVELS = [128, 164, 220]
fill_colour = (255, 255, 255)

while True:
    r = LEVELS[digest[0] % len(LEVELS)]
    g = LEVELS[digest[1] % len(LEVELS)]
    b = LEVELS[digest[2] % len(LEVELS)]
    
    if r != g or g != b:
        fill_colour = (r, g, b)
        break
    
    digest = hashlib.md5(digest).digest()

# Lerp bg col slightly
def lerp(a, b, c):
    return a * (1-c) + b * (c)

bg_lerp_amt = 0.1
bg_col = (
    floor(lerp(BG_COL, fill_colour[0], bg_lerp_amt)), 
    floor(lerp(BG_COL, fill_colour[1], bg_lerp_amt)), 
    floor(lerp(BG_COL, fill_colour[2], bg_lerp_amt))
)

# Pixel grid
bits = []
for byte in digest:
    bits.extend([(byte >> i) & 1 for i in range(8)])

half = (GRID_W + 1) // 2
grid_mat = []
bit_index = 0

for row in range(GRID_H):
    half_row = [bits[bit_index % len(bits) + i % len(bits)] for i in range(half)]
    bit_index += half

    full_row = half_row + half_row[:(GRID_W // 2)][::-1]
    grid_mat += full_row

# Image output
img = Image.new("RGB", (PADDING * 2 + GRID_W * GRID_SIZE, PADDING * 2 + GRID_H * GRID_SIZE), color=bg_col)
draw = ImageDraw.Draw(img)

col = 0
row = 0
for i, cell in enumerate(grid_mat):
    cell_x = PADDING + GRID_SIZE * col
    cell_y = PADDING + GRID_SIZE * row
    if grid_mat[i]:
        draw.rectangle([cell_x, cell_y, cell_x + GRID_SIZE, cell_y + GRID_SIZE], fill=fill_colour)

    # Wrap    
    col += 1

    if col == GRID_W:
        row += 1
        col = 0

    if row == GRID_H:
        break

# Save and show
img.save(f"output/{input_str}.png")
img.show()
