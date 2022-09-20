# !/usr/bin/env python
# -*-coding:utf-8 -*-
"""
# Time       ：2022/4/30 21:16
# Author     ：XuJ1E
# version    ：python 3.8
# File       : rename_img.py
"""
import os
import imghdr
import this


class BatchRename():
    def __init__(self):
        self.path = './unclothes/unclothes_bing_square/'  # 表示需要命名处理的文件夹目录，复制地址后注意反斜杠

    def rename(self):
        filelist = os.listdir(self.path)  # 获取文件路径
        total_num = len(filelist)  # 获取文件长度（文件夹下图片个数）
        i = 1  # 表示文件的命名是从1开始的
        for item in filelist:
            if item.endswith('.jpg') or item.endswith('.png'):
                # 初始的图片的格式为jpg格式的（或者源文件是png格式及其他格式，后面的转换格式就可以调整为自己需要的格式即可，我习惯转成.jpg）
                src = os.path.join(os.path.abspath(self.path), item)
                dst = os.path.join(os.path.abspath(self.path),
                                format(str(i), '0>4s') + '_0' + '.jpg')  # 处理后的格式也为jpg格式的，当然这里可以改成png格式
                try:
                    os.rename(src, dst)
                    print('Successful converting %s to %s' % (src, dst))
                    i = i + 1
                except:
                    continue
            else:
                print(f'This {item} have problem')
            # elif item.endswith('.png'):
            #     src = os.path.join(os.path.abspath(self.path), item)
            #     dst = os.path.join(os.path.abspath(self.path),
            #                        'N' + format(str(i), '0>4s') + '_0' + '.png')  # 处理后的格式也为jpg格式的，当然这里可以改成png格式
            #     try:
            #         os.rename(src, dst)
            #         print('Successful converting %s to %s' % (src, dst))
            #         i = i + 1
            #     except:
            #         continue

        print('total %d to rename & converted %d img' % (total_num, i-1))


if __name__ == '__main__':
    demo = BatchRename()
    demo.rename()