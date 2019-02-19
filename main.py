import subprocess
def video720(path):
    subprocess.run("./ffmpeg -i ./video_in/" + path + " -b: 2M -r 30 -s 1280x720 -f mp4 " + path + "_720p.mp4")
    print('Convert ' + path + ' to 720p' + ' successfully!')
    return'720 done'

def video480(path):
    subprocess.run("./ffmpeg -i ./video_in/" + path + " -b: 2M -r 30 -s 640x480 -f mp4 " + path + "_480p.mp4")
    print('Convert ' + path + ' to 480p' + ' successfully!')
    return'480 done'


if __name__ == '__main__':
    path = ""
    coroutine720 = video720(path)
    coroutine480 = video480(path)

