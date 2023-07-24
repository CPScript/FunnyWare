import time
import random
import os
import pyglet
import psutil

# mp3 files (add more if you like)
MP3_FILES = ["hiss.mp3"]

# Function to play the MP3 file
def play_music(mp3_file):
    player = pyglet.media.Player()
    source = pyglet.media.load(mp3_file)
    player.queue(source)
    player.play()
    while player.playing:
        time.sleep(1)

def main():
    random.seed()

    while True:
        # Check for minecraft (bedrock edition)
        for process in psutil.process_iter(['pid', 'name']):
            if process.info['name'] == 'Minecraft':
                # Generate a random time between 0 and 5 minutes (300 seconds)
                time.sleep(300)
                random_time = random.randint(0, 300)
                time.sleep(random_time)

                # Select mp3
                mp3_file = (MP3_FILES) # mp3_file = random.choice(MP3_FILES)

                # Play the selected MP3 file
                play_music(mp3_file)

        # Adjust the sleep time as needed to avoid excessive CPU usage
        time.sleep(6)

if __name__ == "__main__":
    main()
