import subprocess
import os
import json
from queue import Queue


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
    VL = subprocess.Popen(cmd)
    i = i + 1
    subprocess.Popen.poll(VL)
    while VL.returncode:
        pass
    print("Finish video480\n")
    return 0


def video720(pathin):
    global j
    cmd = ['ffmpeg', '-i', pathin, '-r', '30', '-y', '-s', 'hd720', './video/out720p_'+str(j)+'.mp4']
    VH = subprocess.Popen(cmd)
    j = j + 1
    subprocess.Popen.poll(VH)
    while VH.returncode:
        pass
    print("Finish video720\n")
    return 0


if __name__ == '__main__':
    input_Q = Queue()
    i = 0
    j = 0
    if not os.path.exists('./video/'):
        os.mkdir('./video/')
    while True:
        input_Q.put('./newvideo.mp4')
        path = input_Q.get()
        V4 = video480(path)
        V7 = video720(path)
        while V4 or V7:
            pass
        # unittest.main()

