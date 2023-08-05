# -*- coding: utf-8 -*-
"""
@Time ： 2023/8/5 14:06
@Auth ： fuqiang
@File ：main.py
"""
import subprocess

"""
    command中参数详解:
        -to: 表示最终生成视频的时间长度
        -filter_complex: 表示复杂滤波器
        [0:v]|[1:v]:分别表示输入的是第一个文件和第二个文件
        [ckout]是定义的一个参数，用于保存输出的结果，可以是任意的, [out]同理
        colorkey=grb:m:n grb表示颜色的16进制，m表示设置colorkey相似值, n表示colorkey融合值
    https://blog.csdn.net/migu123/article/details/129314333
"""
bg_img = 'bg.jpg'
video = 'video.mp4'
out_video = 'result_video.mp4'
command = 'ffmpeg -y -v 24 -i {} -i {}  -to 00:00:14  -filter_complex  "[1:v]colorkey=0x00ff00:0.41:0.05[ckout];[' \
          '0:v][ckout]overlay[out]" -c:v libx264  -map "[out]" {}'.format(bg_img, video, out_video)
subprocess.call(command, shell=True)
