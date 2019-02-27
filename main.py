import subprocess
import os
import json
from queue import Queue


class Video():
    def __init__(self):
        self.i = 0
        self.j = 0
        self.v4output_path = ''
        self.v7output_path = ''

    def ffprobe(self, patin, patout):
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

    def video480(self, pathin):
        self.v4output_path = './video/out480p_'+str(self.i)+'.mp4'
        cmd = ['ffmpeg', '-i', pathin, '-r', '30', '-y', '-s', 'hd480', self.v4output_path]  # encode
        VL = subprocess.Popen(cmd)
        self.i = self.i + 1
        subprocess.Popen.poll(VL)
        while VL.returncode:
            pass
        print("Finish video480\n")
        return 0

    def video720(self, pathin):
        self.v7output_path = './video/out720p_'+str(self.j)+'.mp4'
        cmd = ['ffmpeg', '-i', pathin, '-r', '30', '-y', '-s', 'hd720', self.v7output_path]
        VH = subprocess.Popen(cmd)
        self.j = self.j + 1
        subprocess.Popen.poll(VH)
        while VH.returncode:
            pass
        print("Finish video720\n")
        return 0


if __name__ == '__main__':
    input_Q = Queue()
    if not os.path.exists('./video/'):
        os.mkdir('./video/')
    V = Video()
    while True:
        input_Q.put('./newvideo.mp4')
        path = input_Q.get()
        V4 = V.video480(path)
        V7 = V.video720(path)
        while V4 or V7:
            pass
        # unittest.main()

