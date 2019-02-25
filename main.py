import subprocess
import os
import json

def ffprobe(patin,patout):
    info_in = subprocess.check_output(['ffprobe', '-v', 'warning','-print_format', 'json','-show_streams',
                                       '-show_format', patin])
    info_in = json.loads(info_in)
    info_out = subprocess.check_output(['ffprobe', '-v', 'warning','-print_format', 'json','-show_streams',
                                       '-show_format', patout])
    info_out = json.loads(info_out)
    orig_duration = float(info_in['streams'][0]['duration'])
    new_duration =  float(info_out['streams'][0]['duration'])
    if orig_duration == new_duration:
        return True
    else:
        return False


def video480(pathin):
    cmd = ['ffmpeg', '-i', pathin,'-r', '30', '-y', '-s', 'hd480', './video/out480p.mp4']
    try:
        subprocess.check_call(cmd)
    except OSError:
        return False
    except subprocess.CalledProcessError as e:
        return False
    result = ffprobe(path, "./video/out480p.mp4")
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
    path = "/Users/liuknan/Documents/GitHub/exercise-2-ffmpeg-liuknan/newvideo.mp4"
    if not os.path.exists('./video/'):
        os.mkdir('./video/')
    Out480p = video480(path)
    Out720p = video720(path)

