import os
from queue import Queue
from main import Video
import threading


def test_one():
        v = Video()
        input_q = Queue()
        if not os.path.exists('./video/'):
            os.mkdir('./video/')
        input_q.put('./newvideo.mp4')
        path = input_q.get()
        v4 = threading.Thread(target=v.video480, args=(path,))
        v7 = threading.Thread(target=v.video720, args=(path,))
        v4.start()
        v7.start()
        v4.join()
        result4 = v.ffprobe(path, v.v4output_path)  # check the duration
        v7.join()
        result7 = v.ffprobe(path, v.v7output_path)
        assert result4
        assert result7

