# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# Time       ：2022/5/6 13:50
# Author     ：XuJ1E
# version    ：python 3.8
# File       : paste_img.py
"""
from PIL import Image
import os


def Square_Generated(read_file):
    '''
        This is the func to transfer the nonsquare img to square img
    '''
    image = Image.open(read_file)  # import img
    w, h = image.size  # get the size of img
    print(f'original image size as:{w}x{h}')
    # if w > 1440 or h > 1440:
    #     # take the size of the longest side of the length, color determines the color to fill the img
    #     new_image = Image.new('RGB', size=(max(w, h), max(w, h)), color='white')
    #     # print(background)
    #     length = int(abs(w - h)//2)  # Fill the shorter side symmetrically
    #     box = (length, 0) if w < h else (0, length)  # put it in the box
    #     new_image.paste(image, box)  # Generate new image
    #     new_image = new_image.resize((1280, 1280), Image.ANTIALIAS)
    #     return new_image
    # elif w <= 1440 and h <= 1440:
    #     ori_image = Image.new('RGB', size=(max(w, h), max(w, h)), color='white')
    #     length = int(abs(w - h)//2)
    #     box = (length, 0) if w < h else (0, length)
    #     ori_image.paste(image, box)
    #     ori_image = ori_image.resize((1280, 1280), Image.ANTIALIAS)
    #     return ori_image
    # elif w < 1024 and h < 1024:
    paste_image = Image.new('RGB', size=(max(w, h), max(w, h)), color='white')
    length = int(abs(w - h) // 2)
    box = (length, 0) if w < h else (0, length)
    paste_image.paste(image, box)
    paste_image = paste_image.resize((256, 256), Image.ANTIALIAS)
    return paste_image


source_path = './unclothes/unclothes_bing/'  # path of nonsquare img
save_path = './unclothes/unclothes_bing_square/'  # path of generate square img
if not os.path.exists(save_path):
    os.mkdir(save_path)


file_names = os.listdir(source_path)  # load the img name of nonsquare
for i in range(len(file_names)):
    img = Square_Generated(source_path + file_names[i])
    img.save(save_path + file_names[i], 'JPEG')  # save square img
    print('Processing number', i)
    print(f'The new image size as:{img.size}\n')

