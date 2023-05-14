import os
import zipfile
import shutil

folder_path = os.path.dirname(os.path.abspath(__file__)) # 获取程序所在文件夹路径

# 遍历程序所在文件夹和所有子文件夹中的所有文件
for dirpath, dirnames, filenames in os.walk(folder_path):
    for filename in filenames:
        name, ext = os.path.splitext(filename)
        # 如果文件名是一位数字或两位数字，则在前面加上0或00
        if name.isdigit():
            new_name = name.zfill(3)
            new_filename = new_name + ext
            old_file_path = os.path.join(dirpath, filename)
            new_file_path = os.path.join(dirpath, new_filename)
            os.rename(old_file_path, new_file_path)

    # 对最末一级的子文件夹进行压缩操作
    if not dirnames and '.vscode' not in dirpath:
        zipf = zipfile.ZipFile(dirpath + '.zip', 'w', zipfile.ZIP_STORED)
        for root, dirs, files in os.walk(dirpath):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), dirpath))
        zipf.close()
        shutil.rmtree(dirpath) # 压缩后删除源文件

# 将此文件夹中所有的zip压缩文件更改后缀名为cbz
for filename in os.listdir(folder_path):
    if filename.endswith('.zip'):
        new_filename = filename.replace('.zip', '.cbz')
        old_file_path = os.path.join(folder_path, filename)
        new_file_path = os.path.join(folder_path, new_filename)
        os.rename(old_file_path, new_file_path)