# game/level_manager.py
import json
import os
from game.brick import Brick

def load_level(level):
    file_path = os.path.join("levels", f"level{level}.json")
    with open(file_path) as f:
        data = json.load(f)

    rows = data["rows"]
    cols = data["cols"]
    speed = data["ball_speed"]
    brick_width = 800 // cols
    brick_height = 30
    bricks = []

    for row in range(rows):
        for col in range(cols):
            x = col * brick_width + 1
            y = row * brick_height + 1
            bricks.append(Brick(x, y, brick_width - 2, brick_height - 2))

    return bricks, speed
