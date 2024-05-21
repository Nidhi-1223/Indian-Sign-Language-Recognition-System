'''
for 20 signs
'''

# import os
# '''
# detect-copy - 20 signs
# best - 20 signs (best better than best0)
# '''
# os.system("python yolov5\detect.py --weights best.pt --img 416 --conf 0.5 --source 0")


import os

os.system("python yolov5\detect.py --weights 20_best.pt --img 416 --conf 0.5 --source 0")