from __future__ import unicode_literals
import youtube_dl
import json

ydl_opts = {
#     'postprocessors': [{

#      'key': 'FFmpegExtractAudio', # Tách lấy audio

#      'preferredcodec': 'mp3', # Format ưu tiên là mp3

#      'preferredquality': '192', # Chất lượng bitrate
# }],
}

ytLink = ["https://www.youtube.com/watch?v=0YF8vecQWYs"]

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    data = ydl.extract_info(ytLink)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)