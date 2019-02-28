# python-CI
Python CI template for EC500 Software Engineering

## Prerequisite
You need to install "ffmpeg" for this program. 'pip install ffmpeg'
python 3.6
## functions
This program could convert an video to both 480p and 720p. And there are two functions named video720 and video480 do this job. Before running the program, you could change the path of your input video file then load it into the program. Then the program will creat two threads two encode the program. After finishing its job, the program will also check the output information of these two output videos. The program could get the right duration time and compare them with the duration time of two outputs. If the duration time is not right, the program will return false.

![1](https://github.com/ec500-software-engineering/exercise-2-ffmpeg-liuknan/raw/master/ex2.png)
## Estimation
For single program, it will use 30% of the CPU. When the number of programs comes to 6, they will take up 80% of cpu.
![1](https://github.com/ec500-software-engineering/exercise-2-ffmpeg-liuknan/blob/master/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202019-02-27%20%E4%B8%8B%E5%8D%8811.03.58.png)
![2](https://github.com/ec500-software-engineering/exercise-2-ffmpeg-liuknan/blob/master/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202019-02-27%20%E4%B8%8B%E5%8D%8811.05.19.png)
