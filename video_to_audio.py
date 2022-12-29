# pip install moviepy
from moviepy.editor import VideoFileClip, AudioFileClip
from pathlib import Path


video_path = Path(r'your_path_to_video')


def video_to_audio(path):
    # 1-st variant
    # audio = AudioFileClip(f"{video_path}")

    # 2-nd variant
    video = VideoFileClip(f"{path}")
    audio = video.audio

    audio.write_audiofile(f"{path.stem}.mp3", buffersize=2000)  # wright audio


if __name__ == '__main__':
    video_to_audio(video_path)
