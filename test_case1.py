import os
from queue import Queue
from main import Video


def test_one():
        V = Video()
        input_q = Queue()
        if not os.path.exists('./video/'):
            os.mkdir('./video/')
        input_q.put('./newvideo.mp4')
        path = input_q.get()
        v4 = V.video480(path)
        while v4:
            pass
        result = V.ffprobe(path, V.v4output_path)
        assert result

