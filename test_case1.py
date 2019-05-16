import os
from main import Video


def test_one():
        v = Video()
        v.convert()
        files = os.listdir("./video/")
        for file in files:
            result = v.ffprobe(file[:-8]+".mp4","./video/"+file)  # check the duration
            assert result

