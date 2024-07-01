#!/usr/bin/env python3

import os, sys, ffmpeg, eyed3
from yt_dlp import YoutubeDL

print('Youtube to mp3 converter script by CiscoSteve42')

yt_url = input('Enter a Youtube URL:\n> ')
file_name = input('Enter a desired file name (without extension):\n> ')
song_name = input('Enter the song title:\n> ')
artist_name = input('Enter the name of the artist:\n> ')
album_name = input('Enter the name of the album:\n> ')

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': f'{file_name}.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
with YoutubeDL(ydl_opts) as ydl:
    ydl.download([yt_url])

input_file = f"{file_name}.webm"
output_file = f"{file_name}.mp3"
ffmpeg.input(input_file).output(output_file).run(overwrite_output=True)

audiofile = eyed3.load(output_file)
if audiofile.tag is None:
    audiofile.initTag()

audiofile.tag.title = song_name
audiofile.tag.artist = artist_name
audiofile.tag.album = album_name
audiofile.tag.save()

current_directory = os.getcwd()
destination_directory = input('Please enter the desired directory for your mp3 file:\n> ')

source_path = os.path.join(current_directory, output_file)
destination_path = os.path.join(destination_directory, output_file)
os.rename(source_path, destination_path)

print(f"File moved successfully to {destination_directory}")

