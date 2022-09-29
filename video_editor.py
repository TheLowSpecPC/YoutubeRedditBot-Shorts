from moviepy.editor import VideoFileClip
import os
from os.path import isfile, join
import config


def makeCompilation(path = "bot\\Reddit\\",):

    n = config.part
    for fileName in os.listdir(path):
        filePath = join(path, fileName);
        if isfile(filePath) and fileName.endswith(".mp4"):
            Vid = VideoFileClip(filePath)
            Vid = Vid.resize((1080,1920))
            Vid.write_videofile("bot\\Output\\Reddit Memes Part %04i #shorts.mp4" %n,
                                threads=8, remove_temp=True, codec="libx264",
                                audio_codec="aac", preset="medium", fps=20)
            n+=1

    return "Finished Editing"

if __name__ == "__main__":
    makeCompilation(path = "bot\\Reddit\\",)