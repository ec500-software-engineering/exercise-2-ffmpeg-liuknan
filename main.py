"""
In this program, I use ffmpeg to convert mp4 file to 480p and 720. I use thread so user could convert several file
at the same time. it also has a function to check the duration of input and output to make sure that the durations of
input and output are the same.
"""
import subprocess
import os
import json
import threading
from queue import Queue


class Video:
    def __init__(self):
        """
        i and j are counters.
        v4 and v7 output_path are path for output files.
        """
        self.i = 0  # counter for video480
        self.j = 0  # counter for video720
        self.v4output_path = ''  # output path for video 480
        self.v7output_path = ''  # output path for video 720
        self.inputqueue = Queue()


    def ffprobe(self, patin, patout):
        """
        For testers to check the durations of input file and output file.
        :param patin: the input path of file.
        :param patout: the output path of file.
        :return: a boolean for pytest to check.
        """
        info_in = subprocess.check_output(['ffprobe', '-v', 'warning', '-print_format', 'json', '-show_streams',
                                           '-show_format', patin], universal_newlines=True)  # check input info
        info_in = json.loads(info_in)   # load the info
        info_out = subprocess.check_output(['ffprobe', '-v', 'warning', '-print_format', 'json', '-show_streams',
                                           '-show_format', patout], universal_newlines=True)  # check output info
        info_out = json.loads(info_out)  # load info
        orig_duration = float(info_in['streams'][0]['duration'])  # check duration
        new_duration = float(info_out['streams'][0]['duration'])  # check duration
        if orig_duration == new_duration:  # check the difference between input duration and output duration
            return True
        else:
            return False

    def video480(self, pathin):
        """
        convert mp4 to 480p.
        :param pathin: input path
        :return: 0 if no errors occurred.
        """
        if not os.path.exists('./video/'):  # create output folder
            os.mkdir('./video/')
        self.v4output_path = "./video/"+pathin[:-4]+"480p.mp4"  # update the output path
        cmd = ['ffmpeg', '-i', pathin, '-r', '30', '-y', '-s', 'hd480', self.v4output_path]  # encode
        vl = subprocess.Popen(cmd)  # convert
        self.i = self.i + 1  # counter + 1
        ret = vl.wait()  # wait until the child process is done
        if not ret == 0:  # error detect
            print("Error occurred")
        else:
            print("Finish video480\n")
            return 0

    def video720(self, pathin):
        """
        convert mp4 to 720p.
        :param pathin: input path
        :return:  0 if no errors occurred.
        """
        if not os.path.exists('./video/'):  # create output folder
            os.mkdir('./video/')
        self.v7output_path = "./video/"+pathin[:-4]+"720p.mp4"  # output path

        cmd = ['ffmpeg', '-i', pathin, '-r', '30', '-y', '-s', 'hd720', self.v7output_path]  # ffmpeg command
        vh = subprocess.Popen(cmd)  # crate process
        self.j = self.j + 1  # counter
        ret = vh.wait()  # wait
        if not ret == 0:
            print("Error occurred")
        else:
            print("Finish video720\n")
            return 0

    def convert(self):
        """
        get files from input queue and convert them.
        :return:no return.
        """
        while not self.inputqueue.empty():
            file = self.inputqueue.get()
            v4 = threading.Thread(target=self.video480, args=(file,))  # convert to 480p
            v4.start()
            v7 = threading.Thread(target=self.video720, args=(file,))  # convert to 720p
            v7.start()
            # v4.join()
            # v7.join()

    def input(self):
        """
        input queue
        :return: no return
        """
        Files = os.listdir()  # list documents
        for file in Files:
            file_name_list = file.split('.')  # check .mp4 file
            if file_name_list[-1] == 'mp4' \
                    or file_name_list[-1] == '.mp4' \
                    or file_name_list[-1] == '.avi' \
                    or file_name_list[-1] == '.wmv' \
                    or file_name_list[-1] == '.flv' \
                    or file_name_list[-1] == '.mov':
                self.inputqueue.put(file)

    def start(self):
        """
        start the whole program
        :return: no return
        """
        inputthread = threading.Thread(target=self.input)
        inputthread.start()
        convertthread = threading.Thread(target=self.convert)
        convertthread.start()


if __name__ == '__main__':
    V = Video()
    V.start()
    # while V4 or V7:
    #     pass
    # unittest.main()

