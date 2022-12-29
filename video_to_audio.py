# pip install moviepy
from moviepy.editor import VideoFileClip, AudioFileClip
from pathlib import Path


video_path = Path(path_of_video)  # path_of_video

# 1-st variant
# audio = AudioFileClip(f"{video_path}")

# 2-nd variant
video = VideoFileClip(f"{video_path}")
audio = video.audio

audio.write_audiofile(f"{video_path.stem}.mp3", buffersize=2000)  # wright audio

