# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# Time       ：2022/4/28 13:40
# Author     ：XuJ1E
# version    ：python 3.8
# File       : fine_width_height.py
"""
import PIL.Image as Image
import os


source_path = './trash/'
save_path = './trash/'


def img_proxy(path):
    image = Image.open(path)
    w, h = image.size
    new_img = Image.new('RGB', size=(w, h), color='white')
    return new_img


filename = os.listdir(source_path)
for i in range(len(filename)):
    img = img_proxy(source_path + filename[i])
    img.save(save_path+filename[i], 'JPEG')
    print(f'Processing number img_{i}')
    print(img.size)