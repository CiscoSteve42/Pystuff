import yt_dlp, os

def download_audio(url, file_name):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{file_name}.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)

    return info_dict

url = input('Enter a Youtube URL:\n> ')
file_name = input('Enter a desired file name (without extension):\n> ')

downloaded_info = download_audio(url, file_name)
print(downloaded_info)


