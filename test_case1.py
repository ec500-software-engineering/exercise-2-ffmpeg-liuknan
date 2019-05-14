import os
from queue import Queue
from main import Video
import threading


def test_one():
        V = Video()
        input_q = Queue()
        if not os.path.exists('./video/'):
            os.mkdir('./video/')
        input_q.put('./newvideo.mp4')
        path = input_q.get()
        V4 = threading.Thread(target=V.video480,args=path)
        V7 = threading.Thread(target=V.video720,args=path)
        V4.start()
        V7.start()
        V4.join()
        result4 = V.ffprobe(path, V.v4output_path)  # check the duration
        V7.join()
        result7 = V.ffprobe(path, V.v7output_path)
        assert result4
        assert result7

