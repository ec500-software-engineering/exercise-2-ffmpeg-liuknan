import subprocess
import os
import json
import threading
import unittest
import time
from queue import Queue


class CollisionTestCase(unittest.TestCase):
    global i

    def test_one(self):
        info_in = subprocess.check_output(['ffprobe', '-v', 'warning', '-print_format', 'json', '-show_streams',
                                           '-show_format', 'newvideo.mp4'])  # check output
        info_in = json.loads(info_in)
        info_out = subprocess.check_output(['ffprobe', '-v', 'warning', '-print_format', 'json', '-show_streams',
                                            '-show_format', './video/out480p_'+str(i)+'.mp4'])
        info_out = json.loads(info_out)
        orig_duration = float(info_in['streams'][0]['duration'])  # check if there is any difference
        new_duration = float(info_out['streams'][0]['duration'])
        self.assertEqual(orig_duration, new_duration)


def ffprobe(patin, patout):
    info_in = subprocess.check_output(['ffprobe', '-v', 'warning', '-print_format', 'json', '-show_streams',
                                       '-show_format', patin])  # check output
    info_in = json.loads(info_in)   # load the info
    info_out = subprocess.check_output(['ffprobe', '-v', 'warning', '-print_format', 'json', '-show_streams',
                                       '-show_format', patout])
    info_out = json.loads(info_out)
    orig_duration = float(info_in['streams'][0]['duration'])  # check if there is any difference
    new_duration = float(info_out['streams'][0]['duration'])
    if orig_duration == new_duration:
        return True
    else:
        return False


def video480(pathin):
    global i
    cmd = ['ffmpeg', '-i', pathin, '-r', '30', '-y', '-s', 'hd480', './video/out480p_'+str(i)+'.mp4']  # encode
    try:
        subprocess.Popen(cmd)
    except OSError:
        return False
    except subprocess.CalledProcessError:
        return False
    time.sleep(2)
    result = ffprobe(path, './video/out480p_0.mp4')   # get the result of duration check
    i = i + 1
    if result:
        print("Success")
        return True
    else:
        print("False")
        return False


def video720(pathin):
    global j
    cmd = ['ffmpeg', '-i', pathin, '-r', '30', '-y', '-s', 'hd720', './video/out720p_'+str(j)+'.mp4']
    try:
        subprocess.Popen(cmd)
    except OSError:
        return False
    except subprocess.CalledProcessError:
        return False
    time.sleep(2)
    j = j + 1
    if ffprobe(path, './video/out720p_0.mp4'):
        print("Success")
        return True
    else:
        print("False")
        return False


if __name__ == '__main__':
    input_Q = Queue()
    i = 0
    j = 0
    if not os.path.exists('./video/'):
        os.mkdir('./video/')
    while True:
        input_Q.put('./newvideo.mp4')
        path = input_Q.get()
        thread1 = threading.Thread(target=video480, args=(path,))  # two threads
        thread2 = threading.Thread(target=video720, args=(path,))
        thread1.start()
        thread2.start()
        time.sleep(5)
        # unittest.main()

