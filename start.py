import os
import fnmatch
import time
import multiprocessing

cameras = []
for file in os.listdir('/dev'):
  if fnmatch.fnmatch(file, 'video[0-9]'):
     cameras.append(int(file[-1:]))

def launchcam():
  #os.popen("mjpg_streamer -o \"output_http.so -w ./www -p " + "" + "\" -i \"input_opencv.so --filter cvfilter_py.so --fargs ./compression.py --d " + str(cameras[index]) + "\"")
  #os.popen("mjpg_streamer -o \"output_http.so -w ./www -p 8080\" -i \"input_opencv.so --filter cvfilter_py.so --fargs ./compression.py --d " + str(cameras[0]) + "\" -i \"input_opencv.so --filter cvfilter_py.so --fargs ./compression.py --d " + str(cameras[1]) + "\"")
  os.popen("mjpg_streamer -o \"output_http.so -w ./www -p 8080\" -i input_opencv.so --filter cvfilter_py.so --fargs ./compression.py --d " + str(cameras[0]) + " -i input_opencv.so --filter cvfilter_py.so --fargs ./compression.py --d " + str(cameras[1]) + "\"")


'''
if len(cameras) >= 1:
    p1 = multiprocessing.Process(target=launchcam,args=(0,))
    p1.start()
time.sleep(2)
if len(cameras) >= 2:
    p2 = multiprocessing.Process(target=launchcam,args=(1,))
    p2.start()
time.sleep(2)

p1.join()
'''
#for index in range(len(cameras)):
#    os.popen("mjpg_streamer -o \"output_http.so -w ./www -p " + str((25565 + index)) + "\" -i \"input_opencv.so --filter cvfilter_py.so --fargs ./compression.py --d " + str(cameras[index]) + "\"")
