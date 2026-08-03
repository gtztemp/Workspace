import subprocess
import time

SOUND = "/usr/share/sounds/freedesktop/stereo/bell.oga"

while True:
    time.sleep(3600)

    for _ in range(3):
        try:
            _ = subprocess.run(["paplay", SOUND], check=True)
        except FileNotFoundError:
            print("Audio player 'paplay' not found.")
            break
        except subprocess.CalledProcessError:
            print("Could not play sound.")
            break

        time.sleep(0.5)

    print("⏰ Reminder ! ! !")
