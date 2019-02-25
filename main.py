import subprocess
import os
import json
import threading
ProcessNumber = 5


def ffprobe(patin,patout):
    info_in = subprocess.check_output(['ffprobe', '-v', 'warning','-print_format', 'json','-show_streams',
                                       '-show_format', patin])  #check output
    info_in = json.loads(info_in)   #load the info
    info_out = subprocess.check_output(['ffprobe', '-v', 'warning','-print_format', 'json','-show_streams',
                                       '-show_format', patout])
    info_out = json.loads(info_out)
    orig_duration = float(info_in['streams'][0]['duration'])  # check if there is any difference
    new_duration =  float(info_out['streams'][0]['duration'])
    if orig_duration == new_duration:
        return True
    else:
        return False


def video480(pathin):
    cmd = ['ffmpeg', '-i', pathin,'-r', '30', '-y', '-s', 'hd480', './video/out480p.mp4']  # encode
    try:
        subprocess.check_call(cmd)
    except OSError:
        return False
    except subprocess.CalledProcessError as e:
        return False
    result = ffprobe(path, "./video/out480p.mp4")   # get the result of duration check
    if result:
        print("Success")
        return True
    else:
        print("False")
        return False


def video720(pathin):
    cmd = ['ffmpeg', '-i', pathin,'-r', '30', '-y', '-s', 'hd720', './video/out720p.mp4']
    try:
        subprocess.run(cmd)
    except OSError:
        return False
    # except subprocess.CalledProcessError as e:
    #     return False

    if ffprobe(path, "./video/out720p.mp4"):
        print("Success")
        return True
    else:
        print("False")
        return False



if __name__ == '__main__':
    path = "newvideo.mp4"
    if not os.path.exists('./video/'):
        os.mkdir('./video/')
    thread1 = threading.Thread(target=video480, args=(path))  # two threads
    thread2 = threading.Thread(target=video720, args=(path))
    thread1.start()
    thread2.start()

