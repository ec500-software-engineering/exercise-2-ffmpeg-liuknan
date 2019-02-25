# python-CI-template
Python CI template for EC500 Software Engineering

## Prerequisite
You need to install "ffmpeg" for this program. 'pip install ffmpeg'
python 3.6
## functions
This program could convert an video to both 480p and 720p. And there are two functions named video720 and video480 do this job. Before running the program, you could change the path of your input video file then load it into the program. Then the program will creat two threads two encode the program. After finishing its job, the program will also check the output information of these two output videos. The program could get the right duration time and compare them with the duration time of two outputs. If the duration time is not right, the program will return false.

![1](https://github.com/ec500-software-engineering/exercise-2-ffmpeg-liuknan/raw/master/ex2.png)
