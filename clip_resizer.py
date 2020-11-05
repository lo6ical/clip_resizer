import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import moviepy.editor as mp
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

#getting the video path with tkinter and giving the clip a name
Tk().withdraw()
filename = askopenfilename()
clipname = os.path.basename(filename)
print("Resolution: (480, 648, 720)")
resolution = int(input())
print("Clip length in seconds (from the end): ")
clip_duration = float(input())
clipname = f"({resolution}p)" + clipname

#resizing the clip
clip = mp.VideoFileClip(filename)
video_length = clip.duration
start_time = video_length - clip_duration
clip_cut = clip.subclip(start_time)
clip_resized = clip_cut.resize(height=resolution)
clip_resized.write_videofile(clipname)



