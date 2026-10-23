import math
import shutil
import time

# ---------------- Settings ---------------- #

FPS = 30

DRAW_FRAMES = 100
HOLD_FRAMES = 40

SCALE = 1.5
CHAR = "*"

THICKNESS = 1
POINTS = 1200

# ------------------------------------------- #


def clear_terminal():
    print("\033[2J", end="", flush=True)


def cursor_home():
    print("\033[H", end="", flush=True)


def terminal_size():
    size = shutil.get_terminal_size(fallback=(80, 24))
    return size.lines, size.columns


def generate_heart(progress, rows, cols):
    cx = cols // 2
    cy = rows // 2

    points = set()

    total = max(2, int(progress * POINTS))

    for i in range(total):
        # Start from bottom tip and draw around
        t = math.pi + (2 * math.pi * i / POINTS)

        x = 16 * math.sin(t) ** 3

        y = (
            13 * math.cos(t)
            - 5 * math.cos(2 * t)
            - 2 * math.cos(3 * t)
            - math.cos(4 * t)
        )

        tx = round(x * SCALE) + cx
        ty = round(-y * SCALE) + cy

        for dy in range(-THICKNESS, THICKNESS + 1):
            for dx in range(-THICKNESS, THICKNESS + 1):
                nx = tx + dx
                ny = ty + dy

                if 0 <= nx < cols and 0 <= ny < rows:
                    points.add((ny, nx))

    return points


def render(points, rows, cols):

    screen = [[" "] * cols for _ in range(rows)]

    for y, x in points:
        screen[y][x] = CHAR

    print("\n".join("".join(row) for row in screen), end="")


def animate():

    clear_terminal()

    frame = 0

    try:
        while True:
            rows, cols = terminal_size()

            cursor_home()

            progress = min(frame / DRAW_FRAMES, 1.0)

            heart = generate_heart(progress, rows, cols)

            render(heart, rows, cols)

            frame += 1

            if frame > DRAW_FRAMES + HOLD_FRAMES:
                frame = 0

            time.sleep(1 / FPS)

    except KeyboardInterrupt:
        clear_terminal()
        print("Animation stopped.")


if __name__ == "__main__":
    animate()
