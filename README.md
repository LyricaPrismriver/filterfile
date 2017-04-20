# filterfile
批量筛选文件进行操作的小工具

筛选时对all_files和all_dirs进行操作,这两都是一维列表
比如我要选大小等于100字节的文件:
filtered_dirs = all_dirs
filtered_files = [x for x in all_files if os.path.getsize() == 100]
