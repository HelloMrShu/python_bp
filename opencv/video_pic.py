# coding=utf-8

import shutil
import cv2

# 全局变量
video_path = './videos/qd.mp4'  # 视频地址
dst_folder = './video_frame'  # 存放帧图片的位置
freq = 25  # 帧提取频率
video = cv2.VideoCapture()
fps = video.get(cv2.CAP_PROP_FPS)
print(f"{fps} frames per second")

frame = video.get(cv2.CAP_PROP_FRAME_COUNT)
print(frame)
exit(1)

if not video.open(video_path):
    print("can't open video")
    exit(1)

count = 1
index = 1
while True:
    _, frame = video.read()
    if frame is None:
        break
    if count:
        save_path = "{}/{:>03d}.jpg".format(dst_folder, index)
        cv2.imwrite(save_path, frame)
        index += 1
    count += 1
video.release()

print("Totally extract {:d} pics".format(index - 1))
