import ctypes
import random
import time

# List of Windows system sounds
system_sounds = [
    'SystemAsterisk',
    'SystemExclamation',
    'SystemExit',
    'SystemHand',
    'SystemQuestion',
    'SystemStart',
    'SystemDefault',
]

def play_random_system_sound():
    sound_alias = random.choice(system_sounds)
    ctypes.windll.user32.MessageBeep(getattr(ctypes.windll.user32, sound_alias))

# Main loop
while True:
    play_random_system_sound()
    time.sleep(300)  # Play a sound every 5 minutes (300 seconds)
