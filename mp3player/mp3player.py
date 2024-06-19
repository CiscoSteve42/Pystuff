#!/usr/bin/env python3

import os, pygame


def init_mixer():
    pygame.mixer.init()


def play_music(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()


def list_songs(music_dir):
    songs = os.listdir(music_dir)
    return [os.path.join(music_dir, song) for song in songs if song.endswith('.mp3')]


def main():
    init_mixer()
    
    music_dir = '/home/dad/Music'  
    songs = list_songs(music_dir)
    if not songs:
        print(f"No MP3 files found in '{music_dir}' directory.")
        return
    
    print("Python Mp3 Player, by CiscoSteve42")
    print("Available songs:")
    for idx, song in enumerate(songs, start=1):
        print(f"{idx}. {os.path.basename(song)}")
    
    while True:
        choice = input("Enter song number to play (or q to quit): ")
        if choice.lower() == 'q':
            break
        
        try:
            song_idx = int(choice) - 1
            if 0 <= song_idx < len(songs):
                selected_song = songs[song_idx]
                print(f"Playing: {os.path.basename(selected_song)}")
                play_music(selected_song)
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)
            else:
                print("Invalid song number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number or 'q' to quit.")

if __name__ == "__main__":
    main()

