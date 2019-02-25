import subprocess
import json
import os
class TestClass(object):
    def test_one(self):
        while not (os.path.exists('./video/out480p.mp4')):
            pass
        info_in = subprocess.check_output(['ffprobe', '-v', 'warning', '-print_format', 'json', '-show_streams',
                                           '-show_format', 'newvideo.mp4'])  # check output
        info_in = json.loads(info_in)
        info_out = subprocess.check_output(['ffprobe', '-v', 'warning', '-print_format', 'json', '-show_streams',
                                            '-show_format', './video/out480p.mp4'])
        info_out = json.loads(info_out)
        orig_duration = float(info_in['streams'][0]['duration'])  # check if there is any difference
        new_duration = float(info_out['streams'][0]['duration'])
        assert orig_duration == new_duration
