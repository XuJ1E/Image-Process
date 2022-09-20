# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# Time       ：2022/5/13 9:06
# Author     ：XuJ1E
# version    ：python 3.8
# File       : detect_img.py
"""
import os
import imghdr


def readitem(path):
    list = []
    print('-------------detecting-----------')
    for filename in os.listdir(path):
        list.append(filename)
        img = open(path + filename, 'rb')
        if imghdr.what(img) != 'jpeg':
            print(f'Image {img.name[-11:-4]} is a png file')
        elif imghdr.what(img) == 'jpeg':
            pass
            # print(f'Image {img.name[-11:-4]} is a jpeg file')
        else:
            print(f'None type in this filepath {path}')
    print(f'This filepath have {len(list)} img')
    print('------------end None--------------')


readitem('./unclothes/unclothes_bing_1440_jpg/')
readitem('./clothes/clothes_bing_1440_jpg/')
# readitem('./clothes_bing_256_png/')
# readitem('./unclothes_bing_256_png/')