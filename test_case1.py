"""
This test will test the duration of input file and output file.
"""
import os
from main import Video
import threading


def test_one():
    """
    To check if the input duration and output duration are equal
    :return:  no return
    """
    v = Video()
    t = threading.Thread(target=v.start)  # convert video
    t.start()
    t.join()
    files = os.listdir("./video/")  # find output files
    for file in files:  # check duration
        result = v.ffprobe(file[:-8]+".mp4","./video/"+file)  # check the duration
        assert result  # if input and output durations are not equal, assert error

