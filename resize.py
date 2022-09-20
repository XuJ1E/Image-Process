# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# Time       ：2022/9/20 11:07
# Author     ：XuJ1E
# version    ：python 3.8
# File       : resize.py
"""
import os
import shutil
from PIL import Image
from torchvision import transforms

name = 'valid'
image_size = 512
path = f'./dataset/{name}'
# source = [path + '/' + i for i in os.listdir(path)]
source = os.listdir(path)
# print(source)
target = f'./new_dataset/{name}'


if os.path.exists(target):
    shutil.rmtree(target)
    print('Remove path - %s' % target)
os.makedirs(target)
print('Create path - %s' % target)

Resize = transforms.Compose([
    transforms.ToTensor(),
    transforms.Resize(size=(image_size, image_size)),
    transforms.ToPILImage(),
])


for i, img_path in enumerate(source):
    print(img_path)
    length = len(source)
    image = Image.open(f'{path}/{img_path}')
    image = Resize(image)
    image.save(f'{target}/{img_path}')
    print(f'saved image of {i}/{length} ------')

