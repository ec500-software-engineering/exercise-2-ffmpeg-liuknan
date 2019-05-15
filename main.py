import subprocess
import os
import json
import threading
from queue import Queue


class Video:
    def __init__(self):
        self.i = 0  # counter for video480
        self.j = 0  # counter for video720
        self.v4output_path = ''  # output path for video 480
        self.v7output_path = ''  # output path for video 720

    def ffprobe(self, patin, patout):
        info_in = subprocess.check_output(['ffprobe', '-v', 'warning', '-print_format', 'json', '-show_streams',
                                           '-show_format', patin], universal_newlines=True)  # check output
        info_in = json.loads(info_in)   # load the info
        info_out = subprocess.check_output(['ffprobe', '-v', 'warning', '-print_format', 'json', '-show_streams',
                                           '-show_format', patout], universal_newlines=True)
        info_out = json.loads(info_out)
        orig_duration = float(info_in['streams'][0]['duration'])  # check if there is any difference
        new_duration = float(info_out['streams'][0]['duration'])
        if orig_duration == new_duration:
            return True
        else:
            return False

    def video480(self, pathin):
        self.v4output_path = './video/out480p_'+str(self.i)+'.mp4'  # update the output path
        cmd = ['ffmpeg', '-i', pathin, '-r', '30', '-y', '-s', 'hd480', self.v4output_path]  # encode
        vl = subprocess.Popen(cmd)  # convert
        self.i = self.i + 1  # counter + 1
        vl.wait()  # wait until the child process is done
        print("Finish video480\n")
        return 0

    def video720(self, pathin):
        self.v7output_path = './video/out720p_'+str(self.j)+'.mp4'

        cmd = ['ffmpeg', '-i', pathin, '-r', '30', '-y', '-s', 'hd720', self.v7output_path]
        vh = subprocess.Popen(cmd)
        self.j = self.j + 1
        vh.wait()
        print("Finish video720\n")
        return 0


if __name__ == '__main__':
    input_Q = Queue()
    if not os.path.exists('./video/'):
        os.mkdir('./video/')
    V = Video()
    input_Q.put('./newvideo.mp4')
    while True:
        while not input_Q.empty():
            path = input_Q.get()
            V.video480(path)
            V.video720(path)
    # while V4 or V7:
    #     pass
    # unittest.main()

