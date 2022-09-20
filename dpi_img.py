# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# Time       ：2022/5/12 20:10
# Author     ：XuJ1E
# version    ：python 3.8
# File       : dpi_img.py
"""
from PIL import Image as ImagePIL
import os


def transfer(infile, outfile):
    im = ImagePIL.open(infile)
    im.save(outfile, dpi=(72.0, 72.0))  ##500.0,500.0分别为想要设定的dpi值


if __name__ == '__main__':
    for root, dirs, files in os.walk("./test_img_256/"):  ##ori_img为需要修改的图片存储的文件夹名字
        print(f'This file has about {len(files)}')
        for item in files:
            list = item.split(".")
            if list[-1] == "jpg":
                try:
                    new_name = list[0] + ".jpg"
                    print(f"Load the image:{new_name}")
                    # os.rename("./data/datasets/unclothes" + item, "./data/datasets/unclothes" + new_name)
                    print(new_name)
                    transfer("./test_img_256/" + new_name, "./test_img_256/" + new_name)
                except:
                    print(f'This image has some problem, then del {item}')
                    del item
                    continue