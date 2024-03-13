# !/usr/bin/python
# -*- coding:utf-8 -*-
# time: 2019/04/16--17:12
__author__ = 'Sven'

'''
把分P视频整合到一个文件夹里面
'''

import os
import shutil

def move_files_from_subdirs_to_root(root_dir):  
    # 遍历root_dir下的所有子目录  
    for subdir, dirs, files in os.walk(root_dir):  
        # 如果当前遍历的目录不是root_dir，则处理其中的文件  
        if subdir != root_dir:  
            # 遍历子目录中的文件  
            for file in files:  
                # 构造文件的完整路径  
                src_file = os.path.join(subdir, file)
                # 构造目标路径，即root_dir下的文件路径  
                dst_file = os.path.join(root_dir, file)  
                # 移动文件  
                shutil.move(src_file, dst_file)  
                print(f"Moved {src_file} to {dst_file}")  

if __name__ == '__main__':
    rootpath = input('请输入要整合的根目录:')
    move_files_from_subdirs_to_root(rootpath)
