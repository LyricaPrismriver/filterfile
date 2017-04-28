#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import os, os.path, shutil
from itimer import itimer

#os.system(r'net use z: \\ip\folder')
#复制局域网文件需先映射
#原文件夹
SRC = os.path.normpath('Z:\\')
#目标文件夹
DEST = os.path.normpath('D:\\codes\\msc1')
#记录日志的文件夹
LOG = 'log.txt'
#文件列表
all_files = []
#目录列表
all_dirs = []
LINESEP = os.linesep
t = itimer()
f = open(LOG, 'a')

#遍历原文件夹并存储文件和文件夹信息
def forfiles(path, files):
    for file in files:
       pathfile = os.path.join(path, file)
       if os.path.isfile(pathfile):
           all_files.append(pathfile)
       else:
           all_dirs.append(pathfile)
           forfiles(pathfile, os.listdir(pathfile))

t.setStart()
forfiles(SRC, os.listdir(SRC))
#记录所用时间
f.write('get all folders and files from %s uses %.4f s%s' % (SRC, t.getSec(), LINESEP))
f.flush()
#复制到目标文件夹
def copyfiles(dirlist, filelist, dest):
   salt = 1
   if SRC[-1] == '\\':
       salt = 0
    #先创建文件夹
   for dir in dirlist:
       destdir = os.path.join(dest, dir[len(SRC) + salt:])
       if not os.path.exists(destdir):
            os.mkdir(destdir)
   for i in range(len(filelist)):
        destfile = os.path.join(dest, filelist[i][len(SRC) + salt:])
        if os.path.exists(destfile):
            os.chmod(destfile, stat.S_IWRITE)
            os.remove(destfile)
        try:
            shutil.copy(filelist[i], destfile)
        except IOError as e:
            f.write('[%d/%d]error: %s %s ' % (i, files_count, destfile, LINESEP))
            f.write('I/O error: %s %s' % (e, LINESEP))
            f.flush()
            print('[%d/%d]error: %s' % (i, files_count, destfile))
            pass
        print('[%d/%d]done: %s' % (i, files_count, destfile))

t.setStart()
#筛选文件,筛选时对all_files和all_folder进行操作,这两都是一维列表
filtered_dirs = [x for x in all_dirs if '.svn' not in x]
filtered_files = [x for x in all_files if '.svn' not in x]
copyfiles(filtered_dirs, filtered_files, DEST)
f.write('copy all folders and files from %s to %s uses %.4f s%s' % (SRC, DEST, t.getSec(), LINESEP))
f.close()
